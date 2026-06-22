# gen_art_experiment_1 — test_idea

> Phase: `invention_loop` · round 2 · `gen_art`
> Run: `run_4SjiUyyE35Gi` — Argument-Adjunct Asymmetry in Spoken-Register Dependency Distance Minimization
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_experiment_1` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-22 12:11:31 UTC

```
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

<research_methodology>
Design experiments like a researcher, not a programmer running a script.

- Every method needs a meaningful baseline — the current standard approach, not a strawman.
- Control your variables. When comparing methods, hold everything else constant.
- Results need variance, not just point estimates. A single run proves nothing.
- Implement the proposed method and baseline side-by-side in the same pipeline to eliminate implementation-level confounds.
</research_methodology>

<task>
Implement the research methodology as a production-ready experimental system.
Adapt your implementation approach based on the hypothesis and domain requirements.
</task>

<critical_requirements>
- Fully implement the methodology described in hypothesis
- Use appropriate frameworks based on research domain
- Load and process data from the specified data_filepath
- Complete working systems
- Handle all edge cases, errors, and exceptions properly
- Always implement baseline comparison method
</critical_requirements>

<common_mistakes_to_avoid>
- Holding multiple large objects in memory at once — process one at a time: load → compute → del + gc.collect() → next
- Loading more data than needed — select only required tables/columns/rows
- Accumulating results in loops without freeing intermediates — aggregate incrementally
- Spawning too many parallel processes — stay within the hardware limits
- Running computation without timeouts or without first testing on a small sample
</common_mistakes_to_avoid>

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
Your workspace: `/ai-inventor/aii_data/runs/run_4SjiUyyE35Gi/3_invention_loop/iter_2/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_4SjiUyyE35Gi/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_4SjiUyyE35Gi/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_4SjiUyyE35Gi/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/results/out.json`
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
id: gen_plan_experiment_1_idx2
type: experiment
title: Sentence-Level Asymmetry Analysis with Bootstrap CIs and Honest Power Reporting
summary: >-
  Implement a rigorous sentence-level reanalysis of the argument-adjunct asymmetry hypothesis using per-sentence MDD aggregation,
  sentence-level bootstrap resampling (preserving clustering), length normalization via residuals, per-language asymmetry
  indices with 95% bootstrap CIs, Cohen's d effect sizes, and one-sample t-test on asymmetry indices. Explicitly report language
  sample sizes and statistical power limitations. Output method_out.json with per-language estimates, bootstrap distributions,
  diagnostic plots, and honest interpretation of cross-linguistic generalizability.
runpod_compute_profile: cpu_heavy
implementation_pseudocode: |-
  # SENTENCE-LEVEL ASYMMETRY ANALYSIS WITH BOOTSTRAP CONFIDENCE INTERVALS
  # =====================================================================

  ## Phase 1: Data Loading and Preprocessing (5 minutes)

  1. Load dependency arc dataset from ../gen_art_dataset_1/full_data_out.json
     - Extract fields: language, modality, deprel, dependency_distance, sentence_length, sentence_id, metadata_treebank
     - Verify data structure: one JSON line per arc, metadata fields nested
     - Check for missing values: if any, log and skip arc
     - Total arc count expected: ~128,162 arcs across Slovenian and French (from dataset artifact)

  2. Separate treebanks by language:
     - LANGUAGE_PAIRS = {"sl": ("sl_sst", "sl_ssj"), "fr": ("fr_rhapsodie", "fr_gsd")}
     - Within each language, identify SPOKEN treebank (sst, rhapsodie) and WRITTEN treebank (ssj, gsd)
     - Log counts per language-modality-treebank

  3. Validate relation categories:
     - ARGUMENT = {"nsubj", "obj", "iobj", "ccomp", "xcomp", "csubj", "csubj:outer"}
     - ADJUNCT = {"advcl", "acl", "acl:relcl"}
     - MODIFIER = {"nmod", "amod", "advmod"} + nmod subtypes (nmod:tmod, nmod:poss, etc.) + amod/advmod subtypes
     - Create label classification: map deprel → category. Log any unclassified relations.

  ## Phase 2: Sentence-Level Aggregation (10 minutes)

  4. Group arcs by (language, modality, sentence_id):
     - For each sentence, collect all dependency arcs
     - Exclude arcs where deprel == "root" (root arcs have no meaningful distance)
     - Group arcs by relation_category (ARGUMENT, ADJUNCT, MODIFIER)

  5. Compute sentence-level MDD per category:
     - For each (language, modality, sentence_id, category) group:
       - Compute mean_distance = average of dependency_distance values in that category
       - If category has 0 arcs for this sentence, set mean_distance = NaN (signal missing data for this category)
       - Retrieve sentence_length from the first arc in this sentence (constant per sentence)
     - Output: DataFrame with columns [language, modality, treebank, sentence_id, category, sentence_length, mdd, arc_count_in_category]
       - arc_count_in_category = N arcs in this category for this sentence (for diagnostics)

  6. Remove sentences with 0 valid arcs in ANY of the 3 categories:
     - A sentence is valid iff it has ≥1 arc in EACH of ARGUMENT, ADJUNCT, MODIFIER
     - Rationale: can only compute residuals and compare when all categories are present
     - Log counts before/after filtering

  ## Phase 3: Sentence-Length Normalization (10 minutes)

  7. Normalize MDD by sentence length:
     - For each (language, modality, category) stratum:
       - Fit OLS regression: log(mdd) ~ log(sentence_length)
       - Compute residuals as: residual_mdd = log(mdd) - log(sentence_length) * slope - intercept
         (or equivalently: residual = log(mdd) - fitted_value)
       - Store regression coefficients and r-squared for reporting
     - Include MODIFIER category in this normalization (it is the control)
     - Output: DataFrame with columns [language, modality, sentence_id, category, sentence_length, mdd, residual_mdd, arc_count]

  ## Phase 4: Per-Language Bootstrap Analysis (30 minutes)

  8. For each language ("sl", "fr"), compute sentence-level bootstrap CIs:
     - Separate into SPOKEN and WRITTEN subsets (by modality column)
     - For each relation_category in {ARGUMENT, ADJUNCT, MODIFIER}:
       - Compute spoken-minus-written MDD difference at sentence level:
         Δ_mdd_raw[i] = mdd_spoken[i] - mdd_written[i] for matching sentence indices (if paired) OR
         Δ_mdd = mean(residual_mdd_spoken) - mean(residual_mdd_written) with bootstrap on unpaired samples
         → Use UNPAIRED bootstrap (more likely: spoken and written are disjoint sentence sets)
       - Bootstrap procedure (B=1000 iterations):
         FOR b in range(1000):
           - Resample SPOKEN sentences: select n_spoken sentences WITH REPLACEMENT from spoken_data
           - Resample WRITTEN sentences: select n_written sentences WITH REPLACEMENT from written_data
           - Compute residual mean for each modality
           - Store Δ_mdd_bootstrap[b] = mean(resample_spoken_residuals) - mean(resample_written_residuals)
       - Extract 95% CI from bootstrap distribution: [2.5th percentile, 97.5th percentile]
       - Compute bootstrap SE = std(Δ_mdd_bootstrap)
       - Store: {category: {mean_diff, ci_lower, ci_upper, se_bootstrap, n_spoken, n_written}}

  9. Compute per-language asymmetry index:
     - asymmetry_index = Δ_mdd_ADJUNCT - Δ_mdd_ARGUMENT
     - Bootstrap CI on asymmetry index (1000 resamples, paired procedure):
       FOR b in range(1000):
         - Resample sentences at sentence level WITH REPLACEMENT (same indices for all categories)
         - For each category, compute Δ_mdd_bootstrap[b]
         - Store asymmetry_index_bootstrap[b] = Δ_mdd_ADJUNCT_b - Δ_mdd_ARGUMENT_b
     - Extract 95% CI from asymmetry bootstrap distribution
     - Effect size: Cohen's d_asymmetry = asymmetry_index / std(Δ_mdd_residuals_pooled)

  10. Compute per-language effect sizes:
      - For each category (ARGUMENT, ADJUNCT, MODIFIER):
        - Cohen's d = (mean_residual_spoken - mean_residual_written) / sd_residuals_pooled
        - sd_residuals_pooled = sqrt(((n_spoken - 1)*var_spoken + (n_written - 1)*var_written) / (n_spoken + n_written - 2))
      - Report d values with 95% CIs (via bootstrap on Cohen's d)

  ## Phase 5: Cross-Language Statistical Test (10 minutes)

  11. One-sample t-test on per-language asymmetry indices:
      - Null hypothesis: mean asymmetry_index across languages = 0
      - Compute t-statistic: t = mean(asymmetry_indices) / (se_asymmetry / sqrt(n_languages))
      - df = n_languages - 1
      - Report p-value, 95% CI on mean asymmetry, and explicit warning:
        "With n_languages={n_languages}, this test is statistically underpowered for cross-linguistic inference (recommended n≥6). Results are exploratory."

  ## Phase 6: Diagnostic Plots and Output Assembly (10 minutes)

  12. Generate diagnostic plots:
      - Plot 1: Asymmetry index by language (point estimate + 95% CI error bars)
        - x-axis: language
        - y-axis: asymmetry_index (with 0-line marked)
        - Labels: CI bounds and n_sentences per language
      - Plot 2: Bootstrap distributions (overlaid histogram) for each category by language
        - Separate panels per language
        - Color by category (ARGUMENT=red, ADJUNCT=blue, MODIFIER=green)
        - Include 95% CI shaded region
      - Plot 3: Residual MDD by category (violin or box plot) for each language
        - Separate spoken/written with different colors
      - Save plots as PNG at resolution 300 dpi

  13. Assemble method_out.json output:
      {
        "metadata": {
          "method": "sentence-level bootstrap CI analysis with length normalization",
          "n_languages": n_languages,
          "languages": ["sl", "fr"],
          "b_bootstrap": 1000,
          "data_path": "../gen_art_dataset_1/full_data_out.json",
          "execution_date": "YYYY-MM-DD"
        },
        "data_filtering": {
          "total_arcs_input": count,
          "sentences_before_filter": count,
          "sentences_after_filter": count,
          "reason_exclusion": "sentences with <1 arc in any category"
        },
        "length_normalization": {
          "procedure": "OLS regression of log(mdd) ~ log(sentence_length) per language-modality-category; residuals used in bootstrap",
          "per_language_regression_stats": {
            "sl": {
              "spoken": {"ARGUMENT": {"slope": ..., "intercept": ..., "r_sq": ...}, ...},
              "written": {...}
            },
            "fr": {...}
          }
        },
        "per_language_results": {
          "sl": {
            "language": "Slovenian",
            "spoken_treebank": "sl_sst",
            "written_treebank": "sl_ssj",
            "n_sentences_spoken": count,
            "n_sentences_written": count,
            "categories": {
              "ARGUMENT": {
                "mean_diff_residual_mdd": value,
                "ci_lower": value,
                "ci_upper": value,
                "se_bootstrap": value,
                "cohens_d": value,
                "cohens_d_ci_lower": value,
                "cohens_d_ci_upper": value,
                "interpretation": "shorter in spoken" or "no difference" or "longer in spoken"
              },
              "ADJUNCT": {...},
              "MODIFIER": {...}
            },
            "asymmetry_index": {
              "value": asymmetry_index,
              "ci_lower": ci_lower,
              "ci_upper": ci_upper,
              "se_bootstrap": se_bootstrap,
              "cohens_d_asymmetry": value,
              "interpretation": "positive" or "negative" or "near-zero"
            }
          },
          "fr": {...}
        },
        "cross_language_test": {
          "test_type": "one-sample t-test on per-language asymmetry indices",
          "null_hypothesis": "mean asymmetry index = 0 across languages",
          "n_languages": n_languages,
          "df": df,
          "t_statistic": t,
          "p_value": p,
          "mean_asymmetry_across_languages": value,
          "ci_lower": ci_lower,
          "ci_upper": ci_upper,
          "power_warning": "UNDERPOWERED: n_languages={} < 6. Cross-linguistic generalization is exploratory.",
          "critical_note": "Results should not be interpreted as confirming a cross-linguistic universal. Larger verified spoken treebank sample required."
        },
        "hypothesis_interpretation": {
          "primary_prediction_1": "ARGUMENT relations show positive Δ (shorter in spoken)",
          "primary_prediction_2": "ADJUNCT relations show negative or near-zero Δ (not shorter or longer in spoken)",
          "primary_prediction_3": "Asymmetry index (ADJUNCT - ARGUMENT) is significantly positive",
          "control_prediction": "MODIFIER relations show near-zero Δ (control)",
          "verdict_by_language": {
            "sl": {
              "argument_shorter_in_spoken": boolean,
              "adjunct_not_shorter_in_spoken": boolean,
              "asymmetry_positive": boolean,
              "overall_confirmation": "yes" or "partial" or "no"
            },
            "fr": {...}
          },
          "overall_support": "asymmetry confirmed in X/Y languages, null in Y, contradicted in Z"
        },
        "caveats_and_limitations": [
          "Only 2 verified spoken-written language pairs: Slovenian and French. Cross-linguistic generalization is premature.",
          "English ESL treebank removed due to L2 learner confound; not included in 'verified' set.",
          "Bootstrap procedure assumes arcs are independent after grouping by sentence (within-sentence clustering via aggregation).",
          "Length normalization via log-linear regression may not fully capture sentence-length confound; alternative: within-length-bins analysis.",
          "Sample size per language: ~6000 spoken, ~13000 written (Slovenian). Spoken sample size is limiting factor for precision.",
          "Asymmetry index is derived from two differences; CI may reflect compounded uncertainty.",
          "No correction for multiple comparisons across categories (3 categories × 2 languages = 6 hypothesis tests). Consider Bonferroni.",
          "Case-richness modulation analysis deferred due to insufficient sample of case-rich and case-poor verified languages."
        ],
        "reproducibility": {
          "code_repo": "method.py",
          "data_inputs": ["../gen_art_dataset_1/full_data_out.json"],
          "data_outputs": ["method_out.json", "diagnostic_plots/"],
          "random_seed": seed_value,
          "package_versions": {
            "pandas": version,
            "numpy": version,
            "scipy": version,
            "matplotlib": version
          }
        }
      }

  ## Phase 7: Edge Cases and Troubleshooting

  14. Handle edge cases:
      - Empty categories in a sentence: Mark residual_mdd as NaN and exclude from that category's analysis (DONE in step 6)
      - Negative sentence lengths: Should not occur; log warning if found
      - MDD = 0 (head and dep at same position): Log warning; should not occur (positions are distinct)
      - log(mdd) with mdd < 1: All integer positions ≥1, so mdd ≥1 by definition. No issue.
      - Singular covariance in regression: Should not occur; log warning if residuals cannot be computed
      - Bootstrap distribution with CI including 0: Report honestly; do not claim significance
      - Language with <30 valid sentences: Warn that bootstrap may be unstable; consider increasing B

  ## Phase 8: Summary Output to Console

  15. Print executive summary:
      - Per-language asymmetry indices and CIs
      - Cross-language t-test result and power warning
      - Verdict: asymmetry confirmed, partial, or null
      - Brief interpretation relative to hypothesis

  ## Pseudocode End

  Total estimated runtime: 60 minutes (5 min load → 10 min agg → 10 min norm → 30 min bootstrap → 10 min test+output → 5 min diagnostics)
fallback_plan: |-
  1. DATA LOADING FAILURE: If full_data_out.json is corrupted or missing, fall back to mini_data_out.json (sample of ~1000 arcs) for testing code logic. Results on mini_data will not be conclusive but will verify statistical pipeline correctness.

  2. BOOTSTRAP CONVERGENCE: If bootstrap distributions show high variance or irregular shapes after 1000 resamples, increase B to 5000 and re-run (cost: ~2x runtime). Histogram inspection will reveal if B is sufficient (smooth distribution = OK, jagged = increase B).

  3. INSUFFICIENT SENTENCES PER CATEGORY: If any language-modality-category stratum has <30 sentences after filtering, (a) report this explicitly in method_out.json, (b) do NOT run bootstrap for that stratum (mark as underpowered), (c) compute point estimates only (mean and SD) without CI, (d) skip Cohen's d for that stratum.

  4. REGRESSION SINGULARITY: If log-linear regression fails (singular covariance matrix), fall back to: (a) simple z-score normalization: (mdd - mean_mdd) / sd_mdd per stratum (coarser but robust), or (b) residuals from robust regression (statsmodels RLM).

  5. LINGUISTIC INCONSISTENCY: If a treebank is found to violate the spoken/written designation during analysis (e.g., unexpected mode split in deprel frequencies), flag it in method_out.json and re-run excluding that treebank. Report in caveats.

  6. COMPUTATION TIMEOUT: If bootstrap runs exceed 6 hours, (a) reduce B from 1000 to 500, (b) parallelize bootstrap loops using Python multiprocessing (already planned in aii-parallel-computing check), (c) use NumPy vectorized operations instead of loops where possible.

  7. OUTPUT FILE SIZE: If method_out.json exceeds 50 MB (unlikely but possible if per-sentence residuals are stored), use aii-file-size-limit skill to split into method_out.json (summary stats) and method_out_bootstrap_distributions.json (detailed bootstrap samples). Both files are valid outputs.
testing_plan: |-
  ## MINI-SCALE SMOKE TESTS (First 15 minutes)

  1. **Load and Parse Test**
     - Load first 100 rows of full_data_out.json
     - Verify schema: all required fields present, data types correct
     - Check language-modality-treebank mapping is correct
     - Expected output: No parse errors, metadata confirms ~100 arcs loaded

  2. **Relation Classification Test**
     - Extract deprel values from first 100 arcs
     - Classify each into ARGUMENT/ADJUNCT/MODIFIER
     - Verify all relations match expected categories (no unclassified values)
     - Expected output: 100% classification rate

  3. **Sentence Aggregation Test (on 100-arc sample)**
     - Group by sentence_id, compute sentence-level MDD per category
     - Verify: mdd values are positive, arc_counts match manual check
     - Expected output: ~20-30 unique sentences, each with 3 categories

  4. **Length Normalization Test (on 100-arc sample)**
     - Fit OLS log(mdd) ~ log(sentence_length) for one language-modality-category
     - Verify: slope and intercept are reasonable (slope ~ 0.5-1.0), r_sq > 0.1
     - Compute residuals, verify mean ≈ 0 (by regression property)
     - Expected output: Coefficients reported, residual mean < 1e-10

  5. **Bootstrap Test (on mini sample, B=10)**
     - Run bootstrap with only B=10 resamples on one language-category combination
     - Verify: bootstrap loop completes without error, output shape is correct
     - Verify: bootstrap CI bounds are different (not identical), bracketing the point estimate
     - Expected output: 10 bootstrap values, CI computed, no Inf/NaN values

  6. **One-Sample t-test Test**
     - Manually create 3 dummy asymmetry indices (e.g., [0.1, -0.05, 0.15])
     - Compute t-test against 0
     - Verify: t-statistic, df, p-value are computed correctly (hand-check formula)
     - Expected output: t ≈ 0.4, df=2, p > 0.5 (not significant, as expected for noisy data)

  7. **Diagnostic Plot Test**
     - Generate one diagnostic plot (asymmetry by language) using dummy data
     - Verify: plot is saved as PNG, contains labels and legend
     - Expected output: PNG file created, readable

  ## FULL-SCALE VALIDATION (Next 30 minutes)

  8. **Load Full Dataset**
     - Load all of full_data_out.json
     - Log total arc count, arc count per language-modality-category, sentence count
     - Expected output: ~128k arcs, ~20k sentences (from artifact description)

  9. **Completeness Check**
     - Verify no missing values in critical columns (dependency_distance, sentence_length, deprel)
     - Count rows with NaN after loading
     - Expected output: 0 rows with missing critical fields

  10. **Distribution Sanity Checks**
      - Compute summary stats (min, max, median) for dependency_distance per language-modality-category
      - Verify: distances are all positive integers, median < 10 (typical for natural language)
      - Plot histogram of MDD values per language
      - Expected output: Distributions look reasonable (right-skewed, no extreme outliers)

  11. **Before/After Length Normalization**
      - Compute raw Δ_mdd (spoken - written) for ARGUMENT before normalization
      - Compute residual Δ_mdd after normalization
      - Verify: normalization reduces magnitude of Δ if sentence length is a confound
      - Expected output: |Δ_residual| < |Δ_raw| for at least one language (normalization has effect)

  12. **Bootstrap Stability Check**
      - For one language-category combination, run bootstrap with B=1000
      - Compute bootstrap SE
      - Re-run bootstrap independently (same B) and compare SE
      - Verify: SE estimates differ by <5% (bootstrap is stable)
      - Expected output: Two SE values within 5% of each other

  13. **CI Validity Check**
      - For each language-category, verify 95% CI does NOT bracket 0 when point estimate is significantly different from 0 (p < 0.05 by t-test)
      - Verify CI is symmetric around point estimate (approximately, for normal-ish distributions)
      - Expected output: CIs are sensible and match hypothesis predictions if confirmed

  14. **Statistical Assumption Check**
      - Verify residuals (from length normalization) are approximately normal (Q-Q plot)
      - Run Shapiro-Wilk test on residuals; expect p > 0.05 for normality (not always true, but check)
      - Expected output: Residuals appear roughly normal, or document if severely skewed

  15. **Power and Precision Check**
      - Report n_languages and n_sentences per language in console output
      - Verify: if n_languages < 3, print explicit warning
      - Compute post-hoc power of one-sample t-test (using observed effect size and n_languages)
      - Expected output: Power estimate < 0.5 for observed effect size (confirms underpowered)

  16. **Cross-Check Against Hypothesis Predictions**
      - For each language, check: are ARGUMENT CIs significantly < 0 (shorter in spoken)?
      - For each language, check: are ADJUNCT CIs significantly > 0 (longer in spoken)?
      - For each language, check: are MODIFIER CIs near 0 (control)?
      - Expected output: Pattern matches prediction for at least one language; null or opposite for others is flagged as non-confirmation

  ## FINAL CHECKS (Last 5 minutes)

  17. **Output Integrity**
      - Verify method_out.json is valid JSON (parseable)
      - Verify all required fields are present (metadata, per_language_results, cross_language_test, caveats)
      - Verify no NaN/Inf values in final output (would indicate computation error)
      - Expected output: method_out.json parses cleanly, no NaN values

  18. **Reproducibility Check**
      - Verify random seed is set at start of script
      - Run script twice with same seed; verify output.json outputs are identical
      - Expected output: Two runs produce byte-identical JSON files

  19. **Console Summary Print**
      - Print 1-page executive summary to console:
        - Per-language asymmetry indices and CIs
        - Cross-language t-test result with power warning
        - Verdict: asymmetry confirmed / partial / null
      - Expected output: Human-readable summary confirming successful analysis

  ## SUCCESS CRITERIA

  - All 19 tests pass without errors
  - method_out.json contains all required sections with valid numeric values
  - Per-language results show consistent patterns (not random scatter)
  - Bootstrap CIs are narrower than raw SE (bootstrap refinement is working)
  - Cross-language t-test is reported with explicit power limitation
  - Console output matches method_out.json (no discrepancies)
  - All caveats and limitations are clearly stated
  - Diagnostic plots are generated and interpretable
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

--- Dependency 1 ---
id: art_F2XD0ACeTqeG
type: dataset
title: 'Slovenian Spoken-Written UD Treebank: Dependency Arc Classification Dataset'
summary: >-
  Dataset of 128,162 dependency arcs extracted from the Slovenian spoken-written Universal Dependencies treebank pair (sl_sst=spoken,
  sl_ssj=written) from commul/universal_dependencies (HuggingFace, UD v2.17). Each example is one classified dependency arc
  with: language (sl), modality (spoken/written), treebank id, sentence_id, deprel label, dependent UPOS, dependency_distance
  (|head_pos - dep_pos|, 1-indexed), sentence_length (non-PUNCT token count), and language_case_richness index (0.9406, computed
  from 81,750 nominals). Relations are classified into three categories — ARGUMENT (nsubj, obj, iobj, ccomp, xcomp, csubj
  subtypes: 28,621 arcs), ADJUNCT (advcl, acl, acl:relcl: 15,483 arcs), MODIFIER (nmod, amod, advmod subtypes: 84,058 arcs).
  Punctuation tokens and root arcs are excluded. The Slovenian pair was chosen as primary dataset because: (1) clean, unambiguous
  spoken/written split; (2) morphologically rich language ideal for case-richness modulation analysis (case_richness=0.9406
  vs English ~0.03); (3) sl_sst directly authored by reviewer Kaja Dobrovoljc (JSI/University of Ljubljana); (4) both treebanks
  use consistent UD annotation scheme. Corpus statistics: sl_sst 6,121 sentences (spoken), sl_ssj 13,435 sentences (written).
  Output schema follows exp_sel_data_out format with input field encoding pipe-delimited arc features and output field containing
  the relation category.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_4SjiUyyE35Gi/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
out_dependency_files:
  file_list:
  - data.py
  - full_data_out.json
  - mini_data_out.json
  - preview_data_out.json
  data_file_paths:
  - full_data_out.json
  - mini_data_out.json
  - preview_data_out.json

Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</dependencies>

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

<available_domain_handbooks>
If your domain has a handbook, read the relevant skill file BEFORE working on that domain.

- **Multi-LLM Agents** — framework choices, implementation patterns, agent orchestration
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
TODO 2. Read preview files from dependencies to understand data structure. Use ALL datasets provided — do not skip or select a subset. Read domain handbook if applicable (see <available_domain_handbooks>). Test basic functionality with 'uv run'.
TODO 3. Fully implement our method AND baseline (comparison) as described in artifact plan in './method.py'. Use exp_gen_sol_out.json schema in aii-json skill for output format validation. Include everything specified in the artifact plan, but you may also implement additional relevant methods or analysis beyond what's listed. Be very attentive to meticulously and exhaustively fix any errors in your code.
</todos>
```

### [2] HUMAN-USER prompt · 2026-06-22 12:11:31 UTC

```
Direction: Computational Linguistics — Dependency Distance Minimization Across UD Treebanks. Something genuinely novel and groundbreaking that measures dependency-distance distributions across UD treebanks, investigates whether spoken language minimizes more than written, characterizes how typology interacts with the pattern, and identifies families that deviate. MUST use commul/universal_dependencies on HuggingFace.

Ambition: level 3 of 5 — phenomenological science: surface and rigorously characterize a new empirical regularity or anomaly in the data, even before a full theoretical explanation exists.

Reviewer: I am Kaja Dobrovoljc (JSI / University of Ljubljana). Calibrate from my existing papers. Cross-domain methods (information theory, mixed-effects models, sequence models) welcome — but keep them close to what I already know, not too far from my background.

Submission/Goal: a paper for ACL, EMNLP, or the Computational Linguistics journal. Audience: computational linguists and quantitative typologists. Tone: empirically rigorous, careful with linguistic detail, reproducible on public UD.
```

### [3] SKILL-INPUT — aii-python · 2026-06-22 12:11:49 UTC

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

### [4] SKILL-INPUT — aii-long-running-tasks · 2026-06-22 12:11:59 UTC

The agent loaded the **aii-long-running-tasks** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-long-running-tasks
description: Gradual scaling pattern for long-running autonomous tasks. Use when running experiments, evaluations, or any code that processes data at increasing scale with runtime checks.
---

## Core Principles

1. **Time budget first**: Read your time/runtime constraints before running anything. Set every Bash timeout to fit within the budget.
2. **Start small, scale up**: Run on minimal input first, fix errors, then increase scale.
3. **Extrapolate before scaling**: Use recorded runtimes to predict whether the next step fits in the budget. Don't guess — calculate.
4. **Background execution**: For anything that takes >1 min, run in background (`run_in_background=true`) and do useful work while waiting.
5. **Stop early if needed**: Quality results on less data beats a timeout or crash. It's always acceptable to stop at a smaller scale.

---

## Gradual Scaling Sequence

Run code at increasing data sizes, checking runtime at each step.

Substitute your actual file names:
- `{mini_file}` — mini JSON (3 examples) from dependency workspace
- `{full_file}` — full dataset from dependency workspace
- `{script}` — your processing script (e.g., `./method.py`, `./eval.py`)
- `{schema}` — JSON schema to validate output against

**STEP 1 — MINI DATA:** Run `{script}` on `{mini_file}`. Do NOT truncate logs. Fix all errors. Validate output against `{schema}`. Verify you are NOT using mock scripts, mock data, or mock APIs.

**STEP 2 — 10 EXAMPLES:** Modify `{script}` to load only the first 10 examples from `{full_file}`. Run and fix errors. Validate schema. Record the runtime.

**STEP 3 — 50 EXAMPLES:** Load first 50 examples from `{full_file}`. Run and fix errors. Record runtime. **EXTRAPOLATE**: Using runtimes from steps 2-3, estimate time per example. Calculate how many examples fit in your remaining time budget. If 50 already used most of the budget, stop here.

**STEP 4 — 100 EXAMPLES (if budget allows):** Load first 100 examples. Run and fix errors. Record runtime. Re-extrapolate with the new data point.

**STEP 5 — 200 EXAMPLES (if budget allows):** Load first 200 examples from `{full_file}`. Run and fix errors. Record runtime.

**STEP 6 — MAXIMIZE:** Using all recorded runtimes, extrapolate time-per-example (it may not be perfectly linear — account for overhead). Calculate the maximum number of examples that fits within your remaining time budget with a 10% safety margin. Load that many (or all if they fit). Run and validate.

## Final Testing Phase

After completing the scaling sequence, redo the entire sequence **one more time** up to your final example count:

mini → 10 → 50 → 100 → 200 → max

At each scale: look for issues, fix problems, validate output, ensure it completes within time limits.

---

## Background Execution

For any step that takes >1 min, run as a **background task**:

1. Launch with Bash `run_in_background=true`
2. While it runs, use the time productively:
   - Sanity-check previous outputs
   - Verify file integrity (correct field names, non-empty values)
   - Review code for edge cases at larger scale
   - Prepare the next step
3. Check back on the background task to get results
4. If it failed, fix errors and re-run

---

## Resource Limits

Set hard RAM and CPU time limits so code fails fast instead of crashing the system. Read limits from `<hardware>` and leave headroom for the OS (e.g., if 16GB total, cap at 14GB).

Python example using stdlib `resource` module:
```python
import resource
resource.setrlimit(resource.RLIMIT_AS, (14 * 1024**3, 14 * 1024**3))  # 14GB RAM
resource.setrlimit(resource.RLIMIT_CPU, (3600, 3600))  # 1 hour CPU time
```
Exceeding RAM raises `MemoryError`. Exceeding CPU time sends `SIGKILL`.

## Monitoring

At each step, record runtime AND check resource usage (`free -h` for RAM, `top -bn1 | head -5` for CPU). If memory usage is climbing toward the limit or CPU is pegged, stop and investigate before scaling further.
````

### [5] SKILL-INPUT — aii-json · 2026-06-22 12:11:59 UTC

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

### [6] SKILL-INPUT — aii-use-hardware · 2026-06-22 12:11:59 UTC

The agent loaded the **aii-use-hardware** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-use-hardware
description: Detect hardware and use it responsibly. Covers CPU/RAM/GPU detection, memory-safe data processing, and resource-aware computation.
---

**Step 1** — Run `bash scripts/get_hardware.sh` (relative to this skill's directory).

Read the `=== CGROUP ===` section carefully. If `Type: cgroup v1` or `cgroup v2`:
- You are in a **container with hard resource limits**. Exceeding them = OOM kill, no recovery.
- **Never** use `psutil.virtual_memory().total`, `free -h`, `/proc/meminfo`, `os.cpu_count()`, or `nproc` for resource limits — these report **host** values, not your container's allocation.
- **Always** read limits from the cgroup paths shown in the output, or use the Python helpers below.
- For **runtime memory monitoring**, read current usage from cgroup too:
  - v2: `/sys/fs/cgroup/memory.current`
  - v1: `/sys/fs/cgroup/memory/memory.usage_in_bytes`

**Step 2** — Use Step 1 results to pick package variants **before** installing.

Defaults often target the most powerful environment — PyPI's `torch` ships with CUDA libs even on CPU-only hosts. Wrong variant = wasted disk, slow setup, possible import-time failures.

If `=== GPU ===` shows `No GPU`, install torch's CPU build (skips ~4.5GB of CUDA libs):
```bash
uv pip install torch --extra-index-url https://download.pytorch.org/whl/cpu
```
Same idea for any library whose wheel selection depends on detected hardware (GPU/CPU-only builds, architecture-specific wheels).

After install, sanity-check imports right away (`python -c "import torch"`). Disk-pressure or interrupted installs leave half-built wheels (e.g. `libtorch_global_deps.so` missing) — catch these before the experiment runs.

**Step 3** — Set Python constants from the Step 1 results:
```python
import os, math, torch, psutil
from pathlib import Path

def _detect_cpus() -> int:
    """Detect actual CPU allocation (containers/pods/bare metal)."""
    try:  # cgroups v2 quota
        parts = Path("/sys/fs/cgroup/cpu.max").read_text().split()
        if parts[0] != "max":
            return math.ceil(int(parts[0]) / int(parts[1]))
    except (FileNotFoundError, ValueError): pass
    try:  # cgroups v1 quota
        q = int(Path("/sys/fs/cgroup/cpu/cpu.cfs_quota_us").read_text())
        p = int(Path("/sys/fs/cgroup/cpu/cpu.cfs_period_us").read_text())
        if q > 0:
            return math.ceil(q / p)
    except (FileNotFoundError, ValueError): pass
    try:  # CPU affinity (cpuset — used by RunPod, Docker --cpuset-cpus)
        return len(os.sched_getaffinity(0))
    except (AttributeError, OSError): pass
    return os.cpu_count() or 1

def _container_ram_gb() -> float | None:
    """Read RAM limit from cgroup (containers/pods)."""
    for p in ["/sys/fs/cgroup/memory.max", "/sys/fs/cgroup/memory/memory.limit_in_bytes"]:
        try:
            v = Path(p).read_text().strip()
            if v != "max" and int(v) < 1_000_000_000_000:
                return int(v) / 1e9
        except (FileNotFoundError, ValueError): pass
    return None

NUM_CPUS = _detect_cpus()
HAS_GPU = torch.cuda.is_available()
VRAM_GB = torch.cuda.get_device_properties(0).total_mem / 1e9 if HAS_GPU else 0
DEVICE = torch.device("cuda" if HAS_GPU else "cpu")
TOTAL_RAM_GB = _container_ram_gb() or psutil.virtual_memory().total / 1e9
AVAILABLE_RAM_GB = min(psutil.virtual_memory().available / 1e9, TOTAL_RAM_GB)
```

## Step 4 — Set Memory Limits

OOM kills the entire container. **Every script MUST set RAM and VRAM limits at startup.**

Decide the budget based on what the script actually needs. Estimate data size × 2-5x for in-memory overhead, then add ~50% breathing room for temporaries. You may use up to 90% of available RAM/VRAM, but **scale gradually** — start small (e.g. 30-50%), verify it works, then increase toward the limit. Never exceed 90% to keep a buffer for the OS, system processes, and the agent runtime itself. Going over crashes the container/machine with no recovery.

```python
import resource, psutil

_avail = psutil.virtual_memory().available
RAM_BUDGET = ???  # YOU decide: estimate what this script needs (in bytes)
assert RAM_BUDGET < _avail, f"Budget {RAM_BUDGET/1e9:.1f}GB > available {_avail/1e9:.1f}GB"
resource.setrlimit(resource.RLIMIT_AS, (RAM_BUDGET * 3, RAM_BUDGET * 3))  # 3x: virtual > RSS; raises MemoryError on exceed

if HAS_GPU:
    _free, _total = torch.cuda.mem_get_info(0)
    VRAM_BUDGET = ???  # YOU decide: estimate GPU memory needs
    torch.cuda.set_per_process_memory_fraction(min(VRAM_BUDGET / _total, 0.95))  # raises OutOfMemoryError on exceed
```

## Memory-Safe Data Processing

- **One at a time**: load one large object → process → `del obj; gc.collect()` → next
- **Load only what you need**: select specific tables/columns/rows, not entire databases
- **Test small first**: run on a sample before scaling to full data to estimate memory/time
- **Free intermediates in loops**: don't accumulate large results — aggregate incrementally
- **Size before loading**: check file/dataset size before loading; if it's >30% of `RAM_BUDGET`, chunk it

## Common Mistakes (from real crashes)

- **Skipping this skill entirely** — loading data with no RAM detection, no limits, no budget. Container OOM-killed, all agents lost.
- **Using `psutil.virtual_memory().total` instead of `_container_ram_gb()`** — reports host RAM (e.g. 66 GB) when container limit is 28 GB. You MUST use the cgroup-aware functions above.
- **Loading all tables from a multi-table database at once** — one agent loaded 14 RelBench tables simultaneously, spiked past container limit.
- **Setting no memory limits** — without `resource.setrlimit` (RAM) and `set_per_process_memory_fraction` (VRAM), a runaway script OOM-kills the container instead of raising a catchable error.
- **Using `os.cpu_count()` directly** — returns host CPUs (e.g. 192) instead of container limit (e.g. 4) on RunPod/Docker. Always use `_detect_cpus()` above which checks cgroup quota → CPU affinity → `os.cpu_count()` in order.

## Hardware Use

- Keep these results in mind for ALL subsequent tasks — don't assume more than detected
- GPU if available and parallelizable, multiprocessing if multiple CPUs
- Push available resources to their full potential — don't leave hardware idle
````

### [7] SKILL-INPUT — aii-parallel-computing · 2026-06-22 12:11:59 UTC

The agent loaded the **aii-parallel-computing** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-parallel-computing
description: "CRITICAL PERFORMANCE SKILL. Maximize hardware utilization for compute-intensive tasks. Covers GPU acceleration, CPU parallelism, and async I/O. The difference between hours of failure and minutes of success. Use whenever writing ANY script that processes data, makes API calls, or does computation."
---

**ALWAYS parallelize. Sequential processing is unacceptable for any non-trivial workload.** A sequential script doing 1000 API calls takes hours and fails halfway. An async version finishes in minutes with proper error handling. ALWAYS ask: "Can this run in parallel?" — the answer is almost always yes.

Read aii-use-hardware skill first → get `NUM_CPUS`, `HAS_GPU`, `VRAM_GB`, `device`. Set `NUM_WORKERS` proportional to available CPU capacity — check `psutil.cpu_percent(interval=1)` and scale accordingly (e.g. 30% used → use ~70% of cores).

## Decision Tree (follow strictly)

- **I/O-bound** (API calls, downloads, web, file reads) → `asyncio` + `aiohttp` with `Semaphore(NUM_WORKERS * 4)`. NEVER do sequential HTTP requests in a loop.
- **CPU-bound, vectorizable** → GPU available: PyTorch on device / No GPU: NumPy vectorized ops. NEVER loop over array elements in Python.
- **CPU-bound, independent items** → `ProcessPoolExecutor(max_workers=NUM_WORKERS)`. NEVER process items one-by-one when they're independent.
- **Sequential** → only acceptable when items have data dependencies (each depends on the previous result).

## GPU Rules

- Use up to 90% of available VRAM — scale gradually (start small, increase after each successful run, keep 10% buffer)
- Move to device → compute → move back: `torch.tensor(data, device=device)` → `.cpu().numpy()`
- OOM fallback: catch `torch.cuda.OutOfMemoryError` → `empty_cache()` → halve batch size → retry on GPU. Keep reducing until it fits. Stay on GPU.
- Batch large data: chunk it, `del batch` between iterations to free VRAM

## Parallelism Rules

- **CPU-bound**: `ProcessPoolExecutor` + `as_completed`, pre-allocate result list indexed by submission order
- **I/O-bound**: `asyncio` + `aiohttp`, `Semaphore(NUM_WORKERS * 4)`, single shared `ClientSession`, `asyncio.gather(*tasks, return_exceptions=True)`
- Always add `tenacity` retries for transient failures, always set timeouts on HTTP requests
- **CRITICAL — `ProcessPoolExecutor` start method**: Default `fork` deadlocks with loguru (and any threading library). ALWAYS pass `mp_context=multiprocessing.get_context("spawn")` when constructing `ProcessPoolExecutor` in any script that uses loguru, threading, or async I/O. Example:
  ```python
  import multiprocessing as mp
  from concurrent.futures import ProcessPoolExecutor
  with ProcessPoolExecutor(max_workers=N, mp_context=mp.get_context("spawn")) as pool:
      ...
  ```
````

### [8] SKILL-INPUT — aii-file-size-limit · 2026-06-22 12:11:59 UTC

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

### [9] SYSTEM-USER prompt · 2026-06-22 12:20:33 UTC

```
[Your previous response had no visible output. Please continue and produce a user-visible response.]
```

### [10] SYSTEM-USER prompt · 2026-06-22 12:25:55 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_4SjiUyyE35Gi/3_invention_loop/iter_2/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_4SjiUyyE35Gi/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_4SjiUyyE35Gi/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_4SjiUyyE35Gi/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/results/out.json`
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
id: gen_plan_experiment_1_idx2
type: experiment
title: Sentence-Level Asymmetry Analysis with Bootstrap CIs and Honest Power Reporting
summary: >-
  Implement a rigorous sentence-level reanalysis of the argument-adjunct asymmetry hypothesis using per-sentence MDD aggregation,
  sentence-level bootstrap resampling (preserving clustering), length normalization via residuals, per-language asymmetry
  indices with 95% bootstrap CIs, Cohen's d effect sizes, and one-sample t-test on asymmetry indices. Explicitly report language
  sample sizes and statistical power limitations. Output method_out.json with per-language estimates, bootstrap distributions,
  diagnostic plots, and honest interpretation of cross-linguistic generalizability.
runpod_compute_profile: cpu_heavy
implementation_pseudocode: |-
  # SENTENCE-LEVEL ASYMMETRY ANALYSIS WITH BOOTSTRAP CONFIDENCE INTERVALS
  # =====================================================================

  ## Phase 1: Data Loading and Preprocessing (5 minutes)

  1. Load dependency arc dataset from ../gen_art_dataset_1/full_data_out.json
     - Extract fields: language, modality, deprel, dependency_distance, sentence_length, sentence_id, metadata_treebank
     - Verify data structure: one JSON line per arc, metadata fields nested
     - Check for missing values: if any, log and skip arc
     - Total arc count expected: ~128,162 arcs across Slovenian and French (from dataset artifact)

  2. Separate treebanks by language:
     - LANGUAGE_PAIRS = {"sl": ("sl_sst", "sl_ssj"), "fr": ("fr_rhapsodie", "fr_gsd")}
     - Within each language, identify SPOKEN treebank (sst, rhapsodie) and WRITTEN treebank (ssj, gsd)
     - Log counts per language-modality-treebank

  3. Validate relation categories:
     - ARGUMENT = {"nsubj", "obj", "iobj", "ccomp", "xcomp", "csubj", "csubj:outer"}
     - ADJUNCT = {"advcl", "acl", "acl:relcl"}
     - MODIFIER = {"nmod", "amod", "advmod"} + nmod subtypes (nmod:tmod, nmod:poss, etc.) + amod/advmod subtypes
     - Create label classification: map deprel → category. Log any unclassified relations.

  ## Phase 2: Sentence-Level Aggregation (10 minutes)

  4. Group arcs by (language, modality, sentence_id):
     - For each sentence, collect all dependency arcs
     - Exclude arcs where deprel == "root" (root arcs have no meaningful distance)
     - Group arcs by relation_category (ARGUMENT, ADJUNCT, MODIFIER)

  5. Compute sentence-level MDD per category:
     - For each (language, modality, sentence_id, category) group:
       - Compute mean_distance = average of dependency_distance values in that category
       - If category has 0 arcs for this sentence, set mean_distance = NaN (signal missing data for this category)
       - Retrieve sentence_length from the first arc in this sentence (constant per sentence)
     - Output: DataFrame with columns [language, modality, treebank, sentence_id, category, sentence_length, mdd, arc_count_in_category]
       - arc_count_in_category = N arcs in this category for this sentence (for diagnostics)

  6. Remove sentences with 0 valid arcs in ANY of the 3 categories:
     - A sentence is valid iff it has ≥1 arc in EACH of ARGUMENT, ADJUNCT, MODIFIER
     - Rationale: can only compute residuals and compare when all categories are present
     - Log counts before/after filtering

  ## Phase 3: Sentence-Length Normalization (10 minutes)

  7. Normalize MDD by sentence length:
     - For each (language, modality, category) stratum:
       - Fit OLS regression: log(mdd) ~ log(sentence_length)
       - Compute residuals as: residual_mdd = log(mdd) - log(sentence_length) * slope - intercept
         (or equivalently: residual = log(mdd) - fitted_value)
       - Store regression coefficients and r-squared for reporting
     - Include MODIFIER category in this normalization (it is the control)
     - Output: DataFrame with columns [language, modality, sentence_id, category, sentence_length, mdd, residual_mdd, arc_count]

  ## Phase 4: Per-Language Bootstrap Analysis (30 minutes)

  8. For each language ("sl", "fr"), compute sentence-level bootstrap CIs:
     - Separate into SPOKEN and WRITTEN subsets (by modality column)
     - For each relation_category in {ARGUMENT, ADJUNCT, MODIFIER}:
       - Compute spoken-minus-written MDD difference at sentence level:
         Δ_mdd_raw[i] = mdd_spoken[i] - mdd_written[i] for matching sentence indices (if paired) OR
         Δ_mdd = mean(residual_mdd_spoken) - mean(residual_mdd_written) with bootstrap on unpaired samples
         → Use UNPAIRED bootstrap (more likely: spoken and written are disjoint sentence sets)
       - Bootstrap procedure (B=1000 iterations):
         FOR b in range(1000):
           - Resample SPOKEN sentences: select n_spoken sentences WITH REPLACEMENT from spoken_data
           - Resample WRITTEN sentences: select n_written sentences WITH REPLACEMENT from written_data
           - Compute residual mean for each modality
           - Store Δ_mdd_bootstrap[b] = mean(resample_spoken_residuals) - mean(resample_written_residuals)
       - Extract 95% CI from bootstrap distribution: [2.5th percentile, 97.5th percentile]
       - Compute bootstrap SE = std(Δ_mdd_bootstrap)
       - Store: {category: {mean_diff, ci_lower, ci_upper, se_bootstrap, n_spoken, n_written}}

  9. Compute per-language asymmetry index:
     - asymmetry_index = Δ_mdd_ADJUNCT - Δ_mdd_ARGUMENT
     - Bootstrap CI on asymmetry index (1000 resamples, paired procedure):
       FOR b in range(1000):
         - Resample sentences at sentence level WITH REPLACEMENT (same indices for all categories)
         - For each category, compute Δ_mdd_bootstrap[b]
         - Store asymmetry_index_bootstrap[b] = Δ_mdd_ADJUNCT_b - Δ_mdd_ARGUMENT_b
     - Extract 95% CI from asymmetry bootstrap distribution
     - Effect size: Cohen's d_asymmetry = asymmetry_index / std(Δ_mdd_residuals_pooled)

  10. Compute per-language effect sizes:
      - For each category (ARGUMENT, ADJUNCT, MODIFIER):
        - Cohen's d = (mean_residual_spoken - mean_residual_written) / sd_residuals_pooled
        - sd_residuals_pooled = sqrt(((n_spoken - 1)*var_spoken + (n_written - 1)*var_written) / (n_spoken + n_written - 2))
      - Report d values with 95% CIs (via bootstrap on Cohen's d)

  ## Phase 5: Cross-Language Statistical Test (10 minutes)

  11. One-sample t-test on per-language asymmetry indices:
      - Null hypothesis: mean asymmetry_index across languages = 0
      - Compute t-statistic: t = mean(asymmetry_indices) / (se_asymmetry / sqrt(n_languages))
      - df = n_languages - 1
      - Report p-value, 95% CI on mean asymmetry, and explicit warning:
        "With n_languages={n_languages}, this test is statistically underpowered for cross-linguistic inference (recommended n≥6). Results are exploratory."

  ## Phase 6: Diagnostic Plots and Output Assembly (10 minutes)

  12. Generate diagnostic plots:
      - Plot 1: Asymmetry index by language (point estimate + 95% CI error bars)
        - x-axis: language
        - y-axis: asymmetry_index (with 0-line marked)
        - Labels: CI bounds and n_sentences per language
      - Plot 2: Bootstrap distributions (overlaid histogram) for each category by language
        - Separate panels per language
        - Color by category (ARGUMENT=red, ADJUNCT=blue, MODIFIER=green)
        - Include 95% CI shaded region
      - Plot 3: Residual MDD by category (violin or box plot) for each language
        - Separate spoken/written with different colors
      - Save plots as PNG at resolution 300 dpi

  13. Assemble method_out.json output:
      {
        "metadata": {
          "method": "sentence-level bootstrap CI analysis with length normalization",
          "n_languages": n_languages,
          "languages": ["sl", "fr"],
          "b_bootstrap": 1000,
          "data_path": "../gen_art_dataset_1/full_data_out.json",
          "execution_date": "YYYY-MM-DD"
        },
        "data_filtering": {
          "total_arcs_input": count,
          "sentences_before_filter": count,
          "sentences_after_filter": count,
          "reason_exclusion": "sentences with <1 arc in any category"
        },
        "length_normalization": {
          "procedure": "OLS regression of log(mdd) ~ log(sentence_length) per language-modality-category; residuals used in bootstrap",
          "per_language_regression_stats": {
            "sl": {
              "spoken": {"ARGUMENT": {"slope": ..., "intercept": ..., "r_sq": ...}, ...},
              "written": {...}
            },
            "fr": {...}
          }
        },
        "per_language_results": {
          "sl": {
            "language": "Slovenian",
            "spoken_treebank": "sl_sst",
            "written_treebank": "sl_ssj",
            "n_sentences_spoken": count,
            "n_sentences_written": count,
            "categories": {
              "ARGUMENT": {
                "mean_diff_residual_mdd": value,
                "ci_lower": value,
                "ci_upper": value,
                "se_bootstrap": value,
                "cohens_d": value,
                "cohens_d_ci_lower": value,
                "cohens_d_ci_upper": value,
                "interpretation": "shorter in spoken" or "no difference" or "longer in spoken"
              },
              "ADJUNCT": {...},
              "MODIFIER": {...}
            },
            "asymmetry_index": {
              "value": asymmetry_index,
              "ci_lower": ci_lower,
              "ci_upper": ci_upper,
              "se_bootstrap": se_bootstrap,
              "cohens_d_asymmetry": value,
              "interpretation": "positive" or "negative" or "near-zero"
            }
          },
          "fr": {...}
        },
        "cross_language_test": {
          "test_type": "one-sample t-test on per-language asymmetry indices",
          "null_hypothesis": "mean asymmetry index = 0 across languages",
          "n_languages": n_languages,
          "df": df,
          "t_statistic": t,
          "p_value": p,
          "mean_asymmetry_across_languages": value,
          "ci_lower": ci_lower,
          "ci_upper": ci_upper,
          "power_warning": "UNDERPOWERED: n_languages={} < 6. Cross-linguistic generalization is exploratory.",
          "critical_note": "Results should not be interpreted as confirming a cross-linguistic universal. Larger verified spoken treebank sample required."
        },
        "hypothesis_interpretation": {
          "primary_prediction_1": "ARGUMENT relations show positive Δ (shorter in spoken)",
          "primary_prediction_2": "ADJUNCT relations show negative or near-zero Δ (not shorter or longer in spoken)",
          "primary_prediction_3": "Asymmetry index (ADJUNCT - ARGUMENT) is significantly positive",
          "control_prediction": "MODIFIER relations show near-zero Δ (control)",
          "verdict_by_language": {
            "sl": {
              "argument_shorter_in_spoken": boolean,
              "adjunct_not_shorter_in_spoken": boolean,
              "asymmetry_positive": boolean,
              "overall_confirmation": "yes" or "partial" or "no"
            },
            "fr": {...}
          },
          "overall_support": "asymmetry confirmed in X/Y languages, null in Y, contradicted in Z"
        },
        "caveats_and_limitations": [
          "Only 2 verified spoken-written language pairs: Slovenian and French. Cross-linguistic generalization is premature.",
          "English ESL treebank removed due to L2 learner confound; not included in 'verified' set.",
          "Bootstrap procedure assumes arcs are independent after grouping by sentence (within-sentence clustering via aggregation).",
          "Length normalization via log-linear regression may not fully capture sentence-length confound; alternative: within-length-bins analysis.",
          "Sample size per language: ~6000 spoken, ~13000 written (Slovenian). Spoken sample size is limiting factor for precision.",
          "Asymmetry index is derived from two differences; CI may reflect compounded uncertainty.",
          "No correction for multiple comparisons across categories (3 categories × 2 languages = 6 hypothesis tests). Consider Bonferroni.",
          "Case-richness modulation analysis deferred due to insufficient sample of case-rich and case-poor verified languages."
        ],
        "reproducibility": {
          "code_repo": "method.py",
          "data_inputs": ["../gen_art_dataset_1/full_data_out.json"],
          "data_outputs": ["method_out.json", "diagnostic_plots/"],
          "random_seed": seed_value,
          "package_versions": {
            "pandas": version,
            "numpy": version,
            "scipy": version,
            "matplotlib": version
          }
        }
      }

  ## Phase 7: Edge Cases and Troubleshooting

  14. Handle edge cases:
      - Empty categories in a sentence: Mark residual_mdd as NaN and exclude from that category's analysis (DONE in step 6)
      - Negative sentence lengths: Should not occur; log warning if found
      - MDD = 0 (head and dep at same position): Log warning; should not occur (positions are distinct)
      - log(mdd) with mdd < 1: All integer positions ≥1, so mdd ≥1 by definition. No issue.
      - Singular covariance in regression: Should not occur; log warning if residuals cannot be computed
      - Bootstrap distribution with CI including 0: Report honestly; do not claim significance
      - Language with <30 valid sentences: Warn that bootstrap may be unstable; consider increasing B

  ## Phase 8: Summary Output to Console

  15. Print executive summary:
      - Per-language asymmetry indices and CIs
      - Cross-language t-test result and power warning
      - Verdict: asymmetry confirmed, partial, or null
      - Brief interpretation relative to hypothesis

  ## Pseudocode End

  Total estimated runtime: 60 minutes (5 min load → 10 min agg → 10 min norm → 30 min bootstrap → 10 min test+output → 5 min diagnostics)
fallback_plan: |-
  1. DATA LOADING FAILURE: If full_data_out.json is corrupted or missing, fall back to mini_data_out.json (sample of ~1000 arcs) for testing code logic. Results on mini_data will not be conclusive but will verify statistical pipeline correctness.

  2. BOOTSTRAP CONVERGENCE: If bootstrap distributions show high variance or irregular shapes after 1000 resamples, increase B to 5000 and re-run (cost: ~2x runtime). Histogram inspection will reveal if B is sufficient (smooth distribution = OK, jagged = increase B).

  3. INSUFFICIENT SENTENCES PER CATEGORY: If any language-modality-category stratum has <30 sentences after filtering, (a) report this explicitly in method_out.json, (b) do NOT run bootstrap for that stratum (mark as underpowered), (c) compute point estimates only (mean and SD) without CI, (d) skip Cohen's d for that stratum.

  4. REGRESSION SINGULARITY: If log-linear regression fails (singular covariance matrix), fall back to: (a) simple z-score normalization: (mdd - mean_mdd) / sd_mdd per stratum (coarser but robust), or (b) residuals from robust regression (statsmodels RLM).

  5. LINGUISTIC INCONSISTENCY: If a treebank is found to violate the spoken/written designation during analysis (e.g., unexpected mode split in deprel frequencies), flag it in method_out.json and re-run excluding that treebank. Report in caveats.

  6. COMPUTATION TIMEOUT: If bootstrap runs exceed 6 hours, (a) reduce B from 1000 to 500, (b) parallelize bootstrap loops using Python multiprocessing (already planned in aii-parallel-computing check), (c) use NumPy vectorized operations instead of loops where possible.

  7. OUTPUT FILE SIZE: If method_out.json exceeds 50 MB (unlikely but possible if per-sentence residuals are stored), use aii-file-size-limit skill to split into method_out.json (summary stats) and method_out_bootstrap_distributions.json (detailed bootstrap samples). Both files are valid outputs.
testing_plan: |-
  ## MINI-SCALE SMOKE TESTS (First 15 minutes)

  1. **Load and Parse Test**
     - Load first 100 rows of full_data_out.json
     - Verify schema: all required fields present, data types correct
     - Check language-modality-treebank mapping is correct
     - Expected output: No parse errors, metadata confirms ~100 arcs loaded

  2. **Relation Classification Test**
     - Extract deprel values from first 100 arcs
     - Classify each into ARGUMENT/ADJUNCT/MODIFIER
     - Verify all relations match expected categories (no unclassified values)
     - Expected output: 100% classification rate

  3. **Sentence Aggregation Test (on 100-arc sample)**
     - Group by sentence_id, compute sentence-level MDD per category
     - Verify: mdd values are positive, arc_counts match manual check
     - Expected output: ~20-30 unique sentences, each with 3 categories

  4. **Length Normalization Test (on 100-arc sample)**
     - Fit OLS log(mdd) ~ log(sentence_length) for one language-modality-category
     - Verify: slope and intercept are reasonable (slope ~ 0.5-1.0), r_sq > 0.1
     - Compute residuals, verify mean ≈ 0 (by regression property)
     - Expected output: Coefficients reported, residual mean < 1e-10

  5. **Bootstrap Test (on mini sample, B=10)**
     - Run bootstrap with only B=10 resamples on one language-category combination
     - Verify: bootstrap loop completes without error, output shape is correct
     - Verify: bootstrap CI bounds are different (not identical), bracketing the point estimate
     - Expected output: 10 bootstrap values, CI computed, no Inf/NaN values

  6. **One-Sample t-test Test**
     - Manually create 3 dummy asymmetry indices (e.g., [0.1, -0.05, 0.15])
     - Compute t-test against 0
     - Verify: t-statistic, df, p-value are computed correctly (hand-check formula)
     - Expected output: t ≈ 0.4, df=2, p > 0.5 (not significant, as expected for noisy data)

  7. **Diagnostic Plot Test**
     - Generate one diagnostic plot (asymmetry by language) using dummy data
     - Verify: plot is saved as PNG, contains labels and legend
     - Expected output: PNG file created, readable

  ## FULL-SCALE VALIDATION (Next 30 minutes)

  8. **Load Full Dataset**
     - Load all of full_data_out.json
     - Log total arc count, arc count per language-modality-category, sentence count
     - Expected output: ~128k arcs, ~20k sentences (from artifact description)

  9. **Completeness Check**
     - Verify no missing values in critical columns (dependency_distance, sentence_length, deprel)
     - Count rows with NaN after loading
     - Expected output: 0 rows with missing critical fields

  10. **Distribution Sanity Checks**
      - Compute summary stats (min, max, median) for dependency_distance per language-modality-category
      - Verify: distances are all positive integers, median < 10 (typical for natural language)
      - Plot histogram of MDD values per language
      - Expected output: Distributions look reasonable (right-skewed, no extreme outliers)

  11. **Before/After Length Normalization**
      - Compute raw Δ_mdd (spoken - written) for ARGUMENT before normalization
      - Compute residual Δ_mdd after normalization
      - Verify: normalization reduces magnitude of Δ if sentence length is a confound
      - Expected output: |Δ_residual| < |Δ_raw| for at least one language (normalization has effect)

  12. **Bootstrap Stability Check**
      - For one language-category combination, run bootstrap with B=1000
      - Compute bootstrap SE
      - Re-run bootstrap independently (same B) and compare SE
      - Verify: SE estimates differ by <5% (bootstrap is stable)
      - Expected output: Two SE values within 5% of each other

  13. **CI Validity Check**
      - For each language-category, verify 95% CI does NOT bracket 0 when point estimate is significantly different from 0 (p < 0.05 by t-test)
      - Verify CI is symmetric around point estimate (approximately, for normal-ish distributions)
      - Expected output: CIs are sensible and match hypothesis predictions if confirmed

  14. **Statistical Assumption Check**
      - Verify residuals (from length normalization) are approximately normal (Q-Q plot)
      - Run Shapiro-Wilk test on residuals; expect p > 0.05 for normality (not always true, but check)
      - Expected output: Residuals appear roughly normal, or document if severely skewed

  15. **Power and Precision Check**
      - Report n_languages and n_sentences per language in console output
      - Verify: if n_languages < 3, print explicit warning
      - Compute post-hoc power of one-sample t-test (using observed effect size and n_languages)
      - Expected output: Power estimate < 0.5 for observed effect size (confirms underpowered)

  16. **Cross-Check Against Hypothesis Predictions**
      - For each language, check: are ARGUMENT CIs significantly < 0 (shorter in spoken)?
      - For each language, check: are ADJUNCT CIs significantly > 0 (longer in spoken)?
      - For each language, check: are MODIFIER CIs near 0 (control)?
      - Expected output: Pattern matches prediction for at least one language; null or opposite for others is flagged as non-confirmation

  ## FINAL CHECKS (Last 5 minutes)

  17. **Output Integrity**
      - Verify method_out.json is valid JSON (parseable)
      - Verify all required fields are present (metadata, per_language_results, cross_language_test, caveats)
      - Verify no NaN/Inf values in final output (would indicate computation error)
      - Expected output: method_out.json parses cleanly, no NaN values

  18. **Reproducibility Check**
      - Verify random seed is set at start of script
      - Run script twice with same seed; verify output.json outputs are identical
      - Expected output: Two runs produce byte-identical JSON files

  19. **Console Summary Print**
      - Print 1-page executive summary to console:
        - Per-language asymmetry indices and CIs
        - Cross-language t-test result with power warning
        - Verdict: asymmetry confirmed / partial / null
      - Expected output: Human-readable summary confirming successful analysis

  ## SUCCESS CRITERIA

  - All 19 tests pass without errors
  - method_out.json contains all required sections with valid numeric values
  - Per-language results show consistent patterns (not random scatter)
  - Bootstrap CIs are narrower than raw SE (bootstrap refinement is working)
  - Cross-language t-test is reported with explicit power limitation
  - Console output matches method_out.json (no discrepancies)
  - All caveats and limitations are clearly stated
  - Diagnostic plots are generated and interpretable
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

--- Dependency 1 ---
id: art_F2XD0ACeTqeG
type: dataset
title: 'Slovenian Spoken-Written UD Treebank: Dependency Arc Classification Dataset'
summary: >-
  Dataset of 128,162 dependency arcs extracted from the Slovenian spoken-written Universal Dependencies treebank pair (sl_sst=spoken,
  sl_ssj=written) from commul/universal_dependencies (HuggingFace, UD v2.17). Each example is one classified dependency arc
  with: language (sl), modality (spoken/written), treebank id, sentence_id, deprel label, dependent UPOS, dependency_distance
  (|head_pos - dep_pos|, 1-indexed), sentence_length (non-PUNCT token count), and language_case_richness index (0.9406, computed
  from 81,750 nominals). Relations are classified into three categories — ARGUMENT (nsubj, obj, iobj, ccomp, xcomp, csubj
  subtypes: 28,621 arcs), ADJUNCT (advcl, acl, acl:relcl: 15,483 arcs), MODIFIER (nmod, amod, advmod subtypes: 84,058 arcs).
  Punctuation tokens and root arcs are excluded. The Slovenian pair was chosen as primary dataset because: (1) clean, unambiguous
  spoken/written split; (2) morphologically rich language ideal for case-richness modulation analysis (case_richness=0.9406
  vs English ~0.03); (3) sl_sst directly authored by reviewer Kaja Dobrovoljc (JSI/University of Ljubljana); (4) both treebanks
  use consistent UD annotation scheme. Corpus statistics: sl_sst 6,121 sentences (spoken), sl_ssj 13,435 sentences (written).
  Output schema follows exp_sel_data_out format with input field encoding pipe-delimited arc features and output field containing
  the relation category.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_4SjiUyyE35Gi/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
out_dependency_files:
  file_list:
  - data.py
  - full_data_out.json
  - mini_data_out.json
  - preview_data_out.json
  data_file_paths:
  - full_data_out.json
  - mini_data_out.json
  - preview_data_out.json

Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</dependencies>

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

<available_domain_handbooks>
If your domain has a handbook, read the relevant skill file BEFORE working on that domain.

- **Multi-LLM Agents** — framework choices, implementation patterns, agent orchestration
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
TODO 1. Use aii-json skill's format script with `--input method_out.json` to generate full, mini, and preview versions. If not in your workspace (see <workspace> above), copy them there. Run 'ls -lh' to verify these three files exist (DO NOT read them).
TODO 2. Apply aii-file-size-limit skill's file size check procedure (100MB limit) to method_out.json and full_method_out.json.
TODO 3. Ensure a `pyproject.toml` exists in your workspace with ALL dependencies pinned to the exact versions installed in your .venv (run `.venv/bin/pip freeze` to get them). This is required for reproducibility. The [project] section must include name, version, requires-python, and a dependencies list with pinned versions (e.g. `numpy==2.0.2`, not `numpy>=2.0`).
</todos>

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "ExperimentExpectedFiles": {
      "description": "All expected output files from experiment artifact.",
      "properties": {
        "script": {
          "description": "Path to method.py script. Example: 'method.py'",
          "title": "Script",
          "type": "string"
        },
        "full_output": {
          "description": "Full method output JSON file. Example: 'full_method_out.json'",
          "title": "Full Output",
          "type": "string"
        },
        "mini_output": {
          "description": "Mini method output JSON file. Example: 'mini_method_out.json'",
          "title": "Mini Output",
          "type": "string"
        },
        "preview_output": {
          "description": "Preview method output JSON file. Example: 'preview_method_out.json'",
          "title": "Preview Output",
          "type": "string"
        }
      },
      "required": [
        "script",
        "full_output",
        "mini_output",
        "preview_output"
      ],
      "title": "ExperimentExpectedFiles",
      "type": "object"
    }
  },
  "description": "Experiment artifact \u2014 structured output + file metadata.\n\nImplements research methodology with baseline comparison.\nProduces method.py and method_out.json files.",
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
      "$ref": "#/$defs/ExperimentExpectedFiles",
      "description": "All output files you created. Must include method.py script plus full/mini/preview method output JSON files."
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
  "title": "ExperimentArtifact",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````
