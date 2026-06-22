#!/usr/bin/env python3
# /// script
# dependencies = ["loguru"]
# ///
"""
Convert UD treebank dependency-arc data into exp_sel_data_out.json format.
Each example = one sentence from a treebank, with full arc-level statistics as input/output.
"""

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
    base = deprel.split(":")[0]
    if deprel in ARGUMENT_RELS or base in ARGUMENT_RELS:
        return "ARGUMENT"
    if deprel in ADJUNCT_RELS or base == "acl":
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
    logger.info(f"  {config}: {len(rows)} sentences loaded")
    return rows


def sentence_to_example(row: dict, config: str, language: str, modality: str, sent_idx: int) -> dict | None:
    """Convert one UD sentence to one exp_sel_data_out example."""
    heads   = row.get("head", [])
    deprels = row.get("deprel", [])
    tokens  = row.get("tokens", [])
    upos    = row.get("upos", [])
    feats   = row.get("feats", [])

    if not heads or not deprels:
        return None

    sent_len = len(heads)
    arc_stats = defaultdict(list)  # cat -> [dist, ...]

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
        arc_stats[cat].append(abs(h - (i + 1)))

    # Require at least one arc of any category
    if not arc_stats:
        return None

    # Build per-category MDD summary
    cat_summary = {}
    for cat in ["ARGUMENT", "ADJUNCT", "MODIFIER"]:
        dists = arc_stats.get(cat, [])
        cat_summary[cat] = {
            "count": len(dists),
            "mdd": round(sum(dists) / len(dists), 4) if dists else None,
        }

    # Case richness for this sentence
    noun_idx = UPOS_IDX["NOUN"]
    pron_idx = UPOS_IDX["PRON"]
    noun_total = pron_total = noun_case = pron_case = 0
    for u, f in zip(upos, feats):
        u_int = u if isinstance(u, int) else UPOS_IDX.get(u, -1)
        has_case = isinstance(f, str) and f and "Case=" in f
        if u_int == noun_idx:
            noun_total += 1
            if has_case:
                noun_case += 1
        elif u_int == pron_idx:
            pron_total += 1
            if has_case:
                pron_case += 1

    # Input: sentence text + arc summary
    text = row.get("text", "")
    input_str = json.dumps({
        "text": text,
        "sent_len": sent_len,
        "treebank": config,
        "modality": modality,
        "language": language,
        "arc_stats": cat_summary,
    }, ensure_ascii=False)

    # Output: structured summary of spoken/written contrast-relevant features
    output_str = json.dumps({
        "modality": modality,
        "language": language,
        "argument_mdd": cat_summary["ARGUMENT"]["mdd"],
        "adjunct_mdd":  cat_summary["ADJUNCT"]["mdd"],
        "modifier_mdd": cat_summary["MODIFIER"]["mdd"],
        "argument_count": cat_summary["ARGUMENT"]["count"],
        "adjunct_count":  cat_summary["ADJUNCT"]["count"],
        "modifier_count": cat_summary["MODIFIER"]["count"],
        "noun_with_case": noun_case,
        "pron_with_case": pron_case,
        "noun_total": noun_total,
        "pron_total": pron_total,
    }, ensure_ascii=False)

    return {
        "input": input_str,
        "output": output_str,
        "metadata_fold": "full",
        "metadata_treebank": config,
        "metadata_language": language,
        "metadata_modality": modality,
        "metadata_sent_id": str(row.get("sent_id", sent_idx)),
        "metadata_sent_len": sent_len,
        "metadata_row_index": sent_idx,
        "metadata_task_type": "dependency_distance_analysis",
    }


@logger.catch(reraise=True)
def main():
    (WORKSPACE / "logs").mkdir(exist_ok=True)

    # All 4 treebank configs belong to the single source dataset commul/universal_dependencies.
    # They are grouped under one dataset entry because the hypothesis requires spoken-written pairs.
    all_examples = []

    for config, meta in TREEBANKS.items():
        lang     = meta["language"]
        modality = meta["modality"]
        logger.info(f"Processing {config} ({lang}, {modality})")

        rows = load_splits(config, meta["splits"])

        for i, row in enumerate(rows):
            ex = sentence_to_example(row, config, lang, modality, i)
            if ex is not None:
                all_examples.append(ex)

        logger.info(f"  {config}: {sum(1 for e in all_examples if e['metadata_treebank'] == config)} examples so far")

    datasets = [{"dataset": "commul/universal_dependencies", "examples": all_examples}]

    full_data_out = {"datasets": datasets}
    out_path = WORKSPACE / "full_data_out.json"
    out_path.write_text(json.dumps(full_data_out, ensure_ascii=False, indent=2))

    total = sum(len(d["examples"]) for d in datasets)
    logger.info(f"Saved full_data_out.json: {total} total examples across {len(datasets)} datasets")


if __name__ == "__main__":
    main()
