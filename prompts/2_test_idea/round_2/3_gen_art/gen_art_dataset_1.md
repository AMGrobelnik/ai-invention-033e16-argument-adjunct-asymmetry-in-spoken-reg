# gen_art_dataset_1 — test_idea

> Phase: `invention_loop` · round 2 · `gen_art`
> Run: `run_4SjiUyyE35Gi` — Argument-Adjunct Asymmetry in Spoken-Register Dependency Distance Minimization
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_dataset_1` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-22 12:11:21 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: An artifact executor (Step 3.3: GEN_ART in the invention loop)

Executing a plan to produce a concrete artifact.
GEN_PAPER_TEXT will use your artifact in the next paper draft.

Rigorous artifact with clear results → strong paper. Sloppy artifact → misdirected research.
</your_role>
</ai_inventor_context>

<task>
Find, evaluate, and prepare high-quality datasets for the research experiment.
Adapt your search strategy based on the hypothesis and domain requirements.
</task>

<common_mistakes_to_avoid>
Critical pitfalls from past runs. MUST check for and avoid each one.

**1. Picking Obscure or Unusable Datasets**
Do NOT select datasets just because they match a keyword. Red flags: very few downloads (<100), no documentation (dataset card, paper, or GitHub page). Prefer well-used datasets (not necessarily popular or widely known) with clear documentation.
CHECK: >100 downloads? Has documentation? If any "no" → find a better dataset.

**2. Fabricating Dataset Provenance**
Do NOT invent justifications for why a dataset is relevant. If a dataset name contains a number (e.g., "797"), do NOT assume it refers to a specific benchmark suite, OpenML ID, or paper without verification. In past runs, an agent assumed "797" referred to "OpenML benchmark suite 797" with zero evidence, then fabricated a rationale. This was completely false.
CHECK: Can you cite a specific, verifiable source (paper, benchmark page, dataset card) confirming this dataset is what you claim? If not, do not make provenance claims.

**3. Not Verifying Dataset Usefulness**
Always sanity-check that a dataset is actually suitable for the task before committing. Download a sample, inspect the features, and run a quick baseline appropriate for the domain. If the dataset lacks signal or structure for the hypothesis being tested, the entire experiment is wasted.

**4. Settling for the Only Search Result**
If your search returns only 1-2 results, your search terms are too narrow. Broaden your queries, try different keyword combinations, or search for well-known benchmark datasets in the domain. A single obscure result from a narrow query should never be your final choice.
CHECK: Fewer than 5 candidate datasets? Run additional searches with broader or different terms before making a selection.
</common_mistakes_to_avoid>

<critical_requirements>
- Keep final response under 300 characters
</critical_requirements>

<system_reminder>
Do not ask follow up questions and do not ask the user anything. Execute all steps independently.
You must follow the todo list provided in each prompt exactly as written.
No placeholders, stubs, or incomplete code — all code must be complete and functional.
</system_reminder>

<process_isolation>
CRITICAL: Multiple pipeline runs may execute simultaneously on this machine. `ps aux | grep method.py` matches ALL runs, not just yours.
- NEVER kill processes by name (`killall`, `pkill -f`, `ps aux | grep ... | xargs kill`). This kills OTHER runs' processes.
- NEVER monitor processes by name (`ps aux | grep method.py`). You will see other runs' processes and get confused.
- ALWAYS use PID-based process management:
  Run: `uv run method.py & PID=$!` or `timeout <seconds> uv run method.py & PID=$!`
  Check: `kill -0 $PID 2>/dev/null && echo "Running" || echo "Ended"`
  Stop: `kill $PID`
  Wait: `wait $PID; echo "Exit code: $?"`
  Monitor: `tail -f logs/run.log & TAIL_PID=$!` then `kill $TAIL_PID` when done
</process_isolation>

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_4SjiUyyE35Gi/3_invention_loop/iter_2/gen_art/gen_art_dataset_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_4SjiUyyE35Gi/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_4SjiUyyE35Gi/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/file.py`, `/ai-inventor/aii_data/runs/run_4SjiUyyE35Gi/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_4SjiUyyE35Gi/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_dataset_1_idx1
type: dataset
title: >-
  Audit and Verify Spoken-Written UD Treebank Pairs with Dependency Metrics and Case-Richness Index
summary: >-
  Load all treebanks from commul/universal_dependencies on HuggingFace, audit each for genuine transcribed speech vs. written
  text using official UD GitHub documentation, identify verified spoken-written language pairs, extract and classify all dependency
  arcs into ARGUMENT (nsubj, obj, iobj, ccomp, xcomp), ADJUNCT (advcl, acl, acl:relcl), and MODIFIER (nmod, amod, advmod)
  categories, compute mean dependency distance (MDD) per relation type per treebank, and recompute case-richness using a transparent,
  single-procedure methodology (proportion of NOUN + PRON tokens with non-empty Case feature). Output JSON with verified language
  pairs, dependency metrics, and a detailed audit report documenting which treebanks were included/excluded with justification.
runpod_compute_profile: cpu_heavy
ideal_dataset_criteria: >-
  Real Universal Dependencies treebanks (300+ language-specific configurations in commul/universal_dependencies on HuggingFace);
  specifically: (1) treebanks explicitly documented as transcribed natural speech in official UD GitHub READMEs or academic
  papers; (2) matched pairs with a written counterpart in the same language; (3) dependency annotation in CONLL-U format with
  lemmas, UPOS, morphological features (including Case), and UD dependency relations; (4) size ≥ 50 sentences minimum per
  split for statistical validity; (5) access to metadata (genre, domain, source, speaker demographics where available). Priority:
  Slovenian sl_sst + sl_ssj pair (documented as transcribed speech); French fr_rhapsodie + fr_gsd pair (documented as transcribed
  speech); English en_gum (conversational/interview/vlog/speech genres only, paired with written subset en_ewt or en_partut,
  if low-overlap); secondary exploration of other mixed-modality treebanks (Danish, Polish, Swedish, Greek, etc.) documented
  in 2022 LREC overview, but only after verification.
dataset_search_plan: "Execute the following steps in sequence:\n\n**Phase 1: Discover and Audit Treebanks (Primary)**\n\n\
  1. Load commul/universal_dependencies from HuggingFace Datasets library; iterate through all available configurations (treebank\
  \ identifiers) to identify which are marked as spoken or contain mixed modality in their name or metadata.\n\n2. For each\
  \ candidate spoken treebank (sl_sst, fr_rhapsodie, en_gum, and any others flagged in HuggingFace metadata):\n   - Fetch\
  \ the official UD GitHub repository README file (e.g., https://github.com/UniversalDependencies/UD_Slovenian-SST/blob/master/README.md)\n\
  \   - Verify the DATA SOURCE section: confirm that the source is transcribed natural speech (not transcribed written text,\
  \ journalism, or L2 learner corpora)\n   - Document: treebank name, language, data source, speech type (monologic, dialogic,\
  \ multi-party), size (sentences, tokens, speakers where available), availability of audio recordings or speech metadata\n\
  \   - EXCLUDE any treebank where: (a) the source is written text (e.g., de_hdt = newspaper, ru_syntagrus = journalistic),\
  \ (b) the corpus is L2 learner speech (en_eslspok), or (c) documentation is missing or ambiguous\n\n3. For each verified\
  \ spoken treebank, identify a written counterpart in the same language:\n   - Search the UD GitHub organization for alternate\
  \ treebanks of the same language\n   - Prioritize treebanks annotated as news, fiction, or web-based (clearly written)\n\
  \   - Document the pairing rationale (e.g., sl_sst spoken + sl_ssj written Slovenian Standard treebank)\n   - Note any data\
  \ overlap issues (e.g., en_gum spoken and en_ewt written may share sources) and document the decision to include or exclude\
  \ the pair\n\n4. Special handling for English:\n   - Load en_gum and filter by genre metadata (\"conversation\", \"vlog\"\
  , \"speech\", \"podcast\" = SPOKEN; \"news\", \"fiction\", \"web\", \"email\", \"blog\", \"government\", \"legal\" = WRITTEN)\n\
  \   - If en_gum spoken subset is >= 50 sentences, pair it with a distinct written baseline (prefer en_partut over en_ewt\
  \ to minimize overlap; document choice)\n   - If en_gum spoken is too sparse (< 50 sentences), document as \"insufficient\
  \ English native spoken data\" and acknowledge in the audit report\n\n5. Output audit_report.txt with columns: TREEBANK_ID\
  \ | LANGUAGE | VERIFIED_SPOKEN? (YES/NO) | REASON (transcribed_speech / newspaper / learner_ESL / missing_docs / low_sample)\
  \ | WRITTEN_PAIR | DATA_SIZE | SOURCE_NOTES | INCLUDED_IN_ANALYSIS? (YES/NO)\n\n**Phase 2: Load and Structure Data (Primary)**\n\
  \n6. For each verified spoken-written pair, load both treebanks from HuggingFace in CONLL-U format.\n\n7. For each treebank,\
  \ extract all sentences and dependency arcs:\n   - Iterate through all sentences in train + dev + test splits (combined)\n\
  \   - For each dependency arc (head_id, dependent_id, deprel), record: (a) the deprel label (e.g., \"nsubj\", \"advcl:relcl\"\
  ), (b) the linear distance = abs(head_position - dependent_position), (c) sentence length (token count)\n   - Separate enhancement\
  \ dependencies (those marked with subtypes, e.g., \"acl:relcl\") from core dependency labels for classification purposes\n\
  \n8. Classify every dependency relation into one of three categories:\n   - ARGUMENT: nsubj, obj, iobj, ccomp, xcomp (obligatory,\
  \ core grammatical participants)\n   - ADJUNCT: advcl, acl, acl:relcl (optional, peripheral, elaborating information; collapse\
  \ acl and acl:relcl into a single ADJUNCT category for statistical power)\n   - MODIFIER: nmod, amod, advmod (nominal/adverbial\
  \ modifiers; these serve as the within-analysis control)\n   - EXCLUDED: all other relations (case, mark, det, etc.) to\
  \ focus on the three categories of interest\n\n9. For each treebank × relation_category combination, compute:\n   - Mean\
  \ Dependency Distance (MDD) = mean of all linear distances in that category\n   - Sentence-length-adjusted MDD = regress\
  \ log(MDD) on log(sentence_length), extract residuals per sentence, and use residuals as the normalized metric\n   - Count\
  \ of dependency arcs in each category (for weighting and transparency)\n\n10. Store intermediate results as:\n    - {\"\
  treebank\": \"sl_sst\", \"language\": \"Slovenian\", \"modality\": \"spoken\", \"relation_category\": \"ARGUMENT\", \"mdd\"\
  : 1.45, \"mdd_normalized\": -0.12, \"arc_count\": 3421}\n    - {\"treebank\": \"sl_ssj\", \"language\": \"Slovenian\", \"\
  modality\": \"written\", \"relation_category\": \"ARGUMENT\", \"mdd\": 2.10, \"mdd_normalized\": 0.34, \"arc_count\": 8942}\n\
  \    - (etc. for each treebank-category pair)\n\n**Phase 3: Compute Case-Richness Index (Secondary)**\n\n11. For each language\
  \ in the verified pairs (Slovenian, French, English, + any additional treebanks):  \n    - Load BOTH spoken and written\
  \ treebanks\n    - Iterate through all tokens across both treebanks combined (union of train+dev+test)\n    - Filter to\
  \ NOUN and PRON tokens only (exclude PROPN per hypothesis specification)\n    - Count tokens with non-empty Case feature\
  \ in the UD morphological annotation (conllu[token][\"feats\"][\"Case\"] is not None/empty)\n    - Compute case_richness\
  \ = (tokens_with_case) / (total_noun_pron_tokens)\n    - Document token counts used for transparency: total_noun_count,\
  \ total_pron_count, noun_with_case, pron_with_case\n\n12. Store case-richness index as:\n    - {\"language\": \"Slovenian\"\
  , \"case_richness\": 0.94, \"noun_tokens\": 12403, \"noun_with_case\": 11659, \"pron_tokens\": 3441, \"pron_with_case\"\
  : 3389}\n    - (repeat for each language)\n\n13. (Optional sanity check) Cross-reference case-richness values with WALS\
  \ typological data (manually via web search if time permits; document any large discrepancies).\n\n**Phase 4: Assemble Final\
  \ Output**\n\n14. Create data_out.json with structure:\n    ```json\n    {\n      \"metadata\": {\n        \"hypothesis\"\
  : \"Argument-adjunct asymmetry in spoken-written dependency distance\",\n        \"verified_language_pairs\": 2,\n     \
  \   \"verified_languages\": [\"Slovenian\", \"French\"],\n        \"timestamp\": \"2026-06-22\",\n        \"procedure_version\"\
  : \"1.0\"\n      },\n      \"treebank_audit\": [\n        {\"treebank_id\": \"sl_sst\", \"language\": \"Slovenian\", \"\
  verified_spoken\": true, \"source\": \"Transcribed natural speech from GOS corpus\", \"tokens\": 98393, \"included\": true},\n\
  \        {\"treebank_id\": \"sl_ssj\", \"language\": \"Slovenian\", \"verified_spoken\": false, \"source\": \"Slovenian\
  \ Standard Treebank (written)\", \"tokens\": 456789, \"included\": true},\n        ...\n      ],\n      \"dependency_metrics\"\
  : [\n        {\"treebank\": \"sl_sst\", \"language\": \"Slovenian\", \"modality\": \"spoken\", \"relation_category\": \"\
  ARGUMENT\", \"mdd\": 1.45, \"mdd_residual\": -0.12, \"arc_count\": 3421, \"arc_percentage\": 28.5},\n        {\"treebank\"\
  : \"sl_ssj\", \"language\": \"Slovenian\", \"modality\": \"written\", \"relation_category\": \"ARGUMENT\", \"mdd\": 2.10,\
  \ \"mdd_residual\": 0.34, \"arc_count\": 8942, \"arc_percentage\": 31.2},\n        ...\n      ],\n      \"case_richness_index\"\
  : [\n        {\"language\": \"Slovenian\", \"case_richness\": 0.94, \"noun_tokens_with_case\": 11659, \"total_noun_tokens\"\
  : 12403, \"pron_tokens_with_case\": 3389, \"total_pron_tokens\": 3441},\n        {\"language\": \"French\", \"case_richness\"\
  : 0.08, \"noun_tokens_with_case\": 1203, \"total_noun_tokens\": 15102, ...},\n        ...\n      ],\n      \"language_pairs_summary\"\
  : [\n        {\"language\": \"Slovenian\", \"spoken_treebank\": \"sl_sst\", \"written_treebank\": \"sl_ssj\", \"spoken_tokens\"\
  : 98393, \"written_tokens\": 456789, \"spoken_minus_written_arg_mdd_residual\": -0.46, \"spoken_minus_written_adj_mdd_residual\"\
  : 0.18, \"spoken_minus_written_mod_mdd_residual\": 0.02},\n        {\"language\": \"French\", \"spoken_treebank\": \"fr_rhapsodie\"\
  , \"written_treebank\": \"fr_gsd\", \"spoken_tokens\": 44242, \"written_tokens\": 401692, \"spoken_minus_written_arg_mdd_residual\"\
  : -0.31, \"spoken_minus_written_adj_mdd_residual\": 0.22, \"spoken_minus_written_mod_mdd_residual\": -0.04},\n        ...\n\
  \      ]\n    }\n    ```\n\n15. Ensure all rows in data_out.json include metadata_fold field (set to \"full\" for all rows,\
  \ since no train/dev/test split is needed for this descriptive analysis).\n\n16. Create audit_report.txt (plain text, human-readable)\
  \ with:\n    - Summary table of treebank audit decisions\n    - Detailed reasoning for each exclusion (if any)\n    - Data\
  \ quality notes (e.g., missing morphological features in fr_rhapsodie)\n    - Limitations and caveats\n    - Recommendations\
  \ for future verification (e.g., manual spot-checks of annotation quality)\n\n**Phase 5: Validation and Quality Control**\n\
  \n17. Sanity checks:\n    - Verify that MDD values are positive and plausible (typically 1.0–3.0 for natural languages)\n\
  \    - Confirm that sentence-length-normalized residuals have mean ≈ 0 and are roughly symmetric\n    - Cross-check case-richness\
  \ values for obvious errors (should be 0–1 range; flag any language with case_richness > 0.95 or < 0.05 for manual review)\n\
  \    - Confirm that all verified treebanks have sufficient sample sizes (≥ 50 sentences per category)\n\n18. Document any\
  \ data cleaning steps (e.g., handling of multiword tokens, exclusion of punctuation, special dependency arcs).\n\n**Fallback\
  \ and Failure Scenarios**\n\n- **Sparse spoken data**: If a language has < 50 sentences in the spoken subset, document as\
  \ \"insufficient_sample\" and exclude from primary analysis; note it as a secondary candidate pending additional treebank\
  \ coverage.\n- **Missing morphological features**: If a treebank (e.g., fr_rhapsodie) lacks Case annotations, document this\
  \ limitation and compute case-richness using only the language's other verified treebank (if available).\n- **Data overlap**:\
  \ If spoken and written treebanks share sources (e.g., en_gum and en_ewt), document the shared fraction and decide pair-wise\
  \ whether the overlap is acceptable; prioritize clean non-overlapping pairs.\n- **Ambiguous documentation**: If a treebank's\
  \ UD GitHub documentation is unclear, search for the corresponding academic paper (2016 papers for early treebanks, 2020+\
  \ papers for newer ones) or contact the treebank maintainers (document the attempt).\n- **Discovery of additional verified\
  \ pairs**: If the audit uncovers additional high-confidence spoken-written pairs (e.g., Danish DDT if verified as genuinely\
  \ spoken), include them in Phase 2–4 steps; report final count in audit_report.txt."
target_num_datasets: 1
</artifact_plan>



<available_resources>
<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **HARD LIMIT**: Maximum $10 USD total spend on LLM API calls (OpenRouter). Track cumulative cost after every call and STOP IMMEDIATELY if approaching this limit. Never exceed this budget under any circumstances.
</software_constraints>

<skills>
Skills are self-contained capabilities with instructions, context, and tools.

- aii-web-tools: Web search (Serper), page/PDF fetch as markdown, regex grep over page/PDF text
- aii-semscholar-bib: Batch-fetch BibTeX from Semantic Scholar
- aii-openrouter-llms: Search and call 300+ LLMs via OpenRouter
- aii-hf-datasets: Search, preview, download HuggingFace datasets
- aii-owid-datasets: Search and load Our World in Data tables
- aii-lean: Compile/verify Lean 4 code, Mathlib search, tactic suggestions
- aii-image-gen: Generate/edit images via Gemini 3 Pro Image (Nano Banana Pro)
- aii-json: Validate JSON against schemas, generate mini/preview variants
- aii-paper-writing: Academic paper structure, bibliography, citations
- aii-paper-to-latex: Assemble LaTeX papers and compile to PDF
- aii-parallel-computing: GPU acceleration, CPU parallelism, async I/O
- aii-python: Python coding standards for experiment scripts
- aii-use-hardware: Detect CPU/RAM/GPU, memory-safe processing
- aii-long-running-tasks: Gradual scaling pattern for long-running tasks
- aii-colab: Google Colab runtime constraints for notebooks
- aii-file-size-limit: Check and split oversized output files
- aii-handbook-multi-llm-agents: Multi-LLM agent orchestration patterns
</skills>
</available_resources>

<available_data_sources>
Use the sources appropriate to your task. Read the relevant skill file BEFORE using each source.

- **HuggingFace Hub** (HF) — ML datasets (NLP, vision, tabular, benchmarks)
- **Our World in Data** (OWID) — Global statistics (energy, health, economics, environment, demographics)
- **Alternate methods** — Python/shell (sklearn.datasets, openml, direct URL, APIs, etc.)

If the plan specifies a source or one fits better, use it.
You may combine sources. Use web search (aii-web-tools skill) to research candidates (background, papers, provenance) — NOT to find/download datasets.
</available_data_sources>

<available_domain_handbooks>
If your domain has a handbook, read the relevant skill file BEFORE working on that domain.

- **Multi-LLM Agents** — dataset selection, evaluation metrics, agent orchestration patterns
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-python, aii-long-running-tasks, aii-json, aii-file-size-limit, aii-use-hardware, aii-parallel-computing.
TODO 2. Read skill files for your data sources (see <available_data_sources>) and domain handbook if applicable (see <available_domain_handbooks>). Based on plan and context, decide which source(s) to use. Include everything specified in the artifact plan, but you may also collect additional relevant data beyond what's listed. Run 8 diverse searches across chosen source(s) — BROAD, GENERAL terms, not very specific. Parallelize where supported.
TODO 3. Identify the 4 most promising datasets. IMPORTANT: Only consider datasets under 300MB. Preview/inspect sample rows for each candidate. Parallelize previews.
TODO 4. Research each candidate BEFORE choosing which to download. For each, search the web (aii-web-tools skill): dataset name, papers citing it, original source/task, popularity. Red flags: no search results, no papers, anonymized features (F1, F2...), <100 downloads, no documentation. Green flags: papers using it, clear documentation, meaningful features, established benchmark. Also consider: will features/structure allow meaningful evaluation of the planned method?
TODO 5. Decide which to KEEP vs DISCARD. Look for: clear structure, relevant fields, quality examples matching requirements, confirmed provenance. Determine which 2 datasets have the most suitable data. Download and save to `temp/datasets/`. Parallelize downloads.
</todos>
````

### [2] HUMAN-USER prompt · 2026-06-22 12:11:21 UTC

```
Direction: Computational Linguistics — Dependency Distance Minimization Across UD Treebanks. Something genuinely novel and groundbreaking that measures dependency-distance distributions across UD treebanks, investigates whether spoken language minimizes more than written, characterizes how typology interacts with the pattern, and identifies families that deviate. MUST use commul/universal_dependencies on HuggingFace.

Ambition: level 3 of 5 — phenomenological science: surface and rigorously characterize a new empirical regularity or anomaly in the data, even before a full theoretical explanation exists.

Reviewer: I am Kaja Dobrovoljc (JSI / University of Ljubljana). Calibrate from my existing papers. Cross-domain methods (information theory, mixed-effects models, sequence models) welcome — but keep them close to what I already know, not too far from my background.

Submission/Goal: a paper for ACL, EMNLP, or the Computational Linguistics journal. Audience: computational linguists and quantitative typologists. Tone: empirically rigorous, careful with linguistic detail, reproducible on public UD.
```

### [3] SKILL-INPUT — aii-python · 2026-06-22 12:11:55 UTC

The agent loaded the **aii-python** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-python
description: Python coding standards for experiment and evaluation scripts. Covers environment setup, logging, error handling, and code structure.
---

## Environment Setup

- Python 3.12+
- **NEVER use `pip` or `.venv/bin/pip`** — they are not installed. Use `uv` for ALL package operations:
  ```bash
  uv venv .venv --python=3.12
  source .venv/bin/activate  # or: .venv/bin/python script.py
  uv pip install pandas loguru  # NOT: pip install
  ```
- Create `.toml` file with dependencies, create uv `.venv` and activate it
- NO inline dependencies (no `# /// script` headers)

## Logging

Use `loguru` for all logging. Add a file sink alongside stdout.

```python
from loguru import logger
import sys

logger.remove()  # Remove default handler
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")
```

Rules:
- Log every major step (data loading, processing start/end, results)
- If applicable, log every LLM API call input and output
- Truncate long outputs in logs (add truncation logic for potentially large strings)
- Use `logger.error()` in except blocks (traceback auto-captured)

## Error Handling

- Wrap major operations in try/except blocks
- Use `@logger.catch(reraise=True)` decorator on main functions — without `reraise=True`, the script exits 0 even on uncaught exceptions, hiding failures from downstream consumers
- Use explicit exception types, not bare `except:`
- Never silently swallow exceptions — always log them

```python
@logger.catch(reraise=True)
def main():
    try:
        data = load_data(path)
    except FileNotFoundError:
        logger.error("Data file not found")
        raise
    except json.JSONDecodeError:
        logger.error("Invalid JSON in data file")
        raise
```

## Code Structure

- Use `pathlib.Path` for file operations: `Path("data/input.json").read_text()` not `open(...).read()`
- Use type hints for function signatures
- Use keyword arguments for functions with more than 4 parameters
- No hardcoded paths — derive from script location or accept as arguments

## Script Pattern

Standard pattern for experiment/evaluation scripts:

```python
#!/usr/bin/env python3
"""Brief description of what this script does."""

from loguru import logger
from pathlib import Path
import json
import sys

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

@logger.catch(reraise=True)
def main():
    # Load data
    data_path = Path("full_data_out.json")
    logger.info(f"Loading data from {data_path}")
    data = json.loads(data_path.read_text())
    logger.info(f"Loaded {len(data['examples'])} examples")

    # Process
    results = []
    for i, example in enumerate(data["examples"]):
        try:
            result = process(example)
            results.append(result)
        except Exception:
            logger.error(f"Failed on example {i}")
            continue

    # Save output
    output = {"examples": results}
    Path("method_out.json").write_text(json.dumps(output, indent=2))
    logger.info(f"Saved {len(results)} results")

if __name__ == "__main__":
    main()
```
````

### [4] SKILL-INPUT — aii-hf-datasets · 2026-06-22 12:11:55 UTC

The agent loaded the **aii-hf-datasets** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-hf-datasets
description: Searches, previews, and downloads datasets from HuggingFace Hub. Use when user needs machine learning datasets, training data, HuggingFace datasets, dataset discovery, or .parquet/.json exports.
---

## Contents

- Workflow (3-phase dataset discovery)
- Scripts (Search, Preview, Download)

**IMPORTANT - Parallel execution:** GNU `parallel` subshells do NOT inherit `source activate`. Use `export` for variables and **single-quoted** command templates so parallel's subshells can resolve them:
```
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

---

## Workflow: 3-Phase Dataset Discovery

### Phase 1: Search for Datasets
Find datasets with metadata (configs, splits, features, sizes)
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_search_datasets.py --query "sentiment analysis" --limit 5
```

### Phase 2: Preview Dataset (if promising)
Inspect metadata AND sample rows in one call
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_preview_datasets.py openai/gsm8k
```

### Phase 3: Download Dataset (if suitable)
Download after reviewing the preview
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_download_datasets.py openai/gsm8k --config main --split train
```

---

## Scripts

### Search HuggingFace Datasets (aii_hf_search_datasets.py)

Search and discover datasets on HuggingFace Hub.

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_search_datasets.py --query "text classification" --limit 5
```

**Parallel execution (multiple queries):**

IMPORTANT: Use full python path with GNU parallel (venv activate does NOT work in parallel subshells):
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_hf_search_datasets.py" && \
parallel -j 10 -k --group --will-cite '$PY $S --query {} --limit 3' ::: 'sentiment' 'classification' 'translation'
```

**Example output:**
```
Found 5 dataset(s) for query='text classification'

============================================================
Dataset 1: stanfordnlp/imdb
Downloads: 2,500,000 | Likes: 1,234
Description: Large Movie Review Dataset for binary sentiment classification...
Tags: text-classification, en, sentiment-analysis
```

**Result fields per dataset:**

Each entry in ``results`` carries:

- ``id`` / ``downloads`` / ``likes`` / ``tags`` / ``description`` — standard
  HF metadata
- ``has_loader_script`` (bool) — repo ships a top-level ``<repo>.py`` loader.
  ``datasets>=3`` won't run these directly; the dataset is reachable only
  via the Datasets Server's pre-converted parquet shards. Treat as a yellow
  flag.
- ``loadable`` (bool) — **prefer datasets where this is ``True``.** Means
  the dataset is reachable via *some* path: either native parquet (no
  script) or HF auto-converted the script's output to parquet. When
  ``False``, the script needs deps HF can't install (e.g. ``conllu``,
  custom audio decoders) and ``aii_hf_datasets__download_datasets`` will
  fail — pick a different candidate.

**Parameters:**

`--query` (optional)
- Search query string
- Example: `--query "sentiment analysis"`

`--limit` (optional)
- Maximum number of results (default: 5)

`--tags` (optional)
- Filter by tags (comma-separated)
- Format: `category:value`
- Examples: `language:en`, `task_categories:text-classification`

`--sort` (optional)
- Sort by field: `downloads`, `likes` (default: downloads)

**Tips:**
- Search displays full dataset metadata
- Use tags to filter: `--tags "language:en,task_categories:translation"`

---

### Preview HuggingFace Dataset (aii_hf_preview_datasets.py)

Inspect a specific dataset - shows metadata AND sample rows.

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_preview_datasets.py openai/gsm8k --num-rows 5
```

**Parallel execution (multiple datasets):**

IMPORTANT: Use full python path with GNU parallel:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_hf_preview_datasets.py" && \
parallel -j 10 -k --group --will-cite '$PY $S {} --num-rows 3' ::: 'openai/gsm8k' 'imdb' 'squad'
```

**Example output:**
```
============================================================
Dataset: openai/gsm8k
============================================================
Downloads: 425,109 | Likes: 1,102

Description: GSM8K (Grade School Math 8K) is a dataset of 8.5K high quality
linguistically diverse grade school math word problems...

Configs: main, socratic

--- Sample Rows (train) ---
Columns: question, answer

Row 1:
  question: Natalia sold clips to 48 of her friends in April...
  answer: Natalia sold 48/2 = <<48/2=24>>24 clips in May...
```

**Parameters:**

`dataset_id` (required, positional)
- HuggingFace dataset ID
- Examples: `openai/gsm8k`, `glue`, `imdb`

`--config` (optional)
- Dataset configuration/subset name
- Auto-detects first config if not specified

`--split` (optional)
- Split to preview (default: `train`)

`--num-rows` (optional)
- Number of sample rows (default: 5, max: 20)

**Tips:**
- Use after search to verify data structure
- Streaming mode - doesn't download full dataset

---

### Download HuggingFace Dataset (aii_hf_download_datasets.py)

Download datasets and save to files.

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_download_datasets.py openai/gsm8k --config main --split train
```

**Parallel execution (multiple datasets):**

IMPORTANT: Use full python path with GNU parallel. Use `eval {}` pattern when datasets need different flags (e.g. `--config`):
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_hf_download_datasets.py" && \
parallel -j 10 -k --group --will-cite 'eval {}' ::: '$PY $S openai/gsm8k --config main --split train' '$PY $S imdb --split train' '$PY $S squad --split train'
```

**Example output:**
```
Downloaded: openai/gsm8k

  train:
    Rows: 7,473
    Preview: temp/datasets/preview_openai_gsm8k_main_train.json
    Mini: temp/datasets/mini_openai_gsm8k_main_train.json
    Full: temp/datasets/full_openai_gsm8k_main_train.json
```

**Parameters:**

`dataset_id` (required, positional)
- HuggingFace dataset ID
- Examples: `openai/gsm8k`, `imdb`

`--config` (optional)
- Dataset configuration/subset name
- Use preview to see available configs

`--split` (optional)
- Specific split to load (e.g., `train`, `test`)
- If not specified, loads all splits

`--output-dir` (optional)
- Output directory (default: `temp/datasets/`)

**Output files (auto-saved):**
1. **Preview**: `preview_{dataset}_{split}.json` - 3 truncated rows - **READ THIS** for quick inspection
2. **Mini**: `mini_{dataset}_{split}.json` - 3 full rows - for development/testing
3. **Full**: `full_{dataset}_{split}.json` - All rows - **DO NOT READ directly** - use as input path for code

**Tips:**
- Only read preview file directly with Read tool
- Mini and full are input paths for processing code

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````

### [5] SKILL-INPUT — aii-file-size-limit · 2026-06-22 12:19:04 UTC

The agent loaded the **aii-file-size-limit** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

```
---
name: aii-file-size-limit
description: File size check procedure for splitting oversized output files. Use after generating JSON output files to check and split files exceeding the provided size limit.
---

## File Size Check

After generating output files, run `ls -lh` to check sizes. If ANY file exceeds the provided file size limit:

1. Create directory with same base name (e.g., `data_out/` for `full_data_out.json`)
2. Split into parts under the limit named: `full_data_out_1.json`, `full_data_out_2.json`, etc.
3. Place parts in directory (e.g., `data_out/full_data_out_1.json`, `data_out/full_data_out_2.json`)
4. Delete the original oversized file
5. Update the script to read from split files: `for f in sorted(glob.glob('data_out/full_data_out_*.json')): data.extend(json.load(open(f)))`
6. For each split part, generate its own mini/preview versions with the json skill's format script
```

### [6] SYSTEM-USER prompt · 2026-06-22 12:19:28 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_4SjiUyyE35Gi/3_invention_loop/iter_2/gen_art/gen_art_dataset_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_4SjiUyyE35Gi/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_4SjiUyyE35Gi/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/file.py`, `/ai-inventor/aii_data/runs/run_4SjiUyyE35Gi/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_4SjiUyyE35Gi/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_dataset_1_idx1
type: dataset
title: >-
  Audit and Verify Spoken-Written UD Treebank Pairs with Dependency Metrics and Case-Richness Index
summary: >-
  Load all treebanks from commul/universal_dependencies on HuggingFace, audit each for genuine transcribed speech vs. written
  text using official UD GitHub documentation, identify verified spoken-written language pairs, extract and classify all dependency
  arcs into ARGUMENT (nsubj, obj, iobj, ccomp, xcomp), ADJUNCT (advcl, acl, acl:relcl), and MODIFIER (nmod, amod, advmod)
  categories, compute mean dependency distance (MDD) per relation type per treebank, and recompute case-richness using a transparent,
  single-procedure methodology (proportion of NOUN + PRON tokens with non-empty Case feature). Output JSON with verified language
  pairs, dependency metrics, and a detailed audit report documenting which treebanks were included/excluded with justification.
runpod_compute_profile: cpu_heavy
ideal_dataset_criteria: >-
  Real Universal Dependencies treebanks (300+ language-specific configurations in commul/universal_dependencies on HuggingFace);
  specifically: (1) treebanks explicitly documented as transcribed natural speech in official UD GitHub READMEs or academic
  papers; (2) matched pairs with a written counterpart in the same language; (3) dependency annotation in CONLL-U format with
  lemmas, UPOS, morphological features (including Case), and UD dependency relations; (4) size ≥ 50 sentences minimum per
  split for statistical validity; (5) access to metadata (genre, domain, source, speaker demographics where available). Priority:
  Slovenian sl_sst + sl_ssj pair (documented as transcribed speech); French fr_rhapsodie + fr_gsd pair (documented as transcribed
  speech); English en_gum (conversational/interview/vlog/speech genres only, paired with written subset en_ewt or en_partut,
  if low-overlap); secondary exploration of other mixed-modality treebanks (Danish, Polish, Swedish, Greek, etc.) documented
  in 2022 LREC overview, but only after verification.
dataset_search_plan: "Execute the following steps in sequence:\n\n**Phase 1: Discover and Audit Treebanks (Primary)**\n\n\
  1. Load commul/universal_dependencies from HuggingFace Datasets library; iterate through all available configurations (treebank\
  \ identifiers) to identify which are marked as spoken or contain mixed modality in their name or metadata.\n\n2. For each\
  \ candidate spoken treebank (sl_sst, fr_rhapsodie, en_gum, and any others flagged in HuggingFace metadata):\n   - Fetch\
  \ the official UD GitHub repository README file (e.g., https://github.com/UniversalDependencies/UD_Slovenian-SST/blob/master/README.md)\n\
  \   - Verify the DATA SOURCE section: confirm that the source is transcribed natural speech (not transcribed written text,\
  \ journalism, or L2 learner corpora)\n   - Document: treebank name, language, data source, speech type (monologic, dialogic,\
  \ multi-party), size (sentences, tokens, speakers where available), availability of audio recordings or speech metadata\n\
  \   - EXCLUDE any treebank where: (a) the source is written text (e.g., de_hdt = newspaper, ru_syntagrus = journalistic),\
  \ (b) the corpus is L2 learner speech (en_eslspok), or (c) documentation is missing or ambiguous\n\n3. For each verified\
  \ spoken treebank, identify a written counterpart in the same language:\n   - Search the UD GitHub organization for alternate\
  \ treebanks of the same language\n   - Prioritize treebanks annotated as news, fiction, or web-based (clearly written)\n\
  \   - Document the pairing rationale (e.g., sl_sst spoken + sl_ssj written Slovenian Standard treebank)\n   - Note any data\
  \ overlap issues (e.g., en_gum spoken and en_ewt written may share sources) and document the decision to include or exclude\
  \ the pair\n\n4. Special handling for English:\n   - Load en_gum and filter by genre metadata (\"conversation\", \"vlog\"\
  , \"speech\", \"podcast\" = SPOKEN; \"news\", \"fiction\", \"web\", \"email\", \"blog\", \"government\", \"legal\" = WRITTEN)\n\
  \   - If en_gum spoken subset is >= 50 sentences, pair it with a distinct written baseline (prefer en_partut over en_ewt\
  \ to minimize overlap; document choice)\n   - If en_gum spoken is too sparse (< 50 sentences), document as \"insufficient\
  \ English native spoken data\" and acknowledge in the audit report\n\n5. Output audit_report.txt with columns: TREEBANK_ID\
  \ | LANGUAGE | VERIFIED_SPOKEN? (YES/NO) | REASON (transcribed_speech / newspaper / learner_ESL / missing_docs / low_sample)\
  \ | WRITTEN_PAIR | DATA_SIZE | SOURCE_NOTES | INCLUDED_IN_ANALYSIS? (YES/NO)\n\n**Phase 2: Load and Structure Data (Primary)**\n\
  \n6. For each verified spoken-written pair, load both treebanks from HuggingFace in CONLL-U format.\n\n7. For each treebank,\
  \ extract all sentences and dependency arcs:\n   - Iterate through all sentences in train + dev + test splits (combined)\n\
  \   - For each dependency arc (head_id, dependent_id, deprel), record: (a) the deprel label (e.g., \"nsubj\", \"advcl:relcl\"\
  ), (b) the linear distance = abs(head_position - dependent_position), (c) sentence length (token count)\n   - Separate enhancement\
  \ dependencies (those marked with subtypes, e.g., \"acl:relcl\") from core dependency labels for classification purposes\n\
  \n8. Classify every dependency relation into one of three categories:\n   - ARGUMENT: nsubj, obj, iobj, ccomp, xcomp (obligatory,\
  \ core grammatical participants)\n   - ADJUNCT: advcl, acl, acl:relcl (optional, peripheral, elaborating information; collapse\
  \ acl and acl:relcl into a single ADJUNCT category for statistical power)\n   - MODIFIER: nmod, amod, advmod (nominal/adverbial\
  \ modifiers; these serve as the within-analysis control)\n   - EXCLUDED: all other relations (case, mark, det, etc.) to\
  \ focus on the three categories of interest\n\n9. For each treebank × relation_category combination, compute:\n   - Mean\
  \ Dependency Distance (MDD) = mean of all linear distances in that category\n   - Sentence-length-adjusted MDD = regress\
  \ log(MDD) on log(sentence_length), extract residuals per sentence, and use residuals as the normalized metric\n   - Count\
  \ of dependency arcs in each category (for weighting and transparency)\n\n10. Store intermediate results as:\n    - {\"\
  treebank\": \"sl_sst\", \"language\": \"Slovenian\", \"modality\": \"spoken\", \"relation_category\": \"ARGUMENT\", \"mdd\"\
  : 1.45, \"mdd_normalized\": -0.12, \"arc_count\": 3421}\n    - {\"treebank\": \"sl_ssj\", \"language\": \"Slovenian\", \"\
  modality\": \"written\", \"relation_category\": \"ARGUMENT\", \"mdd\": 2.10, \"mdd_normalized\": 0.34, \"arc_count\": 8942}\n\
  \    - (etc. for each treebank-category pair)\n\n**Phase 3: Compute Case-Richness Index (Secondary)**\n\n11. For each language\
  \ in the verified pairs (Slovenian, French, English, + any additional treebanks):  \n    - Load BOTH spoken and written\
  \ treebanks\n    - Iterate through all tokens across both treebanks combined (union of train+dev+test)\n    - Filter to\
  \ NOUN and PRON tokens only (exclude PROPN per hypothesis specification)\n    - Count tokens with non-empty Case feature\
  \ in the UD morphological annotation (conllu[token][\"feats\"][\"Case\"] is not None/empty)\n    - Compute case_richness\
  \ = (tokens_with_case) / (total_noun_pron_tokens)\n    - Document token counts used for transparency: total_noun_count,\
  \ total_pron_count, noun_with_case, pron_with_case\n\n12. Store case-richness index as:\n    - {\"language\": \"Slovenian\"\
  , \"case_richness\": 0.94, \"noun_tokens\": 12403, \"noun_with_case\": 11659, \"pron_tokens\": 3441, \"pron_with_case\"\
  : 3389}\n    - (repeat for each language)\n\n13. (Optional sanity check) Cross-reference case-richness values with WALS\
  \ typological data (manually via web search if time permits; document any large discrepancies).\n\n**Phase 4: Assemble Final\
  \ Output**\n\n14. Create data_out.json with structure:\n    ```json\n    {\n      \"metadata\": {\n        \"hypothesis\"\
  : \"Argument-adjunct asymmetry in spoken-written dependency distance\",\n        \"verified_language_pairs\": 2,\n     \
  \   \"verified_languages\": [\"Slovenian\", \"French\"],\n        \"timestamp\": \"2026-06-22\",\n        \"procedure_version\"\
  : \"1.0\"\n      },\n      \"treebank_audit\": [\n        {\"treebank_id\": \"sl_sst\", \"language\": \"Slovenian\", \"\
  verified_spoken\": true, \"source\": \"Transcribed natural speech from GOS corpus\", \"tokens\": 98393, \"included\": true},\n\
  \        {\"treebank_id\": \"sl_ssj\", \"language\": \"Slovenian\", \"verified_spoken\": false, \"source\": \"Slovenian\
  \ Standard Treebank (written)\", \"tokens\": 456789, \"included\": true},\n        ...\n      ],\n      \"dependency_metrics\"\
  : [\n        {\"treebank\": \"sl_sst\", \"language\": \"Slovenian\", \"modality\": \"spoken\", \"relation_category\": \"\
  ARGUMENT\", \"mdd\": 1.45, \"mdd_residual\": -0.12, \"arc_count\": 3421, \"arc_percentage\": 28.5},\n        {\"treebank\"\
  : \"sl_ssj\", \"language\": \"Slovenian\", \"modality\": \"written\", \"relation_category\": \"ARGUMENT\", \"mdd\": 2.10,\
  \ \"mdd_residual\": 0.34, \"arc_count\": 8942, \"arc_percentage\": 31.2},\n        ...\n      ],\n      \"case_richness_index\"\
  : [\n        {\"language\": \"Slovenian\", \"case_richness\": 0.94, \"noun_tokens_with_case\": 11659, \"total_noun_tokens\"\
  : 12403, \"pron_tokens_with_case\": 3389, \"total_pron_tokens\": 3441},\n        {\"language\": \"French\", \"case_richness\"\
  : 0.08, \"noun_tokens_with_case\": 1203, \"total_noun_tokens\": 15102, ...},\n        ...\n      ],\n      \"language_pairs_summary\"\
  : [\n        {\"language\": \"Slovenian\", \"spoken_treebank\": \"sl_sst\", \"written_treebank\": \"sl_ssj\", \"spoken_tokens\"\
  : 98393, \"written_tokens\": 456789, \"spoken_minus_written_arg_mdd_residual\": -0.46, \"spoken_minus_written_adj_mdd_residual\"\
  : 0.18, \"spoken_minus_written_mod_mdd_residual\": 0.02},\n        {\"language\": \"French\", \"spoken_treebank\": \"fr_rhapsodie\"\
  , \"written_treebank\": \"fr_gsd\", \"spoken_tokens\": 44242, \"written_tokens\": 401692, \"spoken_minus_written_arg_mdd_residual\"\
  : -0.31, \"spoken_minus_written_adj_mdd_residual\": 0.22, \"spoken_minus_written_mod_mdd_residual\": -0.04},\n        ...\n\
  \      ]\n    }\n    ```\n\n15. Ensure all rows in data_out.json include metadata_fold field (set to \"full\" for all rows,\
  \ since no train/dev/test split is needed for this descriptive analysis).\n\n16. Create audit_report.txt (plain text, human-readable)\
  \ with:\n    - Summary table of treebank audit decisions\n    - Detailed reasoning for each exclusion (if any)\n    - Data\
  \ quality notes (e.g., missing morphological features in fr_rhapsodie)\n    - Limitations and caveats\n    - Recommendations\
  \ for future verification (e.g., manual spot-checks of annotation quality)\n\n**Phase 5: Validation and Quality Control**\n\
  \n17. Sanity checks:\n    - Verify that MDD values are positive and plausible (typically 1.0–3.0 for natural languages)\n\
  \    - Confirm that sentence-length-normalized residuals have mean ≈ 0 and are roughly symmetric\n    - Cross-check case-richness\
  \ values for obvious errors (should be 0–1 range; flag any language with case_richness > 0.95 or < 0.05 for manual review)\n\
  \    - Confirm that all verified treebanks have sufficient sample sizes (≥ 50 sentences per category)\n\n18. Document any\
  \ data cleaning steps (e.g., handling of multiword tokens, exclusion of punctuation, special dependency arcs).\n\n**Fallback\
  \ and Failure Scenarios**\n\n- **Sparse spoken data**: If a language has < 50 sentences in the spoken subset, document as\
  \ \"insufficient_sample\" and exclude from primary analysis; note it as a secondary candidate pending additional treebank\
  \ coverage.\n- **Missing morphological features**: If a treebank (e.g., fr_rhapsodie) lacks Case annotations, document this\
  \ limitation and compute case-richness using only the language's other verified treebank (if available).\n- **Data overlap**:\
  \ If spoken and written treebanks share sources (e.g., en_gum and en_ewt), document the shared fraction and decide pair-wise\
  \ whether the overlap is acceptable; prioritize clean non-overlapping pairs.\n- **Ambiguous documentation**: If a treebank's\
  \ UD GitHub documentation is unclear, search for the corresponding academic paper (2016 papers for early treebanks, 2020+\
  \ papers for newer ones) or contact the treebank maintainers (document the attempt).\n- **Discovery of additional verified\
  \ pairs**: If the audit uncovers additional high-confidence spoken-written pairs (e.g., Danish DDT if verified as genuinely\
  \ spoken), include them in Phase 2–4 steps; report final count in audit_report.txt."
target_num_datasets: 1
</artifact_plan>



<available_resources>
<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **HARD LIMIT**: Maximum $10 USD total spend on LLM API calls (OpenRouter). Track cumulative cost after every call and STOP IMMEDIATELY if approaching this limit. Never exceed this budget under any circumstances.
</software_constraints>

<skills>
Skills are self-contained capabilities with instructions, context, and tools.

- aii-web-tools: Web search (Serper), page/PDF fetch as markdown, regex grep over page/PDF text
- aii-semscholar-bib: Batch-fetch BibTeX from Semantic Scholar
- aii-openrouter-llms: Search and call 300+ LLMs via OpenRouter
- aii-hf-datasets: Search, preview, download HuggingFace datasets
- aii-owid-datasets: Search and load Our World in Data tables
- aii-lean: Compile/verify Lean 4 code, Mathlib search, tactic suggestions
- aii-image-gen: Generate/edit images via Gemini 3 Pro Image (Nano Banana Pro)
- aii-json: Validate JSON against schemas, generate mini/preview variants
- aii-paper-writing: Academic paper structure, bibliography, citations
- aii-paper-to-latex: Assemble LaTeX papers and compile to PDF
- aii-parallel-computing: GPU acceleration, CPU parallelism, async I/O
- aii-python: Python coding standards for experiment scripts
- aii-use-hardware: Detect CPU/RAM/GPU, memory-safe processing
- aii-long-running-tasks: Gradual scaling pattern for long-running tasks
- aii-colab: Google Colab runtime constraints for notebooks
- aii-file-size-limit: Check and split oversized output files
- aii-handbook-multi-llm-agents: Multi-LLM agent orchestration patterns
</skills>
</available_resources>

<available_data_sources>
Use the sources appropriate to your task. Read the relevant skill file BEFORE using each source.

- **HuggingFace Hub** (HF) — ML datasets (NLP, vision, tabular, benchmarks)
- **Our World in Data** (OWID) — Global statistics (energy, health, economics, environment, demographics)
- **Alternate methods** — Python/shell (sklearn.datasets, openml, direct URL, APIs, etc.)

If the plan specifies a source or one fits better, use it.
You may combine sources. Use web search (aii-web-tools skill) to research candidates (background, papers, provenance) — NOT to find/download datasets.
</available_data_sources>

<available_domain_handbooks>
If your domain has a handbook, read the relevant skill file BEFORE working on that domain.

- **Multi-LLM Agents** — dataset selection, evaluation metrics, agent orchestration patterns
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. For the top 2 datasets, create data.py (uv inline script) that: loads from temp/datasets/, standardizes to exp_sel_data_out.json schema (aii-json skill), extracts all examples per dataset, handles domain requirements, saves to full_data_out.json.

Each data ROW must be a separate example — do NOT create one example per dataset or per fold. Each data point (row, sample, instance) = one example. 500 rows → 500 examples. The output is GROUPED BY DATASET:
```json
{
  "datasets": [
    {
      "dataset": "iris",
      "examples": [
        {"input": "...", "output": "...", "metadata_fold": 2, "metadata_feature_names": [...]},
        ...
      ]
    },
    {
      "dataset": "adult_census",
      "examples": [...]
    }
  ]
}
```
Per-example required fields:
- `input`: input features/text (tabular: JSON string of feature values)
- `output`: target/label (as string)
Per-example optional metadata via `metadata_<name>` fields (flat, not nested object):
- `metadata_fold`: fold assignment (int), `metadata_feature_names`: feature name list, `metadata_task_type`: "classification"/"regression", `metadata_n_classes`: number of classes, `metadata_row_index`: original row index, etc.
Do NOT use `split`, `dataset`, or `context` as per-example fields. Dataset name goes at the group level, metadata goes in `metadata_*` fields.
TODO 2. Run 'uv run data.py' and fix errors. Validate full_data_out.json against exp_sel_data_out.json schema (aii-json skill) — fix errors. Generate preview, mini, full versions with aii-json skill's format script.
TODO 3. Read preview to inspect examples. Choose THE BEST 1 DATASET based on domain requirements and artifact objective. Be very attentive to meticulously and exhaustively fix any errors in your code.
</todos>
````

### [7] SKILL-INPUT — aii-json · 2026-06-22 12:19:34 UTC

The agent loaded the **aii-json** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-json
description: JSON validation and formatting toolkit. Validate JSON files against schemas for experiment pipelines, and generate full/mini/preview versions of JSON datasets. Use for validating pipeline outputs, checking schema compliance, or creating size-optimized JSON variants.
---

## Contents

- Validating JSON (schema validation against experiment schemas)
- Formatting JSON (generate full/mini/preview versions)

**IMPORTANT - Parallel execution:** GNU `parallel` subshells do NOT inherit `source activate`. Use `export` for variables and **single-quoted** command templates so parallel's subshells can resolve them:
```
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

---

## Validating JSON

Validate JSON files against predefined schemas for experiment-based hypothesis selection, data collection, solution generation, and evaluation.

### Quick Start

1. Read the schema spec you need to adhere to (e.g., `schemas/exp_eval_sol_out.json`)
2. Create your output file following that schema structure
3. Validate:

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_validate_schema.py --format exp_eval_sol_out --file /path/to/eval_out.json
```

### Script: aii_json_validate_schema.py

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_validate_schema.py --format exp_eval_sol_out --file /tmp/eval_out.json
```

**Parallel execution (multiple validations):**

IMPORTANT: When validating multiple files, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_json_validate_schema.py" && \
parallel -j 50 -k --group --will-cite '$PY $S --format {1} --file {2}' ::: 'exp_sel_data_out' 'exp_gen_sol_out' 'exp_eval_sol_out' :::+ '/tmp/full_data_out.json' '/tmp/method_out.json' '/tmp/eval_out.json'
```

**Example output (success):**
```
Validating: aii_json_validate_schema.py
Format: exp_eval_sol_out

✓ Validation PASSED
```

**Example output (failure):**
```
Validating: aii_json_validate_schema.py
Format: exp_sel_data_out

✗ Validation FAILED

Errors:
  Path: datasets → 0 → examples → 0
  Error: 'output' is a required property
  Validator: required
```

**Parameters:**

`--format` (required)
- Format type to validate against
- Determines which schema to use

`--file` (required)
- Path to JSON file to validate
- Must be valid JSON
- **Always pass an absolute path.** Relative paths resolve from the
  ability server's CWD (typically ``/ai-inventor/aii_server``), not from
  your agent workspace, so ``data_out/x.json`` will silently look in the
  wrong directory and fail with "Could not load JSON file". The validate
  endpoint also accepts a ``workspace_dir`` arg if you need to keep a
  relative path — pass your workspace path there.

**Tips:**
- Fix errors in your JSON and rerun validation until it passes

### Schema Files

Schemas are stored in `.claude/skills/aii-json/schemas/`:

**Hypothesis Selection & Evaluation:**
- `sel_hypo_out.json` - Hypothesis Selection output (all hypotheses with selected flags)
- `feasibility_eval_all.json` - All hypotheses with feasibility scores
- `feasibility_eval_top.json` - Top 5 most feasible hypotheses
- `novelty_research_one.json` - Single hypothesis novelty research arguments with citations
- `novelty_eval_all.json` - All hypotheses with novelty scores
- `novelty_eval_top.json` - Single best selected hypothesis

**Experiment Pipeline:**
- `exp_sel_data_out.json` - Experiment Data Selection format
- `exp_gen_sol_out.json` - Experiment Solution Generation format
- `exp_eval_sol_out.json` - Experiment Solution Evaluation format

---

## Formatting JSON

Generate three size-optimized versions of a JSON file for efficient development and preview:
- **full**: Identical to original (all data)
- **mini**: First 3 items only (for quick testing)
- **preview**: Mini + all strings truncated to 200 chars (for quick inspection)

### Quick Start

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_format_mini_preview.py --input method_out.json
```

### Script: aii_json_format_mini_preview.py

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_format_mini_preview.py --input method_out.json
```

**Parallel execution (multiple files):**

IMPORTANT: When formatting multiple files, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_json_format_mini_preview.py" && \
parallel -j 50 -k --group --will-cite '$PY $S --input {}' ::: 'full_data_out.json' 'method_out.json' 'eval_out.json'
```

**Example output:**
```
Generated 3 versions:
  Full (50 items): /path/to/full_method_out.json
  Mini (3 items): /path/to/mini_method_out.json
  Preview (3 items, truncated): /path/to/preview_method_out.json
```

**Parameters:**

`--input` (required)
- Path to input JSON file
- Must have a top-level array
- Example: `method_out.json`, `full_data_out.json`

`--output-dir` (optional)
- Output directory for generated files
- Default: same directory as input file
- Files are prefixed with `full_`, `mini_`, `preview_`

**Output Files:**

All three files use the same base name with different prefixes:
- `full_{basename}.json` - Complete dataset (identical to original)
- `mini_{basename}.json` - First 3 array items only
- `preview_{basename}.json` - First 3 items with strings truncated to 200 chars

**Tips:**
- Input JSON must have a top-level array structure
- String truncation is recursive (applies to nested objects and arrays)
- Use preview files for quick inspection without reading large datasets
- Use mini files for developing/testing code before running on full dataset

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````

### [8] SYSTEM-USER prompt · 2026-06-22 12:20:42 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_4SjiUyyE35Gi/3_invention_loop/iter_2/gen_art/gen_art_dataset_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_4SjiUyyE35Gi/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_4SjiUyyE35Gi/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/file.py`, `/ai-inventor/aii_data/runs/run_4SjiUyyE35Gi/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_4SjiUyyE35Gi/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_dataset_1_idx1
type: dataset
title: >-
  Audit and Verify Spoken-Written UD Treebank Pairs with Dependency Metrics and Case-Richness Index
summary: >-
  Load all treebanks from commul/universal_dependencies on HuggingFace, audit each for genuine transcribed speech vs. written
  text using official UD GitHub documentation, identify verified spoken-written language pairs, extract and classify all dependency
  arcs into ARGUMENT (nsubj, obj, iobj, ccomp, xcomp), ADJUNCT (advcl, acl, acl:relcl), and MODIFIER (nmod, amod, advmod)
  categories, compute mean dependency distance (MDD) per relation type per treebank, and recompute case-richness using a transparent,
  single-procedure methodology (proportion of NOUN + PRON tokens with non-empty Case feature). Output JSON with verified language
  pairs, dependency metrics, and a detailed audit report documenting which treebanks were included/excluded with justification.
runpod_compute_profile: cpu_heavy
ideal_dataset_criteria: >-
  Real Universal Dependencies treebanks (300+ language-specific configurations in commul/universal_dependencies on HuggingFace);
  specifically: (1) treebanks explicitly documented as transcribed natural speech in official UD GitHub READMEs or academic
  papers; (2) matched pairs with a written counterpart in the same language; (3) dependency annotation in CONLL-U format with
  lemmas, UPOS, morphological features (including Case), and UD dependency relations; (4) size ≥ 50 sentences minimum per
  split for statistical validity; (5) access to metadata (genre, domain, source, speaker demographics where available). Priority:
  Slovenian sl_sst + sl_ssj pair (documented as transcribed speech); French fr_rhapsodie + fr_gsd pair (documented as transcribed
  speech); English en_gum (conversational/interview/vlog/speech genres only, paired with written subset en_ewt or en_partut,
  if low-overlap); secondary exploration of other mixed-modality treebanks (Danish, Polish, Swedish, Greek, etc.) documented
  in 2022 LREC overview, but only after verification.
dataset_search_plan: "Execute the following steps in sequence:\n\n**Phase 1: Discover and Audit Treebanks (Primary)**\n\n\
  1. Load commul/universal_dependencies from HuggingFace Datasets library; iterate through all available configurations (treebank\
  \ identifiers) to identify which are marked as spoken or contain mixed modality in their name or metadata.\n\n2. For each\
  \ candidate spoken treebank (sl_sst, fr_rhapsodie, en_gum, and any others flagged in HuggingFace metadata):\n   - Fetch\
  \ the official UD GitHub repository README file (e.g., https://github.com/UniversalDependencies/UD_Slovenian-SST/blob/master/README.md)\n\
  \   - Verify the DATA SOURCE section: confirm that the source is transcribed natural speech (not transcribed written text,\
  \ journalism, or L2 learner corpora)\n   - Document: treebank name, language, data source, speech type (monologic, dialogic,\
  \ multi-party), size (sentences, tokens, speakers where available), availability of audio recordings or speech metadata\n\
  \   - EXCLUDE any treebank where: (a) the source is written text (e.g., de_hdt = newspaper, ru_syntagrus = journalistic),\
  \ (b) the corpus is L2 learner speech (en_eslspok), or (c) documentation is missing or ambiguous\n\n3. For each verified\
  \ spoken treebank, identify a written counterpart in the same language:\n   - Search the UD GitHub organization for alternate\
  \ treebanks of the same language\n   - Prioritize treebanks annotated as news, fiction, or web-based (clearly written)\n\
  \   - Document the pairing rationale (e.g., sl_sst spoken + sl_ssj written Slovenian Standard treebank)\n   - Note any data\
  \ overlap issues (e.g., en_gum spoken and en_ewt written may share sources) and document the decision to include or exclude\
  \ the pair\n\n4. Special handling for English:\n   - Load en_gum and filter by genre metadata (\"conversation\", \"vlog\"\
  , \"speech\", \"podcast\" = SPOKEN; \"news\", \"fiction\", \"web\", \"email\", \"blog\", \"government\", \"legal\" = WRITTEN)\n\
  \   - If en_gum spoken subset is >= 50 sentences, pair it with a distinct written baseline (prefer en_partut over en_ewt\
  \ to minimize overlap; document choice)\n   - If en_gum spoken is too sparse (< 50 sentences), document as \"insufficient\
  \ English native spoken data\" and acknowledge in the audit report\n\n5. Output audit_report.txt with columns: TREEBANK_ID\
  \ | LANGUAGE | VERIFIED_SPOKEN? (YES/NO) | REASON (transcribed_speech / newspaper / learner_ESL / missing_docs / low_sample)\
  \ | WRITTEN_PAIR | DATA_SIZE | SOURCE_NOTES | INCLUDED_IN_ANALYSIS? (YES/NO)\n\n**Phase 2: Load and Structure Data (Primary)**\n\
  \n6. For each verified spoken-written pair, load both treebanks from HuggingFace in CONLL-U format.\n\n7. For each treebank,\
  \ extract all sentences and dependency arcs:\n   - Iterate through all sentences in train + dev + test splits (combined)\n\
  \   - For each dependency arc (head_id, dependent_id, deprel), record: (a) the deprel label (e.g., \"nsubj\", \"advcl:relcl\"\
  ), (b) the linear distance = abs(head_position - dependent_position), (c) sentence length (token count)\n   - Separate enhancement\
  \ dependencies (those marked with subtypes, e.g., \"acl:relcl\") from core dependency labels for classification purposes\n\
  \n8. Classify every dependency relation into one of three categories:\n   - ARGUMENT: nsubj, obj, iobj, ccomp, xcomp (obligatory,\
  \ core grammatical participants)\n   - ADJUNCT: advcl, acl, acl:relcl (optional, peripheral, elaborating information; collapse\
  \ acl and acl:relcl into a single ADJUNCT category for statistical power)\n   - MODIFIER: nmod, amod, advmod (nominal/adverbial\
  \ modifiers; these serve as the within-analysis control)\n   - EXCLUDED: all other relations (case, mark, det, etc.) to\
  \ focus on the three categories of interest\n\n9. For each treebank × relation_category combination, compute:\n   - Mean\
  \ Dependency Distance (MDD) = mean of all linear distances in that category\n   - Sentence-length-adjusted MDD = regress\
  \ log(MDD) on log(sentence_length), extract residuals per sentence, and use residuals as the normalized metric\n   - Count\
  \ of dependency arcs in each category (for weighting and transparency)\n\n10. Store intermediate results as:\n    - {\"\
  treebank\": \"sl_sst\", \"language\": \"Slovenian\", \"modality\": \"spoken\", \"relation_category\": \"ARGUMENT\", \"mdd\"\
  : 1.45, \"mdd_normalized\": -0.12, \"arc_count\": 3421}\n    - {\"treebank\": \"sl_ssj\", \"language\": \"Slovenian\", \"\
  modality\": \"written\", \"relation_category\": \"ARGUMENT\", \"mdd\": 2.10, \"mdd_normalized\": 0.34, \"arc_count\": 8942}\n\
  \    - (etc. for each treebank-category pair)\n\n**Phase 3: Compute Case-Richness Index (Secondary)**\n\n11. For each language\
  \ in the verified pairs (Slovenian, French, English, + any additional treebanks):  \n    - Load BOTH spoken and written\
  \ treebanks\n    - Iterate through all tokens across both treebanks combined (union of train+dev+test)\n    - Filter to\
  \ NOUN and PRON tokens only (exclude PROPN per hypothesis specification)\n    - Count tokens with non-empty Case feature\
  \ in the UD morphological annotation (conllu[token][\"feats\"][\"Case\"] is not None/empty)\n    - Compute case_richness\
  \ = (tokens_with_case) / (total_noun_pron_tokens)\n    - Document token counts used for transparency: total_noun_count,\
  \ total_pron_count, noun_with_case, pron_with_case\n\n12. Store case-richness index as:\n    - {\"language\": \"Slovenian\"\
  , \"case_richness\": 0.94, \"noun_tokens\": 12403, \"noun_with_case\": 11659, \"pron_tokens\": 3441, \"pron_with_case\"\
  : 3389}\n    - (repeat for each language)\n\n13. (Optional sanity check) Cross-reference case-richness values with WALS\
  \ typological data (manually via web search if time permits; document any large discrepancies).\n\n**Phase 4: Assemble Final\
  \ Output**\n\n14. Create data_out.json with structure:\n    ```json\n    {\n      \"metadata\": {\n        \"hypothesis\"\
  : \"Argument-adjunct asymmetry in spoken-written dependency distance\",\n        \"verified_language_pairs\": 2,\n     \
  \   \"verified_languages\": [\"Slovenian\", \"French\"],\n        \"timestamp\": \"2026-06-22\",\n        \"procedure_version\"\
  : \"1.0\"\n      },\n      \"treebank_audit\": [\n        {\"treebank_id\": \"sl_sst\", \"language\": \"Slovenian\", \"\
  verified_spoken\": true, \"source\": \"Transcribed natural speech from GOS corpus\", \"tokens\": 98393, \"included\": true},\n\
  \        {\"treebank_id\": \"sl_ssj\", \"language\": \"Slovenian\", \"verified_spoken\": false, \"source\": \"Slovenian\
  \ Standard Treebank (written)\", \"tokens\": 456789, \"included\": true},\n        ...\n      ],\n      \"dependency_metrics\"\
  : [\n        {\"treebank\": \"sl_sst\", \"language\": \"Slovenian\", \"modality\": \"spoken\", \"relation_category\": \"\
  ARGUMENT\", \"mdd\": 1.45, \"mdd_residual\": -0.12, \"arc_count\": 3421, \"arc_percentage\": 28.5},\n        {\"treebank\"\
  : \"sl_ssj\", \"language\": \"Slovenian\", \"modality\": \"written\", \"relation_category\": \"ARGUMENT\", \"mdd\": 2.10,\
  \ \"mdd_residual\": 0.34, \"arc_count\": 8942, \"arc_percentage\": 31.2},\n        ...\n      ],\n      \"case_richness_index\"\
  : [\n        {\"language\": \"Slovenian\", \"case_richness\": 0.94, \"noun_tokens_with_case\": 11659, \"total_noun_tokens\"\
  : 12403, \"pron_tokens_with_case\": 3389, \"total_pron_tokens\": 3441},\n        {\"language\": \"French\", \"case_richness\"\
  : 0.08, \"noun_tokens_with_case\": 1203, \"total_noun_tokens\": 15102, ...},\n        ...\n      ],\n      \"language_pairs_summary\"\
  : [\n        {\"language\": \"Slovenian\", \"spoken_treebank\": \"sl_sst\", \"written_treebank\": \"sl_ssj\", \"spoken_tokens\"\
  : 98393, \"written_tokens\": 456789, \"spoken_minus_written_arg_mdd_residual\": -0.46, \"spoken_minus_written_adj_mdd_residual\"\
  : 0.18, \"spoken_minus_written_mod_mdd_residual\": 0.02},\n        {\"language\": \"French\", \"spoken_treebank\": \"fr_rhapsodie\"\
  , \"written_treebank\": \"fr_gsd\", \"spoken_tokens\": 44242, \"written_tokens\": 401692, \"spoken_minus_written_arg_mdd_residual\"\
  : -0.31, \"spoken_minus_written_adj_mdd_residual\": 0.22, \"spoken_minus_written_mod_mdd_residual\": -0.04},\n        ...\n\
  \      ]\n    }\n    ```\n\n15. Ensure all rows in data_out.json include metadata_fold field (set to \"full\" for all rows,\
  \ since no train/dev/test split is needed for this descriptive analysis).\n\n16. Create audit_report.txt (plain text, human-readable)\
  \ with:\n    - Summary table of treebank audit decisions\n    - Detailed reasoning for each exclusion (if any)\n    - Data\
  \ quality notes (e.g., missing morphological features in fr_rhapsodie)\n    - Limitations and caveats\n    - Recommendations\
  \ for future verification (e.g., manual spot-checks of annotation quality)\n\n**Phase 5: Validation and Quality Control**\n\
  \n17. Sanity checks:\n    - Verify that MDD values are positive and plausible (typically 1.0–3.0 for natural languages)\n\
  \    - Confirm that sentence-length-normalized residuals have mean ≈ 0 and are roughly symmetric\n    - Cross-check case-richness\
  \ values for obvious errors (should be 0–1 range; flag any language with case_richness > 0.95 or < 0.05 for manual review)\n\
  \    - Confirm that all verified treebanks have sufficient sample sizes (≥ 50 sentences per category)\n\n18. Document any\
  \ data cleaning steps (e.g., handling of multiword tokens, exclusion of punctuation, special dependency arcs).\n\n**Fallback\
  \ and Failure Scenarios**\n\n- **Sparse spoken data**: If a language has < 50 sentences in the spoken subset, document as\
  \ \"insufficient_sample\" and exclude from primary analysis; note it as a secondary candidate pending additional treebank\
  \ coverage.\n- **Missing morphological features**: If a treebank (e.g., fr_rhapsodie) lacks Case annotations, document this\
  \ limitation and compute case-richness using only the language's other verified treebank (if available).\n- **Data overlap**:\
  \ If spoken and written treebanks share sources (e.g., en_gum and en_ewt), document the shared fraction and decide pair-wise\
  \ whether the overlap is acceptable; prioritize clean non-overlapping pairs.\n- **Ambiguous documentation**: If a treebank's\
  \ UD GitHub documentation is unclear, search for the corresponding academic paper (2016 papers for early treebanks, 2020+\
  \ papers for newer ones) or contact the treebank maintainers (document the attempt).\n- **Discovery of additional verified\
  \ pairs**: If the audit uncovers additional high-confidence spoken-written pairs (e.g., Danish DDT if verified as genuinely\
  \ spoken), include them in Phase 2–4 steps; report final count in audit_report.txt."
target_num_datasets: 1
</artifact_plan>



<available_resources>
<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **HARD LIMIT**: Maximum $10 USD total spend on LLM API calls (OpenRouter). Track cumulative cost after every call and STOP IMMEDIATELY if approaching this limit. Never exceed this budget under any circumstances.
</software_constraints>

<skills>
Skills are self-contained capabilities with instructions, context, and tools.

- aii-web-tools: Web search (Serper), page/PDF fetch as markdown, regex grep over page/PDF text
- aii-semscholar-bib: Batch-fetch BibTeX from Semantic Scholar
- aii-openrouter-llms: Search and call 300+ LLMs via OpenRouter
- aii-hf-datasets: Search, preview, download HuggingFace datasets
- aii-owid-datasets: Search and load Our World in Data tables
- aii-lean: Compile/verify Lean 4 code, Mathlib search, tactic suggestions
- aii-image-gen: Generate/edit images via Gemini 3 Pro Image (Nano Banana Pro)
- aii-json: Validate JSON against schemas, generate mini/preview variants
- aii-paper-writing: Academic paper structure, bibliography, citations
- aii-paper-to-latex: Assemble LaTeX papers and compile to PDF
- aii-parallel-computing: GPU acceleration, CPU parallelism, async I/O
- aii-python: Python coding standards for experiment scripts
- aii-use-hardware: Detect CPU/RAM/GPU, memory-safe processing
- aii-long-running-tasks: Gradual scaling pattern for long-running tasks
- aii-colab: Google Colab runtime constraints for notebooks
- aii-file-size-limit: Check and split oversized output files
- aii-handbook-multi-llm-agents: Multi-LLM agent orchestration patterns
</skills>
</available_resources>

<available_data_sources>
Use the sources appropriate to your task. Read the relevant skill file BEFORE using each source.

- **HuggingFace Hub** (HF) — ML datasets (NLP, vision, tabular, benchmarks)
- **Our World in Data** (OWID) — Global statistics (energy, health, economics, environment, demographics)
- **Alternate methods** — Python/shell (sklearn.datasets, openml, direct URL, APIs, etc.)

If the plan specifies a source or one fits better, use it.
You may combine sources. Use web search (aii-web-tools skill) to research candidates (background, papers, provenance) — NOT to find/download datasets.
</available_data_sources>

<available_domain_handbooks>
If your domain has a handbook, read the relevant skill file BEFORE working on that domain.

- **Multi-LLM Agents** — dataset selection, evaluation metrics, agent orchestration patterns
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Update data.py to only include the chosen 1 dataset and generate full_data_out.json. Re-run to generate full_data_out.json. Validate output format with aii-json skill and fix any errors. Generate full, mini, and preview versions with aii-json skill's format script using `--input full_data_out.json` (creates full_full_data_out.json, mini_full_data_out.json, preview_full_data_out.json — rename to full_data_out.json, mini_data_out.json, preview_data_out.json).
TODO 2. Verify full_data_out.json, preview_data_out.json, and mini_data_out.json exist in your workspace (see <workspace>) and contain correct data.
TODO 3. Apply aii-file-size-limit skill's file size check procedure (100MB limit) to full_data_out.json.
TODO 4. Ensure a `pyproject.toml` exists in your workspace with ALL dependencies pinned to the exact versions installed in your .venv (run `.venv/bin/pip freeze` to get them). This is required for reproducibility. The [project] section must include name, version, requires-python, and a dependencies list with pinned versions (e.g. `numpy==2.0.2`, not `numpy>=2.0`).
</todos>

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "DatasetExpectedFiles": {
      "description": "All expected output files from dataset artifact.",
      "properties": {
        "script": {
          "description": "Path to data.py script. Example: 'data.py'",
          "title": "Script",
          "type": "string"
        },
        "datasets": {
          "description": "Dataset file groups \u2014 one per dataset, each with full/mini/preview variants",
          "items": {
            "$ref": "#/$defs/DatasetFileSet"
          },
          "title": "Datasets",
          "type": "array"
        }
      },
      "required": [
        "script",
        "datasets"
      ],
      "title": "DatasetExpectedFiles",
      "type": "object"
    },
    "DatasetFileSet": {
      "description": "One dataset's three required output variants.",
      "properties": {
        "full": {
          "description": "Full dataset JSON file(s). Single file or split files. Example: ['full_data_out.json'] or ['full_data_out/full_data_out_1.json', 'full_data_out/full_data_out_2.json']",
          "items": {
            "type": "string"
          },
          "title": "Full",
          "type": "array"
        },
        "mini": {
          "description": "Mini dataset JSON file path (3 examples). Example: 'mini_data_out.json'",
          "title": "Mini",
          "type": "string"
        },
        "preview": {
          "description": "Preview dataset JSON file path (10 examples). Example: 'preview_data_out.json'",
          "title": "Preview",
          "type": "string"
        }
      },
      "required": [
        "full",
        "mini",
        "preview"
      ],
      "title": "DatasetFileSet",
      "type": "object"
    }
  },
  "description": "Dataset artifact \u2014 structured output + file metadata.\n\nFinds, evaluates, and prepares datasets for research experiments.\nProduces data.py and full_data_out.json files.",
  "properties": {
    "title": {
      "default": "",
      "description": "Descriptive title (roughly 30-90 characters). Must describe content, NOT a status message.",
      "maxLength": 90,
      "minLength": 30,
      "title": "Title",
      "type": "string"
    },
    "layman_summary": {
      "default": "",
      "description": "One-sentence plain-language summary of what this artifact does, accessible to non-experts. Used only in the per-artifact README, not in downstream prompts.",
      "maxLength": 250,
      "minLength": 80,
      "title": "Layman Summary",
      "type": "string"
    },
    "summary": {
      "default": "",
      "description": "Summary for downstream artifacts: what this artifact provides",
      "maxLength": 5000,
      "minLength": 500,
      "title": "Summary",
      "type": "string"
    },
    "out_expected_files": {
      "$ref": "#/$defs/DatasetExpectedFiles",
      "description": "All output files you created. Must include data.py script plus dataset file groups (full/mini/preview variants)."
    },
    "upload_ignore_regexes": {
      "description": "Regex patterns for workspace paths that must NOT be published to the GitHub repo, matched against each file's path relative to this artifact's workspace root (POSIX form, e.g. 'cache/abc.json'). Applied ON TOP OF the deploy step's built-in exclusions. Use this for executor-specific caches, large transient intermediates, or content-addressed blob stores (e.g. a cache/ dir of thousands of hash-named files) that would bloat the repo. Examples: ['(^|/)cache/', '(^|/)\\\\.weight_cache/', '(^|/)checkpoints/']. Leave empty if every workspace file should be published.",
      "items": {
        "type": "string"
      },
      "title": "Upload Ignore Regexes",
      "type": "array"
    }
  },
  "required": [
    "out_expected_files"
  ],
  "title": "DatasetArtifact",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````
