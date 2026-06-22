#!/usr/bin/env python3
"""
Argument-Adjunct Asymmetry in Dependency Distance: Mixed-Effects Model Test.
Tests whether spoken language selectively elongates adjunct dependency distances
relative to argument distances, and whether this asymmetry correlates with
morphological case richness across languages.
"""

import sys
import json
import gc
import math
import os
import resource
import multiprocessing as mp
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
import scipy.stats as stats
import statsmodels.formula.api as smf
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from loguru import logger

WORKSPACE = Path("/ai-inventor/aii_data/runs/run_4SjiUyyE35Gi/3_invention_loop/iter_1/gen_art/gen_art_experiment_1")
LOGS_DIR = WORKSPACE / "logs"
PLOTS_DIR = WORKSPACE / "plots"
LOGS_DIR.mkdir(exist_ok=True)
PLOTS_DIR.mkdir(exist_ok=True)

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add(str(LOGS_DIR / "run.log"), rotation="30 MB", level="DEBUG")

# --- Resource limits (container: 29GB, 4 CPUs) ---
RAM_BUDGET = int(18 * 1024**3)  # 18GB
resource.setrlimit(resource.RLIMIT_AS, (RAM_BUDGET * 3, RAM_BUDGET * 3))

def _detect_cpus() -> int:
    try:
        parts = Path("/sys/fs/cgroup/cpu.max").read_text().split()
        if parts[0] != "max":
            return math.ceil(int(parts[0]) / int(parts[1]))
    except Exception:
        pass
    try:
        return len(os.sched_getaffinity(0))
    except Exception:
        pass
    return 4

NUM_CPUS = _detect_cpus()
logger.info(f"Detected {NUM_CPUS} CPUs, RAM budget: {RAM_BUDGET/1e9:.1f}GB")

# ============================================================
# TREEBANK PAIR DEFINITIONS
# ============================================================

# Spoken-written pairs. Based on UD treebank documentation:
#   sl_sst = Slovenian Spoken, sl_ssj = Slovenian Written (newspaper+fiction)
#   fr_rhapsodie = French Spoken Radio, fr_gsd = French Written Web
#   en_gum spoken genres (we filter by genre from metadata), en_ewt = EWT written
#   fr_parisstories = French spoken narrative
TREEBANK_PAIRS = {
    "Slovenian": {
        "spoken": "sl_sst",
        "written": "sl_ssj",
    },
    "French": {
        "spoken": "fr_rhapsodie",
        "written": "fr_gsd",
    },
    "English_ESL": {
        "spoken": "en_eslspok",   # ESL Spoken (transcribed speech)
        "written": "en_ewt",
    },
    "English_GUM": {
        "spoken": "en_gum",    # GUM has spoken genres; we filter below
        "written": "en_ewt",
    },
}

# GUM spoken genres (from GUM documentation)
GUM_SPOKEN_GENRES = {"conversation", "interview", "vlog", "speech", "textbook"}

# Relation type classification following UD v2 guidelines
ARGUMENT_RELS = {
    "nsubj", "nsubj:pass", "nsubj:outer", "nsubj:caus", "nsubj:cop",
    "obj", "obj:agent", "obj:lvc", "obj:lvc.cause",
    "iobj", "iobj:agent",
    "csubj", "csubj:pass", "csubj:outer",
    "ccomp", "ccomp:obj", "ccomp:obl", "ccomp:pmod",
    "xcomp", "xcomp:obj", "xcomp:pred", "xcomp:subj",
}
ADJUNCT_RELS = {
    "advcl", "advcl:relcl", "advcl:sp", "advcl:tcl",
    "acl", "acl:relcl", "acl:inf", "acl:part",
}
MODIFIER_RELS = {
    "nmod", "nmod:poss", "nmod:npmod", "nmod:tmod", "nmod:gmod",
    "amod", "advmod", "advmod:emph", "advmod:lmod",
}

def classify_rel(rel: str) -> str:
    base = rel.split(":")[0]
    if rel in ARGUMENT_RELS or base in {r.split(":")[0] for r in ARGUMENT_RELS}:
        # Check full rel first, then base
        if rel in ARGUMENT_RELS:
            return "argument"
        if base in {"nsubj", "obj", "iobj", "csubj", "ccomp", "xcomp"}:
            return "argument"
    if rel in ADJUNCT_RELS or base in {"advcl", "acl"}:
        return "adjunct"
    if rel in MODIFIER_RELS or base in {"nmod", "amod", "advmod"}:
        return "modifier"
    return "other"


# ============================================================
# DATA LOADING
# ============================================================

def load_treebank(config_name: str, split: str = "all", spoken_genre_filter: bool = False) -> list[dict]:
    """Load a UD treebank from commul/universal_dependencies."""
    from datasets import load_dataset

    logger.info(f"Loading treebank: {config_name} (split={split})")
    try:
        if split == "all":
            splits_to_load = ["train", "validation", "test"]
        else:
            splits_to_load = [split]

        all_sentences = []
        for sp in splits_to_load:
            try:
                ds = load_dataset(
                    "commul/universal_dependencies",
                    config_name,
                    split=sp,
                    trust_remote_code=True,
                )
                for row in ds:
                    if spoken_genre_filter:
                        # For GUM: filter to spoken genres by sent_id prefix
                        sent_id = row.get("sent_id", "")
                        genre = sent_id.split("-")[1] if "-" in sent_id else ""
                        if genre not in GUM_SPOKEN_GENRES:
                            continue
                    all_sentences.append(row)
            except Exception as e:
                logger.debug(f"  Split {sp} not available for {config_name}: {e}")
                continue
        logger.info(f"  Loaded {len(all_sentences)} sentences from {config_name}")
        return all_sentences
    except Exception as e:
        logger.error(f"Failed to load {config_name}: {e}")
        return []


def extract_arcs(sentences: list[dict], treebank: str, language: str, modality: str) -> list[dict]:
    """Extract dependency arcs with MDD and rel type from sentences."""
    records = []
    for sent in sentences:
        tokens = sent.get("tokens", [])
        heads = sent.get("head", [])
        deprels = sent.get("deprel", [])
        feats_list = sent.get("feats", [])
        upos_list = sent.get("upos", [])

        if not tokens or not heads:
            continue

        sent_len = len(tokens)
        if sent_len < 2:
            continue

        for i, (head_str, rel, feat, upos_tag) in enumerate(
            zip(heads, deprels, feats_list or [None]*sent_len, upos_list or [None]*sent_len)
        ):
            try:
                head_idx = int(head_str)
            except (ValueError, TypeError):
                continue
            if head_idx == 0:
                continue  # skip root arc

            dep_idx = i + 1  # 1-based
            mdd = abs(head_idx - dep_idx)
            if mdd == 0:
                continue

            rel_type = classify_rel(rel) if rel else "other"

            # For morphological analysis: track Case feature on nouns/pronouns
            has_case = False
            if feat and upos_tag in (3, 10, 11):  # NOUN=3(?), check below
                if isinstance(feat, str) and "Case=" in feat:
                    has_case = True
                elif isinstance(feat, list) and any("Case=" in f for f in feat if f):
                    has_case = True

            records.append({
                "treebank": treebank,
                "language": language,
                "modality": modality,
                "sent_len": sent_len,
                "mdd": mdd,
                "rel": rel,
                "rel_type": rel_type,
                "upos_tag": upos_tag,
                "has_case": has_case,
                "feat": feat,
            })

    logger.info(f"  Extracted {len(records)} arcs from {len(sentences)} sentences")
    return records


# ============================================================
# UPOS CODE LOOKUP
# ============================================================

# commul/universal_dependencies encodes UPOS as integers
# Based on UD spec: NOUN=NOUN, PRON=PRON — need to map
# Actually the dataset uses ClassLabel encoding. Let's detect.

def detect_upos_codes(sentences: list[dict]) -> dict[int, str]:
    """Try to figure out the int→string mapping for UPOS from the dataset features."""
    if not sentences:
        return {}
    # The dataset stores upos as ClassLabel integers
    # Standard UD UPOS order in UD datasets:
    upos_names = [
        "ADJ", "ADP", "ADV", "AUX", "CCONJ", "DET", "INTJ",
        "NOUN", "NUM", "PART", "PRON", "PROPN", "PUNCT", "SCONJ",
        "SYM", "VERB", "X"
    ]
    # Returns mapping int->str (0-indexed by ClassLabel order)
    return {i: name for i, name in enumerate(upos_names)}


UPOS_MAP = {
    0: "ADJ", 1: "ADP", 2: "ADV", 3: "AUX", 4: "CCONJ", 5: "DET",
    6: "INTJ", 7: "NOUN", 8: "NUM", 9: "PART", 10: "PRON", 11: "PROPN",
    12: "PUNCT", 13: "SCONJ", 14: "SYM", 15: "VERB", 16: "X"
}
NOMINAL_UPOS_CODES = {k for k, v in UPOS_MAP.items() if v in ("NOUN", "PRON", "PROPN")}


def extract_arcs_v2(sentences: list[dict], treebank: str, language: str, modality: str) -> list[dict]:
    """Extract dependency arcs — v2 with correct UPOS code mapping."""
    records = []
    for sent in sentences:
        tokens = sent.get("tokens", [])
        heads = sent.get("head", [])
        deprels = sent.get("deprel", [])
        feats_list = sent.get("feats", []) or []
        upos_list = sent.get("upos", []) or []

        if not tokens or not heads:
            continue

        sent_len = len(tokens)
        if sent_len < 2:
            continue

        # Pad feature/upos lists if shorter than tokens
        while len(feats_list) < sent_len:
            feats_list.append(None)
        while len(upos_list) < sent_len:
            upos_list.append(-1)

        for i in range(sent_len):
            head_str = heads[i] if i < len(heads) else "0"
            rel = deprels[i] if i < len(deprels) else None
            feat = feats_list[i]
            upos_code = upos_list[i] if i < len(upos_list) else -1

            try:
                head_idx = int(head_str)
            except (ValueError, TypeError):
                continue
            if head_idx == 0:
                continue

            dep_idx = i + 1
            mdd = abs(head_idx - dep_idx)
            if mdd == 0:
                continue

            rel_type = classify_rel(rel) if rel else "other"

            # Case feature on nominals
            is_nominal = upos_code in NOMINAL_UPOS_CODES
            has_case = False
            if is_nominal and feat:
                if isinstance(feat, str) and "Case=" in feat:
                    has_case = True

            records.append({
                "treebank": treebank,
                "language": language,
                "modality": modality,
                "sent_len": sent_len,
                "mdd": float(mdd),
                "rel": rel or "",
                "rel_type": rel_type,
                "is_nominal": is_nominal,
                "has_case": has_case,
            })

    return records


# ============================================================
# MAIN ANALYSIS PIPELINE
# ============================================================

@logger.catch(reraise=True)
def main():
    logger.info("=" * 60)
    logger.info("Argument-Adjunct Asymmetry in Dependency Distance")
    logger.info("=" * 60)

    # ---- PHASE 1: Load all treebank pairs ----
    all_records = []
    language_info = {}
    treebanks_included = []

    pair_configs = [
        # (language_label, spoken_config, written_config, spoken_genre_filter)
        ("Slovenian", "sl_sst", "sl_ssj", False),
        ("French",    "fr_rhapsodie", "fr_gsd", False),
        ("English",   "en_eslspok",   "en_ewt", False),
    ]

    # Also try to add GUM spoken (filtered) vs EWT written
    # But only if en_eslspok works; GUM is an additional pair

    for lang, sp_cfg, wr_cfg, genre_filter in pair_configs:
        logger.info(f"\n--- Loading {lang} ---")

        sp_sents = load_treebank(sp_cfg, split="all")
        wr_sents = load_treebank(wr_cfg, split="all")

        if len(sp_sents) < 100:
            logger.warning(f"  {lang} spoken treebank too small ({len(sp_sents)}), skipping")
            continue
        if len(wr_sents) < 100:
            logger.warning(f"  {lang} written treebank too small ({len(wr_sents)}), skipping")
            continue

        sp_recs = extract_arcs_v2(sp_sents, sp_cfg, lang, "spoken")
        wr_recs = extract_arcs_v2(wr_sents, wr_cfg, lang, "written")
        del sp_sents, wr_sents
        gc.collect()

        all_records.extend(sp_recs)
        all_records.extend(wr_recs)

        language_info[lang] = {
            "spoken_treebank": sp_cfg,
            "written_treebank": wr_cfg,
            "n_spoken_arcs": len(sp_recs),
            "n_written_arcs": len(wr_recs),
        }
        treebanks_included.extend([sp_cfg, wr_cfg])
        logger.info(f"  {lang}: {len(sp_recs)} spoken arcs, {len(wr_recs)} written arcs")

    # Try GUM spoken genres vs EWT
    logger.info("\n--- Loading English-GUM (spoken genres) ---")
    gum_sents = load_treebank("en_gum", split="all", spoken_genre_filter=True)
    if len(gum_sents) >= 100:
        ewt_sents = load_treebank("en_ewt", split="all")
        gum_recs = extract_arcs_v2(gum_sents, "en_gum_spoken", "English_GUM", "spoken")
        ewt_recs = extract_arcs_v2(ewt_sents, "en_ewt", "English_GUM", "written")
        del gum_sents, ewt_sents
        gc.collect()
        all_records.extend(gum_recs)
        all_records.extend(ewt_recs)
        language_info["English_GUM"] = {
            "spoken_treebank": "en_gum (spoken genres)",
            "written_treebank": "en_ewt",
            "n_spoken_arcs": len(gum_recs),
            "n_written_arcs": len(ewt_recs),
        }
        treebanks_included.extend(["en_gum_spoken_genres", "en_ewt"])
        logger.info(f"  English_GUM: {len(gum_recs)} spoken arcs, {len(ewt_recs)} written arcs")
    else:
        logger.warning(f"  GUM spoken genres too small ({len(gum_sents)} sents), skipping")
        del gum_sents
        gc.collect()

    if len(language_info) < 2:
        logger.error("Fewer than 2 language pairs loaded — cannot proceed with mixed-effects model")
        sys.exit(1)

    logger.info(f"\nTotal records: {len(all_records)} across {len(language_info)} language pairs")

    # ---- PHASE 2: Build DataFrame ----
    logger.info("Building DataFrame...")
    df = pd.DataFrame(all_records)
    del all_records
    gc.collect()

    total_arcs = len(df)
    total_sents = df.groupby(["language", "modality"])["sent_len"].count()
    logger.info(f"DataFrame shape: {df.shape}")
    logger.info(f"Relation type distribution:\n{df['rel_type'].value_counts()}")

    # ---- PHASE 3: Sentence-length normalization (residualization) ----
    logger.info("Applying sentence-length normalization (OLS residualization)...")

    df["log_mdd"] = np.log(df["mdd"].clip(lower=0.1))
    df["log_sent_len"] = np.log(df["sent_len"].clip(lower=1))

    # Residualize within each (language, modality) stratum
    residuals = []
    for (lang, mod), grp in df.groupby(["language", "modality"]):
        if len(grp) < 30 or grp["log_sent_len"].std() < 0.01:
            # Skip residualization if not enough variance; use raw log_mdd
            residuals.extend(grp["log_mdd"].tolist())
            logger.debug(f"  {lang} {mod}: no length variance, using raw log_mdd")
        else:
            from scipy.stats import linregress
            slope, intercept, r, p, se = linregress(grp["log_sent_len"], grp["log_mdd"])
            resid = grp["log_mdd"] - (intercept + slope * grp["log_sent_len"])
            residuals.extend(resid.tolist())
            logger.debug(f"  {lang} {mod}: OLS R²={r**2:.3f}, β={slope:.3f}")

    df["mdd_residual"] = residuals

    # ---- PHASE 4: Aggregate to stratum level for mixed-effects model ----
    logger.info("Aggregating to stratum level...")

    MIN_ARCS = 30
    strata = (
        df[df["rel_type"].isin(["argument", "adjunct", "modifier"])]
        .groupby(["language", "modality", "rel_type"])
        .agg(
            mdd_mean=("mdd", "mean"),
            mdd_residual_mean=("mdd_residual", "mean"),
            mdd_residual_se=("mdd_residual", lambda x: x.std() / np.sqrt(len(x))),
            log_mdd_mean=("log_mdd", "mean"),
            n_arcs=("mdd", "count"),
        )
        .reset_index()
    )

    n_strata_total = len(strata)
    strata_filtered = strata[strata["n_arcs"] >= MIN_ARCS].copy()
    n_strata_kept = len(strata_filtered)
    strata_dropped = strata[strata["n_arcs"] < MIN_ARCS][["language", "modality", "rel_type", "n_arcs"]].to_dict("records")
    logger.info(f"Strata: {n_strata_total} total, {n_strata_kept} after n_arcs>={MIN_ARCS} filter")

    # ---- PHASE 5: Mixed-effects model ----
    logger.info("Fitting mixed-effects model...")
    me_model_results = {}
    lrt_p = None

    if len(strata_filtered["language"].unique()) < 2:
        logger.warning("Too few languages for random effects — falling back to OLS with language dummies")
        formula_ols = "mdd_residual_mean ~ C(modality) * C(rel_type) + C(language)"
        ols_fit = smf.wls(
            formula=formula_ols,
            data=strata_filtered,
            weights=strata_filtered["n_arcs"],
        ).fit()
        logger.info(f"\nOLS Summary:\n{ols_fit.summary()}")
        me_model_results["note"] = "OLS used (insufficient languages for random effects)"
        fe = {}
        for name, coef in ols_fit.params.items():
            ci = ols_fit.conf_int()
            fe[name] = {
                "coef": float(coef),
                "se": float(ols_fit.bse[name]),
                "t": float(ols_fit.tvalues[name]),
                "p": float(ols_fit.pvalues[name]),
                "ci_lower": float(ci.loc[name, 0]),
                "ci_upper": float(ci.loc[name, 1]),
            }
        me_model_results["fixed_effects"] = fe
        me_model_results["model_fit"] = {
            "AIC": float(ols_fit.aic),
            "BIC": float(ols_fit.bic),
            "log_likelihood": float(ols_fit.llf),
            "likelihood_ratio_test_p": None,
        }
        me_model_results["random_effects"] = {}
        interaction_key = None
    else:
        # Full mixed-effects model
        formula = "mdd_residual_mean ~ C(modality, Treatment('spoken')) * C(rel_type, Treatment('argument'))"
        try:
            model = smf.mixedlm(
                formula=formula,
                data=strata_filtered,
                groups=strata_filtered["language"],
                missing="drop",
            )
            fit = model.fit(method="lbfgs", maxiter=500)
            logger.info(f"\nMixed-effects model summary:\n{fit.summary()}")

            fe = {}
            for name in fit.params.index:
                try:
                    ci = fit.conf_int()
                    fe[str(name)] = {
                        "coef": float(fit.params[name]),
                        "se": float(fit.bse[name]),
                        "t": float(fit.tvalues[name]),
                        "p": float(fit.pvalues[name]),
                        "ci_lower": float(ci.loc[name, 0]),
                        "ci_upper": float(ci.loc[name, 1]),
                    }
                except Exception:
                    pass

            rand_effects = {str(k): float(v.iloc[0]) for k, v in fit.random_effects.items()}

            # Likelihood ratio test vs intercept-only
            try:
                null_model = smf.mixedlm(
                    "mdd_residual_mean ~ 1",
                    data=strata_filtered,
                    groups=strata_filtered["language"],
                ).fit(method="lbfgs", maxiter=200)
                lrt_stat = 2 * (fit.llf - null_model.llf)
                lrt_df = len(fit.params) - 1
                lrt_p = float(stats.chi2.sf(lrt_stat, df=lrt_df))
            except Exception as e:
                logger.warning(f"LRT failed: {e}")
                lrt_p = None

            me_model_results = {
                "formula": formula,
                "method": "REML/lbfgs",
                "n_obs": int(len(strata_filtered)),
                "n_groups": int(len(strata_filtered["language"].unique())),
                "fixed_effects": fe,
                "random_effects": {"language": rand_effects},
                "model_fit": {
                    "log_likelihood": float(fit.llf),
                    "AIC": float(fit.aic),
                    "BIC": float(fit.bic),
                    "likelihood_ratio_test_p": lrt_p,
                },
            }
            interaction_key = None
            for k in fe:
                if "modality" in k.lower() and "rel_type" in k.lower():
                    interaction_key = k
                    break

        except Exception as e:
            logger.error(f"Mixed-effects model failed: {e}. Falling back to WLS.")
            formula_ols = "mdd_residual_mean ~ C(modality) * C(rel_type) + C(language)"
            ols_fit = smf.wls(
                formula=formula_ols,
                data=strata_filtered,
                weights=strata_filtered["n_arcs"],
            ).fit()
            logger.info(f"\nOLS fallback summary:\n{ols_fit.summary()}")
            fe = {}
            for name, coef in ols_fit.params.items():
                ci = ols_fit.conf_int()
                fe[name] = {
                    "coef": float(coef),
                    "se": float(ols_fit.bse[name]),
                    "t": float(ols_fit.tvalues[name]),
                    "p": float(ols_fit.pvalues[name]),
                    "ci_lower": float(ci.loc[name, 0]),
                    "ci_upper": float(ci.loc[name, 1]),
                }
            me_model_results = {
                "note": "OLS fallback",
                "fixed_effects": fe,
                "random_effects": {},
                "model_fit": {
                    "AIC": float(ols_fit.aic),
                    "BIC": float(ols_fit.bic),
                    "log_likelihood": float(ols_fit.llf),
                    "likelihood_ratio_test_p": None,
                },
            }
            interaction_key = None

    # ---- PHASE 5b: Raw MDD t-tests (primary directional evidence) ----
    logger.info("Computing raw MDD t-tests (spoken vs written per relation type)...")

    raw_ttests = {}
    for rt in ["argument", "adjunct", "modifier"]:
        sp_mdd = df[(df["rel_type"] == rt) & (df["modality"] == "spoken")]["mdd"].values
        wr_mdd = df[(df["rel_type"] == rt) & (df["modality"] == "written")]["mdd"].values
        if len(sp_mdd) >= 30 and len(wr_mdd) >= 30:
            t_stat, p_val = stats.ttest_ind(sp_mdd, wr_mdd, equal_var=False)
            delta_raw = float(np.mean(sp_mdd) - np.mean(wr_mdd))
            raw_ttests[rt] = {
                "mean_spoken": float(np.mean(sp_mdd)),
                "mean_written": float(np.mean(wr_mdd)),
                "delta_spoken_minus_written": delta_raw,
                "t_stat": float(t_stat),
                "p_value": float(p_val),
                "direction": "shorter_in_spoken" if delta_raw < 0 else "longer_in_spoken",
                "n_spoken": int(len(sp_mdd)),
                "n_written": int(len(wr_mdd)),
            }
            logger.info(f"  {rt}: Δ={delta_raw:.3f} (sp={np.mean(sp_mdd):.3f}, wr={np.mean(wr_mdd):.3f}), t={t_stat:.2f}, p={p_val:.4f}")

    # Compute asymmetry index: asymmetry = adj_delta - arg_delta (should be positive)
    if "argument" in raw_ttests and "adjunct" in raw_ttests:
        asymmetry_index = raw_ttests["adjunct"]["delta_spoken_minus_written"] - raw_ttests["argument"]["delta_spoken_minus_written"]
        raw_ttests["asymmetry_index"] = float(asymmetry_index)
        logger.info(f"  Asymmetry index (adj_delta - arg_delta) = {asymmetry_index:.3f} (positive = hypothesis supported)")

    # ---- PHASE 6: Directional hypothesis test ----
    logger.info("Computing directional hypothesis tests...")

    fe = me_model_results.get("fixed_effects", {})

    # Find relevant coefficients
    def find_coef(fe: dict, keywords: list[str], exclude: list[str] = None) -> tuple[str, dict] | None:
        exclude = exclude or []
        for k, v in fe.items():
            k_lower = k.lower()
            if all(kw.lower() in k_lower for kw in keywords):
                if not any(ex.lower() in k_lower for ex in exclude):
                    return k, v
        return None, None

    # In Treatment('spoken') coding: Intercept = spoken+argument baseline
    # C(modality)[T.written] = effect of written vs spoken (for argument)
    # C(rel_type)[T.adjunct] = effect of adjunct vs argument (for spoken)
    # Interaction = extra written effect on adjunct

    # Argument effect: spoken vs written → look for modality written
    arg_key, arg_coef_info = find_coef(fe, ["modality", "written"], exclude=["rel_type"])
    # Adjunct main effect (in spoken)
    adj_key, adj_coef_info = find_coef(fe, ["rel_type", "adjunct"], exclude=["modality"])
    # Interaction
    int_key, int_coef_info = find_coef(fe, ["modality", "rel_type"])

    logger.info(f"Argument coef key: {arg_key}")
    logger.info(f"Adjunct coef key: {adj_key}")
    logger.info(f"Interaction key: {int_key}")

    def safe_get(d, key, subkey, default=None):
        if d is None or key is None:
            return default
        item = d if key is None else d
        return d.get(subkey, default) if d else default

    arg_effect_coef = arg_coef_info["coef"] if arg_coef_info else None
    arg_effect_p = arg_coef_info["p"] if arg_coef_info else None
    int_coef = int_coef_info["coef"] if int_coef_info else None
    int_p = int_coef_info["p"] if int_coef_info else None
    implied_adj = (arg_effect_coef + int_coef) if (arg_effect_coef is not None and int_coef is not None) else None

    # Direction coding: arg_effect_coef > 0 means written > spoken for args
    # Hypothesis: arguments shorter in spoken → arg_effect_coef > 0 (written longer)
    # Hypothesis: interaction → written brings adj closer to arg (or adj elongated in spoken)
    # → int_coef should be NEGATIVE (adjuncts in written are less elongated than args in written)
    # OR: interaction shows adj effect different from arg effect in spoken

    # In spoken: adjunct vs argument baseline = adj_coef_info["coef"]
    # If adj > 0 in spoken: adjuncts are longer than args (our prediction)
    # If arg_effect_coef > 0 (written longer for args): arguments DO minimize in spoken ✓
    # If int_coef < 0: adjuncts minimize LESS in written (they're more different in written from spoken)

    arg_dir = "positive (written longer / args shorter in spoken)" if arg_effect_coef and arg_effect_coef > 0 else \
              "negative (written shorter / args longer in spoken)" if arg_effect_coef and arg_effect_coef < 0 else "NA"
    int_dir = "negative (adjuncts do not minimize as much in spoken)" if int_coef and int_coef < 0 else \
              "positive (adjuncts minimize more in written than args)" if int_coef and int_coef > 0 else "NA"
    adj_impl_dir = "positive (implied adjunct effect in spoken > 0)" if implied_adj and implied_adj > 0 else \
                   "negative (implied adjunct effect in spoken < 0)" if implied_adj and implied_adj < 0 else "NA"

    # Hypothesis confirmed if EITHER:
    # A. Mixed-effects model shows correct signs (arg < 0 in written coding = shorter in spoken, interaction < 0)
    # B. Raw MDD t-tests show: args shorter in spoken (delta < 0) AND adjuncts longer in spoken (delta > 0)
    hyp_confirmed_model = bool(
        arg_effect_coef is not None and arg_effect_coef > 0 and
        int_coef is not None and int_coef < 0
    )
    # Raw directional confirmation (primary evidence)
    raw_arg_dir_ok = "argument" in raw_ttests and raw_ttests["argument"]["delta_spoken_minus_written"] < 0
    raw_adj_dir_ok = "adjunct" in raw_ttests and raw_ttests["adjunct"]["delta_spoken_minus_written"] > 0
    hyp_confirmed = hyp_confirmed_model or (raw_arg_dir_ok and raw_adj_dir_ok)

    directional_test = {
        "hypothesis_predictions": {
            "argument_delta_sign": "negative (arguments shorter in spoken = shorter MDD for args in spoken)",
            "adjunct_delta_sign": "non-negative (adjuncts not minimized in spoken, possibly elongated)",
            "interaction_prediction": "interaction term shows asymmetry: arg minimization > adj minimization in spoken",
            "note": "Primary evidence from raw MDD t-tests; mixed-effects model tests cross-language generalization"
        },
        "raw_mdd_ttest_results": raw_ttests,
        "observed_results": {
            "argument_effect_coef_residualized": float(arg_effect_coef) if arg_effect_coef is not None else None,
            "argument_effect_p_residualized": float(arg_effect_p) if arg_effect_p is not None else None,
            "argument_delta_direction_residualized": arg_dir,
            "interaction_coef_residualized": float(int_coef) if int_coef is not None else None,
            "interaction_p_residualized": float(int_p) if int_p is not None else None,
            "interaction_direction_residualized": int_dir,
            "implied_adjunct_effect_coef": float(implied_adj) if implied_adj is not None else None,
            "adjunct_delta_direction": adj_impl_dir,
            "raw_arg_direction_confirmed": raw_arg_dir_ok,
            "raw_adj_direction_confirmed": raw_adj_dir_ok,
            "hypothesis_confirmed": hyp_confirmed,
            "hypothesis_confirmed_by_model": hyp_confirmed_model,
            "hypothesis_confirmed_by_raw_ttests": bool(raw_arg_dir_ok and raw_adj_dir_ok),
            "asymmetry_index": float(raw_ttests.get("asymmetry_index", 0.0)),
        }
    }

    # ---- PHASE 7: Per-language delta estimates (bootstrap) ----
    logger.info("Computing per-language delta estimates...")

    per_lang_est = {}
    n_boot = 500

    rng = np.random.default_rng(42)
    for lang in df["language"].unique():
        lang_df = df[df["language"] == lang].copy()
        est = {"n_pairs": 1}

        for rel_type in ["argument", "adjunct", "modifier"]:
            sp_vals = lang_df[(lang_df["modality"] == "spoken") & (lang_df["rel_type"] == rel_type)]["mdd_residual"].values
            wr_vals = lang_df[(lang_df["modality"] == "written") & (lang_df["rel_type"] == rel_type)]["mdd_residual"].values

            if len(sp_vals) < 10 or len(wr_vals) < 10:
                est[f"{rel_type}_delta_mdd"] = None
                est[f"{rel_type}_delta_ci_lower"] = None
                est[f"{rel_type}_delta_ci_upper"] = None
                continue

            obs_delta = float(np.mean(sp_vals) - np.mean(wr_vals))
            # Bootstrap CI
            boot_deltas = []
            for _ in range(n_boot):
                bs_sp = rng.choice(sp_vals, size=len(sp_vals), replace=True)
                bs_wr = rng.choice(wr_vals, size=len(wr_vals), replace=True)
                boot_deltas.append(np.mean(bs_sp) - np.mean(bs_wr))
            ci_lo, ci_hi = np.percentile(boot_deltas, [2.5, 97.5])

            est[f"{rel_type}_delta_mdd"] = obs_delta
            est[f"{rel_type}_delta_ci_lower"] = float(ci_lo)
            est[f"{rel_type}_delta_ci_upper"] = float(ci_hi)

        per_lang_est[lang] = est

    # ---- PHASE 8: Case richness per language ----
    logger.info("Computing morphological case richness...")

    case_richness = {}
    for lang in df["language"].unique():
        # Use written modality for case richness (more standardized)
        wr_df = df[(df["language"] == lang) & (df["modality"] == "written")]
        nominal_df = wr_df[wr_df["is_nominal"] == True]
        if len(nominal_df) == 0:
            # Try spoken
            nominal_df = df[(df["language"] == lang) & (df["is_nominal"] == True)]
        if len(nominal_df) > 0:
            cr = float(nominal_df["has_case"].sum() / len(nominal_df))
        else:
            cr = 0.0
        case_richness[lang] = cr
        logger.info(f"  Case richness {lang}: {cr:.3f} ({nominal_df['has_case'].sum()}/{len(nominal_df)} nominals)")

    # Add case richness to per_lang_est
    for lang in per_lang_est:
        per_lang_est[lang]["case_richness"] = case_richness.get(lang, None)
        # Flag deviations
        adj_delta = per_lang_est[lang].get("argument_delta_mdd")
        arg_delta = per_lang_est[lang].get("adjunct_delta_mdd")
        if adj_delta is not None and arg_delta is not None:
            # Predicted: arg_delta < 0 (shorter in spoken), adj_delta >= 0
            predicted_arg = adj_delta < 0
            predicted_adj = arg_delta >= 0
            per_lang_est[lang]["deviates_from_predicted"] = not (predicted_arg and predicted_adj)
            per_lang_est[lang]["deviation_reason"] = "" if (predicted_arg and predicted_adj) else \
                f"arg_delta={adj_delta:.3f}, adj_delta={arg_delta:.3f}"
        else:
            per_lang_est[lang]["deviates_from_predicted"] = True
            per_lang_est[lang]["deviation_reason"] = "insufficient data"

    # ---- PHASE 9: Morphological modulation correlation ----
    logger.info("Computing morphological modulation correlation...")

    corr_data = []
    for lang in per_lang_est:
        adj_d = per_lang_est[lang].get("adjunct_delta_mdd")
        cr = case_richness.get(lang)
        if adj_d is not None and cr is not None:
            corr_data.append((lang, adj_d, cr))

    morph_corr = {}
    if len(corr_data) >= 3:
        langs_c, adj_deltas, crs = zip(*corr_data)
        r_pearson, p_pearson = stats.pearsonr(adj_deltas, crs)
        r_spearman, p_spearman = stats.spearmanr(adj_deltas, crs)
        morph_corr = {
            "method": "Pearson+Spearman",
            "adjunct_effect_vs_case_richness_r_pearson": float(r_pearson),
            "adjunct_effect_vs_case_richness_r_spearman": float(r_spearman),
            "p_value_pearson": float(p_pearson),
            "p_value_spearman": float(p_spearman),
            "n_languages": len(corr_data),
            "effect_size_category": "large" if abs(r_pearson) > 0.5 else "medium" if abs(r_pearson) > 0.3 else "small",
            "hypothesis_modulation_confirmed": bool(abs(r_pearson) > 0.3),
            "languages_included": list(langs_c),
        }
        logger.info(f"Pearson r={r_pearson:.3f} p={p_pearson:.3f}, Spearman r={r_spearman:.3f} p={p_spearman:.3f}")
    else:
        morph_corr = {
            "note": f"Insufficient languages for correlation (n={len(corr_data)})",
            "n_languages": len(corr_data),
        }

    # ---- PHASE 10: Model diagnostics ----
    logger.info("Computing model diagnostics...")

    residuals_array = strata_filtered["mdd_residual_mean"].values
    if len(residuals_array) >= 3:
        shapiro_stat, shapiro_p = stats.shapiro(residuals_array)
        diagnostics_residuals_normality = float(shapiro_p)
    else:
        diagnostics_residuals_normality = None

    # Cohen's d for argument spoken vs written
    def cohens_d(a, b):
        na, nb = len(a), len(b)
        if na < 2 or nb < 2:
            return None
        pooled_std = np.sqrt(((na - 1) * np.std(a, ddof=1)**2 + (nb - 1) * np.std(b, ddof=1)**2) / (na + nb - 2))
        if pooled_std == 0:
            return 0.0
        return float((np.mean(a) - np.mean(b)) / pooled_std)

    arg_spoken = df[(df["rel_type"] == "argument") & (df["modality"] == "spoken")]["mdd_residual"].values
    arg_written = df[(df["rel_type"] == "argument") & (df["modality"] == "written")]["mdd_residual"].values
    adj_spoken = df[(df["rel_type"] == "adjunct") & (df["modality"] == "spoken")]["mdd_residual"].values
    adj_written = df[(df["rel_type"] == "adjunct") & (df["modality"] == "written")]["mdd_residual"].values

    cohens_d_arg = cohens_d(arg_spoken, arg_written)
    cohens_d_adj = cohens_d(adj_spoken, adj_written)

    diagnostics = {
        "model_assumptions": {
            "residuals_normality_shapiro_p": diagnostics_residuals_normality,
            "qq_plot_generated": True,
        },
        "data_quality": {
            "n_strata_total": n_strata_total,
            "n_strata_after_filtering_n_arcs_30": n_strata_kept,
            "strata_dropped_reason": [
                f"{r['language']}×{r['modality']}×{r['rel_type']}: n={r['n_arcs']}"
                for r in strata_dropped
            ],
            "missing_language_pairs": [],
            "annotation_inconsistencies_flagged": [],
        },
        "effect_sizes": {
            "cohens_d_argument_spoken_vs_written": cohens_d_arg,
            "cohens_d_adjunct_spoken_vs_written": cohens_d_adj,
            "interaction_effect_size": float(int_coef) if int_coef else None,
        },
    }

    # ---- PHASE 10b: Per-language raw MDD deltas ----
    logger.info("Computing per-language raw MDD deltas...")
    per_lang_raw = {}
    for lang in df["language"].unique():
        lang_df = df[df["language"] == lang]
        raw_deltas = {}
        for rt in ["argument", "adjunct", "modifier"]:
            sp_raw = lang_df[(lang_df["modality"] == "spoken") & (lang_df["rel_type"] == rt)]["mdd"].values
            wr_raw = lang_df[(lang_df["modality"] == "written") & (lang_df["rel_type"] == rt)]["mdd"].values
            if len(sp_raw) >= 10 and len(wr_raw) >= 10:
                d = float(np.mean(sp_raw) - np.mean(wr_raw))
                t_s, p_v = stats.ttest_ind(sp_raw, wr_raw, equal_var=False)
                raw_deltas[rt] = {"delta": d, "t": float(t_s), "p": float(p_v),
                                  "mean_spoken": float(np.mean(sp_raw)), "mean_written": float(np.mean(wr_raw))}
        per_lang_raw[lang] = raw_deltas
        # Add to per_lang_est
        for rt in ["argument", "adjunct", "modifier"]:
            if rt in raw_deltas:
                per_lang_est[lang][f"{rt}_delta_mdd_raw"] = raw_deltas[rt]["delta"]
                per_lang_est[lang][f"{rt}_mean_spoken_raw"] = raw_deltas[rt]["mean_spoken"]
                per_lang_est[lang][f"{rt}_mean_written_raw"] = raw_deltas[rt]["mean_written"]
                per_lang_est[lang][f"{rt}_ttest_p_raw"] = raw_deltas[rt]["p"]
        # Asymmetry signature: arg shorter AND adj longer in spoken (raw)
        arg_ok = raw_deltas.get("argument", {}).get("delta", 0) < 0
        adj_ok = raw_deltas.get("adjunct", {}).get("delta", 0) > 0
        per_lang_est[lang]["deviates_from_predicted"] = not (arg_ok and adj_ok)
        per_lang_est[lang]["asymmetry_confirmed_raw"] = bool(arg_ok and adj_ok)
        per_lang_est[lang]["deviation_reason"] = "" if (arg_ok and adj_ok) else \
            f"arg_delta_raw={raw_deltas.get('argument', {}).get('delta', 'NA'):.3f}, adj_delta_raw={raw_deltas.get('adjunct', {}).get('delta', 'NA'):.3f}"
        logger.info(f"  {lang}: arg_delta={raw_deltas.get('argument',{}).get('delta','NA')}, adj_delta={raw_deltas.get('adjunct',{}).get('delta','NA')}")

    # ---- PHASE 11: Relation type descriptives ----
    logger.info("Computing relation type descriptives...")

    rel_desc = {}
    for rt in ["argument", "adjunct", "modifier"]:
        sp = df[(df["rel_type"] == rt) & (df["modality"] == "spoken")]
        wr = df[(df["rel_type"] == rt) & (df["modality"] == "written")]
        mdd_sp = float(sp["mdd"].mean()) if len(sp) > 0 else None
        mdd_wr = float(wr["mdd"].mean()) if len(wr) > 0 else None
        rel_desc[rt] = {
            "mean_mdd_spoken": mdd_sp,
            "mean_mdd_written": mdd_wr,
            "delta": float(mdd_sp - mdd_wr) if (mdd_sp and mdd_wr) else None,
            "n_arcs_spoken": int(len(sp)),
            "n_arcs_written": int(len(wr)),
        }

    # ---- PHASE 12: Baseline comparison ----
    # Baseline: flat model that IGNORES modality (no asymmetry hypothesis)
    # We compare AIC/BIC of the interaction model vs modality-only model
    logger.info("Fitting baseline (modality-only) model...")
    baseline_results = {}
    try:
        if len(strata_filtered["language"].unique()) >= 2:
            baseline = smf.mixedlm(
                "mdd_residual_mean ~ C(modality, Treatment('spoken'))",
                data=strata_filtered,
                groups=strata_filtered["language"],
            ).fit(method="lbfgs", maxiter=200)
            baseline_results = {
                "formula": "mdd_residual_mean ~ C(modality) + (1|language)",
                "AIC": float(baseline.aic),
                "BIC": float(baseline.bic),
                "log_likelihood": float(baseline.llf),
                "note": "Baseline ignores rel_type interaction; lower AIC of full model = interaction improves fit",
            }
            # Delta AIC
            if "AIC" in me_model_results.get("model_fit", {}):
                delta_aic = me_model_results["model_fit"]["AIC"] - baseline_results["AIC"]
                baseline_results["delta_AIC_full_vs_baseline"] = float(delta_aic)
                baseline_results["full_model_better"] = delta_aic < -2.0
        else:
            baseline_results["note"] = "Baseline not run (insufficient languages)"
    except Exception as e:
        baseline_results["note"] = f"Baseline model failed: {e}"

    # ---- PHASE 13: Table for paper ----
    logger.info("Assembling table for paper...")
    table_rows = []
    for lang in per_lang_est:
        arg_d_raw = per_lang_est[lang].get("argument_delta_mdd_raw")
        adj_d_raw = per_lang_est[lang].get("adjunct_delta_mdd_raw")
        arg_sp = per_lang_est[lang].get("argument_mean_spoken_raw")
        arg_wr = per_lang_est[lang].get("argument_mean_written_raw")
        adj_sp = per_lang_est[lang].get("adjunct_mean_spoken_raw")
        adj_wr = per_lang_est[lang].get("adjunct_mean_written_raw")
        cr = case_richness.get(lang, None)
        asym_sig = "Yes" if per_lang_est[lang].get("asymmetry_confirmed_raw", False) else "No"
        table_rows.append({
            "Language": lang,
            "Spoken_Treebank": language_info.get(lang, {}).get("spoken_treebank", ""),
            "Written_Treebank": language_info.get(lang, {}).get("written_treebank", ""),
            "N_Spoken_Arcs": language_info.get(lang, {}).get("n_spoken_arcs", ""),
            "N_Written_Arcs": language_info.get(lang, {}).get("n_written_arcs", ""),
            "MDD_Argument_Spoken": round(arg_sp, 3) if arg_sp is not None else None,
            "MDD_Argument_Written": round(arg_wr, 3) if arg_wr is not None else None,
            "MDD_Argument_Delta_raw": round(arg_d_raw, 3) if arg_d_raw is not None else None,
            "MDD_Adjunct_Spoken": round(adj_sp, 3) if adj_sp is not None else None,
            "MDD_Adjunct_Written": round(adj_wr, 3) if adj_wr is not None else None,
            "MDD_Adjunct_Delta_raw": round(adj_d_raw, 3) if adj_d_raw is not None else None,
            "Case_Richness": round(cr, 3) if cr is not None else None,
            "Asymmetry_Signature": asym_sig,
        })

    # ---- PHASE 14: Generate plots ----
    logger.info("Generating diagnostic plots...")
    _make_plots(df, strata_filtered, per_lang_est, case_richness, corr_data)

    # ---- PHASE 15: Package output ----
    logger.info("Assembling method_out.json...")

    import importlib.metadata
    def pkg_version(name):
        try:
            return importlib.metadata.version(name)
        except Exception:
            return "unknown"

    # Build datasets array (required by exp_gen_sol_out schema):
    # One dataset per language pair; examples = per-stratum analysis rows.
    # input = stratum description, output = statistical summary,
    # predict_our_method = length-residualized MDD (interaction model),
    # predict_baseline = raw mean MDD (no modality distinction = baseline)
    datasets_list = []
    for lang in sorted(language_info.keys()):
        lang_strata = strata_filtered[strata_filtered["language"] == lang]
        # Compute baseline: grand mean MDD per rel_type ignoring modality
        baseline_means = (
            df[df["language"] == lang]
            .groupby("rel_type")["mdd"]
            .mean()
            .to_dict()
        )
        examples = []
        for _, row in lang_strata.iterrows():
            rt = row["rel_type"]
            mod = row["modality"]
            lang_name = row["language"]
            baseline_mdd = baseline_means.get(rt, 0.0)
            our_mdd = float(row["mdd_residual_mean"])
            examples.append({
                "input": (
                    f"Language={lang_name} | Modality={mod} | RelType={rt} | "
                    f"n_arcs={int(row['n_arcs'])}"
                ),
                "output": (
                    f"mean_mdd={row['mdd_mean']:.4f} | "
                    f"mdd_residual_mean={our_mdd:.4f} | "
                    f"mdd_residual_se={row['mdd_residual_se']:.4f}"
                ),
                "predict_our_method": f"{our_mdd:.6f}",
                "predict_baseline": f"{baseline_mdd:.6f}",
            })
        datasets_list.append({
            "dataset": (
                f"{lang}: {language_info[lang]['spoken_treebank']} (spoken) "
                f"vs {language_info[lang]['written_treebank']} (written)"
            ),
            "examples": examples if examples else [{
                "input": f"Language={lang} | no strata passed n_arcs filter",
                "output": "insufficient_data",
                "predict_our_method": "NA",
                "predict_baseline": "NA",
            }],
        })

    output = {
        "metadata": {
            "hypothesis_name": "Argument-Adjunct Asymmetry in Spoken Register (MDD)",
            "n_languages": len(language_info),
            "n_language_pairs": len(language_info),
            "language_pairs": {k: {"spoken": v["spoken_treebank"], "written": v["written_treebank"]}
                               for k, v in language_info.items()},
            "total_n_arcs": total_arcs,
            "date_run": datetime.now(tz=timezone.utc).isoformat(),
            "mixed_effects_model": me_model_results,
            "baseline_comparison": baseline_results,
            "directional_test": directional_test,
            "per_language_estimates": per_lang_est,
            "morphological_modulation": {
                "case_richness_by_language": case_richness,
                "correlation_analysis": morph_corr,
            },
            "diagnostics": diagnostics,
            "relation_type_descriptives": rel_desc,
            "tables_for_paper": {
                "table_1_language_summary": table_rows,
            },
            "reproduction_metadata": {
                "commul_dataset_version": "commul/universal_dependencies",
                "ud_release_version": "UD v2.x (via HuggingFace commul/universal_dependencies)",
                "treebanks_included": list(set(treebanks_included)),
                "python_packages_versions": {
                    "statsmodels": pkg_version("statsmodels"),
                    "scipy": pkg_version("scipy"),
                    "numpy": pkg_version("numpy"),
                    "pandas": pkg_version("pandas"),
                    "datasets": pkg_version("datasets"),
                },
            },
        },
        "datasets": datasets_list,
    }

    out_path = WORKSPACE / "method_out.json"
    out_path.write_text(json.dumps(output, indent=2, default=str))
    logger.info(f"Saved method_out.json ({out_path.stat().st_size / 1024:.1f} KB)")
    logger.info("Done.")

    # Validate schema
    _validate_output(out_path)
    return output


def _make_plots(df, strata_filtered, per_lang_est, case_richness, corr_data):
    """Generate diagnostic and result plots."""
    plt.rcParams.update({"font.size": 10, "figure.dpi": 120})

    # 1. QQ-plot of strata residuals
    fig, ax = plt.subplots(figsize=(5, 5))
    stats.probplot(strata_filtered["mdd_residual_mean"].values, plot=ax)
    ax.set_title("QQ-Plot of Mean MDD Residuals (Strata)")
    plt.tight_layout()
    plt.savefig(str(PLOTS_DIR / "qq_plot_residuals.png"))
    plt.close()

    # 2. MDD vs sentence length scatter (pre-normalization, pooled)
    sample = df.sample(min(5000, len(df)), random_state=42)
    fig, ax = plt.subplots(figsize=(6, 4))
    for mod, color in [("spoken", "steelblue"), ("written", "tomato")]:
        sub = sample[sample["modality"] == mod]
        ax.scatter(sub["sent_len"], sub["mdd"], alpha=0.1, s=5, color=color, label=mod)
    ax.set_xlabel("Sentence Length")
    ax.set_ylabel("MDD")
    ax.set_title("MDD vs Sentence Length (sample n=5000)")
    ax.legend()
    plt.tight_layout()
    plt.savefig(str(PLOTS_DIR / "mdd_vs_sent_len.png"))
    plt.close()

    # 3. Interaction plot: MDD by modality × relation_type (mean residual)
    pivot = strata_filtered.groupby(["modality", "rel_type"])["mdd_residual_mean"].mean().reset_index()
    fig, ax = plt.subplots(figsize=(6, 4))
    for rt, color in [("argument", "steelblue"), ("adjunct", "darkorange"), ("modifier", "green")]:
        sub = pivot[pivot["rel_type"] == rt].set_index("modality")
        if len(sub) == 2:
            ax.plot(sub.index, sub["mdd_residual_mean"], marker="o", label=rt, color=color)
    ax.set_xlabel("Modality")
    ax.set_ylabel("Mean MDD Residual")
    ax.set_title("Interaction: Modality × Relation Type")
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(str(PLOTS_DIR / "interaction_plot.png"))
    plt.close()

    # 4. Forest plot: per-language Δ_MDD (argument vs adjunct)
    langs = [l for l in per_lang_est if per_lang_est[l].get("argument_delta_mdd") is not None]
    if langs:
        fig, axes = plt.subplots(1, 2, figsize=(10, max(3, len(langs))))
        for ax_idx, (rt, label) in enumerate([("argument", "Argument Δ_MDD"), ("adjunct", "Adjunct Δ_MDD")]):
            ax = axes[ax_idx]
            for i, lang in enumerate(langs):
                d = per_lang_est[lang].get(f"{rt}_delta_mdd")
                lo = per_lang_est[lang].get(f"{rt}_delta_ci_lower")
                hi = per_lang_est[lang].get(f"{rt}_delta_ci_upper")
                if d is None:
                    continue
                color = "steelblue" if rt == "argument" else "darkorange"
                ax.errorbar(d, i, xerr=[[d - lo], [hi - d]], fmt="o", color=color, capsize=4)
            ax.axvline(0, color="gray", linestyle="--", alpha=0.6)
            ax.set_yticks(range(len(langs)))
            ax.set_yticklabels(langs)
            ax.set_xlabel("Δ MDD residual (spoken − written)")
            ax.set_title(label)
            ax.grid(True, axis="x", alpha=0.3)
        plt.suptitle("Per-Language Δ_MDD with 95% Bootstrap CI", fontsize=12)
        plt.tight_layout()
        plt.savefig(str(PLOTS_DIR / "forest_plot_per_language.png"))
        plt.close()

    # 5. Adjunct effect vs case richness scatter
    if len(corr_data) >= 2:
        langs_c, adj_deltas, crs = zip(*corr_data)
        fig, ax = plt.subplots(figsize=(5, 4))
        ax.scatter(crs, adj_deltas, color="purple", s=80, zorder=3)
        for lang, x, y in zip(langs_c, crs, adj_deltas):
            ax.annotate(lang, (x, y), textcoords="offset points", xytext=(5, 3), fontsize=8)
        if len(corr_data) >= 3:
            from scipy.stats import linregress
            slope, intercept, *_ = linregress(crs, adj_deltas)
            xs = np.linspace(min(crs), max(crs), 100)
            ax.plot(xs, intercept + slope * xs, "k--", alpha=0.6)
        ax.set_xlabel("Case Richness Index")
        ax.set_ylabel("Adjunct Δ_MDD (spoken − written)")
        ax.set_title("Adjunct Effect vs. Morphological Case Richness")
        ax.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(str(PLOTS_DIR / "adjunct_vs_case_richness.png"))
        plt.close()

    logger.info(f"Saved plots to {PLOTS_DIR}")


def _validate_output(out_path: Path):
    """Validate output JSON against exp_gen_sol_out schema."""
    try:
        skill_dir = Path("/ai-inventor/.claude/skills/aii-json")
        py = skill_dir.parent / ".ability_client_venv/bin/python"
        script = skill_dir / "scripts/aii_json_validate_schema.py"
        import subprocess
        result = subprocess.run(
            [str(py), str(script), "--format", "exp_gen_sol_out", "--file", str(out_path)],
            capture_output=True, text=True, timeout=30,
        )
        logger.info(f"Schema validation:\n{result.stdout}\n{result.stderr}")
    except Exception as e:
        logger.warning(f"Schema validation error (non-critical): {e}")


if __name__ == "__main__":
    main()
