# gen_strat_1 — test_idea

> Phase: `invention_loop` · round 2 · `gen_strat`
> Run: `run_4SjiUyyE35Gi` — Argument-Adjunct Asymmetry in Spoken-Register Dependency Distance Minimization
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_strat_1` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-22 12:03:36 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A strategy planner (Step 3.1: GEN_STRAT in the invention loop)

Each iteration of the invention loop runs: GEN_STRAT → GEN_PLAN → GEN_ART → GEN_PAPER_TEXT → REVIEW_PAPER → UPD_HYPO
Artifact types: RESEARCH (web search), EXPERIMENT (code), DATASET (data collection), EVALUATION (metrics), PROOF (Lean 4)
State persists across iterations: strategies, plans, artifacts, paper_texts (read from the run tree)

You received the hypothesis, iteration status (current + remaining), previous iteration's strategies, available artifact types, existing artifacts, and reviewer feedback.
Your strategy governs THIS iteration only. You define what artifacts to create NOW.

Focused strategy → efficient progress. Scattered strategy → wasted iteration.
</your_role>
</ai_inventor_context>

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

<time_budgets>

Each artifact executor has a fixed time budget (including writing code, debugging, testing, and fixing errors):

- research: 3h
- dataset: 6h
- experiment: 6h
- evaluation: 3h
- proof: 3h

</time_budgets>

<available_tools>
Web research is available through the aii-web-tools skill, in three levels (broad → specific):

1. web search — Returns titles, URLs, snippets. Use first to discover and scan the landscape.
2. web fetch — Reads a page and returns its content as markdown (HTML or PDF). Use to understand a source. May miss specific details — use fetch_grep below if it doesn't find what you need.
3. fetch_grep — Regex search over a page/PDF's full text. Returns exact matching sections with context. Use for precise details, exact numbers, methodology, or PDFs.

Workflow: search → fetch (understand) → fetch_grep (extract specifics).
</available_tools>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<research_methodology>
Think like a researcher planning a study for a top venue.

- All strategies run in parallel and their artifacts combine into one pool. Together they must build toward a publishable paper — each strategy contributes a distinct, necessary piece. No strategy should be a standalone island.
- Ask yourself: what would a reviewer need to see? Proper baselines, controlled comparisons, ablations that isolate what matters. Plan artifacts that preempt reviewer objections.
- Depth over breadth. One well-designed experiment with proper controls beats five shallow ones.
- Match your evaluation to your claims. Measure what the hypothesis actually asserts.
- When results are weak or partial, vary the approach before writing it off. One failed method doesn't falsify the hypothesis.
- If iterations remain, think about what the NEXT iteration will need. Leave useful building blocks — datasets, baselines, preliminary results — that future strategies can build on, refine, or compare against.
</research_methodology>

<principles>
1. FOCUS ON NOVELTY - every strategy must lead to a genuinely novel contribution
2. MAXIMIZE PARALLELIZATION - all artifacts in your strategy run in parallel
3. BUILD ON EXISTING WORK - use completed artifacts from previous iterations, learn from failures
4. ITERATE ON THE METHOD - a negative result is about the approach, not the hypothesis. Try different methods, parameters, data, or formulations within the hypothesis bounds.
5. DIAGNOSE BEFORE DECIDING - before each iteration, review what worked, what didn't, and why. Use that to choose what to try next. Gaps are action items, not conclusions.
6. SET DEPENDENCIES WISELY - depends_on is a list of {id, label} objects referencing existing artifacts; each label is a short free-text type (a word or two, e.g. "dataset", "validates", "extends") that tags how the dep is used
7. PLAN FOR DEPENDENCIES - if an artifact depends on another (e.g. experiments need datasets), ensure prerequisites exist first or plan them this iteration for the next
</principles>

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

<hypothesis>
Your strategy should advance this hypothesis.

kind: hypothesis
title: >-
  Argument-Adjunct Asymmetry in Spoken-Register Dependency Distance Minimization: Evidence from Verified Spoken-Written Universal
  Dependencies Treebank Pairs
hypothesis: >-
  The widely reported reduction in mean dependency distance (MDD) in spoken compared to written language is not uniformly
  distributed across dependency relation types. Instead, it reflects a systematic argument-adjunct asymmetry: (a) argument-structure
  relations (nsubj, obj, iobj, ccomp, xcomp) are significantly shorter in spoken than in written registers after sentence-length
  normalization, consistent with incremental-processing pressure; but (b) adjunct relations (advcl, acl, acl:relcl) show no
  reduction and are on average longer in spoken than in written language, consistent with right-adjunction (post-clause afterthought
  appending) under real-time production constraints; and (c) nominal/adverbial modifiers (nmod, amod, advmod) show near-zero
  spoken-written difference, serving as a within-analysis control. This asymmetry is demonstrated in at least two verified
  spoken-written treebank pairs (Slovenian sl_sst/sl_ssj and French fr_rhapsodie/fr_gsd), where 'spoken' is defined strictly
  as transcribed natural speech annotated under the UD framework. The originally hypothesized morphological case-richness
  modulation — that languages with richer case marking show larger adjunct elongation in speech — is not supported by available
  evidence and is dropped from the primary hypothesis; it is retained only as a secondary exploratory question pending a sufficient
  sample of verified spoken treebanks. Cross-linguistic generalization of the asymmetry beyond Slovenian and French remains
  an open empirical question requiring replication on a wider set of genuinely spoken corpora.
motivation: >-
  Dependency distance minimization (DDM) is one of the most-replicated cross-linguistic universals in quantitative linguistics,
  yet its spoken-language behaviour is understood only at the aggregate level: spoken language has shorter mean dependency
  distances than written language. This coarse finding masks heterogeneity that matters both theoretically and typologically.
  If adjunct relations are NOT minimized—or are actively elongated—in spoken language due to incremental right-adjunction
  (afterthought syntax), then the aggregate reduction is driven entirely by argument placement, and aggregate MDD comparisons
  are conflating two opposing pressures. This misattribution distorts typological rankings of languages by DDM efficiency
  and misidentifies which structural features are responsible for cross-linguistic variance. Correcting it requires a relation-type-stratified
  analysis. Additionally, if case-marking morphology amplifies spoken adjunct elongation (by freeing modifiers from order-constrained
  positions), this provides the first empirical bridge between morphological typology and register-specific DDM behaviour—a
  connection that has been hypothesised but never tested at this level of granularity. The result would be a new empirical
  regularity grounded in cognitive (incremental processing) and structural (morphological freedom) factors, reportable as
  a phenomenological finding before a full formal account is required.
assumptions:
- >-
  Spoken UD treebanks (e.g., Slovenian SST, French Rhapsodie, English spoken GUM, and others) faithfully represent spontaneous
  spoken syntax in their UD dependency annotations, enabling valid comparison with written treebanks of the same language.
- >-
  The argument vs. adjunct distinction in UD (core dependents: nsubj, obj, iobj, ccomp, xcomp vs. peripheral dependents: advcl,
  acl, acl:relcl, nmod) is consistent enough across languages to support cross-linguistic aggregation, after excluding language-specific
  annotation idiosyncrasies.
- >-
  Sentence length is the primary confound between spoken and written MDD (spoken sentences are shorter on average), and residual
  spoken-written differences after length normalisation reflect genuine register effects rather than artefacts.
- >-
  A language's morphological case-marking richness (operationalised as the proportion of nominals carrying overt case morphology
  in the UD treebank) provides a valid proxy for the degree to which word order is decoupled from grammatical function, enabling
  more positionally free right-adjunction in spoken registers.
- >-
  Enough spoken-written UD treebank pairs exist within commul/universal_dependencies covering typologically diverse languages
  (at minimum four pairs spanning morphologically rich and poor languages) to test cross-linguistic generalisability.
investigation_approach: >-
  Load all spoken and written Universal Dependencies treebank pairs from commul/universal_dependencies on HuggingFace. For
  each sentence, extract all dependency arcs and classify each arc's relation label into one of three categories: ARGUMENT
  (nsubj, obj, iobj, ccomp, xcomp), ADJUNCT (advcl, acl, acl:relcl), and MODIFIER (nmod, amod, advmod). Compute mean dependency
  distance (MDD) per relation category per treebank. Apply sentence-length normalisation (regress log-MDD on log-sentence-length
  and use residuals) to remove the confound that spoken sentences are shorter. For each language pair, compute the spoken-minus-written
  MDD difference separately for argument and adjunct categories. Test the main hypothesis using a linear mixed-effects model
  with modality (spoken/written), relation category (argument/adjunct), and their interaction as fixed effects, with language
  as a random intercept. Test the typological modulation by correlating the per-language spoken-adjunct elongation effect
  with a morphological case richness index derived from each language's UD treebank (proportion of nominals with non-empty
  case feature). Report which language families deviate from the asymmetry pattern and what their structural properties are.
success_criteria: >-
  The hypothesis is confirmed if: (1) the interaction term modality × relation_category is statistically significant (p <
  0.05) in the mixed-effects model, with argument distances shorter in spoken and adjunct distances NOT shorter (or longer)
  in spoken; (2) the sentence-length-normalised spoken-adjunct MDD difference is positive (spoken adjuncts longer) in at least
  two of the four largest language pairs; (3) the spoken-adjunct elongation effect correlates positively (r > 0.3) with morphological
  case richness across languages. The hypothesis is disconfirmed if: (i) adjunct MDD follows the same direction as argument
  MDD (both shorter in spoken) after length normalisation across all tested languages; or (ii) the interaction is absent or
  reversed. A partial confirmation (asymmetry holds but no morphological modulation) would still be a publishable finding,
  calling for alternative explanations of the cross-linguistic variance.
related_works:
- >-
  Liu (2008) 'Dependency distance as a metric of language comprehension difficulty' (Physics of Life Reviews): establishes
  MDD as a cross-linguistic measure and finds spoken dialogue (Japanese) has shorter MDD than written news, but does not stratify
  by relation type and does not test whether adjunct relations drive or counteract the aggregate effect.
- >-
  Futrell, Mahowald & Gibson (2015) 'Large-scale evidence of dependency length minimization in 37 languages' (PNAS): demonstrates
  DDM as a universal across 37 languages using aggregate MDD; does not examine spoken registers or the argument/adjunct distinction.
- >-
  Ferrer-i-Cancho et al. (2022) 'The optimality of syntactic dependency distances' (Physical Review E): computes the eta-score
  (L_min/L) for 93 languages measuring how close each language is to the minimum possible dependency length; does not include
  spoken treebanks and does not stratify by relation type.
- >-
  Poiret & Liu (2023) 'Cross-linguistic variations in dependency distance minimization' (PACLIC 37): compares MDD across languages
  and registers including spoken/written French by relation type (subject, oblique object), finding argument distances shorter
  in spoken French — but does not test adjunct relations, does not control for sentence length systematically, and does not
  examine the direction of adjunct distances or morphological modulation.
- >-
  Dobrovoljc (2025) 'Counting trees: A treebank-driven exploration of syntactic variation in speech and writing across languages'
  (arXiv 2505.22774): compares spoken and written UD treebanks (English, Slovenian) using structural inventory (delexicalized
  subtree shapes) and finds spoken corpora have fewer, less diverse structures; does not use dependency distance metrics and
  does not address the argument/adjunct asymmetry.
- >-
  Sinnemäki & Haakana (2023) 'Head and dependent marking and dependency length in possessive noun phrases' (PMC): finds morphological
  marking interacts with dependency length in possessives, supporting a link between morphological complexity and DDM; does
  not examine spoken vs. written registers or extend to adjunct vs. argument distinctions broadly.
inspiration: >-
  The hypothesis is inspired by two cross-domain transfers. First, from psycholinguistics and incremental sentence processing:
  the distinction between obligatory arguments (which must be integrated immediately for semantic interpretation) and optional
  adjuncts (which can be appended after clause completion) maps directly onto the cognitive difference between items that
  demand real-time proximity and items that tolerate deferral. This suggests a mechanism — incremental right-adjunction in
  speech — that would selectively elongate adjunct distances. Second, from information theory and source coding: morphological
  case marking acts as a redundancy channel that makes word-order position less informative for adjunct interpretation, analogous
  to error-correcting codes that allow more permissive channel use. Languages with richer case morphology can afford to 'transmit'
  modifiers late (post-clause position) without ambiguity, predicting larger spoken-adjunct elongation. This combination of
  incremental processing theory and morphological redundancy provides a mechanistic account for both the within-language asymmetry
  and the cross-linguistic modulation.
terms:
- term: Mean Dependency Distance (MDD)
  definition: >-
    The average linear distance (number of intervening words) between syntactically related word pairs (head and dependent)
    across all dependency arcs in a corpus or sentence; the primary scalar measure of dependency distance minimization.
- term: Argument relation
  definition: >-
    A dependency relation between a predicate and a core grammatical participant whose presence is selected by the predicate's
    argument structure; in UD: nsubj (nominal subject), obj (direct object), iobj (indirect object), ccomp (clausal complement),
    xcomp (open clausal complement). Arguments are semantically obligatory and must be integrated immediately for incremental
    interpretation.
- term: Adjunct/modifier relation
  definition: >-
    A dependency relation between a head and an optional, non-selected dependent that provides peripheral or elaborating information;
    in UD: advcl (adverbial clause), acl (adnominal clause), acl:relcl (relative clause), nmod (nominal modifier). Adjuncts
    can logically be appended after main clause production without disrupting core meaning construction.
- term: Argument-adjunct asymmetry
  definition: >-
    The central empirical claim of this hypothesis: that spoken-register MDD reduction (relative to written) is directionally
    opposite for argument vs. adjunct relation types — arguments shorter in speech, adjuncts not shorter (or longer) in speech.
- term: Sentence-length normalisation
  definition: >-
    A procedure to remove the confound that spoken sentences are shorter on average than written sentences (which mechanically
    produces shorter distances); operationalised by regressing log-MDD on log-sentence-length and analysing residuals, or
    by including log-sentence-length as a covariate in a mixed-effects model.
- term: Morphological case richness
  definition: >-
    A treebank-derived index of how extensively a language uses overt case morphology on nominals; operationalised as the
    proportion of nominal tokens (nouns, pronouns) carrying a non-empty Case feature in the UD morphological annotation. High
    values indicate case-marking languages (Finnish, Slovenian, Turkish); low values indicate positional languages (English,
    Mandarin).
- term: Right-adjunction
  definition: >-
    The spoken-language construction strategy of appending adverbial clauses, relative clauses, or postverbal nominals after
    the main clause has been completed, creating long-distance dependencies between the modifier and its head; associated
    with afterthought syntax and incremental speech planning under real-time production constraints.
- term: Universal Dependencies (UD)
  definition: >-
    A cross-linguistically consistent framework for morphosyntactic annotation of natural language text and speech, providing
    a standardised set of dependency relation labels and part-of-speech tags across 300+ treebanks for 180+ languages; the
    data basis for this study via commul/universal_dependencies on HuggingFace.
summary: >-
  Spoken language is known to have shorter overall dependency distances than written language, but this paper hypothesises
  that this aggregate reduction hides a systematic argument-adjunct asymmetry: argument dependencies (subject, object, clausal
  complements) are shorter in spoken registers, while adjunct dependencies (adverbial clauses, relative clauses, nominal modifiers)
  show no reduction or are actually longer, due to incremental right-adjunction in speech. This cross-linguistic asymmetry,
  testable with commul/universal_dependencies, is predicted to be amplified in morphologically rich case-marking languages
  where word order is more permissive for modifiers.
_relation_rationale: >-
  Same conceptual frame; narrows scope to verified spoken treebanks and drops unsupported case-richness modulation claim.
_confidence_delta: decreased
_key_changes:
- >-
  Restricted the evidential base to verified spoken treebanks only (Slovenian sl_sst and French fr_rhapsodie confirmed); English
  en_eslspok removed as a primary corpus due to L2 learner confound.
- >-
  Dropped the morphological case-richness modulation claim as a primary hypothesis component: r=0.194, p=0.507 across 14 languages
  is a clear null, and the 3-language estimate is confounded by the ESL outlier.
- >-
  Explicitly framed the 14-language extension as a failed replication (28.6% conformance, all tests p>0.80) caused by misidentified
  spoken treebanks (e.g., de_hdt=newspaper, ru_syntagrus=journalistic), not as 'moderate generalization'.
- >-
  Recast the argument-adjunct asymmetry as a well-supported exploratory finding in 2 languages (Slovenian and French), not
  a confirmed cross-linguistic universal.
- >-
  Added modifier (nmod, amod, advmod) near-zero control as an explicit, named prediction to strengthen the hypothesis structure.
- >-
  Cross-linguistic generalization restated as an open empirical question requiring a wider set of verified spoken UD treebanks.
- >-
  Case-richness modulation demoted from primary claim to secondary exploratory question, requiring at minimum 6+ verified
  spoken pairs spanning the morphological richness continuum.
- >-
  Investigation approach must now audit every 'spoken' treebank against UD documentation before inclusion, replacing or dropping
  any that is transcribed written text.
relation_type: evolution
</hypothesis>

<iteration_status>
Current iteration: 2 of 2
Remaining (including this one): 1
</iteration_status>

<previous_strategies>
Strategies from the PREVIOUS iteration. You can CONTINUE these directions,
ADAPT based on what worked and what didn't in the artifacts produced, or PIVOT if results suggest a better path.

--- Strategy 1 ---
kind: strategy
id: gen_strat_1_idx1
title: Argument-Adjunct Asymmetry in Spoken-Register Dependency Distance Minimization
objective: >-
  Empirically establish the hypothesized argument-adjunct asymmetry in dependency distance minimization (MDD) across spoken
  and written UD treebanks, and test whether morphological case richness modulates the effect cross-linguistically.
rationale: >-
  The core hypothesis predicts a specific directional interaction: argument dependencies (nsubj, obj, iobj, ccomp, xcomp)
  are significantly shorter in spoken language (consistent with incremental processing), while adjunct dependencies (advcl,
  acl, acl:relcl, nmod) show no reduction or are actually longer (due to right-adjunction and afterthought syntax). This fine-grained
  asymmetry has never been tested before at this level of granularity—prior work only examined aggregate MDD reduction. Iteration
  1 should establish whether the asymmetry exists across available spoken-written UD language pairs and whether morphological
  case marking modulates the magnitude of the effect. Iteration 2 can investigate deviating language families, refine relation-type
  classifications, and explore alternative explanations for partial confirmations.
artifact_directions:
- id: dataset_iter1_dir1
  type: dataset
  objective: >-
    Acquire all publicly available spoken-written UD language pairs, extract and classify dependency relations (argument vs.
    adjunct), compute morphological case richness, and produce a standardized JSON dataset ready for statistical analysis.
  approach: >-
    Load commul/universal_dependencies from HuggingFace Hub and identify all language pairs with both spoken and written treebanks
    (e.g., English GUM, French Rhapsodie, Slovenian SST, and others). For each sentence in each treebank, extract all dependency
    arcs and classify each dependency relation label into one of three categories: ARGUMENT (nsubj, obj, iobj, ccomp, xcomp),
    ADJUNCT (advcl, acl, acl:relcl), or MODIFIER (all other relations). Compute distance = |head_position - dependent_position|
    and sentence_length for each arc. Derive a morphological case-richness index for each language as the proportion of nominal
    tokens (NOUN, PRON) carrying a non-empty Case feature in the UD morphological annotation. Output data_out.json in standardized
    format with {language, modality (spoken/written), sentence_id, relation_category, dependency_distance, sentence_length,
    language_case_richness} tuples, plus a mini preview for validation.
  depends_on: []
- id: experiment_iter1_dir2
  type: experiment
  objective: >-
    Test the core hypothesis by fitting a mixed-effects model with modality (spoken/written) × relation_category (argument/adjunct)
    interaction on sentence-length-normalized MDD, and determine whether the interaction is statistically significant with
    the predicted directionality.
  approach: >-
    Load the dataset produced by the DATASET artifact (data_out.json). For each language pair and relation category, compute
    mean dependency distance (MDD) separately for spoken and written registers. Apply sentence-length normalization by regressing
    log(MDD) on log(sentence_length) within each language-modality-category stratum and using residuals as the outcome. Compute
    per-language spoken-minus-written MDD difference (Δ_MDD) for arguments and adjuncts separately. Fit a linear mixed-effects
    model: log(MDD_residual) ~ modality × relation_category + (1 | language) with Restricted Maximum Likelihood estimation.
    Test the significance of the modality × relation_category interaction term (target: p < 0.05) and verify directionality:
    argument Δ_MDD should be negative (shorter in spoken), while adjunct Δ_MDD should be non-negative or positive. Compute
    and report effect sizes (Cohen's d or model coefficients), 95% confidence intervals, per-language delta estimates. Output
    method_out.json with mixed-effects model summary table, per-language estimates with CIs, interaction term p-value, and
    diagnostic plots.
  depends_on: []
- id: evaluation_iter1_dir3
  type: evaluation
  objective: >-
    Validate statistical rigor of the core finding, test the secondary morphological modulation hypothesis, and characterize
    language families that deviate from the predicted asymmetry pattern.
  approach: >-
    Load EXPERIMENT results (method_out.json) and raw dataset (data_out.json). (1) Compute bootstrap 95% confidence intervals
    on effect sizes (1000 resamples within each language) and assess statistical power via effect-size distribution analysis.
    (2) Test the morphological modulation hypothesis: compute Pearson correlation between per-language spoken-adjunct Δ_MDD
    and case-richness index; report r, p-value, and 95% CI. (3) Generate diagnostic visualizations: scatter plots (case richness
    vs. spoken-adjunct elongation, color-coded by language family), bar plots (argument vs. adjunct MDD by modality, error
    bars = 95% CI). (4) Run sensitivity ablations: re-fit the main model without sentence-length normalization to demonstrate
    its necessity; re-fit with alternative normalization methods (e.g., including log-sentence-length as a predictor instead
    of residualizing). (5) Identify and characterize language pairs or families where the asymmetry fails or reverses (e.g.,
    adjuncts as short as or shorter than arguments in spoken language despite length normalization); extract their typological
    properties (case richness, word order, predominant adjunct type). Output eval_out.json with {interaction_robust_ci, morphological_correlation_r_pvalue,
    ablation_results, language_family_deviations_with_properties}.
  depends_on: []
expected_outcome: >-
  After Iteration 1 completes, we will have: (1) a publicly reproducible, fully documented dataset of all spoken-written UD
  language pairs with standardized dependency classifications, morphological case metadata, and dependency distance measurements;
  (2) a rigorous statistical test of the core argument-adjunct asymmetry hypothesis at the interaction level, with p-value,
  effect sizes, and per-language estimates; (3) an empirical test of the morphological modulation prediction (correlation
  of case richness with spoken-adjunct elongation); (4) identification of which language families support vs. deviate from
  the asymmetry hypothesis and their structural properties; (5) confidence that either the hypothesis is confirmed at publishable
  rigor, or deviations are well-characterized for Iteration 2 refinement. All results and analysis code will be reproducible
  on public UD data, enabling downstream verification and extension.
summary: >-
  This strategy executes a complete empirical test of the argument-adjunct asymmetry hypothesis using public Universal Dependencies
  treebanks. The DATASET artifact acquires and prepares all available spoken-written UD pairs, extracts dependency metrics,
  and computes morphological case richness. The EXPERIMENT artifact implements the core hypothesis test via mixed-effects
  modeling of MDD with modality × relation_category interaction, after sentence-length normalization. The EVALUATION artifact
  validates statistical rigor, tests the morphological modulation prediction via correlation analysis, and characterizes deviations
  to prepare for Iteration 2. All three artifacts contribute distinct, essential components of an empirical argument toward
  either confirming or productively revising the hypothesis.
</previous_strategies>

<dependency_rules>
- depends_on is a list of objects {id, label} — each entry references an existing artifact and tags how it is being used
- "id" can ONLY reference IDs from <existing_artifacts> — never IDs you are proposing (all new artifacts run in parallel)
- "label" is a SHORT free-text type label (a word or two, NOT a sentence) describing what role the dep plays — e.g. "dataset", "validates", "extends", "supersedes". Required on every dep.
- Setting depends_on provides the dependency's out_dependency_files to your artifact at execution time
- If no suitable existing artifacts exist, use empty depends_on
- New artifact IDs are assigned by the system after submission — do not invent IDs for your proposed artifacts
</dependency_rules>

<available_artifact_types>
Artifact types you can plan. Use this to choose the right types for your strategy objectives.

<artifact_types>
RESEARCH
Web research to answer key questions — like a researcher making decisions.
Runtime: LLM Agent, no code execution.
Tools: the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text).
Capabilities: Find, synthesize, and compare information across sources; survey SOTA and best practices.
Deps: REQUIRED none | OPTIONAL other RESEARCH to build on prior findings

EXPERIMENT
Run code to test hypotheses, implement methods, and collect empirical results.
Runtime: Python 3.12, UV (any pip package), isolated workspace, gradual scaling (mini → full data).
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-json (schema validation), aii-openrouter-llms (call any LLM — GPT, Gemini, Llama, etc.), domain-specific as needed.
Capabilities: Implement and run any code-based experiment, compare method vs baselines.
Deps: REQUIRED at least one DATASET | OPTIONAL RESEARCH for methodology guidance

DATASET
Collect, prepare, and merge datasets for experiments and analysis.
Runtime: Python 3.12, UV, isolated workspace.
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-hf-datasets (HuggingFace Hub — ML datasets, many UCI/OpenML/Kaggle mirrors), aii-owid-datasets (Our World in Data — global statistics), aii-json (schema validation). Also any Python source (sklearn.datasets, openml, direct URLs, APIs) — must verify within 300MB limit.
Capabilities: Search, acquire, transform, combine, and standardize data from any available source.
Deps: REQUIRED none | OPTIONAL RESEARCH for guidance on what data to collect

EVALUATION
Evaluate experiment results with metrics, statistical analysis, and validity checks.
Runtime: Python 3.12, UV (any evaluation library), isolated workspace, gradual scaling matching experiment.
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-json (schema validation), aii-openrouter-llms (call any LLM — GPT, Gemini, Llama, etc.), domain-specific as needed.
Capabilities: Compute any quantitative metrics and statistical tests, analyze validity and robustness.
Deps: REQUIRED at least one EXPERIMENT | OPTIONAL DATASET if reference data needed

PROOF
Formally prove mathematical statements in Lean 4 with automated iteration.
Runtime: LLM agent with Lean 4 compiler feedback loop.
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-lean (proof verification, Mathlib search, tactics: ring, linarith, nlinarith, omega, simp, etc.)
Capabilities: Formally verify properties and inequalities, iterative proof development, lemma decomposition.
Deps: REQUIRED none | OPTIONAL RESEARCH for mathematical background
</artifact_types>
</available_artifact_types>

<artifact_executor_scope>
IMPORTANT: Each artifact executor has a focused prompt that guides it to do ONE thing well. It will NOT perform tasks outside its scope — assigning the wrong work to the wrong artifact type wastes an iteration. Match the task to the right executor.

RESEARCH executor scope:
  Output: research_out.json with {answer, sources, follow_up_questions} + research_report.md
  DOES: Web research — search, read, synthesize information from papers/docs/APIs into a structured report
  DOES NOT: Run code, download files, execute scripts, compute anything — no shell/Python access
  Use for literature surveys, API documentation, technical specifications — pure information gathering

EXPERIMENT executor scope:
  Output: method_out.json with results (metrics, predictions, analysis) — the core computational work
  DOES: Implement and run methods/algorithms, compute metrics, compare approaches, produce quantitative results
  DOES NOT: Collect new datasets (depends on DATASET artifacts for input data), write formal proofs
  This is the right artifact for any code that processes data and produces results

DATASET executor scope:
  Output: data_out.json with rows of {input, output, metadata_fold, ...} — raw data only, no derived computations
  DOES: Download/generate datasets, analyze candidates to pick the best ones, standardize to JSON schema (features, labels, folds, metadata), validate schema, split into full/mini/preview
  DOES NOT: Run experiments, train models, compute derived statistics (PID/MI/correlations/synergy matrices) as final output
  If you need to COMPUTE something from data (synergy matrices, MI scores, timing benchmarks), use an EXPERIMENT artifact instead

EVALUATION executor scope:
  Output: eval_out.json with evaluation results
  DOES: Any evaluation of experiment results — metrics, statistical tests, ablations, comparisons, visualizations, robustness checks, error analysis, etc.
  DOES NOT: Implement new methods (use EXPERIMENT), collect data (use DATASET)
  This is for analyzing experiment outputs from any angle

PROOF executor scope:
  Output: Lean 4 proof files (.lean) with verified theorems
  DOES: Write and verify Lean 4 formal proofs with Mathlib, iterative compilation
  DOES NOT: Run Python experiments, collect data, do empirical analysis
  Use only when formal mathematical guarantees are needed
</artifact_executor_scope>

<artifact_planning_rules>
RESEARCH: Plan early — findings guide dataset selection, experiment design, and methodology.
EXPERIMENT: Must depend on at least one DATASET. Define clear metrics and baselines before running. Consider trying multiple method variations rather than a single approach.
DATASET:
- Plan for REAL third-party datasets (HuggingFace, Kaggle, direct-download URLs) — downloadable within time and size constraints
- Describe dataset criteria (domain, size, format) — executors find exact sources, but you can suggest candidates or search directions
- ALWAYS prefer real datasets over synthetic. Synthetic is a LAST RESORT only when no suitable real data exists
EVALUATION: Must depend on at least one EXPERIMENT. Focus on statistical rigor and validity checks.
PROOF: Use only when the hypothesis requires formal mathematical guarantees. Lean 4 + Mathlib.
</artifact_planning_rules>

<existing_artifacts>
--- Item 1 ---
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
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json
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

--- Item 2 ---
id: art_Gq_zeOShbi_1
type: experiment
title: Argument-Adjunct Asymmetry in Dependency Distance Across UD Treebanks
summary: |-
  Experiment tests the hypothesis that spoken language selectively minimizes dependency distance for arguments (nsubj, obj, ccomp, xcomp) but NOT for adjuncts (advcl, acl), using 922,399 dependency arcs from 3 spoken-written treebank pairs (Slovenian sl_sst/sl_ssj, French fr_rhapsodie/fr_gsd, English en_eslspok/en_ewt) from commul/universal_dependencies on HuggingFace.

  KEY RESULTS:
  - Arguments: mean MDD spoken=2.718 vs written=3.042, Δ=-0.324, t=-13.00, p≈10⁻³⁸ (significantly SHORTER in spoken, confirming dependency length minimization)
  - Adjuncts: mean MDD spoken=6.578 vs written=5.975, Δ=+0.603, t=+6.15, p≈10⁻¹⁰ (significantly LONGER in spoken, asymmetry confirmed)
  - Modifiers: mean MDD spoken=2.101 vs written=2.102, Δ≈0, p=0.951 (no effect — control)
  - Asymmetry index (adj_delta − arg_delta) = +0.927 (large effect)
  - 2/3 language pairs (Slovenian, French) individually confirm the asymmetry; English ESL pair is confounded by L2 learner grammar

  METHODS: Per-arc dependency distance computed as |head_idx − dep_idx|. Sentence-length normalization via OLS residualization (log_mdd ~ log_sent_len) within each (language, modality) stratum. Mixed-effects model with modality × rel_type interaction and random intercepts per language (singular fit with n=3 groups; primary evidence from pooled raw t-tests). Morphological case richness computed from nominal token Case features: Slovenian=0.587, English=0.420, French=0.180.

  BASELINE: Modality-only mixed-effects model (no rel_type interaction) compared via AIC/BIC to the full interaction model.

  OUTPUT FILES: method_out.json with full results (20KB), 5 diagnostic plots (QQ-plot, MDD vs sentence length scatter, interaction plot, per-language forest plot with 95% bootstrap CIs, adjunct effect vs case richness scatter). Schema validated against exp_gen_sol_out.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_4SjiUyyE35Gi/3_invention_loop/iter_1/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json
out_dependency_files:
  file_list:
  - method.py
  - full_method_out.json
  - mini_method_out.json
  - preview_method_out.json

--- Item 3 ---
id: art_keVDdRwzuK2n
type: evaluation
title: 'Argument-Adjunct Asymmetry in Dependency Distance: 14-Language UD Eval'
summary: |-
  This evaluation rigorously tests the argument-adjunct asymmetry hypothesis in dependency distance minimization (DDM) across 14 language pairs from the Universal Dependencies dataset (commul/universal_dependencies on HuggingFace). For each language, spoken and written treebanks were loaded, dependency arcs classified as argument (nsubj, obj, iobj, ccomp, xcomp) or adjunct (advcl, acl, acl:relcl), and mean dependency distances computed after pooled sentence-length residualization (log-log OLS regression fitted on spoken+written together to avoid within-group residual mean = 0 artefact).

  Six metric groups were computed:

  1. BOOTSTRAP CIs (1000 resamples per language per category): Per-language 95% CIs on Δ_MDD_residual (spoken minus written), using pooled residualization within each resample. CIs stored per language in eval_out.json.

  2. COHEN'S D DISTRIBUTIONS: Per-language effect sizes for argument and adjunct categories. Histograms saved to figures/effect_size_distributions.png.

  3. MORPHOLOGICAL MODULATION: Pearson r between case richness (proportion of NOUN/PRON with Case feature) and Δ_MDD_adjunct across 14 languages. Result: r=0.194, p=0.507 — not significant, suggesting morphological case alone does not predict cross-linguistic variance in adjunct behaviour.

  4. SENSITIVITY ABLATIONS: Three model variants tested (no length normalization, length as covariate, Huber robust regression), confirming directional consistency of results.

  5. LANGUAGE-FAMILY DEVIATIONS: Conformance rate = 28.6% (4/14 languages conform to predicted pattern: argument shorter in spoken AND adjunct not shorter). Deviation profiles with working hypotheses provided for all 10 non-conforming languages.

  6. INTERACTION ROBUSTNESS: Language-level paired t-test: Δ_MDD_argument mean=−0.0069, p=0.810; Δ_MDD_adjunct mean=+0.0028, p=0.928; asymmetry paired t=0.235, p=0.818. The interaction is directionally consistent with the hypothesis (argument negative, adjunct positive) but not statistically significant at conventional levels, constituting an honest null/weak result. Mixed-effects model encountered singular matrix (likely due to insufficient between-language variance at the aggregate level); language-level paired tests used as primary inference tool.

  Languages analysed: English, Slovenian, French, Italian, German, Portuguese, Spanish, Chinese, Turkish, Finnish, Czech, Polish, Russian, Arabic (14 total). Figures: delta_mdd_by_language.png, morphological_modulation.png, effect_size_distributions.png.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_4SjiUyyE35Gi/3_invention_loop/iter_1/gen_art/gen_art_evaluation_1
out_expected_files:
- eval.py
- full_eval_out.json
- mini_eval_out.json
- preview_eval_out.json
out_dependency_files:
  file_list:
  - eval.py
  - full_eval_out.json
  - mini_eval_out.json
  - preview_eval_out.json
</existing_artifacts>

<current_paper>
The current paper draft — represents the research story so far.

Use this to understand what's working, what's not, and what gaps remain.
Gaps and weak results signal what to try differently — not what to conclude.

# Introduction

The human language faculty exhibits a remarkable preference for linear word orders that minimize the distance between syntactically dependent words. This dependency distance minimization (DDM) has been demonstrated across 37 languages using large parsed corpora [1], holds for diverse language families [2], and correlates with processing difficulty in psycholinguistic tasks [3, 4]. The universality of the principle is striking: despite vast differences in morphology, phonology, and historical origin, languages organize their words according to a common pressure to keep related elements close.

Yet a coarser observation shadows this universal: spoken language has shorter mean dependency distances than written language [3]. The implication seems straightforward: speakers minimize distances more aggressively than writers. But this inference rests on aggregate statistics. If the reduction is driven entirely by a subset of dependency relations—say, core arguments—while other relations (such as adjuncts) show no reduction or even elongation in speech, then the aggregate pattern masks two opposing pressures, and misattributes the locus of the phenomenon. This misattribution has concrete consequences for linguistic theory and typology. A theory of DDM that assumes uniform minimization across all relations would be fundamentally incomplete, and typological rankings of languages by their "efficiency" in minimizing distance would conflate incomparable quantities.

We propose a refined hypothesis grounded in cognitive processing constraints: the observed spoken-language reduction in mean dependency distance reflects not uniform minimization, but a systematic **argument-adjunct asymmetry**. Arguments—core grammatical participants selected by a predicate (subject, object, clausal complements)—are significantly shorter in spoken than in written language, consistent with incremental processing pressure: these elements must be integrated immediately for semantic interpretation. Adjuncts—optional modifiers and peripheral dependents—show no reduction or paradoxically *lengthen* in spoken language, due to **right-adjunction** strategy: speakers append adverbial clauses, relative clauses, and postverbal nominal modifiers as afterthoughts after the main clause is complete, maximizing locality constraints for arguments while tolerating distance for adjuncts.

This asymmetry should not be uniform across languages. In morphologically rich, case-marking languages (e.g., Slovenian, Finnish), word order is more flexible for adjuncts because case morphology disambiguates grammatical roles; speakers can thus more freely place adjuncts post-verbally in speech. In positional languages (e.g., English, Mandarin), stricter word order constraints may force adjuncts earlier, counteracting the right-adjunction tendency. We predict that the magnitude of spoken-adjunct elongation correlates positively with a language's morphological case richness.

## Contributions

This paper makes four contributions:

1. **Phenomena**: We characterize a previously undocumented argument-adjunct asymmetry in register-specific dependency distance, showing that the aggregate spoken-language reduction in DDM is not uniform but directionally opposite for arguments versus adjuncts [ARTIFACT:art_Gq_zeOShbi_1].

2. **Mechanism**: We ground the asymmetry in incremental processing theory and right-adjunction syntax, providing a principled explanation for why arguments shorten but adjuncts resist or lengthen in speech.

3. **Cross-linguistic evidence**: We test the hypothesis across 14 language pairs from Universal Dependencies, demonstrating the generality of the argument asymmetry while identifying language-family deviations and working hypotheses for non-conforming languages [ARTIFACT:art_keVDdRwzuK2n].

4. **Typological implications**: We show that morphological case richness does not significantly predict the cross-linguistic variance in adjunct elongation at the aggregate level, suggesting that other structural features (word order rigidity, prosodic phrasing, interaction dynamics) may be more load-bearing.

# Related Work

## Dependency Distance Minimization as Universal

The principle that human languages minimize dependency distance has roots in information theory and cognitive science. Liu [3] proposed dependency distance as a cognitive metric for sentence comprehension difficulty, grounding the preference in working memory constraints: holding unresolved syntactic expectations in memory incurs a cost proportional to how long the language processor must wait to integrate a dependent element. Futrell, Mahowald, and Gibson [1] systematically tested DDM across 37 typologically diverse languages using large parsed corpora, finding that all languages organize words such that actual dependency lengths are substantially shorter than conservative random baselines. They argued that this universality reflects a core cognitive pressure: efficient parsing and production require minimizing the integration cost of dependencies. Ferrer-i-Cancho et al. [5] advanced this line by introducing an optimality score (eta) measuring how close each language's word order comes to a theoretical minimum dependency length given its syntactic structure; they found that half of 93 languages are optimized to 70% or more, suggesting that DDM is not merely a tendency but an organizational principle that languages actively enforce through their grammars.

## Register Variation in Dependency Distance

Although DDM is well-established in aggregate, register-specific variation has been less thoroughly characterized. Liu [3] observed that Japanese spoken dialogue has lower mean dependency distance than written news text but did not stratify by relation type. Dobrovoljc [6] recently compared spoken and written treebanks for English and Slovenian using delexicalized dependency subtree inventories as the unit of analysis, finding that spoken corpora contain fewer and less diverse syntactic structures than written counterparts. This finding supports the intuition that speech exhibits distinct structural preferences, but it does not directly measure dependency distance or examine the direction of change by relation type. Poiret and Liu [7] examined French by relation type, comparing subject, object, and oblique relations in spoken and written corpora, and found that argument distances are shorter in speech—consistent with our argument findings—but they did not test adjunct relations, did not systematically normalize for sentence length, and did not investigate cross-linguistic modulation.

## Morphology and Syntactic Complexity

A growing body of work connects morphological marking to syntactic organization. Sinnemäki and Haakana [8] studied the interaction of head and dependent marking with dependency length in possessive noun phrases across languages, finding an inverse relationship between the two marking types but no significant cross-linguistic correlation between dependency length and morphological complexity alone. This suggests that morphological and syntactic complexity are partially independent dimensions, though their work focused on a narrow construction (possessives) rather than adjuncts broadly. The hypothesis that case morphology liberates word order flexibility for adjuncts is implicit in much typological work [9, 10] but has not been tested against register-specific dependency distance variation.

## Incremental Processing and Adjuncts

Incremental processing theory, developed by Gibson [11, 12] and others, proposes that language comprehension unfolds in real time, with the parser continuously integrating new words into an emerging syntactic structure. Storage cost (the burden of maintaining unresolved dependencies in working memory) and integration cost (the cost of linking a new word to a distant head) both penalize long-distance dependencies. In speech, where real-time production constraints are acute, incremental pressure should favor short argument distances; arguments are obligatory and must be interpreted immediately for semantic composition. Adjuncts, by contrast, are optional and can be semantically interpreted after the main clause is complete, relaxing the incremental pressure. This suggests an asymmetry in how the two relation types respond to register-specific cognitive pressures—an asymmetry our data support.

# Methods

## Data and Corpora

We extracted dependency arcs from three spoken-written Universal Dependencies (UD) treebank pairs from commul/universal_dependencies (HuggingFace, UD v2.17) [ARTIFACT:art_F2XD0ACeTqeG]:

- **Slovenian**: sl_sst (spoken, Slovenian Spoken Treebank, 6,121 sentences) vs. sl_ssj (written, Slovenian Marked Up Corpus, 13,435 sentences)
- **French**: fr_rhapsodie (spoken, 6,032 sentences) vs. fr_gsd (written, 16,341 sentences)
- **English**: en_eslspok (spoken, ESL learner speech, 2,662 sentences) vs. en_ewt (written, English Web Treebank, 12,543 sentences)

These pairs were chosen because: (1) they represent typologically diverse languages (Indo-European, diverse morphological profiles); (2) they have clear spoken-written annotations; (3) Slovenian, authored by reviewer Kaja Dobrovoljc, uses consistent UD annotation; (4) they include both morphologically rich (Slovenian, case-richness = 0.587) and morphologically poor (French = 0.180, English = 0.420) languages. The English pair includes ESL learner speech, which may introduce confounds; we discuss this limitation below.

## Dependency Arc Classification

For each sentence, we extracted all dependency arcs (head-dependent pairs) and classified each arc's UD deprel label into one of three categories:

- **Arguments** (28,621 arcs in 3-language pool): nsubj, obj, iobj, ccomp, xcomp, csubj. These are core participants obligatory for propositional interpretation.
- **Adjuncts** (15,483 arcs): advcl, acl, acl:relcl. These are optional, semantically peripheral modifiers.
- **Modifiers** (84,058 arcs): nmod, amod, advmod, and other nominal/adverbial/adjectival modifications. These serve as a control category.

Punctuation tokens and root arcs were excluded. We computed mean dependency distance (MDD) for each arc as |head_position − dependent_position| in 1-indexed token positions.

## Sentence-Length Normalization

Spoken sentences are typically shorter than written sentences, mechanically producing shorter distances. To remove this confound, we performed OLS residualization: for each (language, modality) stratum, we regressed log(MDD) on log(sentence_length) and retained residuals. This procedure removes the linear relationship between sentence length and distance while preserving the relationship's residual variance. All subsequent statistical tests were performed on residualized MDD.

## Statistical Analysis

We used a linear mixed-effects model to test whether the spoken-written MDD difference varies by relation type (argument vs. adjunct). The model formula was:

```
mdd_residual_mean ~ C(modality, Treatment('spoken')) * C(rel_type, Treatment('argument')) + (1 | language)
```

with modality (spoken/written), relation type (argument/adjunct/modifier), their interaction, and random intercepts per language. We also performed per-arc independent t-tests (n = 922,399 pooled arcs) as a complementary robustness check. Morphological case richness was computed from the UD morphological feature columns: we counted all NOUN and PRON tokens with a non-empty Case feature and divided by the total count of nominals.

# Results

[FIGURE:fig1]

## Main Finding: Argument-Adjunct Asymmetry

The raw, per-arc t-tests reveal a clear asymmetry [ARTIFACT:art_Gq_zeOShbi_1]:

**Arguments** (n_spoken = 16,820; n_written = 105,125):
- Mean MDD spoken: 2.718 words
- Mean MDD written: 3.042 words
- Δ (spoken − written): −0.324 words
- t = −13.00, p ≈ 10⁻³⁸
- **Direction**: Significantly shorter in spoken

**Adjuncts** (n_spoken = 2,972; n_written = 24,674):
- Mean MDD spoken: 6.578 words
- Mean MDD written: 5.975 words
- Δ (spoken − written): +0.603 words
- t = +6.15, p ≈ 10⁻¹⁰
- **Direction**: Significantly longer in spoken

**Modifiers** (n_spoken = 21,087; n_written = 156,218):
- Mean MDD spoken: 2.101 words
- Mean MDD written: 2.102 words
- Δ (spoken − written): −0.001 words
- t = −0.062, p = 0.951
- **Direction**: No effect (control)

**Asymmetry Index**: (Δ_adjunct − Δ_argument) = (+0.603) − (−0.324) = 0.927, a large effect size indicating that adjuncts show 0.927 additional words of elongation relative to the argument shortening.

These patterns hold across the pooled data and are robust to sentence-length residualization. The mixed-effects model confirms directional consistency, though singular matrix issues with only three language groups prevent reliable random-effects estimation at the aggregate level; we thus report the raw t-tests as primary evidence.

## Per-Language Patterns

[FIGURE:fig2]

Separately analyzing each language pair reveals heterogeneity [ARTIFACT:art_Gq_zeOShbi_1]:

**Slovenian** (case-richness = 0.587):
- Argument Δ: −0.165 (spoken shorter), t-test p = 5.5e-5
- Adjunct Δ: +0.219 (spoken longer), t-test p = 0.083
- **Asymmetry confirmed**: Arguments minimize, adjuncts do not
- Modifiers Δ: +0.263 (spoken longer, opposite to aggregate, possibly due to short Slovenian spoken sentences)

**French** (case-richness = 0.180):
- Argument Δ: −0.634 (spoken shorter), t-test p = 8.1e-36
- Adjunct Δ: +0.143 (spoken longer), t-test p = 0.470
- **Asymmetry confirmed**: Large argument effect, smaller adjunct effect
- Modifiers Δ: +0.184 (spoken longer)

**English** (case-richness = 0.420, ESL learner speech):
- Argument Δ: −0.674 (spoken shorter), t-test p = 1.3e-141
- Adjunct Δ: −0.318 (spoken shorter), t-test p = 0.229
- **Asymmetry not confirmed**: Both arguments and adjuncts shorten
- Modifiers Δ: −0.176 (spoken shorter)

The English pair deviates from the predicted pattern. We attribute this to the nature of the spoken corpus (en_eslspok): it consists of non-native (ESL) learner speech, which may have distinct structural preferences from native speech. ESL speakers produce fewer complex embedded structures and adjust their grammar to avoid difficulty [13], potentially collapsing the adjunct-argument distinction.

## Morphological Modulation

[FIGURE:fig3]

We tested whether the magnitude of spoken-adjunct elongation (Δ_adjunct per language) correlates with morphological case richness. Across the three languages:

- Slovenian: case-richness = 0.587, adjunct Δ = +0.219
- French: case-richness = 0.180, adjunct Δ = +0.143
- English: case-richness = 0.420, adjunct Δ = −0.318

Pearson r = −0.471, p = 0.688 (not significant). The negative trend suggests that higher case richness might be associated with less adjunct elongation, contrary to our prediction. However, with only three language pairs and one outlier (English ESL), this conclusion is premature. We discuss alternative explanations below.

## Cross-Language Evaluation (14-Language Dataset)

To assess generalizability, we evaluated the hypothesis on a 14-language subset including English, Slovenian, and French plus 11 additional languages [ARTIFACT:art_keVDdRwzuK2n]. Results show:

- **Conformance rate**: 28.6% (4 of 14 languages conform to the predicted argument-shorten, adjunct-not-shorten pattern)
- **Argument effect (pooled 14 languages)**: Mean Δ = −0.0069, p = 0.810 (not significant in paired tests)
- **Adjunct effect (pooled 14 languages)**: Mean Δ = +0.0028, p = 0.928 (not significant in paired tests)
- **Asymmetry paired t-test**: t = 0.235, p = 0.818 (not significant)

This suggests that while the argument-adjunct asymmetry is robust in three-language core analysis, it does not generalize uniformly to all 14 languages. Ten languages deviate, showing patterns such as both arguments and adjuncts shortening (Turkish, Italian, German, others) or both elongating. This heterogeneity points to substantial cross-linguistic variance that simple case-richness indexing does not capture.

## Effect Sizes and Cohen's d

Within-language effect sizes (Cohen's d) for the argument-adjunct interaction are small but directionally consistent:
- Arguments: mean d across 14 languages = −0.0075 (consistent minor shortening)
- Adjuncts: mean d across 14 languages = +0.0131 (consistent minor elongation)
- 85.7% and 78.6% of languages, respectively, showed the predicted direction

# Discussion

## Interpretation: Incremental Processing and Right-Adjunction

The argument-adjunct asymmetry aligns well with incremental sentence processing theory. In real-time production, speakers begin planning and uttering the main clause (predicate + core arguments) before fully planning adjuncts. Arguments must be integrated immediately: a listener hearing "The dog ... the cat" cannot yet form a complete proposition and must hold the incomplete dependency in working memory. A speaker under time pressure thus has incentive to place arguments close to their heads, minimizing storage cost. Adjuncts, by contrast, can be semantically and structurally integrated after the main clause is complete: "The dog chased the cat" is a complete, interpretable utterance, and appending an adjunct ("in the park") adds optional information that does not require pre-integration planning.

This mechanism predicts right-adjunction: spoken language should show systematic clause-final or post-verbal placement of adverbial clauses and relative clauses, with adjuncts placed *after* the main predicate is satisfied. Our data support this: adjuncts in speech are, on average, 0.6 words farther from their heads than in writing, consistent with a strategy of late, post-clause adjunction.

## Why Morphological Case Richness Does Not Predict Cross-Linguistic Variation

Our initial hypothesis predicted that case-marking languages would show larger adjunct elongation because case morphology decouples grammatical function from word order, permitting more flexible adjunct placement. The 14-language evaluation disconfirms this: the correlation between case richness and adjunct elongation is near zero (r = 0.194, p = 0.506).

We propose three explanations:

1. **Word Order Rigidity is Multidimensional**: Case morphology is one factor liberating word order, but sentence-type-specific constraints (e.g., V2 in Germanic languages, Subject-Verb-Object dominance in analytic languages) may override case-marking patterns. A language with rich case marking but strict verb-second (like some Slavic languages under embedded clause constraints) may not show enhanced adjunct freedom in speech.

2. **Interaction Dynamics Override Morphology**: Spoken language is interactive, often involving frequent turn-taking, repair, and backchanneling. These discourse-pragmatic factors may constrain adjunct placement more strongly than morphological case. Adjuncts may be shortened when interactional overlap is high, or elongated to enable simultaneous turn-planning; case marking does not capture this dynamic.

3. **Prosodic Phrasing, Not Case Marking**: Spoken language is organized into intonational phrases, which interact with syntactic structure. Adjuncts may be placed at phrase boundaries, creating distance not because of case marking but because of prosodic constituency. This hypothesis would require prosodic annotation (not available in all UD treebanks) to test.

These alternative mechanisms suggest that the cross-linguistic variance in the argument-adjunct asymmetry is not primarily driven by morphological typology but by a richer set of structural and pragmatic factors.

## Limitations

1. **ESL Confound**: The English spoken corpus (en_eslspok) consists of non-native learner speech, which likely has atypical grammatical properties. Ideally, we would use native English conversational speech (e.g., from the GUM corpus), but that treebank pair was not available in the initial dataset.

2. **Small Language Sample for Morphological Modulation**: With only three core languages (later extended to 14), robust correlation analysis is underpowered. Case richness is also a crude proxy for word-order flexibility; a richer typological index incorporating verb-second, relative clause position, and other constraints would be more informative.

3. **Annotation Heterogeneity Across Treebanks**: While UD is a unified standard, individual treebanks vary in annotation practices, particularly for borderline cases (e.g., whether certain clauses are adverbial or relative). This could introduce noise; however, we followed strict UD guidelines and our large sample sizes should buffer against annotation variance.

4. **Directionality of Causation**: We interpret the asymmetry as reflecting cognitive pressures of incremental production, but we do not have experimental evidence (e.g., self-paced reading, eye-tracking) demonstrating that spoken-adjunct elongation actually reduces comprehension difficulty or production planning load. Our evidence is observational and correlational.

5. **Generalization Beyond Three Core Languages**: The per-language analysis suggests substantial cross-linguistic heterogeneity, with only 29% conformance to the predicted pattern in the 14-language set. This raises the question of whether the asymmetry is a universal principle or a tendency observed primarily in three morphologically and structurally diverse but individually unrepresentative languages.

## Implications for Linguistic Theory

1. **Dependency Distance Minimization is Not Uniform**: The aggregate reduction in DDM in spoken language is not a consequence of uniform, relation-agnostic pressure but of selective minimization on arguments. This implies that theories of DDM (e.g., based on memory constraints) should distinguish between obligatory and optional dependencies, integrating principles from incremental processing.

2. **Typological Rankings Must Stratify by Relation Type**: Cross-linguistic comparisons of DDM efficiency (e.g., using eta-scores or other optimality measures) should report separate scores for arguments and adjuncts. Languages that rank high in overall DDM efficiency may achieve this through argument minimization while allowing adjunct elongation, a pattern that carries different theoretical implications than uniform minimization.

3. **Causality Flows from Incremental Cognition, Not Just Evolution**: The argument-adjunct asymmetry suggests that register-specific phenomena (spoken vs. written) provide a window into the online cognitive constraints that shape language structure. By examining how these constraints operate differentially on different dependency types, we can refine our understanding of the computational pressures that shaped language evolution and continue to govern speech production.

# Conclusion

This paper has demonstrated that the widely reported reduction in mean dependency distance in spoken versus written language masks a systematic asymmetry: arguments are significantly shorter in speech, while adjuncts are paradoxically longer. This finding reframes the phenomenon of spoken-language DDM reduction: it is not a uniform pressure but a selective intensification of argument minimization, driven by incremental processing constraints. The asymmetry is robust across multiple languages and treebank pairs, though cross-linguistic generalization is moderate, suggesting language-family and structural modulators beyond simple morphological case richness.

The work opens several directions for future investigation:

1. **Psycholinguistic Validation**: Conduct self-paced reading and eye-tracking studies on English and Slovenian minimal pairs varying argument and adjunct distances, testing whether the patterns reflect genuine processing difficulty or are epiphenomena of other structural factors.

2. **Prosodic Analysis**: Re-analyze the data using prosodic annotation (intonational phrases, prominence) to test whether adjunct placement is driven by prosodic constituency rather than (or in addition to) case morphology.

3. **Discourse Pragmatics**: Stratify spoken corpora by interactional context (monologue, dialogue, task-based conversation) to assess whether conversational interaction intensifies or mitigates the adjunct-elongation effect.

4. **Expanded Language Sample**: Expand the evaluation to 30+ language families, focusing on typologically contrastive languages (e.g., Turkish vs. English, Japanese vs. Mandarin) to map the space of cross-linguistic variation more completely.

5. **Formal Modeling**: Develop a computational model of incremental production that generates predictions about argument-adjunct distance as a function of cognitive load, morphological flexibility, and prosodic constraints, enabling quantitative comparison with observed corpus patterns.

The argument-adjunct asymmetry in dependency distance is a previously uncharacterized empirical regularity. It demonstrates that fundamental principles of linguistic organization—in this case, dependency distance minimization—operate heterogeneously across relation types, shaped by the immediate cognitive pressures of real-time language production. Understanding this heterogeneity enriches both our account of cross-linguistic universals and our grasp of how cognitive science and linguistic structure intertwine.

# References

[1] Futrell, R., Mahowald, K., & Gibson, E. (2015). Large-scale evidence of dependency length minimization in 37 languages. *Proceedings of the National Academy of Sciences*, 112(33), 10336–10341.

[2] Ferrer-i-Cancho, R., Gómez-Rodríguez, C., Esteban, J. L., & Alemany-Puig, L. (2022). The optimality of syntactic dependency distances. *Physical Review E*, 105(1), 014308.

[3] Liu, H. (2008). Dependency distance as a metric of language comprehension difficulty. *Journal of Cognitive Science*, 9(2), 159–191.

[4] Gibson, E. (1998). Linguistic complexity: Locality of syntactic dependencies. *Cognition*, 68(1), 1–76.

[5] Ferrer-i-Cancho, R. (2022). The distribution of syntactic dependency distances. *Glottometrics*, 58, 35–94.

[6] Dobrovoljc, K. (2025). Counting trees: A treebank-driven exploration of syntactic variation in speech and writing across languages. *Corpus Linguistics and Linguistic Theory*, 21(1), 46–78.

[7] Poiret, C., & Liu, H. (2023). Cross-linguistic variations in dependency distance minimization. In *Proceedings of the 37th Pacific Asia Conference on Language, Information and Computation*, Hong Kong. (pp. 234–243).

[8] Sinnemäki, K., & Haakana, V. (2023). Head and dependent marking and dependency length in possessive noun phrases: A typological study of morphological and syntactic complexity. *Linguistics Vanguard*, 9(1), 45–57.

[9] Hawkins, J. A. (2004). *Efficiency and complexity in grammars*. Oxford University Press.

[10] Greenberg, J. H. (1966). Language universals: With special reference to feature hierarchies. *The Hague: Mouton*.

[11] Friederici, A. D. (2011). The brain basis of linguistic processing. *Annual Review of Linguistics*, 37, 89–112.

[12] Kuperberg, G. R., & Jaeger, T. F. (2016). What does the brain do when you read? *Current Opinion in Behavioral Sciences*, 10, 1–8.

[13] Ellis, N. C., & Schmidt, R. (1997). Morphology and longer-distance dependencies: Laboratory research on the processing of unexpected word order. *Studies in Second Language Acquisition*, 19(3), 323–345.
</current_paper>

<reviewer_feedback>
Paper reviewer feedback from the previous iteration. Your strategy MUST address these critiques.
Prioritize major issues — these are the most impactful improvements to make.

- [MAJOR] (methodology) The 14-language extension uses treebanks that are not spoken corpora. From eval.py: German 'spoken' = de_hdt (Hamburg Dependency Treebank, newspaper text); Russian 'spoken' = ru_syntagrus (SynTagRus, written journalistic); Arabic 'spoken' = ar_padt (Penn Arabic Dependency Treebank, newswire); Chinese 'spoken' = zh_cfl (written learner compositions); Italian 'spoken' = it_vit (Venice Italian Treebank, written legal/administrative); Portuguese 'spoken' = pt_bosque (CETENFolha, written newspaper); Spanish 'spoken' = es_ancora (AnCora, written newspaper). This means the 'spoken vs. written' comparison for most of the 14 languages is actually between two written genres (or learner-written vs. native-written), which undermines any claim about spoken language at all.
  Action: Audit each 'spoken' treebank in the extension against its official UD documentation and remove or replace any that is not transcribed speech. For languages where no genuinely spoken UD treebank exists, drop the language from the cross-linguistic analysis rather than substituting a written treebank. Report the final list of verified spoken treebanks explicitly.
- [MAJOR] (evidence) The paper's headline 14-language result is a clear null: argument pooled p=0.810, adjunct pooled p=0.928, asymmetry paired t p=0.818, conformance rate 28.6% (4/14 languages). The paper characterises this as 'cross-linguistic generalization is moderate' and 'directionally consistent', but a pattern present in 4/14 cases with all tests non-significant is not moderate generalization—it is a failed replication. The framing misleads the reader about what the data actually show.
  Action: Either (a) reframe the 14-language section honestly as a pre-registered replication that failed, discuss why the replication failed (probably because the 'spoken' treebanks are not actually spoken), and treat the 3-language core result as an exploratory finding requiring replication; or (b) fix the treebank selection (see previous critique) and re-run the analysis. Do not describe a null result as 'directionally consistent support'.
- [MAJOR] (methodology) The primary statistical evidence (the pooled arc-level t-tests with n_argument_spoken=16,820 and n_argument_written=105,125) treats every arc as an independent observation. Arcs are not independent: they share sentence structure (multiple arcs per sentence), treebank genre effects (all 16,820 spoken argument arcs are from 3 treebanks), and cross-lingual heterogeneity. Treating 900k arcs as i.i.d. massively deflates p-values (t=-13.00, p≈10⁻³⁸) in a way that has no interpretable meaning for the population-level claim.
  Action: Use sentence-level averages or treebank-level averages as the unit of analysis, then bootstrap at the sentence or treebank level. Report effect sizes with honest confidence intervals that account for the clustered structure. The key question is whether the asymmetry is statistically significant at the language level, not at the arc level.
- [MAJOR] (evidence) A critical internal inconsistency: the dataset artifact (art_F2XD0ACeTqeG summary) reports Slovenian case_richness=0.9406 (81,750 nominals), but the paper body reports 0.587. Similarly, the paper reports English case_richness=0.420 which is implausibly high—English has very limited morphological case (only pronouns retain it) and the true figure should be under 0.05 for NOUN+PRON+PROPN. The method.py code computes case richness from the written modality only, which could explain some discrepancy, but not a near-doubling for Slovenian.
  Action: Recompute case richness using a single, clearly specified procedure: proportion of NOUN+PRON tokens (by UD UPOS) bearing a non-empty Case feature in the combined spoken+written corpus, with PROPN excluded (PROPN case marking often reflects copying from the source language, not inflectional paradigm richness). Report the token counts used. Verify that these values match published typological resources for a sanity check (e.g., WALS morphological case feature).
- [MAJOR] (methodology) The English 'spoken' corpus (en_eslspok) is non-native learner speech from English as a Second Language students. Using this as the spoken English comparison not only confounds modality (spoken vs. written) with nativeness (L1 vs. L2) and proficiency, it also means the 3-language 'core' analysis has only 2 genuinely comparable language pairs (Slovenian and French). The paper dedicates substantial discussion to explaining away the English result as an ESL artifact, but keeps it in the primary analysis.
  Action: Replace en_eslspok with a native English spoken treebank. The method.py code already attempts to load en_gum spoken genres (conversation, interview, vlog, speech) filtered by genre metadata. Use this instead. If GUM spoken genres are insufficient in size, acknowledge the limitation honestly and conduct the 3-language analysis with 2 languages (Slovenian and French), reporting that a native English spoken comparison was not available in the current UD release.
- [MAJOR] (rigor) References [11] and [12] are misattributed in the body text. The paper states 'Incremental processing theory, developed by Gibson [11, 12]...' but reference [11] is Friederici (2011) 'The brain basis of linguistic processing' (Annual Review of Linguistics) and reference [12] is Kuperberg & Jaeger (2016) 'What does the brain do when you read?' These are neurolinguistics and predictive processing papers, not the foundational work on incremental parsing by Gibson (1998) or Levy (2008). Gibson (1998) is correctly listed as reference [4] but is not cited in the incremental processing theory section where it is most relevant.
  Action: Correct the citations in the incremental processing section to [4] (Gibson 1998) for dependency locality theory, and add Levy (2008) 'Expectation-based syntactic comprehension' (Cognition) for expectation-based incremental processing. References [11] and [12] (Friederici, Kuperberg & Jaeger) belong in a different part of the discussion if used at all.
- [MAJOR] (rigor) The paper states the mixed-effects model encountered 'singular matrix issues' and therefore primary evidence comes from pooled raw t-tests. But the mixed-effects model is fitted at the stratum level (n_strata ≈ 12–18 rows, since there are 3–4 languages × 2 modalities × 3 rel_types), and the random effects are estimated over only 3 language groups. A mixed-effects model with n=3 groups cannot reliably estimate between-group variance—the random effect simply degenerates. This is not a software issue to be noted and moved past; it means that the crossed random-effects approach cannot be applied here at all, and a different statistical design is needed.
  Action: With 3 languages, the appropriate analysis is to compute the asymmetry index (Δ_adjunct − Δ_argument) for each language separately, report each with a bootstrap CI, and conduct a sign test or one-sample t-test across the 3 languages with appropriate degrees of freedom (df=2). Explicitly acknowledge that this is underpowered for cross-linguistic inference and that the 3-language result is exploratory.
- [MINOR] (methodology) The paper reports that the Slovenian adjunct delta is p=0.083 and labels this 'asymmetry confirmed.' At conventional α=0.05, this is not significant. At α=0.10 (if pre-specified), it could be considered marginal, but this threshold must be pre-specified rather than selected post-hoc.
  Action: Relabel the Slovenian adjunct result as 'marginal (p=0.083, not significant at α=0.05)'. If the paper intends to use a different significance threshold, specify it in the methods section.
- [MINOR] (novelty) The paper under-acknowledges how much of the 'argument shortening in speech' finding was already present in Poiret & Liu (2023) [7], who examined subject/object/oblique dependency distances by register for French. The paper says Poiret & Liu 'did not test adjunct relations, did not systematically normalize for sentence length'—this is true but the positive argument result is not fully novel.
  Action: Sharpen the novelty claim: the genuinely new element is the adjunct elongation direction and the modifier near-zero control, not the argument shortening per se. Restructure the Related Work section to acknowledge this more directly and frame the paper's contribution as extending and formalising the Poiret & Liu finding while adding the adjunct dimension.
- [MINOR] (clarity) The paper mentions that sl_sst was 'directly authored by reviewer Kaja Dobrovoljc (JSI/University of Ljubljana).' This language is inappropriate in a paper submission—it appears to identify the reviewer by name and institution, which would compromise blind review. Regardless of how this phrasing arose, it must be removed.
  Action: Remove this phrase entirely. Replace with a citation to Dobrovoljc & Erjavec (2012) or the relevant treebank documentation paper.
- [MINOR] (evidence) The paper asserts that the 'Asymmetry Index' of 0.927 is 'a large effect size' but this is the raw MDD difference (in word positions), not a standardised effect size. For a sentence-level claim, 0.927 words of additional distance for adjuncts vs. arguments does convey practical significance, but calling it 'large' without a standardised comparison is imprecise.
  Action: Report Cohen's d for the argument and adjunct spoken-vs.-written comparisons (the code computes these) alongside the raw delta. The d values in the code output (for the 3-language pool) would give a better sense of standardised effect size.
- [MINOR] (scope) The paper uses the same written treebank (en_ewt) as both the comparison for en_eslspok and as the 'written' side of the proposed English_GUM comparison in the code. Using the same written treebank in multiple language-pair analyses creates partial data overlap that inflates the apparent cross-language consistency.
  Action: If a GUM-based analysis is added, use a clearly distinct written comparison corpus (e.g., en_partut or en_lines) rather than reusing en_ewt.
</reviewer_feedback>

<task>
Generate 1 research strategy for THIS iteration.

**ARTIFACT LIMIT: Each strategy may contain AT MOST 3 artifact directions.** Focus on the highest-impact artifacts. Quality over quantity.

Each strategy should:
1. Define a clear OBJECTIVE - what novel contribution we're building toward
2. Plan artifacts to execute NOW - specify type, objective, approach, and depends_on for each
3. Account for parallel execution - all strategies and all planned artifacts run simultaneously, their artifacts are combined into one shared pool


</task><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_4SjiUyyE35Gi/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "ArtifactDep": {
      "description": "A single dependency on an existing artifact, with a short type label.\n\n``id`` and ``label`` are LLM-generated at strategy time. ``label`` is free-text but\nshort \u2014 a word or two naming the type of dependency, not a sentence.\n\n``relation_type`` and ``relation_rationale`` are populated later, in upd_hypo,\nusing the MultiCite citation-function typology (Lauscher et al., NAACL 2022).\nThey are absent at strategy time and may stay absent for legacy runs.",
      "properties": {
        "id": {
          "description": "ID of an existing artifact this artifact depends on",
          "title": "Id",
          "type": "string"
        },
        "label": {
          "description": "Short free-text label naming the type of this dependency (a word or two, not a sentence)",
          "title": "Label",
          "type": "string"
        }
      },
      "required": [
        "id",
        "label"
      ],
      "title": "ArtifactDep",
      "type": "object"
    },
    "ArtifactDirection": {
      "description": "High-level direction for an artifact to execute this iteration.\n\nID is code-assigned (LLMPrompt only \u2014 visible in prompts, not LLM-generated).",
      "properties": {
        "type": {
          "description": "Type of artifact to create",
          "enum": [
            "experiment",
            "research",
            "proof",
            "evaluation",
            "dataset"
          ],
          "title": "Type",
          "type": "string"
        },
        "objective": {
          "description": "What we want to achieve with this artifact",
          "title": "Objective",
          "type": "string"
        },
        "approach": {
          "description": "High-level direction/method",
          "title": "Approach",
          "type": "string"
        },
        "depends_on": {
          "description": "Existing artifacts this depends on, each with a short type label",
          "items": {
            "$ref": "#/$defs/ArtifactDep"
          },
          "title": "Depends On",
          "type": "array"
        }
      },
      "required": [
        "type",
        "objective",
        "approach"
      ],
      "title": "ArtifactDirection",
      "type": "object"
    },
    "Strategy": {
      "description": "A research strategy.\n\nContent fields have LLMPrompt + LLMStructOut markers.\n``id`` is code-assigned (LLMPrompt only \u2014 visible in prompts, not LLM-generated).\n\nID format: gen_strat_idx{N}",
      "properties": {
        "title": {
          "description": "Short name for this strategy",
          "title": "Title",
          "type": "string"
        },
        "objective": {
          "description": "The novel contribution we're building toward",
          "title": "Objective",
          "type": "string"
        },
        "rationale": {
          "description": "Why this strategy is promising",
          "title": "Rationale",
          "type": "string"
        },
        "artifact_directions": {
          "description": "Artifacts to execute THIS iteration",
          "items": {
            "$ref": "#/$defs/ArtifactDirection"
          },
          "title": "Artifact Directions",
          "type": "array"
        },
        "expected_outcome": {
          "description": "What we'll have after this iteration's artifacts complete",
          "title": "Expected Outcome",
          "type": "string"
        },
        "summary": {
          "default": "",
          "description": "Brief summary of the strategy and its expected contribution",
          "title": "Summary",
          "type": "string"
        }
      },
      "required": [
        "title",
        "objective",
        "rationale",
        "artifact_directions",
        "expected_outcome"
      ],
      "title": "Strategy",
      "type": "object"
    }
  },
  "description": "Top-level wrapper for LLM strategy generation output.",
  "properties": {
    "strategies": {
      "description": "List of generated strategies",
      "items": {
        "$ref": "#/$defs/Strategy"
      },
      "title": "Strategies",
      "type": "array"
    }
  },
  "required": [
    "strategies"
  ],
  "title": "Strategies",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-06-22 12:03:36 UTC

```
Direction: Computational Linguistics — Dependency Distance Minimization Across UD Treebanks. Something genuinely novel and groundbreaking that measures dependency-distance distributions across UD treebanks, investigates whether spoken language minimizes more than written, characterizes how typology interacts with the pattern, and identifies families that deviate. MUST use commul/universal_dependencies on HuggingFace.

Ambition: level 3 of 5 — phenomenological science: surface and rigorously characterize a new empirical regularity or anomaly in the data, even before a full theoretical explanation exists.

Reviewer: I am Kaja Dobrovoljc (JSI / University of Ljubljana). Calibrate from my existing papers. Cross-domain methods (information theory, mixed-effects models, sequence models) welcome — but keep them close to what I already know, not too far from my background.

Submission/Goal: a paper for ACL, EMNLP, or the Computational Linguistics journal. Audience: computational linguists and quantitative typologists. Tone: empirically rigorous, careful with linguistic detail, reproducible on public UD.
```

### [3] SYSTEM-USER prompt · 2026-06-22 12:05:42 UTC

```
<validation-feedback>
Attempt 1 failed validation.

You have not created the output file `.terminal_claude_agent_struct_out.json` yet. Use the Write tool to create it.

Please use the Write tool to overwrite `.terminal_claude_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```
