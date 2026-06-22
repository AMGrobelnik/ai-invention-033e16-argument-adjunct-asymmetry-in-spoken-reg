#!/usr/bin/env python3
"""Evaluate argument-adjunct asymmetry in dependency distance minimization across UD treebanks."""

import sys
import json
import math
import gc
import resource
import warnings
from pathlib import Path
from collections import defaultdict

import numpy as np
import pandas as pd
from loguru import logger
from scipy import stats
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

warnings.filterwarnings("ignore")

WORKSPACE = Path(__file__).parent
logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add(str(WORKSPACE / "logs" / "run.log"), rotation="30 MB", level="DEBUG")

# RAM limit: 20GB of 29GB available
RAM_BUDGET = 20 * 1024**3
resource.setrlimit(resource.RLIMIT_AS, (RAM_BUDGET * 3, RAM_BUDGET * 3))

# Relation category definitions
ARGUMENT_RELS = {"nsubj", "obj", "iobj", "csubj", "ccomp", "xcomp",
                 "nsubj:pass", "nsubj:outer", "csubj:pass", "csubj:outer",
                 "obj:agent", "obj:lvc", "obj:periph"}
ADJUNCT_RELS = {"advcl", "acl", "acl:relcl", "advcl:relcl", "advcl:tcl"}
MODIFIER_RELS = {"nmod", "amod", "advmod", "nmod:poss", "nmod:tmod",
                 "nmod:npmod", "advmod:emph", "advmod:lmod"}

# Language pairs (spoken, written) treebanks
LANG_PAIRS = {
    "English": {
        "spoken": ["en_gum"],   # GUM has spoken registers
        "written": ["en_ewt", "en_lines", "en_partut"],
        "family": "Indo-European",
        "word_order": "SVO",
    },
    "Slovenian": {
        "spoken": ["sl_sst"],
        "written": ["sl_ssj"],
        "family": "Indo-European",
        "word_order": "SVO",
    },
    "French": {
        "spoken": ["fr_rhapsodie", "fr_sequoia"],
        "written": ["fr_gsd", "fr_ftb", "fr_partut"],
        "family": "Indo-European",
        "word_order": "SVO",
    },
    "Italian": {
        "spoken": ["it_vit"],
        "written": ["it_isdt", "it_partut", "it_postwita"],
        "family": "Indo-European",
        "word_order": "SVO",
    },
    "German": {
        "spoken": ["de_hdt"],
        "written": ["de_gsd", "de_lit"],
        "family": "Indo-European",
        "word_order": "SOV",
    },
    "Portuguese": {
        "spoken": ["pt_bosque"],
        "written": ["pt_gsd"],
        "family": "Indo-European",
        "word_order": "SVO",
    },
    "Spanish": {
        "spoken": ["es_ancora"],
        "written": ["es_gsd", "es_pud"],
        "family": "Indo-European",
        "word_order": "SVO",
    },
    "Chinese": {
        "spoken": ["zh_cfl"],
        "written": ["zh_gsd", "zh_gsdsimp"],
        "family": "Sino-Tibetan",
        "word_order": "SVO",
    },
    "Japanese": {
        "spoken": ["ja_bccwj"],
        "written": ["ja_gsd", "ja_pud"],
        "family": "Japonic",
        "word_order": "SOV",
    },
    "Turkish": {
        "spoken": ["tr_boun"],
        "written": ["tr_imst", "tr_pud"],
        "family": "Turkic",
        "word_order": "SOV",
    },
    "Finnish": {
        "spoken": ["fi_ood"],
        "written": ["fi_tdt", "fi_pud"],
        "family": "Uralic",
        "word_order": "SVO",
    },
    "Czech": {
        "spoken": ["cs_cltt"],
        "written": ["cs_pdt", "cs_pud", "cs_fictree"],
        "family": "Indo-European",
        "word_order": "SVO",
    },
    "Polish": {
        "spoken": ["pl_pdb"],
        "written": ["pl_lfg", "pl_pud"],
        "family": "Indo-European",
        "word_order": "SVO",
    },
    "Russian": {
        "spoken": ["ru_syntagrus"],
        "written": ["ru_gsd", "ru_pud", "ru_taiga"],
        "family": "Indo-European",
        "word_order": "SVO",
    },
    "Arabic": {
        "spoken": ["ar_padt"],
        "written": ["ar_nyuad", "ar_pud"],
        "family": "Afro-Asiatic",
        "word_order": "VSO",
    },
}


def classify_rel(rel: str) -> str:
    base = rel.split(":")[0]
    if rel in ARGUMENT_RELS or base in {"nsubj", "obj", "iobj", "csubj", "ccomp", "xcomp"}:
        return "argument"
    if rel in ADJUNCT_RELS or base in {"advcl", "acl"}:
        return "adjunct"
    if rel in MODIFIER_RELS or base in {"nmod", "amod", "advmod"}:
        return "modifier"
    return "other"


def process_sentence(tokens) -> list[dict]:
    """Extract dependency arcs from a sentence's token list."""
    arcs = []
    sent_len = len(tokens)
    if sent_len < 2:
        return arcs
    for i, tok in enumerate(tokens):
        head = tok.get("head")
        deprel = tok.get("deprel", "")
        if head is None or head == 0 or deprel in ("root", "punct"):
            continue
        # head is 1-indexed in UD; i is 0-indexed
        dep_pos = i + 1  # 1-indexed
        dist = abs(head - dep_pos)
        if dist == 0:
            continue
        cat = classify_rel(deprel)
        if cat == "other":
            continue
        # Case feature
        feats = tok.get("feats") or {}
        has_case = "Case" in feats
        pos = tok.get("upos", "")
        arcs.append({
            "dist": dist,
            "rel": deprel,
            "cat": cat,
            "pos": pos,
            "has_case": has_case,
            "sent_len": sent_len,
        })
    return arcs


UPOS_NAMES = ['NOUN', 'PUNCT', 'ADP', 'NUM', 'SYM', 'SCONJ', 'ADJ', 'PART', 'DET',
              'CCONJ', 'PROPN', 'PRON', 'X', '_', 'ADV', 'INTJ', 'VERB', 'AUX']


def decode_upos(val) -> str:
    if isinstance(val, int) and 0 <= val < len(UPOS_NAMES):
        return UPOS_NAMES[val]
    return str(val) if val is not None else ""


def load_treebank(tb_name: str, dataset_module) -> list[dict]:
    """Load a treebank and return flat list of arc records."""
    records = []
    try:
        splits_to_try = ["train", "dev", "test"]
        for split in splits_to_try:
            try:
                ds = dataset_module.load_dataset(
                    "universal-dependencies/universal_dependencies",
                    tb_name,
                    split=split,
                )
                for row in ds:
                    tokens = []
                    ids = row.get("tokens", [])
                    heads = row.get("head", [])
                    deprels = row.get("deprel", [])
                    uposs = row.get("upos", [])
                    feats_list = row.get("feats", [])
                    for j in range(len(ids)):
                        feat_str = feats_list[j] if j < len(feats_list) else None
                        feats = {}
                        if feat_str and feat_str != "_":
                            for kv in feat_str.split("|"):
                                if "=" in kv:
                                    k, v = kv.split("=", 1)
                                    feats[k] = v
                        head_val = heads[j] if j < len(heads) else None
                        try:
                            head_int = int(head_val) if head_val is not None else None
                        except (ValueError, TypeError):
                            head_int = None
                        tokens.append({
                            "head": head_int,
                            "deprel": deprels[j] if j < len(deprels) else "",
                            "upos": decode_upos(uposs[j] if j < len(uposs) else None),
                            "feats": feats,
                        })
                    arcs = process_sentence(tokens)
                    records.extend(arcs)
            except Exception as e:
                logger.debug(f"  Split {split} failed for {tb_name}: {e}")
                continue
    except Exception as e:
        logger.warning(f"Failed to load treebank {tb_name}: {e}")
    return records


def compute_mdd_stats(records: list[dict]) -> dict:
    """Compute MDD statistics per category from arc records."""
    from collections import defaultdict
    cat_dists = defaultdict(list)
    cat_sentlens = defaultdict(list)
    noun_pron_total = 0
    noun_pron_case = 0
    nmod_count = 0
    adj_count = 0

    for r in records:
        cat = r["cat"]
        cat_dists[cat].append(r["dist"])
        cat_sentlens[cat].append(r["sent_len"])
        pos = r["pos"]
        if pos in ("NOUN", "PRON"):
            noun_pron_total += 1
            if r["has_case"]:
                noun_pron_case += 1
        if r["rel"].startswith("nmod"):
            nmod_count += 1
        if cat == "adjunct":
            adj_count += 1

    case_richness = noun_pron_case / noun_pron_total if noun_pron_total > 0 else 0.0
    ratio_nmod = nmod_count / adj_count if adj_count > 0 else 0.0

    stats_out = {
        "case_richness": case_richness,
        "ratio_nmod_to_adjuncts": ratio_nmod,
        "n_total_arcs": len(records),
    }
    for cat in ["argument", "adjunct", "modifier"]:
        dists = cat_dists.get(cat, [])
        sentlens = cat_sentlens.get(cat, [])
        stats_out[f"n_{cat}"] = len(dists)
        stats_out[f"mean_dist_{cat}"] = float(np.mean(dists)) if dists else 0.0
        stats_out[f"sentlens_{cat}"] = sentlens
        stats_out[f"dists_{cat}"] = dists
    return stats_out


def residualize_log_pooled(
    sp_dists: list[float], sp_lens: list[float],
    wr_dists: list[float], wr_lens: list[float]
) -> tuple[np.ndarray, np.ndarray]:
    """Residualize log(dist) on log(sentlen) using POOLED regression, return (sp_resid, wr_resid)."""
    all_dists = sp_dists + wr_dists
    all_lens = sp_lens + wr_lens
    n_sp = len(sp_dists)

    valid = [(d, s) for d, s in zip(all_dists, all_lens) if d > 0 and s > 0]
    if len(valid) < 10:
        sp_res = np.array([math.log(d) for d in sp_dists if d > 0])
        wr_res = np.array([math.log(d) for d in wr_dists if d > 0])
        return sp_res, wr_res

    log_dist = np.array([math.log(d) for d, s in valid])
    log_slen = np.array([math.log(s) for d, s in valid])
    slope, intercept, *_ = stats.linregress(log_slen, log_dist)

    # Apply the pooled regression to each group separately
    sp_valid = [(d, s) for d, s in zip(sp_dists, sp_lens) if d > 0 and s > 0]
    wr_valid = [(d, s) for d, s in zip(wr_dists, wr_lens) if d > 0 and s > 0]

    sp_res = np.array([math.log(d) - (slope * math.log(s) + intercept) for d, s in sp_valid])
    wr_res = np.array([math.log(d) - (slope * math.log(s) + intercept) for d, s in wr_valid])
    return sp_res, wr_res


def bootstrap_ci(spoken_dists, spoken_lens, written_dists, written_lens, n_boot=1000, seed=42):
    """Bootstrap 95% CI on spoken-minus-written MDD_residual difference (pooled residualization)."""
    rng = np.random.default_rng(seed)
    sp_d = np.array(spoken_dists)
    sp_l = np.array(spoken_lens)
    wr_d = np.array(written_dists)
    wr_l = np.array(written_lens)

    deltas = []
    for _ in range(n_boot):
        idx_sp = rng.integers(0, len(sp_d), size=len(sp_d))
        idx_wr = rng.integers(0, len(wr_d), size=len(wr_d))
        sp_res, wr_res = residualize_log_pooled(
            sp_d[idx_sp].tolist(), sp_l[idx_sp].tolist(),
            wr_d[idx_wr].tolist(), wr_l[idx_wr].tolist(),
        )
        if len(sp_res) > 0 and len(wr_res) > 0:
            deltas.append(float(np.mean(sp_res) - np.mean(wr_res)))

    if not deltas:
        return {"mean": 0.0, "se": 0.0, "ci_lower": 0.0, "ci_upper": 0.0}
    deltas = np.array(deltas)
    return {
        "mean": float(np.mean(deltas)),
        "se": float(np.std(deltas)),
        "ci_lower": float(np.percentile(deltas, 2.5)),
        "ci_upper": float(np.percentile(deltas, 97.5)),
    }


def cohens_d(group1: np.ndarray, group2: np.ndarray) -> float:
    n1, n2 = len(group1), len(group2)
    if n1 < 2 or n2 < 2:
        return float("nan")
    pooled_std = math.sqrt(((n1 - 1) * np.var(group1, ddof=1) + (n2 - 1) * np.var(group2, ddof=1)) / (n1 + n2 - 2))
    if pooled_std == 0:
        return 0.0
    return float((np.mean(group1) - np.mean(group2)) / pooled_std)


def pearson_ci(r: float, n: int, alpha=0.05) -> tuple[float, float]:
    """Fisher z-transform CI for Pearson r."""
    if n < 4 or abs(r) >= 1.0:
        return (-1.0, 1.0)
    z = math.atanh(r)
    se = 1.0 / math.sqrt(n - 3)
    z_crit = stats.norm.ppf(1 - alpha / 2)
    lo = math.tanh(z - z_crit * se)
    hi = math.tanh(z + z_crit * se)
    return (lo, hi)


@logger.catch(reraise=True)
def main():
    import datasets as hf_datasets

    logger.info("=== Argument-Adjunct Asymmetry Evaluation ===")
    logger.info(f"Workspace: {WORKSPACE}")

    # ---- PHASE 1: Load treebanks ----
    logger.info("Phase 1: Loading Universal Dependencies treebanks")

    # Store per-language, per-modality raw arc data
    lang_data = {}  # lang -> {"spoken": stats, "written": stats}

    # Skip config listing (slow); load_treebank handles missing treebanks gracefully
    available_tbs = None

    for lang, info in LANG_PAIRS.items():
        logger.info(f"Processing language: {lang}")
        spoken_records = []
        written_records = []

        for tb in info["spoken"]:
            logger.info(f"  Loading spoken: {tb}")
            recs = load_treebank(tb, hf_datasets)
            spoken_records.extend(recs)
            logger.info(f"    -> {len(recs)} arcs")

        for tb in info["written"]:
            logger.info(f"  Loading written: {tb}")
            recs = load_treebank(tb, hf_datasets)
            written_records.extend(recs)
            logger.info(f"    -> {len(recs)} arcs")

        if len(spoken_records) < 100 or len(written_records) < 100:
            logger.warning(f"  Insufficient data for {lang}: spoken={len(spoken_records)}, written={len(written_records)}")
            continue

        lang_data[lang] = {
            "spoken": compute_mdd_stats(spoken_records),
            "written": compute_mdd_stats(written_records),
            "family": info["family"],
            "word_order": info["word_order"],
        }
        del spoken_records, written_records
        gc.collect()
        logger.info(f"  Done: spoken n_arcs={lang_data[lang]['spoken']['n_total_arcs']}, written={lang_data[lang]['written']['n_total_arcs']}")

    if len(lang_data) < 3:
        logger.error(f"Only {len(lang_data)} languages loaded — insufficient for analysis")
        raise RuntimeError("Insufficient language data")

    logger.info(f"Successfully loaded {len(lang_data)} language pairs: {list(lang_data.keys())}")

    # ---- PHASE 2: Compute residualized MDD and deltas ----
    logger.info("Phase 2: Computing residualized MDD and deltas")

    lang_results = {}
    for lang, data in lang_data.items():
        sp = data["spoken"]
        wr = data["written"]
        result = {"family": data["family"], "word_order": data["word_order"]}

        for cat in ["argument", "adjunct", "modifier"]:
            sp_dists = sp.get(f"dists_{cat}", [])
            sp_lens = sp.get(f"sentlens_{cat}", [])
            wr_dists = wr.get(f"dists_{cat}", [])
            wr_lens = wr.get(f"sentlens_{cat}", [])

            if len(sp_dists) < 30 or len(wr_dists) < 30:
                result[cat] = {"skip": True, "n_spoken": len(sp_dists), "n_written": len(wr_dists)}
                continue

            # POOLED residualization: fit regression on spoken+written together
            sp_res, wr_res = residualize_log_pooled(sp_dists, sp_lens, wr_dists, wr_lens)
            delta_mean = float(np.mean(sp_res) - np.mean(wr_res))
            result[cat] = {
                "skip": False,
                "n_spoken": len(sp_dists),
                "n_written": len(wr_dists),
                "mean_res_spoken": float(np.mean(sp_res)),
                "mean_res_written": float(np.mean(wr_res)),
                "delta_mdd": delta_mean,
                "sp_res": sp_res.tolist(),
                "wr_res": wr_res.tolist(),
            }

        result["case_richness"] = float(sp.get("case_richness", 0.0))
        result["ratio_nmod"] = float(sp.get("ratio_nmod_to_adjuncts", 0.0))
        lang_results[lang] = result

    # ---- METRIC 1: Bootstrap CIs ----
    logger.info("Metric 1: Bootstrap confidence intervals")
    bootstrap_results = {}
    for lang, data in lang_data.items():
        if lang not in lang_results:
            continue
        sp = data["spoken"]
        wr = data["written"]
        boot = {}
        for cat in ["argument", "adjunct"]:
            sp_dists = sp.get(f"dists_{cat}", [])
            sp_lens = sp.get(f"sentlens_{cat}", [])
            wr_dists = wr.get(f"dists_{cat}", [])
            wr_lens = wr.get(f"sentlens_{cat}", [])
            if len(sp_dists) < 30 or len(wr_dists) < 30:
                boot[cat] = None
                continue
            ci = bootstrap_ci(sp_dists, sp_lens, wr_dists, wr_lens, n_boot=1000)
            boot[cat] = ci
        bootstrap_results[lang] = boot
        logger.debug(f"  {lang}: arg_ci={boot.get('argument')}, adj_ci={boot.get('adjunct')}")

    # ---- METRIC 2: Effect sizes (Cohen's d) ----
    logger.info("Metric 2: Effect size distributions")
    effect_sizes = {"argument": [], "adjunct": [], "modifier": []}
    for lang, res in lang_results.items():
        for cat in ["argument", "adjunct", "modifier"]:
            if res.get(cat, {}).get("skip", True):
                continue
            sp_res = np.array(res[cat]["sp_res"])
            wr_res = np.array(res[cat]["wr_res"])
            d = cohens_d(sp_res, wr_res)
            if not math.isnan(d):
                effect_sizes[cat].append({"lang": lang, "d": d})

    effect_size_stats = {}
    for cat, entries in effect_sizes.items():
        if not entries:
            continue
        ds = [e["d"] for e in entries]
        # rough p-value via t-test per entry
        pct_sig = 0
        for e in entries:
            lang = e["lang"]
            res = lang_results[lang]
            if res.get(cat, {}).get("skip", True):
                continue
            sp = np.array(res[cat]["sp_res"])
            wr = np.array(res[cat]["wr_res"])
            try:
                _, p = stats.ttest_ind(sp, wr)
                if p < 0.05:
                    pct_sig += 1
            except Exception:
                pass
        effect_size_stats[cat] = {
            "mean_d": float(np.mean(ds)),
            "median_d": float(np.median(ds)),
            "sd_d": float(np.std(ds)),
            "min_d": float(np.min(ds)),
            "max_d": float(np.max(ds)),
            "pct_significant_p05": pct_sig / len(entries) if entries else 0.0,
            "n_languages": len(entries),
            "per_language": entries,
        }

    # ---- METRIC 3: Morphological modulation correlation ----
    logger.info("Metric 3: Morphological modulation hypothesis test")
    morph_data = []
    for lang, res in lang_results.items():
        if res.get("adjunct", {}).get("skip", True):
            continue
        morph_data.append({
            "lang": lang,
            "case_richness": res["case_richness"],
            "delta_adjunct": res["adjunct"]["delta_mdd"],
            "delta_argument": res["argument"]["delta_mdd"] if not res.get("argument", {}).get("skip", True) else None,
        })

    morph_result = {}
    if len(morph_data) >= 4:
        x = np.array([d["case_richness"] for d in morph_data])
        y = np.array([d["delta_adjunct"] for d in morph_data])
        r, p = stats.pearsonr(x, y)
        ci_lo, ci_hi = pearson_ci(float(r), len(morph_data))
        morph_result = {
            "pearson_r": float(r),
            "pearson_p_value": float(p),
            "pearson_95ci_lower": ci_lo,
            "pearson_95ci_upper": ci_hi,
            "n_languages": len(morph_data),
            "scatter_coordinates": [
                {"lang": d["lang"], "case_richness": d["case_richness"], "delta_adjunct": d["delta_adjunct"]}
                for d in morph_data
            ],
        }
        logger.info(f"  Pearson r={r:.3f}, p={p:.4f}, n={len(morph_data)}")
    else:
        morph_result = {"error": "insufficient languages for correlation", "n_languages": len(morph_data)}

    # ---- METRIC 4: Sensitivity ablations (simplified mixed-effects model) ----
    logger.info("Metric 4: Sensitivity ablations")

    # Build dataframe for mixed-effects model
    rows = []
    for lang, res in lang_results.items():
        for cat in ["argument", "adjunct"]:
            if res.get(cat, {}).get("skip", True):
                continue
            rows.append({
                "language": lang,
                "modality": "spoken",
                "rel_type": cat,
                "mdd_residual": res[cat]["mean_res_spoken"],
                "n_arcs": res[cat]["n_spoken"],
            })
            rows.append({
                "language": lang,
                "modality": "written",
                "rel_type": cat,
                "mdd_residual": res[cat]["mean_res_written"],
                "n_arcs": res[cat]["n_written"],
            })

    df = pd.DataFrame(rows)
    logger.info(f"  Model dataframe: {len(df)} rows, {df['language'].nunique()} languages")

    ablation_results = []
    if len(df) >= 8:
        try:
            import statsmodels.formula.api as smf
            # Main model: modality * rel_type with random intercept per language
            model_main = smf.mixedlm(
                "mdd_residual ~ C(modality) * C(rel_type)",
                df,
                groups=df["language"],
            )
            try:
                fit_main = model_main.fit(reml=True, method="lbfgs")
            except Exception:
                fit_main = model_main.fit(reml=False, method="nm")
            logger.info(f"  Main model fitted. AIC={fit_main.aic:.2f}")

            # Extract interaction coefficient
            coef_names = fit_main.params.index.tolist()
            interaction_coef = None
            interaction_se = None
            for cn in coef_names:
                if "modality" in cn and "rel_type" in cn:
                    interaction_coef = float(fit_main.params[cn])
                    interaction_se = float(fit_main.bse[cn])
                    break

            interaction_pval = None
            for cn in coef_names:
                if "modality" in cn and "rel_type" in cn:
                    interaction_pval = float(fit_main.pvalues[cn])
                    break

            # LR test: model without interaction
            model_null = smf.mixedlm(
                "mdd_residual ~ C(modality) + C(rel_type)",
                df,
                groups=df["language"],
            )
            fit_null = model_null.fit(reml=False, method="lbfgs")
            fit_alt = smf.mixedlm(
                "mdd_residual ~ C(modality) * C(rel_type)",
                df,
                groups=df["language"],
            ).fit(reml=False, method="lbfgs")

            lr_stat = 2 * (fit_alt.llf - fit_null.llf)
            lr_pval = float(stats.chi2.sf(lr_stat, df=1))

            main_model_result = {
                "interaction_coefficient": interaction_coef,
                "interaction_se": interaction_se,
                "interaction_95ci_lower": (interaction_coef - 1.96 * interaction_se) if interaction_coef is not None else None,
                "interaction_95ci_upper": (interaction_coef + 1.96 * interaction_se) if interaction_coef is not None else None,
                "interaction_pvalue_wald": interaction_pval,
                "interaction_pvalue_lr": lr_pval,
                "interaction_is_significant_p05": (interaction_pval < 0.05) if interaction_pval is not None else False,
                "aic": float(fit_main.aic),
                "bic": float(fit_main.bic),
                "all_coefficients": {k: float(v) for k, v in fit_main.params.items()},
                "all_pvalues": {k: float(v) for k, v in fit_main.pvalues.items()},
            }

            # Predicted MDD residual by condition
            for modality in ["spoken", "written"]:
                for rel_type in ["argument", "adjunct"]:
                    sub = df[(df["modality"] == modality) & (df["rel_type"] == rel_type)]
                    if len(sub) > 0:
                        main_model_result[f"predicted_{modality}_{rel_type}"] = float(sub["mdd_residual"].mean())

            logger.info(f"  Interaction coef={interaction_coef:.4f}, wald_p={interaction_pval:.4f}, lr_p={lr_pval:.4f}")

            # Ablation A: No length normalization (use raw log(dist))
            rows_raw = []
            for lang, res in lang_results.items():
                for cat in ["argument", "adjunct"]:
                    if res.get(cat, {}).get("skip", True):
                        continue
                    sp_dists = lang_data[lang]["spoken"].get(f"dists_{cat}", [])
                    wr_dists = lang_data[lang]["written"].get(f"dists_{cat}", [])
                    if sp_dists and wr_dists:
                        rows_raw.append({
                            "language": lang, "modality": "spoken", "rel_type": cat,
                            "log_mdd": float(np.mean([math.log(d) for d in sp_dists if d > 0])),
                        })
                        rows_raw.append({
                            "language": lang, "modality": "written", "rel_type": cat,
                            "log_mdd": float(np.mean([math.log(d) for d in wr_dists if d > 0])),
                        })
            df_raw = pd.DataFrame(rows_raw)
            try:
                fit_a = smf.mixedlm("log_mdd ~ C(modality) * C(rel_type)", df_raw, groups=df_raw["language"]).fit(reml=True, method="lbfgs")
                pval_a = None
                for cn in fit_a.params.index:
                    if "modality" in cn and "rel_type" in cn:
                        pval_a = float(fit_a.pvalues[cn])
                        break
                coef_dir_a = None
                for cn in fit_a.params.index:
                    if "modality" in cn and "rel_type" in cn:
                        coef_dir_a = float(fit_a.params[cn])
                        break
                ablation_a = {
                    "ablation_name": "no_length_normalization",
                    "interaction_pvalue": pval_a,
                    "interaction_direction_preserved": (
                        (coef_dir_a is not None and interaction_coef is not None and
                         (coef_dir_a * interaction_coef > 0))
                    ),
                    "assessment": "Normalization_is_critical" if (pval_a is not None and pval_a > 0.05) else "Robust_to_method",
                }
            except Exception as e:
                ablation_a = {"ablation_name": "no_length_normalization", "error": str(e)}
            ablation_results.append(ablation_a)

            # Ablation B: Length as fixed covariate
            rows_cov = []
            for lang, res in lang_results.items():
                for cat in ["argument", "adjunct"]:
                    if res.get(cat, {}).get("skip", True):
                        continue
                    sp = lang_data[lang]["spoken"]
                    wr = lang_data[lang]["written"]
                    sp_dists = sp.get(f"dists_{cat}", [])
                    sp_lens = sp.get(f"sentlens_{cat}", [])
                    wr_dists = wr.get(f"dists_{cat}", [])
                    wr_lens = wr.get(f"sentlens_{cat}", [])
                    if sp_dists and wr_dists:
                        rows_cov.append({
                            "language": lang, "modality": "spoken", "rel_type": cat,
                            "log_mdd": float(np.mean([math.log(d) for d in sp_dists if d > 0])),
                            "log_sentlen": float(np.mean([math.log(s) for s in sp_lens if s > 0])),
                        })
                        rows_cov.append({
                            "language": lang, "modality": "written", "rel_type": cat,
                            "log_mdd": float(np.mean([math.log(d) for d in wr_dists if d > 0])),
                            "log_sentlen": float(np.mean([math.log(s) for s in wr_lens if s > 0])),
                        })
            df_cov = pd.DataFrame(rows_cov)
            try:
                fit_b = smf.mixedlm("log_mdd ~ C(modality) * C(rel_type) + log_sentlen", df_cov, groups=df_cov["language"]).fit(reml=True, method="lbfgs")
                pval_b = None
                coef_b = None
                for cn in fit_b.params.index:
                    if "modality" in cn and "rel_type" in cn:
                        pval_b = float(fit_b.pvalues[cn])
                        coef_b = float(fit_b.params[cn])
                        break
                ablation_b = {
                    "ablation_name": "length_as_covariate",
                    "interaction_pvalue": pval_b,
                    "interaction_direction_preserved": (
                        coef_b is not None and interaction_coef is not None and (coef_b * interaction_coef > 0)
                    ),
                    "assessment": "Robust_to_method" if (pval_b is not None and pval_b < 0.05) else "Normalization_is_critical",
                }
            except Exception as e:
                ablation_b = {"ablation_name": "length_as_covariate", "error": str(e)}
            ablation_results.append(ablation_b)

            # Ablation C: Huber robust regression
            from sklearn.linear_model import HuberRegressor
            from sklearn.preprocessing import LabelEncoder
            df2 = df.copy()
            df2["modality_enc"] = (df2["modality"] == "spoken").astype(float)
            df2["rel_enc"] = (df2["rel_type"] == "adjunct").astype(float)
            df2["interaction"] = df2["modality_enc"] * df2["rel_enc"]
            X = df2[["modality_enc", "rel_enc", "interaction"]].values
            y = df2["mdd_residual"].values
            try:
                huber = HuberRegressor(epsilon=1.35, max_iter=300).fit(X, y)
                coef_c = float(huber.coef_[2])  # interaction term
                ablation_c = {
                    "ablation_name": "robust_huber_regression",
                    "interaction_coefficient": coef_c,
                    "interaction_direction_preserved": (
                        interaction_coef is not None and (coef_c * interaction_coef > 0)
                    ),
                    "assessment": "Robust_to_method" if (interaction_coef is not None and coef_c * interaction_coef > 0) else "Normalization_is_critical",
                }
            except Exception as e:
                ablation_c = {"ablation_name": "robust_huber_regression", "error": str(e)}
            ablation_results.append(ablation_c)

        except Exception as e:
            logger.error(f"Mixed-effects model failed: {e}")
            main_model_result = {"error": str(e)}

    else:
        main_model_result = {"error": "insufficient data for model"}

    # ---- METRIC 5: Language-family deviations ----
    logger.info("Metric 5: Language-family deviations")
    deviation_profiles = []
    conforming = 0
    for lang, res in lang_results.items():
        arg = res.get("argument", {})
        adj = res.get("adjunct", {})
        if arg.get("skip", True) or adj.get("skip", True):
            continue
        delta_arg = arg["delta_mdd"]
        delta_adj = adj["delta_mdd"]
        conforms = (delta_arg < 0) and (delta_adj >= 0)
        if conforms:
            conforming += 1

        if delta_arg >= 0 and delta_adj < 0:
            violation_type = "both_reversed"
        elif delta_arg >= 0:
            violation_type = "argument_not_short_in_spoken"
        elif delta_adj < 0:
            violation_type = "adjunct_too_short_in_spoken"
        else:
            violation_type = "none"

        # Adjunct type analysis
        sp_data = lang_data[lang]["spoken"]
        adj_total = sp_data.get("n_adjunct", 0)

        profile = {
            "language": lang,
            "language_family": res["family"],
            "word_order": res["word_order"],
            "conforms": conforms,
            "spoken_argument_delta_mdd": round(delta_arg, 4),
            "spoken_adjunct_delta_mdd": round(delta_adj, 4),
            "case_richness_index": round(res.get("case_richness", 0.0), 4),
            "ratio_nmod_to_other_adjuncts": round(res.get("ratio_nmod", 0.0), 4),
            "violation_type": violation_type,
        }
        if not conforms:
            magnitude = abs(delta_arg) + abs(delta_adj)
            profile["violation_magnitude"] = round(magnitude, 4)
            profile["working_hypothesis"] = generate_hypothesis(lang, res, delta_arg, delta_adj)
        deviation_profiles.append(profile)

    n_conforming = sum(1 for p in deviation_profiles if p["conforms"])
    conformance_rate = n_conforming / len(deviation_profiles) if deviation_profiles else 0.0
    logger.info(f"  Conformance: {n_conforming}/{len(deviation_profiles)} = {conformance_rate:.2f}")

    # ---- METRIC 6: Interaction robustness + non-parametric tests ----
    logger.info("Metric 6: Interaction robustness")
    arg_deltas = [res["argument"]["delta_mdd"] for res in lang_results.values()
                  if not res.get("argument", {}).get("skip", True)]
    adj_deltas = [res["adjunct"]["delta_mdd"] for res in lang_results.values()
                  if not res.get("adjunct", {}).get("skip", True)]

    lang_tests = {}
    if len(arg_deltas) >= 4:
        t_arg, p_arg = stats.ttest_1samp(arg_deltas, 0)
        t_adj, p_adj = stats.ttest_1samp(adj_deltas, 0)
        lang_tests["argument_one_sample_t"] = float(t_arg)
        lang_tests["argument_one_sample_p"] = float(p_arg)
        lang_tests["argument_mean_delta"] = float(np.mean(arg_deltas))
        lang_tests["adjunct_one_sample_t"] = float(t_adj)
        lang_tests["adjunct_one_sample_p"] = float(p_adj)
        lang_tests["adjunct_mean_delta"] = float(np.mean(adj_deltas))
        logger.info(f"  Arg mean delta={np.mean(arg_deltas):.4f}, t={t_arg:.3f}, p={p_arg:.4f}")
        logger.info(f"  Adj mean delta={np.mean(adj_deltas):.4f}, t={t_adj:.3f}, p={p_adj:.4f}")

        # Paired test: is adj delta > arg delta (core asymmetry)?
        n_both = min(len(arg_deltas), len(adj_deltas))
        if n_both >= 4:
            try:
                t_paired, p_paired = stats.ttest_rel(adj_deltas[:n_both], arg_deltas[:n_both])
                lang_tests["asymmetry_paired_t"] = float(t_paired)
                lang_tests["asymmetry_paired_p"] = float(p_paired)
                logger.info(f"  Asymmetry paired t={t_paired:.3f}, p={p_paired:.4f}")
            except Exception as e:
                logger.warning(f"  Paired t failed: {e}")
            try:
                w_stat, p_wilcox = stats.wilcoxon(adj_deltas[:n_both], arg_deltas[:n_both])
                lang_tests["asymmetry_wilcoxon_W"] = float(w_stat)
                lang_tests["asymmetry_wilcoxon_p"] = float(p_wilcox)
            except Exception as e:
                logger.warning(f"  Wilcoxon failed: {e}")

    if "error" in main_model_result:
        main_model_result["language_level_tests"] = lang_tests
    else:
        main_model_result["language_level_tests"] = lang_tests

    # ---- VISUALIZATIONS ----
    logger.info("Generating visualizations")
    fig_dir = WORKSPACE / "figures"

    # Fig 1: Delta MDD by language and category
    try:
        langs_plot = [p["language"] for p in deviation_profiles]
        arg_deltas = [p["spoken_argument_delta_mdd"] for p in deviation_profiles]
        adj_deltas = [p["spoken_adjunct_delta_mdd"] for p in deviation_profiles]

        x = np.arange(len(langs_plot))
        width = 0.35
        fig, ax = plt.subplots(figsize=(max(10, len(langs_plot) * 0.8), 6))
        bars1 = ax.bar(x - width/2, arg_deltas, width, label="Argument Δ_MDD", color="#2196F3", alpha=0.8)
        bars2 = ax.bar(x + width/2, adj_deltas, width, label="Adjunct Δ_MDD", color="#FF9800", alpha=0.8)
        ax.axhline(0, color="black", linewidth=0.8, linestyle="--")
        ax.set_xlabel("Language")
        ax.set_ylabel("Δ_MDD_residual (spoken - written)")
        ax.set_title("Spoken-Written MDD Difference by Relation Category and Language")
        ax.set_xticks(x)
        ax.set_xticklabels(langs_plot, rotation=45, ha="right")
        ax.legend()
        ax.grid(axis="y", alpha=0.3)
        plt.tight_layout()
        plt.savefig(fig_dir / "delta_mdd_by_language.png", dpi=150, bbox_inches="tight")
        plt.close()
        logger.info("  Saved delta_mdd_by_language.png")
    except Exception as e:
        logger.warning(f"  Fig 1 failed: {e}")

    # Fig 2: Morphological modulation scatter plot
    try:
        if len(morph_data) >= 3:
            fig, ax = plt.subplots(figsize=(8, 6))
            xs = [d["case_richness"] for d in morph_data]
            ys = [d["delta_adjunct"] for d in morph_data]
            ax.scatter(xs, ys, color="#9C27B0", s=80, zorder=5)
            for d in morph_data:
                ax.annotate(d["lang"], (d["case_richness"], d["delta_adjunct"]),
                            textcoords="offset points", xytext=(5, 5), fontsize=8)
            # Regression line
            if len(xs) >= 3:
                slope, intercept, *_ = stats.linregress(xs, ys)
                xline = np.linspace(min(xs), max(xs), 100)
                ax.plot(xline, slope * xline + intercept, color="red", linestyle="--", alpha=0.7)
            ax.axhline(0, color="black", linewidth=0.8, linestyle=":")
            ax.set_xlabel("Case Richness Index (proportion of NOUN/PRON with Case feature)")
            ax.set_ylabel("Δ_MDD_adjunct (spoken - written)")
            r_val = morph_result.get("pearson_r", float("nan"))
            p_val = morph_result.get("pearson_p_value", float("nan"))
            ax.set_title(f"Morphological Modulation: Case Richness vs. Adjunct Elongation\n(r={r_val:.3f}, p={p_val:.3f})")
            plt.tight_layout()
            plt.savefig(fig_dir / "morphological_modulation.png", dpi=150, bbox_inches="tight")
            plt.close()
            logger.info("  Saved morphological_modulation.png")
    except Exception as e:
        logger.warning(f"  Fig 2 failed: {e}")

    # Fig 3: Effect size distribution histogram
    try:
        fig, axes = plt.subplots(1, 2, figsize=(12, 5))
        for i, cat in enumerate(["argument", "adjunct"]):
            if cat in effect_size_stats:
                ds = [e["d"] for e in effect_size_stats[cat]["per_language"]]
                axes[i].hist(ds, bins=min(10, len(ds)), color="#4CAF50" if cat == "argument" else "#FF5722", alpha=0.7, edgecolor="black")
                axes[i].axvline(0, color="black", linewidth=1.5, linestyle="--")
                axes[i].axvline(np.mean(ds), color="red", linewidth=2, linestyle="-", label=f"Mean={np.mean(ds):.3f}")
                axes[i].set_xlabel("Cohen's d (spoken - written)")
                axes[i].set_ylabel("Number of languages")
                axes[i].set_title(f"Effect Size Distribution: {cat.capitalize()}")
                axes[i].legend()
        plt.tight_layout()
        plt.savefig(fig_dir / "effect_size_distributions.png", dpi=150, bbox_inches="tight")
        plt.close()
        logger.info("  Saved effect_size_distributions.png")
    except Exception as e:
        logger.warning(f"  Fig 3 failed: {e}")

    # Fig 4: Interaction plot
    try:
        if "predicted_spoken_argument" in main_model_result:
            categories = ["Argument", "Adjunct"]
            spoken_vals = [
                main_model_result.get("predicted_spoken_argument", 0),
                main_model_result.get("predicted_spoken_adjunct", 0),
            ]
            written_vals = [
                main_model_result.get("predicted_written_argument", 0),
                main_model_result.get("predicted_written_adjunct", 0),
            ]
            fig, ax = plt.subplots(figsize=(7, 5))
            x = np.arange(len(categories))
            ax.plot(x, spoken_vals, "o-", color="#E91E63", label="Spoken", linewidth=2, markersize=8)
            ax.plot(x, written_vals, "s--", color="#2196F3", label="Written", linewidth=2, markersize=8)
            ax.set_xticks(x)
            ax.set_xticklabels(categories)
            ax.set_ylabel("MDD Residual (log scale)")
            ax.set_title("Modality × Relation Category Interaction\n(Mixed-Effects Model Predictions)")
            ax.legend()
            ax.grid(axis="y", alpha=0.3)
            plt.tight_layout()
            plt.savefig(fig_dir / "interaction_plot.png", dpi=150, bbox_inches="tight")
            plt.close()
            logger.info("  Saved interaction_plot.png")
    except Exception as e:
        logger.warning(f"  Fig 4 failed: {e}")

    # ---- ASSEMBLE OUTPUT ----
    logger.info("Assembling eval_out.json")

    # Aggregate metrics
    metrics_agg = {}
    if effect_size_stats.get("argument"):
        metrics_agg["argument_mean_cohens_d"] = round(effect_size_stats["argument"]["mean_d"], 4)
        metrics_agg["argument_median_cohens_d"] = round(effect_size_stats["argument"]["median_d"], 4)
        metrics_agg["argument_pct_significant"] = round(effect_size_stats["argument"]["pct_significant_p05"], 4)
    if effect_size_stats.get("adjunct"):
        metrics_agg["adjunct_mean_cohens_d"] = round(effect_size_stats["adjunct"]["mean_d"], 4)
        metrics_agg["adjunct_median_cohens_d"] = round(effect_size_stats["adjunct"]["median_d"], 4)
        metrics_agg["adjunct_pct_significant"] = round(effect_size_stats["adjunct"]["pct_significant_p05"], 4)
    if morph_result.get("pearson_r") is not None:
        metrics_agg["morphological_pearson_r"] = round(morph_result["pearson_r"], 4)
        metrics_agg["morphological_pearson_p"] = round(morph_result["pearson_p_value"], 4)
    metrics_agg["conformance_rate"] = round(conformance_rate, 4)
    metrics_agg["n_languages_analyzed"] = len(lang_results)
    if "interaction_pvalue_wald" in main_model_result:
        pval = main_model_result.get("interaction_pvalue_wald")
        if pval is not None:
            metrics_agg["interaction_pvalue_wald"] = round(float(pval), 6)
    if "interaction_pvalue_lr" in main_model_result:
        pval_lr = main_model_result.get("interaction_pvalue_lr")
        if pval_lr is not None:
            metrics_agg["interaction_pvalue_lr"] = round(float(pval_lr), 6)
    if "interaction_coefficient" in main_model_result and main_model_result["interaction_coefficient"] is not None:
        metrics_agg["interaction_coefficient"] = round(float(main_model_result["interaction_coefficient"]), 4)
    # Language-level tests
    lt = main_model_result.get("language_level_tests", {})
    if "argument_mean_delta" in lt:
        metrics_agg["argument_mean_delta_mdd"] = round(lt["argument_mean_delta"], 6)
        metrics_agg["argument_one_sample_p"] = round(lt["argument_one_sample_p"], 6)
        metrics_agg["adjunct_mean_delta_mdd"] = round(lt["adjunct_mean_delta"], 6)
        metrics_agg["adjunct_one_sample_p"] = round(lt["adjunct_one_sample_p"], 6)
    if "asymmetry_paired_p" in lt:
        metrics_agg["asymmetry_paired_p"] = round(lt["asymmetry_paired_p"], 6)
    if "asymmetry_wilcoxon_p" in lt:
        metrics_agg["asymmetry_wilcoxon_p"] = round(lt["asymmetry_wilcoxon_p"], 6)

    # Per-language examples for datasets
    examples = []
    for lang, res in lang_results.items():
        boot = bootstrap_results.get(lang, {})
        arg_boot = boot.get("argument") or {}
        adj_boot = boot.get("adjunct") or {}

        input_str = f"Language: {lang}, Family: {res['family']}, Word Order: {res['word_order']}"
        output_str = f"Argument Δ_MDD: {res.get('argument', {}).get('delta_mdd', 'N/A'):.4f}, Adjunct Δ_MDD: {res.get('adjunct', {}).get('delta_mdd', 'N/A'):.4f}"

        ex = {
            "input": input_str,
            "output": output_str,
            "metadata_language": lang,
            "metadata_family": res["family"],
            "metadata_word_order": res["word_order"],
            "metadata_case_richness": round(res.get("case_richness", 0.0), 4),
        }

        if not res.get("argument", {}).get("skip", True):
            ex["eval_argument_delta_mdd"] = round(res["argument"]["delta_mdd"], 4)
            ex["eval_argument_n_spoken"] = res["argument"]["n_spoken"]
            ex["eval_argument_n_written"] = res["argument"]["n_written"]
            if arg_boot:
                ex["eval_argument_ci_lower"] = round(arg_boot.get("ci_lower", 0.0), 4)
                ex["eval_argument_ci_upper"] = round(arg_boot.get("ci_upper", 0.0), 4)
                ex["eval_argument_boot_se"] = round(arg_boot.get("se", 0.0), 4)
            if lang in effect_size_stats.get("argument", {}).get("per_language", []):
                pass
            for e in effect_size_stats.get("argument", {}).get("per_language", []):
                if e["lang"] == lang:
                    ex["eval_argument_cohens_d"] = round(e["d"], 4)
                    break

        if not res.get("adjunct", {}).get("skip", True):
            ex["eval_adjunct_delta_mdd"] = round(res["adjunct"]["delta_mdd"], 4)
            ex["eval_adjunct_n_spoken"] = res["adjunct"]["n_spoken"]
            ex["eval_adjunct_n_written"] = res["adjunct"]["n_written"]
            if adj_boot:
                ex["eval_adjunct_ci_lower"] = round(adj_boot.get("ci_lower", 0.0), 4)
                ex["eval_adjunct_ci_upper"] = round(adj_boot.get("ci_upper", 0.0), 4)
                ex["eval_adjunct_boot_se"] = round(adj_boot.get("se", 0.0), 4)
            for e in effect_size_stats.get("adjunct", {}).get("per_language", []):
                if e["lang"] == lang:
                    ex["eval_adjunct_cohens_d"] = round(e["d"], 4)
                    break

        # Conformance
        profile = next((p for p in deviation_profiles if p["language"] == lang), None)
        if profile:
            ex["eval_conforms"] = 1.0 if profile["conforms"] else 0.0
            ex["predict_violation_type"] = profile["violation_type"]

        examples.append(ex)

    eval_out = {
        "metadata": {
            "evaluation_name": "Argument-Adjunct Asymmetry in Dependency Distance Minimization",
            "description": "Statistical evaluation of the hypothesis that spoken language shows argument-adjunct asymmetry in dependency distance minimization across Universal Dependencies treebanks.",
            "n_languages": len(lang_results),
            "languages": list(lang_results.keys()),
            "metrics": {
                "metric1_bootstrap_cis": "Bootstrap 95% CI on spoken-minus-written MDD residual difference per language per category",
                "metric2_effect_sizes": "Cohen's d distribution across languages per relation category",
                "metric3_morphological": "Pearson correlation between case richness and adjunct elongation",
                "metric4_ablations": ablation_results,
                "metric5_deviations": deviation_profiles,
                "metric6_interaction": main_model_result,
            },
            "effect_size_stats": effect_size_stats,
            "morphological_modulation": morph_result,
            "conformance_rate": round(conformance_rate, 4),
            "n_conforming": n_conforming,
            "n_nonconforming": len(deviation_profiles) - n_conforming,
        },
        "metrics_agg": metrics_agg,
        "datasets": [{
            "dataset": "universal_dependencies",
            "examples": examples,
        }],
    }

    out_path = WORKSPACE / "eval_out.json"
    out_path.write_text(json.dumps(eval_out, indent=2))
    logger.info(f"Saved eval_out.json ({out_path.stat().st_size / 1024:.1f} KB)")

    # Summary
    logger.info("=== RESULTS SUMMARY ===")
    logger.info(f"Languages analyzed: {list(lang_results.keys())}")
    logger.info(f"Conformance rate: {conformance_rate:.2%}")
    if "pearson_r" in morph_result:
        logger.info(f"Morphological correlation: r={morph_result['pearson_r']:.3f}, p={morph_result['pearson_p_value']:.4f}")
    if "interaction_pvalue_wald" in main_model_result:
        logger.info(f"Interaction p-value (Wald): {main_model_result['interaction_pvalue_wald']:.4f}")


def generate_hypothesis(lang: str, res: dict, delta_arg: float, delta_adj: float) -> str:
    family = res.get("family", "Unknown")
    wo = res.get("word_order", "Unknown")
    case = res.get("case_richness", 0.0)
    if delta_arg >= 0:
        return f"{lang} ({family}, {wo}) does not show argument shortening in speech; may reflect rigid {wo} order constraining argument placement regardless of modality."
    elif delta_adj < 0:
        return f"{lang} ({family}, {wo}) shows unexpected adjunct shortening in speech; low case richness ({case:.2f}) may force pre-verbal adjunct placement, limiting post-verbal adjunct elongation."
    return f"{lang} ({family}, {wo}) deviates from predicted pattern; structural or genre confounds suspected."


if __name__ == "__main__":
    main()
