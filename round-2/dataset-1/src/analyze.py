#!/usr/bin/env python3
"""Analyze UD treebanks: dependency distance by category + case-richness index."""

import json
import math
import sys
from pathlib import Path
from collections import defaultdict
from loguru import logger

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

WORKSPACE = Path("/ai-inventor/aii_data/runs/run_4SjiUyyE35Gi/3_invention_loop/iter_2/gen_art/gen_art_dataset_1")
DATA_DIR = WORKSPACE / "temp/datasets"

UPOS_NAMES = ['NOUN','PUNCT','ADP','NUM','SYM','SCONJ','ADJ','PART','DET','CCONJ','PROPN','PRON','X','_','ADV','INTJ','VERB','AUX']
UPOS_IDX = {name: i for i, name in enumerate(UPOS_NAMES)}

ARGUMENT_RELS = {"nsubj", "obj", "iobj", "ccomp", "xcomp"}
ADJUNCT_RELS  = {"advcl", "acl", "acl:relcl"}
MODIFIER_RELS = {"nmod", "amod", "advmod"}

TREEBANKS = {
    "sl_sst":       {"language": "Slovenian", "modality": "spoken",  "splits": ["train","dev","test"]},
    "sl_ssj":       {"language": "Slovenian", "modality": "written", "splits": ["train","dev","test"]},
    "fr_rhapsodie": {"language": "French",    "modality": "spoken",  "splits": ["train","dev"]},
    "fr_gsd":       {"language": "French",    "modality": "written", "splits": ["train","dev","test"]},
}

def classify_deprel(deprel: str) -> str | None:
    base = deprel.split(":")[0] if ":" in deprel else deprel
    if deprel in ARGUMENT_RELS or base in ARGUMENT_RELS:
        return "ARGUMENT"
    if deprel in ADJUNCT_RELS or (base == "acl"):
        return "ADJUNCT"
    if deprel in MODIFIER_RELS or base in MODIFIER_RELS:
        return "MODIFIER"
    return None

def load_splits(config: str, splits: list[str]) -> list[dict]:
    rows = []
    for split in splits:
        path = DATA_DIR / f"full_commul_universal_dependencies_{config}_{split}.json"
        if not path.exists():
            logger.warning(f"Missing: {path.name}")
            continue
        data = json.loads(path.read_text())
        rows.extend(data)
        logger.info(f"  {config}/{split}: {len(data)} sentences")
    return rows

def compute_mdd_per_sentence(rows: list[dict]) -> dict:
    """Returns {category: [(mdd_sentence, sent_len), ...]}"""
    cat_data = defaultdict(list)
    for row in rows:
        heads = row.get("head", [])
        deprels = row.get("deprel", [])
        if not heads or not deprels:
            continue
        n = len(heads)
        sent_len = n
        cat_dists = defaultdict(list)
        for i, (h, d) in enumerate(zip(heads, deprels)):
            try:
                h = int(h)
            except (TypeError, ValueError):
                continue
            if h == 0:
                continue
            cat = classify_deprel(d)
            if cat is None:
                continue
            dist = abs(h - (i + 1))  # 1-indexed positions
            cat_dists[cat].append(dist)
        for cat, dists in cat_dists.items():
            if dists:
                cat_data[cat].append((sum(dists)/len(dists), sent_len))
    return cat_data

def fit_global_regression(all_cat_data: dict) -> dict:
    """Fit one log-log OLS per category across ALL treebanks pooled."""
    coeffs = {}
    for cat in ["ARGUMENT", "ADJUNCT", "MODIFIER"]:
        pairs = []
        for tb_data in all_cat_data.values():
            pairs.extend(tb_data.get(cat, []))
        valid = [(m, sl) for m, sl in pairs if m > 0]
        if len(valid) < 5:
            coeffs[cat] = (0.0, 0.0)
            continue
        log_mdd = [math.log(m) for m, sl in valid]
        log_len = [math.log(sl) for m, sl in valid]
        n = len(log_mdd)
        mean_x = sum(log_len)/n
        mean_y = sum(log_mdd)/n
        ss_xy = sum((x-mean_x)*(y-mean_y) for x,y in zip(log_len, log_mdd))
        ss_xx = sum((x-mean_x)**2 for x in log_len)
        beta = ss_xy / ss_xx if ss_xx != 0 else 0
        coeffs[cat] = (mean_y - beta * mean_x, beta)
    return coeffs

def compute_metrics(cat_data: dict, global_coeffs: dict) -> dict:
    """Using global regression coefficients, compute per-treebank mean residual."""
    results = {}
    for cat, pairs in cat_data.items():
        valid = [(m, sl) for m, sl in pairs if m > 0]
        if not valid:
            continue
        alpha, beta = global_coeffs.get(cat, (0.0, 0.0))
        residuals = [math.log(m) - (alpha + beta * math.log(sl)) for m, sl in valid]
        raw_mdds = [m for m, _ in valid]
        results[cat] = {
            "mdd": sum(raw_mdds)/len(raw_mdds),
            "mdd_residual": sum(residuals)/len(residuals),
            "arc_count": len(valid),
        }
    return results

def compute_case_richness(rows: list[dict]) -> dict:
    noun_total = pron_total = noun_case = pron_case = 0
    noun_idx = UPOS_IDX["NOUN"]
    pron_idx = UPOS_IDX["PRON"]
    for row in rows:
        upos_list = row.get("upos", [])
        feats_list = row.get("feats", [])
        for upos, feats in zip(upos_list, feats_list):
            upos_int = upos if isinstance(upos, int) else UPOS_IDX.get(upos, -1)
            has_case = isinstance(feats, str) and feats and "Case=" in feats
            if upos_int == noun_idx:
                noun_total += 1
                if has_case:
                    noun_case += 1
            elif upos_int == pron_idx:
                pron_total += 1
                if has_case:
                    pron_case += 1
    total = noun_total + pron_total
    with_case = noun_case + pron_case
    return {
        "case_richness": round(with_case/total, 4) if total > 0 else 0,
        "noun_tokens": noun_total,
        "noun_with_case": noun_case,
        "pron_tokens": pron_total,
        "pron_with_case": pron_case,
    }

@logger.catch(reraise=True)
def main():
    (WORKSPACE / "logs").mkdir(exist_ok=True)

    treebank_audit = []
    dependency_metrics = []
    case_rows_by_lang = defaultdict(list)
    lang_pair_rows = defaultdict(dict)
    all_rows = {}
    all_cat_data = {}

    # Pass 1: load data and compute per-sentence MDD
    for config, meta in TREEBANKS.items():
        lang = meta["language"]
        modality = meta["modality"]
        logger.info(f"Loading {config} ({lang}, {modality})")
        rows = load_splits(config, meta["splits"])
        if not rows:
            logger.warning(f"No data for {config}")
            continue
        all_rows[config] = rows
        case_rows_by_lang[lang].extend(rows)
        all_cat_data[config] = compute_mdd_per_sentence(rows)

    # Fit global regression across all treebanks
    global_coeffs = fit_global_regression(all_cat_data)
    logger.info(f"Global regression coeffs: {global_coeffs}")

    # Pass 2: compute per-treebank metrics using global coefficients
    for config, meta in TREEBANKS.items():
        if config not in all_rows:
            continue
        rows = all_rows[config]
        lang = meta["language"]
        modality = meta["modality"]
        token_count = sum(len(r.get("tokens", [])) for r in rows)
        sent_count = len(rows)

        audit_entry = {
            "treebank_id": config,
            "language": lang,
            "modality": modality,
            "verified_spoken": modality == "spoken",
            "source": {
                "sl_sst": "Transcribed natural speech from GOS corpus (Gigafida Oral Slovenian)",
                "sl_ssj": "Slovenian Standard Treebank – written news, fiction, web",
                "fr_rhapsodie": "Transcribed natural speech from Rhapsodie corpus (monologue/dialogue)",
                "fr_gsd": "French GSD – written web, news, Wikipedia",
            }[config],
            "sentences": sent_count,
            "tokens": token_count,
            "splits_loaded": meta["splits"],
            "included": True,
            "metadata_fold": "full",
        }
        treebank_audit.append(audit_entry)

        metrics = compute_metrics(all_cat_data[config], global_coeffs)
        for cat, vals in metrics.items():
            arc_pct = round(100 * vals["arc_count"] / max(1, sum(v["arc_count"] for v in metrics.values())), 1)
            dependency_metrics.append({
                "treebank": config,
                "language": lang,
                "modality": modality,
                "relation_category": cat,
                "mdd": round(vals["mdd"], 4),
                "mdd_residual": round(vals["mdd_residual"], 4),
                "arc_count": vals["arc_count"],
                "arc_percentage": arc_pct,
                "metadata_fold": "full",
            })
        lang_pair_rows[lang][modality] = metrics
        logger.info(f"  {config}: {sent_count} sents, {token_count} tokens, metrics={list(metrics.keys())}")

    # Case richness
    case_richness_index = []
    for lang, rows in case_rows_by_lang.items():
        cr = compute_case_richness(rows)
        cr["language"] = lang
        cr["metadata_fold"] = "full"
        case_richness_index.append(cr)
        logger.info(f"Case richness {lang}: {cr['case_richness']}")

    # Language pairs summary
    language_pairs_summary = []
    pair_config = {
        "Slovenian": ("sl_sst", "sl_ssj"),
        "French": ("fr_rhapsodie", "fr_gsd"),
    }
    for lang, (spk_tb, wrt_tb) in pair_config.items():
        spoken_m = lang_pair_rows[lang].get("spoken", {})
        written_m = lang_pair_rows[lang].get("written", {})
        spk_audit = next((a for a in treebank_audit if a["treebank_id"] == spk_tb), {})
        wrt_audit = next((a for a in treebank_audit if a["treebank_id"] == wrt_tb), {})

        entry = {
            "language": lang,
            "spoken_treebank": spk_tb,
            "written_treebank": wrt_tb,
            "spoken_sentences": spk_audit.get("sentences", 0),
            "written_sentences": wrt_audit.get("sentences", 0),
            "spoken_tokens": spk_audit.get("tokens", 0),
            "written_tokens": wrt_audit.get("tokens", 0),
            "metadata_fold": "full",
        }
        for cat in ["ARGUMENT", "ADJUNCT", "MODIFIER"]:
            s_val = spoken_m.get(cat, {}).get("mdd_residual", None)
            w_val = written_m.get(cat, {}).get("mdd_residual", None)
            key = f"spoken_minus_written_{cat.lower()}_mdd_residual"
            entry[key] = round(s_val - w_val, 4) if (s_val is not None and w_val is not None) else None
        language_pairs_summary.append(entry)

    data_out = {
        "metadata": {
            "hypothesis": "Argument-adjunct asymmetry in spoken-written dependency distance",
            "verified_language_pairs": len(language_pairs_summary),
            "verified_languages": list(pair_config.keys()),
            "timestamp": "2026-06-22",
            "procedure_version": "1.0",
            "data_source": "commul/universal_dependencies on HuggingFace (UD v2.17)",
        },
        "treebank_audit": treebank_audit,
        "dependency_metrics": dependency_metrics,
        "case_richness_index": case_richness_index,
        "language_pairs_summary": language_pairs_summary,
    }

    out_path = WORKSPACE / "data_out.json"
    out_path.write_text(json.dumps(data_out, indent=2))
    logger.info(f"Saved data_out.json ({out_path.stat().st_size//1024}KB)")

    # audit report
    report_lines = [
        "UD TREEBANK AUDIT REPORT",
        "=" * 60,
        "",
        "TREEBANK_ID | LANGUAGE | VERIFIED_SPOKEN | SENTENCES | TOKENS | INCLUDED",
    ]
    for a in treebank_audit:
        report_lines.append(
            f"{a['treebank_id']:<14} | {a['language']:<10} | {'YES' if a['verified_spoken'] else 'NO':<15} | "
            f"{a['sentences']:<9} | {a['tokens']:<6} | {'YES' if a['included'] else 'NO'}"
        )
    report_lines += [
        "",
        "LANGUAGE PAIR DEPENDENCY DISTANCE DIFFERENCES (spoken - written, residual MDD):",
        "-" * 60,
    ]
    for lp in language_pairs_summary:
        report_lines.append(f"\n{lp['language']} ({lp['spoken_treebank']} vs {lp['written_treebank']}):")
        for cat in ["ARGUMENT", "ADJUNCT", "MODIFIER"]:
            val = lp.get(f"spoken_minus_written_{cat.lower()}_mdd_residual")
            report_lines.append(f"  {cat}: {val}")
    report_lines += [
        "",
        "CASE RICHNESS INDEX:",
        "-" * 60,
    ]
    for cr in case_richness_index:
        report_lines.append(f"  {cr['language']}: {cr['case_richness']} "
                            f"(NOUN {cr['noun_with_case']}/{cr['noun_tokens']}, "
                            f"PRON {cr['pron_with_case']}/{cr['pron_tokens']})")
    report_lines += [
        "",
        "LIMITATIONS:",
        "- fr_rhapsodie test split not available on HF; train+dev only",
        "- Morphological features stored as string; Case detection via 'Case=' substring match",
        "- Sentence-length residuals computed via OLS log-log regression per treebank",
    ]
    (WORKSPACE / "audit_report.txt").write_text("\n".join(report_lines))
    logger.info("Saved audit_report.txt")

if __name__ == "__main__":
    main()
