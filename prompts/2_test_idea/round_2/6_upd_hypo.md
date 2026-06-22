# upd_hypo — test_idea

> Phase: `invention_loop` · round 2 · `upd_hypo`
> Run: `run_4SjiUyyE35Gi` — Argument-Adjunct Asymmetry in Spoken-Register Dependency Distance Minimization
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `upd_hypo` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-22 12:47:38 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A hypothesis reviser (Step 3.6: UPD_HYPO in the invention loop)

You received the current hypothesis, all artifacts, and the paper draft.
Revise the hypothesis based on what the evidence supports.

Honest revision → focused research. Inflated confidence → wasted iteration.
</your_role>
</ai_inventor_context>

You are revising a research hypothesis based on empirical evidence gathered
during an iterative invention loop. Your role is internal reflection — honest
assessment of what the evidence supports.

SCOPE: Your ONLY output is the revised hypothesis text. You do NOT run code,
produce artifacts, fix bugs, or otherwise act on the evidence yourself — the
next iteration of the invention loop will spawn fresh artifacts based on your
revised hypothesis. Reflect on the evidence and rewrite the hypothesis;
nothing else.

PRINCIPLES:
- Ground every revision in specific artifacts and results
- Treat negative and null results as valuable contributions. If the original
  approach failed, the null result IS often the contribution — frame it as
  such (e.g. "X does not improve Y under conditions Z"). Only pivot to a
  different positive claim when the evidence actually supports one; never
  fabricate a positive narrative to mask a failed approach.
- Increase specificity as evidence accumulates
- Don't inflate confidence without strong evidence
- Preserve the core AII prompt unless evidence clearly contradicts it
- Revise hypothesis text only — never attempt to address feedback by running
  code, proposing fixes, or producing artifacts; the next loop iteration
  handles all artifact generation

<current_hypothesis>
The hypothesis as it stands. Revise it based on the evidence below.

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
</current_hypothesis>

<all_artifacts>
Complete set of research artifacts across all iterations.

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

--- Item 4 ---
id: art_5YIzNa1Lrdf9
type: dataset
title: 'UD Spoken-Written Treebank Pairs: Dependency Distance & Case-Richness'
summary: >-
  This artifact loads four Universal Dependencies treebank configurations from commul/universal_dependencies on HuggingFace
  (sl_sst: Slovenian spoken GOS corpus, sl_ssj: Slovenian written standard treebank, fr_rhapsodie: French spoken Rhapsodie
  corpus, fr_gsd: French written GSD treebank) and produces 35,896 sentence-level examples for the exp_sel_data_out format.
  Each example encodes: (1) the sentence text, length, treebank, modality, and language; (2) per-sentence mean dependency
  distance broken down into ARGUMENT (nsubj/obj/iobj/ccomp/xcomp), ADJUNCT (advcl/acl/acl:relcl), and MODIFIER (nmod/amod/advmod)
  categories; (3) per-sentence NOUN and PRON case marking counts. A global log-log OLS regression (log MDD ~ log sent_len)
  is fit across all treebanks pooled; per-treebank mean residuals serve as the sentence-length-normalized MDD metric. Key
  aggregate results stored in data_out.json: Slovenian case richness 0.94, French case richness 0.10; spoken ARG MDD residuals
  lower than written in both languages (Slovenian: -0.090, French: -0.225); spoken ADJUNCT residuals mixed (Slovenian: -0.050,
  French: +0.135). The treebank audit is documented in audit_report.txt. All data sourced from commul/universal_dependencies
  (1,587 HF downloads, UD v2.17). No LLM API calls were made ($0 spend). The data.py script is fully reproducible using the
  pinned pyproject.toml dependencies.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_4SjiUyyE35Gi/3_invention_loop/iter_2/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json

--- Item 5 ---
id: art_fgB5OzuKO3N0
type: experiment
in_dependencies:
- id: art_F2XD0ACeTqeG
  label: verified dataset basis
title: Sentence-Level Argument-Adjunct Asymmetry Analysis with Bootstrap CIs
summary: >-
  Sentence-level asymmetry analysis of dependency distance minimization (MDD) across spoken (sl_sst, 6121 sentences) and written
  (sl_ssj, 13435 sentences) Slovenian UD treebanks. Method: (1) arc classification into ARGUMENT/ADJUNCT/MODIFIER categories;
  (2) sentence-level MDD aggregation (mean dependency distance per sentence per category); (3) filtering to sentences with
  ≥1 arc in all 3 categories (6186/17686 complete sentences retained); (4) length normalization via OLS log(mdd)~log(sent_len)
  regression fitted on POOLED spoken+written data per (language,category), preserving the modality mean difference in residuals;
  (5) unpaired bootstrap (B=1000, seed=42) of mean residual MDD difference (spoken−written) per category with 95% CIs and
  Cohen's d; (6) asymmetry index = Δ_ADJUNCT − Δ_ARGUMENT with bootstrap CI. Baseline: same bootstrap procedure on raw log(MDD)
  without length normalization. Key results (Slovenian): ARGUMENT Δ=−0.051 CI=[−0.082,−0.019] shorter-in-spoken (CI excludes
  0); ADJUNCT Δ=−0.010 CI=[−0.038,+0.017] no-difference; MODIFIER Δ=+0.114 CI=[+0.090,+0.138] longer-in-spoken (unexpected
  for control); Asymmetry index=0.041 CI=[−0.003,+0.082] d=0.08 near-zero (CI barely includes 0). Verdict: partial confirmation
  — ARGUMENT shortening in spoken confirmed, asymmetry borderline. Only Slovenian available (no French data in dataset); cross-linguistic
  t-test not applicable. Outputs: method.py (full pipeline), method_out.json (exp_gen_sol_out schema-validated, 4 examples:
  3 categories + asymmetry index row), 4 diagnostic PNGs (asymmetry index plot, bootstrap distributions, violin plots, QQ
  plots).
workspace_path: >-
  /ai-inventor/aii_data/runs/run_4SjiUyyE35Gi/3_invention_loop/iter_2/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 6 ---
id: art_RHsCkkQagLE3
type: evaluation
in_dependencies:
- id: art_Gq_zeOShbi_1
  label: prior experiment results for comparison
title: 'Robustness, Power Analysis, and Cross-Language Audit: Arg-Adjunct Asymmetry'
summary: |-
  Evaluation of the argument-adjunct dependency distance asymmetry from iteration 1 across five methodological robustness variants, a Monte Carlo power analysis, and a cross-language audit of 14 Universal Dependencies treebanks.

  ROBUSTNESS VARIANTS (5/5 confirm asymmetry direction):
  - residualized_ols_original (iteration 1 baseline): arg_delta=+0.0071, adj_delta=+0.0196 (implied), interaction=+0.0125, p=0.281. Direction confirmed.
  - raw_mdd: arg_delta=-0.324 (shorter in spoken), adj_delta=+0.603 (longer in spoken). CONFIRMED, large effect.
  - ols_length_covariate: log-scale OLS with sent_len as covariate; arg coef=+0.083 (written>spoken), adj coef=-0.153 (spoken>written). CONFIRMED.
  - huber_robust_regression: Huber M-estimation (k=1.345); arg=+0.085, adj=-0.109. CONFIRMED, robust to outlier arcs.
  - outlier_sensitivity_1pct_trim: After removing top/bottom 1% per stratum (~0.9% of arcs trimmed); arg=-0.299, adj=+0.495. CONFIRMED.

  POWER ANALYSIS (Monte Carlo, conservative OLS without random effects, n_sims=3000):
  - n=3 (current): power=0.109
  - n=4: power=0.130
  - n=6: power=0.179
  - n=8: power=0.249
  - n=12: power=0.363
  - n=20: power=0.526 (extrapolated)
  - 80% power not reached at n=20 under conservative model. Mixed-effects model estimates ~12-20 verified language pairs required.

  CROSS-LANGUAGE AUDIT (14 treebanks assessed):
  - VERIFIED_SPOKEN (3): Slovenian sl_sst/sl_ssj, French fr_rhapsodie/fr_gsd, Italian it_parlato/it_isdt (not yet on HuggingFace)
  - LEARNER_CONFOUNDED (1): English en_eslspok/en_ewt
  - PARTIAL (5): en_gum spoken subset, sv_talbanken interviews, lv_lvtb parliament, fi_ftb, tr_tourism
  - UNVERIFIED_WRITTEN (5): de_hdt, ru_syntagrus, eu_bdt, ar_padt, zh_gsd

  HONEST SCOPE STATEMENT: Asymmetry confirmed in 2 verified spoken-written pairs (Slovenian, French), robust across all 5 analysis variants. Formal generalization underpowered (n=3, power=0.109). Genuine spoken-written UD pairs rare (~2-3 verified as of 2026-06). Recommended expansion: it_parlato (Italian), en_gum spoken subset, sv_talbanken interviews.

  OUTPUTS: eval_out.json (schema-validated), full/mini/preview variants, 3 plots (treebank census, robustness bar chart, power curve). Robustness confirmation rate: 5/5 = 1.0.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_4SjiUyyE35Gi/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1
out_expected_files:
- eval.py
- full_eval_out.json
- mini_eval_out.json
- preview_eval_out.json
</all_artifacts>

<new_artifacts_this_iteration>
These 3 artifacts were created THIS iteration.

id: art_5YIzNa1Lrdf9
type: dataset
title: 'UD Spoken-Written Treebank Pairs: Dependency Distance & Case-Richness'
summary: >-
  This artifact loads four Universal Dependencies treebank configurations from commul/universal_dependencies on HuggingFace
  (sl_sst: Slovenian spoken GOS corpus, sl_ssj: Slovenian written standard treebank, fr_rhapsodie: French spoken Rhapsodie
  corpus, fr_gsd: French written GSD treebank) and produces 35,896 sentence-level examples for the exp_sel_data_out format.
  Each example encodes: (1) the sentence text, length, treebank, modality, and language; (2) per-sentence mean dependency
  distance broken down into ARGUMENT (nsubj/obj/iobj/ccomp/xcomp), ADJUNCT (advcl/acl/acl:relcl), and MODIFIER (nmod/amod/advmod)
  categories; (3) per-sentence NOUN and PRON case marking counts. A global log-log OLS regression (log MDD ~ log sent_len)
  is fit across all treebanks pooled; per-treebank mean residuals serve as the sentence-length-normalized MDD metric. Key
  aggregate results stored in data_out.json: Slovenian case richness 0.94, French case richness 0.10; spoken ARG MDD residuals
  lower than written in both languages (Slovenian: -0.090, French: -0.225); spoken ADJUNCT residuals mixed (Slovenian: -0.050,
  French: +0.135). The treebank audit is documented in audit_report.txt. All data sourced from commul/universal_dependencies
  (1,587 HF downloads, UD v2.17). No LLM API calls were made ($0 spend). The data.py script is fully reproducible using the
  pinned pyproject.toml dependencies.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_4SjiUyyE35Gi/3_invention_loop/iter_2/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json

id: art_fgB5OzuKO3N0
type: experiment
in_dependencies:
- id: art_F2XD0ACeTqeG
  label: verified dataset basis
title: Sentence-Level Argument-Adjunct Asymmetry Analysis with Bootstrap CIs
summary: >-
  Sentence-level asymmetry analysis of dependency distance minimization (MDD) across spoken (sl_sst, 6121 sentences) and written
  (sl_ssj, 13435 sentences) Slovenian UD treebanks. Method: (1) arc classification into ARGUMENT/ADJUNCT/MODIFIER categories;
  (2) sentence-level MDD aggregation (mean dependency distance per sentence per category); (3) filtering to sentences with
  ≥1 arc in all 3 categories (6186/17686 complete sentences retained); (4) length normalization via OLS log(mdd)~log(sent_len)
  regression fitted on POOLED spoken+written data per (language,category), preserving the modality mean difference in residuals;
  (5) unpaired bootstrap (B=1000, seed=42) of mean residual MDD difference (spoken−written) per category with 95% CIs and
  Cohen's d; (6) asymmetry index = Δ_ADJUNCT − Δ_ARGUMENT with bootstrap CI. Baseline: same bootstrap procedure on raw log(MDD)
  without length normalization. Key results (Slovenian): ARGUMENT Δ=−0.051 CI=[−0.082,−0.019] shorter-in-spoken (CI excludes
  0); ADJUNCT Δ=−0.010 CI=[−0.038,+0.017] no-difference; MODIFIER Δ=+0.114 CI=[+0.090,+0.138] longer-in-spoken (unexpected
  for control); Asymmetry index=0.041 CI=[−0.003,+0.082] d=0.08 near-zero (CI barely includes 0). Verdict: partial confirmation
  — ARGUMENT shortening in spoken confirmed, asymmetry borderline. Only Slovenian available (no French data in dataset); cross-linguistic
  t-test not applicable. Outputs: method.py (full pipeline), method_out.json (exp_gen_sol_out schema-validated, 4 examples:
  3 categories + asymmetry index row), 4 diagnostic PNGs (asymmetry index plot, bootstrap distributions, violin plots, QQ
  plots).
workspace_path: >-
  /ai-inventor/aii_data/runs/run_4SjiUyyE35Gi/3_invention_loop/iter_2/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

id: art_RHsCkkQagLE3
type: evaluation
in_dependencies:
- id: art_Gq_zeOShbi_1
  label: prior experiment results for comparison
title: 'Robustness, Power Analysis, and Cross-Language Audit: Arg-Adjunct Asymmetry'
summary: |-
  Evaluation of the argument-adjunct dependency distance asymmetry from iteration 1 across five methodological robustness variants, a Monte Carlo power analysis, and a cross-language audit of 14 Universal Dependencies treebanks.

  ROBUSTNESS VARIANTS (5/5 confirm asymmetry direction):
  - residualized_ols_original (iteration 1 baseline): arg_delta=+0.0071, adj_delta=+0.0196 (implied), interaction=+0.0125, p=0.281. Direction confirmed.
  - raw_mdd: arg_delta=-0.324 (shorter in spoken), adj_delta=+0.603 (longer in spoken). CONFIRMED, large effect.
  - ols_length_covariate: log-scale OLS with sent_len as covariate; arg coef=+0.083 (written>spoken), adj coef=-0.153 (spoken>written). CONFIRMED.
  - huber_robust_regression: Huber M-estimation (k=1.345); arg=+0.085, adj=-0.109. CONFIRMED, robust to outlier arcs.
  - outlier_sensitivity_1pct_trim: After removing top/bottom 1% per stratum (~0.9% of arcs trimmed); arg=-0.299, adj=+0.495. CONFIRMED.

  POWER ANALYSIS (Monte Carlo, conservative OLS without random effects, n_sims=3000):
  - n=3 (current): power=0.109
  - n=4: power=0.130
  - n=6: power=0.179
  - n=8: power=0.249
  - n=12: power=0.363
  - n=20: power=0.526 (extrapolated)
  - 80% power not reached at n=20 under conservative model. Mixed-effects model estimates ~12-20 verified language pairs required.

  CROSS-LANGUAGE AUDIT (14 treebanks assessed):
  - VERIFIED_SPOKEN (3): Slovenian sl_sst/sl_ssj, French fr_rhapsodie/fr_gsd, Italian it_parlato/it_isdt (not yet on HuggingFace)
  - LEARNER_CONFOUNDED (1): English en_eslspok/en_ewt
  - PARTIAL (5): en_gum spoken subset, sv_talbanken interviews, lv_lvtb parliament, fi_ftb, tr_tourism
  - UNVERIFIED_WRITTEN (5): de_hdt, ru_syntagrus, eu_bdt, ar_padt, zh_gsd

  HONEST SCOPE STATEMENT: Asymmetry confirmed in 2 verified spoken-written pairs (Slovenian, French), robust across all 5 analysis variants. Formal generalization underpowered (n=3, power=0.109). Genuine spoken-written UD pairs rare (~2-3 verified as of 2026-06). Recommended expansion: it_parlato (Italian), en_gum spoken subset, sv_talbanken interviews.

  OUTPUTS: eval_out.json (schema-validated), full/mini/preview variants, 3 plots (treebank census, robustness bar chart, power curve). Robustness confirmation rate: 5/5 = 1.0.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_4SjiUyyE35Gi/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1
out_expected_files:
- eval.py
- full_eval_out.json
- mini_eval_out.json
- preview_eval_out.json
</new_artifacts_this_iteration>

<current_paper>
The paper draft from this iteration — represents the current state of the research story.

# Introduction

The human language faculty exhibits a remarkable preference for linear word orders that minimize the distance between syntactically dependent words. This dependency distance minimization (DDM) principle has been demonstrated as a quantitative universal across 37 languages using large parsed corpora [1], holds across diverse language families [2], and correlates with processing difficulty in psycholinguistic tasks [3]. The universality is striking: despite vast differences in morphology, phonology, and historical origin, languages organize their words according to a common cognitive pressure to keep related elements close.

Yet a coarser empirical observation—one that has received little theoretical attention—shadows this universal: spoken language exhibits systematically shorter mean dependency distances than written language [3, 4]. The immediate interpretation is intuitive: speakers minimize distances more aggressively than writers, operating under real-time production constraints. However, this interpretation assumes *uniform* minimization across all dependency relations. If minimization operates selectively—intensifying on certain relation types while relaxing on others—then the aggregate reduction conflates opposing pressures and misattributes the phenomenon's locus.

This paper demonstrates that the spoken-language reduction in MDD is not uniform but reflects a systematic **argument-adjunct asymmetry**. Core grammatical relations selected by a predicate (subjects, objects, clausal complements)—hereafter *arguments*—are significantly shorter in speech than writing, consistent with incremental processing pressure: these elements must be integrated immediately for semantic interpretation. By contrast, optional modifiers and peripheral dependents (adverbial clauses, relative clauses)—hereafter *adjuncts*—show no reduction and paradoxically lengthen in spoken language. This pattern is consistent with a **right-adjunction strategy**: speakers append adjuncts after the main clause is complete, maximizing locality constraints for arguments while tolerating distance for optional elements. A third category, modifiers (nominal and adverbial modifiers of nouns and verbs), serves as a within-analysis control and exhibits near-zero register difference, supporting the specificity of the argument effect.

We test this hypothesis using two verified spoken-written Universal Dependencies (UD) treebank pairs: Slovenian (sl_sst/sl_ssj, 6,121 spoken sentences; Dobrovoljc et al., 2012) and French (fr_rhapsodie/fr_gsd, 6,032 spoken sentences; Lacheret et al., 2014). Both corpora represent transcribed natural dialogue in the UD framework, enabling precise computation of dependency distances with controlled annotation schemes [ARTIFACT:art_5YIzNa1Lrdf9]. We apply sentence-level analysis with bootstrap confidence intervals and multiple normalization procedures, removing sentence-length confounds while preserving register differences. Results confirm argument shortening in both languages (Slovenian: Δ = −0.051, 95% CI [−0.082, −0.019]; French: raw Δ = −0.634, p < 10⁻³⁵) and adjunct non-reduction or elongation (Slovenian: Δ = −0.010, CI [−0.038, 0.017]; French: Δ = +0.143, p = 0.470) [ARTIFACT:art_fgB5OzuKO3N0].

A critical contribution of this work is methodological transparency: we audited 14 UD treebanks claiming to represent 'spoken' language and found that most are actually written genres (newspapers, journalism, learner text, legal documents). Only three treebanks qualify as verified spoken corpora: Slovenian (sl_sst), French (fr_rhapsodie), and Italian (it_parlato, not yet on HuggingFace). This audit undermines the credibility of claims that the asymmetry generalizes across 14+ languages; prior iteration's null results on the 14-language extension are attributable to misidentified treebanks, not to genuine cross-linguistic failure [ARTIFACT:art_RHsCkkQagLE3]. A Monte Carlo power analysis reveals that 80% statistical power requires 12–20 verified spoken-written pairs, far exceeding the current supply of high-quality UD resources. Thus, the argument-adjunct asymmetry is a well-supported phenomenon in Slovenian and French, an exploratory (not yet confirmed) pattern requiring expansion to additional languages.

## Contributions

This paper makes four contributions:

1. **Phenomena**: We characterize a previously undocumented argument-adjunct asymmetry in register-specific dependency distance, showing that the aggregate spoken-language reduction in DDM is not uniform but directionally opposite for arguments versus adjuncts and modifiers [ARTIFACT:art_fgB5OzuKO3N0].

2. **Mechanism**: We ground the asymmetry in incremental processing theory and right-adjunction syntax, providing a principled explanation for why arguments shorten but adjuncts resist or lengthen in speech.

3. **Methodological rigor**: We demonstrate that most UD treebanks labeled 'spoken' are misidentified written genres, and we establish statistical power requirements (12–20 verified pairs) for robust cross-linguistic claims [ARTIFACT:art_RHsCkkQagLE3].

4. **Honest framing**: We present evidence of the asymmetry in two verified spoken-written language pairs as an exploratory finding requiring replication, rather than overstating generality based on flawed cross-linguistic data.

# Related Work

## Dependency Distance Minimization as Universal

Dependency distance minimization has become one of the most-replicated quantitative universals in linguistics. Futrell, Mahowald, and Gibson [1] tested DDM across 37 typologically diverse languages using large parsed corpora, finding that all languages organize words such that actual dependency lengths are substantially shorter than conservative random baselines. They grounded DDM in working memory constraints: holding unresolved syntactic expectations in memory incurs a cost proportional to how long the parser must wait to integrate dependent elements. Ferrer-i-Cancho and colleagues [2] extended this line by introducing an optimality score (eta) measuring how close each language's word order comes to the theoretical minimum dependency length given its syntactic structure; approximately half of 93 languages achieve 70%+ optimization, suggesting DDM is not merely a tendency but an organizational principle enforced through grammar.

However, these foundational studies aggregate over all dependency relations without stratification. The question of whether all relation types equally contribute to the universal remains unanswered—a gap this paper addresses.

## Register Variation and Spoken Language Syntax

Register-specific syntactic variation has been documented across phonology, morphology, and lexical richness [5, 6], but systematic analysis of dependency distance by register and relation type is sparse. Liu [3] observed that Japanese spoken dialogue exhibits lower mean dependency distance than written news but did not stratify by relation type or control for sentence length. Dobrovoljc [4] recently compared spoken and written UD treebanks for English and Slovenian using structural inventory methods (delexicalized dependency subtree shapes), finding that speech contains fewer diverse syntactic structures than writing; this result aligns with intuitions about speech simplification but does not directly measure dependency distance or examine register effects on specific relation types. Poiret and Liu [7], in cross-linguistic work on French, compared dependency distances for subject and oblique relations in spoken versus written corpora and found arguments are shorter in speech—consistent with our argument findings—but they did not systematically test adjunct relations, normalize for sentence length rigorously, or investigate cross-linguistic patterns.

The novelty of this paper lies in the adjunct dimension and the modifier control. Argument shortening in spoken language has been suggested before [7]; what is new is the demonstration that adjuncts are not minimized equally (and are actually elongated in some contexts), and that nominal/adverbial modifiers serve as a control category showing near-zero register effect.

## Morphology, Word Order, and Typology

A substantial body of work connects morphological marking to syntactic organization. Sinnemäki and Haakana [8] studied the interaction of head and dependent marking with dependency length in possessive noun phrases, finding an inverse relationship between marking types but no significant cross-linguistic correlation between dependency length and morphological complexity alone. This suggests morphological and syntactic complexity are partially independent dimensions. The hypothesis that case morphology liberates word order flexibility for adjuncts is implicit in much typological work [9, 10] but has not been directly tested against register-specific dependency distance variation. The current paper reports a Pearson correlation of r = −0.471 (p = 0.688) between case richness and adjunct elongation across our three core languages, a null result that contradicts the initial hypothesis; this null is preserved in the revised framing as an open empirical question pending a larger verified sample.

## Incremental Processing and Working Memory

Incremental processing theory, developed by Gibson [11] and advanced by expectation-based accounts (Levy 2008), proposes that language comprehension unfolds in real time, with continuous integration of new words into an emerging structure. Storage cost (maintaining unresolved dependencies) and integration cost (linking distant dependents to heads) both penalize long-distance dependencies. Critically, incremental pressure should fall more heavily on *obligatory* elements: a listener hearing "The dog ... the cat" cannot yet form a complete proposition and must hold the incomplete dependency in working memory. Adjuncts, by contrast, are semantically optional and can be integrated after core elements are complete. This asymmetry in incremental pressure maps directly onto the argument-adjunct distinction we observe.

# Methods

## Data and Treebank Selection

We extracted dependency arcs from two verified spoken-written Universal Dependencies (UD v2.17, HuggingFace commul/universal_dependencies [12]) treebank pairs:

**Slovenian**: sl_sst (spoken, Slovenian Spoken Treebank, 6,121 sentences) vs. sl_ssj (written, Slovenian Marked Up Corpus, 13,435 sentences). The sl_sst treebank comprises transcribed natural spoken dialogue from the GOS corpus. The sl_ssj treebank contains news text and fiction. Both use consistent UD annotation [13].

**French**: fr_rhapsodie (spoken, 6,032 sentences) vs. fr_gsd (written, 16,341 sentences). The fr_rhapsodie treebank contains transcribed natural dialogue from French radio broadcasts. The fr_gsd treebank comprises web text and news [14].

These pairs were selected because: (1) both represent transcribed natural speech (not elicited, learner, or written approximations); (2) each language offers clear spoken-written annotation in UD; (3) Slovenian and French represent different language families and morphological profiles (Slovenian is morphologically rich with case marking; French is morphologically reduced with positional constraints); (4) both pairs use the same UD annotation scheme, enabling controlled comparison.

## Treebank Audit

In iteration 1, we reported results on 14 language pairs. A post-hoc audit of these treebanks against their official UD documentation (checking source corpus metadata and linguistic description) revealed that most 'spoken' treebanks are misidentified written genres:

- **Verified spoken-written pairs** (3 total): sl_sst/sl_ssj (Slovenian), fr_rhapsodie/fr_gsd (French), it_parlato/it_isdt (Italian; not yet on HuggingFace as of June 2026)
- **Learner-confounded** (1): en_eslspok/en_ewt (English; en_eslspok is non-native ESL learner speech, confounding register with proficiency)
- **Written-genre pairs or partial** (5+): de_hdt (newspaper), ru_syntagrus (journalistic), ar_padt (newswire), zh_cfl (learner compositions), it_vit (legal/administrative text), pt_bosque (newspaper), es_ancora (newspaper) [ARTIFACT:art_RHsCkkQagLE3]

This audit means claims of 14-language generalization in iteration 1 were based on false positives: 11 of the 14 treebanks do not represent genuine spoken-versus-written comparisons. The null results on the 14-language extension (pooled p = 0.810 for arguments, p = 0.928 for adjuncts) are attributable to this fundamental misidentification, not to genuine cross-linguistic failure of the hypothesis.

## Dependency Arc Classification

For each sentence, we extracted all dependency arcs (head-dependent pairs) and classified each arc's UD deprel label into one of three categories:

- **Arguments** (core obligatory participants): nsubj, obj, iobj, ccomp, xcomp, csubj
- **Adjuncts** (optional peripheral modifiers): advcl, acl, acl:relcl
- **Modifiers** (control category): nmod, amod, advmod, and other nominal/adverbial/adjectival modifications

Punctuation tokens and root arcs were excluded. We computed mean dependency distance (MDD) for each arc as |head_position − dependent_position| in 1-indexed token positions.

## Sentence-Length Normalization

Spoken sentences are typically shorter than written sentences on average, mechanically producing shorter distances. To isolate register effects, we performed OLS residualization: for each (language, modality, category) stratum, we fit the model log(MDD) ∼ log(sentence_length) using pooled spoken+written data, then retained residuals. This procedure removes the linear relationship between sentence length and distance while preserving the spoken-written mean difference in residuals. All statistical tests were performed on residualized MDD.

## Statistical Analysis

Unlike iteration 1, which treated 922,399 individual arcs as i.i.d. observations (violating independence assumptions and massively deflating p-values), we perform sentence-level analysis:

1. **Sentence-level aggregation**: For each sentence and category, we compute mean MDD; sentences without at least one arc in a given category are excluded (retaining 6,186/17,686 Slovenian sentences with all three categories). This reduces the effective sample size to sentence level, respecting the clustered structure of the data.

2. **Bootstrap resampling**: We perform 1,000 unpaired bootstrap resamples (B=1000, seed=42) of the mean residual MDD difference (spoken − written) per category, computing 95% confidence intervals and Cohen's d effect sizes [ARTIFACT:art_fgB5OzuKO3N0].

3. **Per-language inference**: With only 2 languages, we compute the asymmetry index (Δ_adjunct − Δ_argument) separately for each language and report results with bootstrap confidence intervals. We acknowledge that formal cross-linguistic hypothesis testing (e.g., one-sample t-test across languages with df=2) is severely underpowered [ARTIFACT:art_RHsCkkQagLE3].

4. **Robustness**: We verified the asymmetry across five methodological variants: (i) residualized OLS (iteration 1 baseline), (ii) raw MDD without normalization, (iii) OLS with log(sent_len) as covariate, (iv) Huber robust regression, (v) 1% outlier trimming. All five variants confirm the asymmetry direction [ARTIFACT:art_RHsCkkQagLE3].

# Results

## Main Finding: Argument-Adjunct Asymmetry in Slovenian

[FIGURE:fig1]

Sentence-level analysis (n=1,313 spoken, n=4,873 written sentences in Slovenian) after length normalization and bootstrap resampling reveals a clear asymmetry:

**Arguments** (n_spoken_arcs = 16,820; n_written = 105,125):
- Mean residual MDD (spoken − written): Δ = −0.051 words
- 95% Bootstrap CI: [−0.082, −0.019]
- Cohen's d: −0.091 (small effect)
- **Interpretation**: Significantly shorter in spoken (CI excludes zero)

**Adjuncts** (n_spoken = 2,972; n_written = 24,674):
- Mean residual MDD: Δ = −0.010 words  
- 95% Bootstrap CI: [−0.038, +0.017]
- Cohen's d: −0.022 (negligible)
- **Interpretation**: No significant difference (CI includes zero); asymmetry confirmed: adjuncts do not minimize as arguments do

**Modifiers** (control, n_spoken = 21,087; n_written = 156,218):
- Mean residual MDD: Δ = +0.114 words
- 95% Bootstrap CI: [+0.090, +0.138]
- Cohen's d: +0.333 (small-to-medium)
- **Interpretation**: Paradoxically longer in spoken (unexpected for a within-analysis control; see Discussion)

**Asymmetry Index** (Δ_adjunct − Δ_argument):
- Value: +0.041
- 95% Bootstrap CI: [−0.003, +0.082]
- **Interpretation**: Near-zero; the asymmetry is driven primarily by argument shortening rather than adjunct elongation

These results hold across all robustness variants [ARTIFACT:art_RHsCkkQagLE3], confirming directional stability.

## Cross-Language Comparison: Slovenian vs. French (Raw Data)

[FIGURE:fig2]

We conducted a preliminary analysis of French data (6,032 spoken sentences; from iteration 1 artifacts) using raw MDD (without residualization, for comparability) to assess generality across the two core languages [ARTIFACT:art_Gq_zeOShbi_1]:

**French raw MDD comparison**:
- **Arguments**: spoken 2.718 vs. written 3.042, Δ = −0.324 (t-test p ≈ 10⁻³⁵)
- **Adjuncts**: spoken 6.578 vs. written 5.975, Δ = +0.603 (t-test p ≈ 10⁻¹⁰)
- **Asymmetry confirmed**: Arguments minimize (as in Slovenian), adjuncts elongate (opposite direction from Slovenian residualized result but consistent with raw direction)

The raw-data French results show the asymmetry is directionally consistent across languages, though effect magnitudes differ (Slovenian has smaller effects post-residualization; French effects are larger pre-normalization). This suggests the phenomenon is robust but cross-language effect homogeneity cannot be assumed.

## Robustness Across Methodological Variants

[FIGURE:fig3]

We tested five distinct analysis pipelines to ensure the asymmetry is not an artifact of any single methodological choice [ARTIFACT:art_RHsCkkQagLE3]:

1. **Residualized OLS** (iteration 1 baseline): interaction coef = +0.0125, p = 0.281; asymmetry direction confirmed
2. **Raw MDD (no normalization)**: arg Δ = −0.324 (p ≈ 10⁻³⁸), adj Δ = +0.603 (p ≈ 10⁻¹⁰); robust, large effects
3. **OLS length covariate**: arg coefficient = +0.083 (written > spoken), adj coef = −0.153 (spoken > written); confirmed
4. **Huber robust regression**: arg Δ = +0.085, adj Δ = −0.109; confirmed despite outlier handling
5. **1% outlier trimming**: arg Δ = −0.299, adj Δ = +0.495; confirmed after removing extreme arcs

**Robustness confirmation rate: 5/5 variants (100%)** confirm asymmetry direction. This demonstrates the finding is not sensitive to preprocessing or normalization choices.

## Statistical Power and Cross-Linguistic Generalization

A Monte Carlo power analysis (n_sims = 3,000 per n_languages scenario) reveals how many verified spoken-written language pairs are required for 80% power under a mixed-effects model [ARTIFACT:art_RHsCkkQagLE3]:

| Number of Language Pairs | Statistical Power | Reject Null Count |
|---|---|---|
| 3 (current) | 0.109 (11%) | 328/3000 |
| 4 | 0.130 (13%) | 390/3000 |
| 6 | 0.179 (18%) | 537/3000 |
| 8 | 0.249 (25%) | 747/3000 |
| 12 | 0.363 (36%) | 1090/3000 |
| 20 | 0.526 (53%) | 1578/3000 |

Note: At n=20, power remains only 53%, well below the conventional 80% threshold. Mixed-effects model estimates place the required sample at 12–20 verified pairs for adequate power. Since only 3 verified spoken-written UD pairs exist (and one is not yet on HuggingFace), cross-linguistic generalization of the asymmetry is a priority for future work, not a settled claim.

# Discussion

## Interpretation: Incremental Processing and Right-Adjunction

The argument-adjunct asymmetry aligns well with incremental sentence processing theory. In real-time production, speakers begin planning and uttering the main clause (predicate + core arguments) before fully planning adjuncts. Arguments must be integrated immediately: a listener hearing "The dog ... the cat" cannot yet form a complete proposition and must hold the unresolved dependency in working memory. A speaker under time pressure thus has incentive to place arguments close to their heads, minimizing storage cost. Adjuncts, by contrast, can be semantically and structurally integrated after the main clause is complete: "The dog chased the cat" is a complete, interpretable utterance, and appending an adjunct ("in the park") adds optional information without requiring pre-integration planning.

This mechanism predicts right-adjunction in speech: adverbial clauses, relative clauses, and postverbal nominal modifiers should be systematically appended after the main predicate is satisfied, creating longer dependencies. The French raw data support this (adjuncts +0.603 words longer in spoken); the Slovenian residualized data show smaller effect magnitudes but directional consistency.

## The Modifier Control: Why Do Modifiers Lengthen in Speech?

The modifier result (Δ = +0.114, CI [+0.090, +0.138] in Slovenian) is unexpected and warrants discussion. We hypothesized modifiers would show near-zero register difference (a control category), but instead they lengthen modestly in spoken language. Two explanations merit consideration:

1. **Noun phrase simplification in speech**: Spoken language may deploy fewer embedded nominal phrases but construct them differently. When present, post-nominal modifiers (especially relative clauses and complex appositives) may be appended to noun phrases as afterthoughts, parallel to the adjunction strategy.

2. **Sentence structure differences**: Spoken language may have shorter sentences overall, causing sentence-level length normalization to incompletely remove structure-related confounds. The residualization procedure assumes a linear log-log relationship; non-linear dependencies might not be fully captured.

We report this finding as observed but acknowledge it complicates the narrative of a clean argument-adjunct control. The core finding—argument shortening combined with adjunct non-reduction—remains robust across all analyses.

## Why Morphological Case Richness Does Not Predict Cross-Linguistic Variance

Our initial hypothesis predicted that case-marking languages would show larger adjunct elongation because case morphology decouples grammatical function from word order, permitting freer adjunct placement. The correlation across three languages is r = −0.471 (p = 0.688), a clear null result contradicting this prediction.

We propose three explanations:

1. **Word Order Rigidity is Multidimensional**: Case morphology is one factor liberating word order, but sentence-type-specific constraints (verb-second in embedded clauses, subject-verb-object dominance in some Romance languages) override case-marking patterns. A language with rich case marking but strict syntactic constraints may show limited adjunct freedom.

2. **Prosodic Phrasing Dominates Morphology**: Spoken language is organized into intonational phrases. Adjuncts may be placed at prosodic phrase boundaries, creating distance not because of case marking but due to prosodic constituency. This hypothesis requires prosodic annotation (unavailable in standard UD) to test rigorously.

3. **Interaction Dynamics Override Morphology**: Spoken language is interactive, with frequent turn-taking and repair. These discourse-pragmatic factors may constrain adjunct placement more strongly than morphological typology.

The null morphological correlation underscores that the argument-adjunct asymmetry is not simply a function of gross typological features but depends on more fine-grained structural and pragmatic properties.

## Limitations

1. **Limited Verified Spoken Treebanks**: Only 2 verified spoken-written UD pairs are currently available on HuggingFace (Slovenian and French), limiting cross-linguistic inference. Our power analysis shows 12–20 pairs are needed for robust hypothesis testing. Until more genuine spoken corpora are annotated in UD, the asymmetry remains an exploratory finding specific to these two languages.

2. **Treebank Annotation Heterogeneity**: While UD is a unified standard, individual treebanks vary in annotation practices, particularly for borderline cases (e.g., whether certain clauses are adverbial or relative). Our large sample sizes at the sentence level should buffer against noise, but heterogeneity could introduce bias.

3. **No Experimental Evidence of Processing Difficulty**: We interpret the asymmetry as reflecting cognitive pressures of incremental production, but we lack direct psycholinguistic evidence (self-paced reading, eye-tracking, fMRI) demonstrating that spoken-adjunct elongation actually reduces comprehension difficulty or production planning load. Our evidence is observational and correlational.

4. **Sentence Length Normalization Imperfection**: Residualization via OLS assumes a linear log-log relationship; non-linear confounds may remain. The modifier result (unexpected lengthening in speech) hints that our normalization does not fully disentangle all sentence-structure effects.

5. **Lack of Prosodic Annotation**: Spoken UD treebanks do not include intonational phrase boundaries or prominence information. Analysis incorporating prosodic structure might reveal that adjunct placement is driven more by prosodic phrasing than by morphological typology.

## Methodological Lessons for Cross-Linguistic UD Research

The treebank audit exposed a critical infrastructure problem: most UD treebanks labeled 'spoken' are misidentified written genres or non-representative samples (ESL learner text, parliamentary speech, etc.). For future work on register-specific phenomena:

1. Verify treebank source material against official UD documentation before making claims about 'spoken' language.
2. Report treebank selection and audit procedures transparently in methods sections.
3. Acknowledge statistical power limitations: n=3 languages provides power ≈ 11% for mixed-effects tests.
4. Treat results from n < 6 verified pairs as exploratory, requiring replication, not as confirmed cross-linguistic universals.

# Conclusion

This paper has identified and rigorously characterized a systematic asymmetry in register-specific dependency distance: arguments are significantly shorter in spoken language, while adjuncts are not minimized to the same degree and may be longer. This asymmetry reframes the phenomenon of spoken-language DDM reduction: it is not a uniform pressure but a selective intensification of argument minimization, driven by incremental processing constraints.

The argument-adjunct asymmetry is robustly demonstrated in two verified spoken-written language pairs (Slovenian and French) and stable across five distinct methodological variants. However, formal cross-linguistic generalization is currently underpowered: Monte Carlo simulations indicate 12–20 verified spoken-written pairs are required for 80% statistical power. Since only 2–3 such pairs exist in current UD resources, the asymmetry should be understood as an exploratory phenomenon in two languages, not yet a confirmed universal.

The work exposes an infrastructure limitation in universal dependencies: the term 'spoken' treebank is often misapplied to written genres, journalism, and elicited speech. Future research should prioritize annotating high-quality transcribed natural speech in UD and auditing existing resources to distinguish genuine spoken corpora from mislabeled written variants.

**Future directions**:

1. **Spoken Treebank Expansion**: Prioritize UD annotation of Italian conversational speech (it_parlato), English conversational genres (en_gum subsets), and Swedish interviews (sv_talbanken spoken subset).

2. **Psycholinguistic Validation**: Conduct self-paced reading and eye-tracking studies on native-speaker minimal pairs varying argument and adjunct distances in both languages, testing whether patterns reflect genuine processing difficulty.

3. **Prosodic Analysis**: Re-analyze data with prosodic annotation (intonational phrases, prominence) to test whether adjunct placement is driven by prosodic constituency rather than (or in addition to) morphological typology.

4. **Discourse Pragmatics**: Stratify spoken corpora by interactional context (monologue, dialogue, task-based conversation) to assess whether conversational interaction intensifies or mitigates the adjunct-elongation effect.

5. **Formal Computational Modeling**: Develop an incremental production model that generates predictions about argument-adjunct distance as a function of cognitive load, morphological flexibility, and prosodic constraints, enabling quantitative comparison with observed corpus patterns.

The argument-adjunct asymmetry in dependency distance is a previously uncharacterized empirical regularity. It demonstrates that fundamental principles of linguistic organization—in this case, dependency distance minimization—operate heterogeneously across relation types, shaped by immediate cognitive pressures of real-time language production.

# References

[1] Futrell, R., Mahowald, K., & Gibson, E. (2015). Large-scale evidence of dependency length minimization in 37 languages. *Proceedings of the National Academy of Sciences of the United States of America*, 112(33), 10336–10341. https://doi.org/10.1073/pnas.1502134112

[2] Ferrer-i-Cancho, R., Gómez-Rodríguez, C., Esteban, J. L., & Alemany-Puig, L. (2022). The optimality of syntactic dependency distances. *Physical Review E*, 105(1), 014308. https://doi.org/10.1103/PhysRevE.105.014308

[3] Liu, H. (2008). Dependency distance as a metric of language comprehension difficulty. *Journal of Cognitive Science*, 9(2), 159–191.

[4] Dobrovoljc, K. (2025). Counting trees: A treebank-driven exploration of syntactic variation in speech and writing across languages. *Corpus Linguistics and Linguistic Theory*, 21(1), 46–78. https://doi.org/10.1515/cllt-2025-0046

[5] Biber, D. (1988). *Variation across speech and writing*. Cambridge University Press.

[6] Conrad, S., & Biber, D. (2001). Variation in English grammar. Studies in Language Variation and Change, 1, 1–21.

[7] Poiret, C., & Liu, H. (2023). Cross-linguistic variations in dependency distance minimization. In *Proceedings of the 37th Pacific Asia Conference on Language, Information and Computation* (PACLIC 37), Hong Kong (pp. 234–243).

[8] Sinnemäki, K., & Haakana, V. (2023). Head and dependent marking and dependency length in possessive noun phrases: A typological study of morphological and syntactic complexity. *Linguistics Vanguard*, 9(1), 45–57. https://doi.org/10.1515/lingvan-2021-0074

[9] Hawkins, J. A. (2004). *Efficiency and complexity in grammars*. Oxford University Press.

[10] Greenberg, J. H. (1966). *Language universals: With special reference to feature hierarchies*. Mouton.

[11] Gibson, E. (1998). Linguistic complexity: Locality of syntactic dependencies. *Cognition*, 68(1), 1–76.

[12] Universal Dependencies contributors. (2024). Universal Dependencies v2.17. Retrieved from https://universaldependencies.org/

[13] Dobrovoljc, K., & Erjavec, T. (2012). The universal dependencies treebank of spoken Slovenian. In *Proceedings of the Eighth International Conference on Language Resources and Evaluation (LREC 2012)* (pp. 2891–2898).

[14] Lacheret, A., Kahane, S., & Beliao, J. (2014). Rhapsodie: A prosodic-syntactic treebank for spoken French. In *Proceedings of the Ninth International Conference on Language Resources and Evaluation (LREC 2014)* (pp. 57–63).
</current_paper>

<reviewer_feedback>
Feedback from the paper reviewer this iteration.

- [MAJOR] (evidence) The core statistical test of the paper's central claim — the asymmetry index (Δ_adjunct − Δ_argument) — has a 95% bootstrap CI of [−0.003, +0.082], which includes zero. The supplementary artifact (art_fgB5OzuKO3N0, method_out.json) confirms: asymmetry_positive = false, verdict = 'partial'. The paper characterizes this as 'near-zero; the asymmetry is driven primarily by argument shortening rather than adjunct elongation,' which is accurate but understates the implication: the direct test of the asymmetry is non-significant at α=0.05. The abstract and contribution claim state 'We characterize a previously undocumented argument-adjunct asymmetry' and 'adjuncts are not minimized to the same degree,' which reads as confirmed when it is not yet formally so.
  Action: Add an explicit statement in the Abstract and Results that the asymmetry index CI barely includes zero (−0.003, +0.082) and the asymmetry is not statistically significant at α=0.05 in Slovenian alone. Reframe the claim as 'we observe a directionally consistent but not yet formally confirmed asymmetry in Slovenian, robustly directional across five analysis variants.' This honest framing, combined with the robustness section, still constitutes a publishable exploratory finding.
- [MAJOR] (methodology) The French analysis uses arc-level t-tests (p ≈ 10⁻³⁵, p ≈ 10⁻¹⁰) from the iteration 1 artifact (art_Gq_zeOShbi_1) that the paper explicitly rejected for Slovenian on grounds of arc non-independence. The method_out.json for the new sentence-level experiment confirms 'Only 1 language — cross-language t-test not applicable.' The paper presents the French arc-level statistics as cross-language corroboration of the new analysis, but this is methodologically inconsistent: if arc-level t-tests are invalid for inference (as the paper argues when correcting Slovenian), they are equally invalid for French. The reported French p-values are meaningless under the new methodology.
  Action: Either: (a) re-run the sentence-level bootstrap analysis for French using the fr_rhapsodie/fr_gsd data (the dataset artifact art_5YIzNa1Lrdf9 already contains French data), apply the same normalization and bootstrap procedure, and report French results on the same methodological footing as Slovenian; or (b) remove the French arc-level statistics from the paper entirely, acknowledge that French was not re-analyzed at the sentence level in this iteration, and limit cross-language claims accordingly. Option (a) is strongly preferred as it would provide genuine two-language evidence.
- [MAJOR] (evidence) The modifier category, described throughout the paper (Abstract, Introduction, Methods) as exhibiting 'near-zero register difference' and serving as 'a within-analysis control,' actually shows Cohen's d = +0.333 with 95% CI [+0.090, +0.138] in residual MDD entirely above zero. This is a small-to-medium positive effect, larger in standardized terms than the argument finding (d = −0.091). A control category with d = +0.333 is not a clean control — it is a third significant finding in the opposite direction from the argument result. The current framing seriously misrepresents what the modifier data show.
  Action: Remove all descriptions of modifiers as 'near-zero control' from the Abstract, Introduction, and contribution statements. Re-label modifiers as a 'comparison category showing unexpected lengthening in speech.' In the Discussion, provide equivalent analytical depth to the modifier finding: what syntactic and discourse-pragmatic mechanisms would cause nominal/adverbial modifiers to lengthen significantly in speech, and how does this interact with the argument-adjunct narrative? The three-way pattern (argument shorten, adjunct null, modifier lengthen) is actually more theoretically interesting than a simple two-category story.
- [MAJOR] (rigor) The power analysis table and the paper's summary statement are directly contradictory. The table shows: at n=20 languages, power = 0.526 (53%). The paper states 'Mixed-effects model estimates place the required sample at 12–20 verified pairs for adequate power.' But the conservative OLS model shown in the table does not reach 80% power at n=20, and the note in full_eval_out.json states explicitly: 'n_languages_required_80pct_power: null — Not reached at n=20 under conservative OLS model.' The paper's text implies 20 pairs suffices when the data show it does not. The caveat about the mixed-effects estimate being lower is buried in the artifacts.
  Action: Correct the text to match the table: state explicitly that under the conservative OLS model, 80% power is not reached even at n=20 languages, and power at n=20 is 53%. If the mixed-effects model gives a lower estimate (e.g., 12 pairs), present both estimates with explanation: 'Under a conservative OLS model, 80% power is not reached at n=20 (power=53%). A mixed-effects model assuming the observed between-language variance estimates approximately 12-20 pairs, but this estimate is itself uncertain given n=3 languages.' This is more honest and still supports the limitation message.
- [MINOR] (methodology) The sentence-length normalization filters from 17,686 total Slovenian sentences to 6,186 (35%) that have at least one arc in all three categories. This exclusion is not neutral: sentences without adjuncts (typically shorter, simpler sentences) are dropped. Since spoken sentences are typically shorter and simpler on average, the filtering may disproportionately exclude spoken sentences, potentially biasing the composition of the remaining 'spoken' subset toward more complex spoken sentences (those with enough syntactic elaboration to contain adjuncts). The 1,313 spoken vs 4,873 written ratio (21% spoken) from 6,121 total spoken sentences is lower than expected if filtering were balanced.
  Action: Report the filtering rates separately by modality: how many spoken (of 6,121) and written (of 13,435) sentences were retained, and whether this ratio differs systematically by modality. If filtering is modality-asymmetric, consider alternative analyses that do not require all-three-category presence per sentence (e.g., analyze each category separately using the full sentence set for that category), and compare results to the filtered analysis.
- [MINOR] (clarity) The paper introduces an 'asymmetry index' defined as Δ_adjunct − Δ_argument and reports a value of 0.041 with CI [−0.003, +0.082]. However, in the cross-language robustness section (Robustness Across Methodological Variants), the reported raw_mdd asymmetry interaction coefficient is 0.927 — presented as a 'large effect.' These two numbers (0.041 and 0.927) are not directly comparable but are presented side by side as if they measure the same thing. The 0.041 is in residualized MDD units after log normalization; the 0.927 is raw word-position distance without normalization. Readers will be confused about which number represents the core claim.
  Action: Clearly label in the Results and Robustness sections which metric each number corresponds to (residualized vs. raw, sentence-level vs. arc-level) and indicate which is the primary inferential measure. Prefer the sentence-level residualized asymmetry index (0.041) as the primary number throughout the paper, and present the raw_mdd result explicitly as an arc-level replication under no normalization — directionally consistent but not the primary analysis.
- [MINOR] (novelty) The Related Work section's treatment of Poiret & Liu (2023) [7] still does not fully engage with the degree to which their French findings overlap with the argument result here. The paper says they 'did not systematically test adjunct relations, normalize for sentence length rigorously, or investigate cross-linguistic patterns' — all true — but does not acknowledge that the positive argument result in French (shorter subject/object distances in speech) is largely a replication of their finding rather than a novel contribution. Since the French analysis in this paper uses arc-level data from the same Rhapsodie corpus, the argument shortening result for French adds little that Poiret & Liu did not already establish.
  Action: State clearly that the argument shortening finding in French corroborates Poiret & Liu's result for the same language and corpus, and that the novel contribution relative to their work is: (a) the adjunct elongation direction; (b) the modifier comparison category; (c) the sentence-level statistical design; and (d) the cross-linguistic scope (including Slovenian). This precise delineation of novelty strengthens the paper by showing exactly what is new rather than implicitly claiming broader novelty.
</reviewer_feedback>



<task>
IMPORTANT: Your ONLY output is the revised hypothesis text. Do NOT run code, produce artifacts,
fix bugs, or attempt to address the evidence yourself — the next iteration of the invention loop
will generate fresh artifacts based on your revised hypothesis. Reflect and rewrite; nothing else.

Do NOT generate a completely new hypothesis. Take the current hypothesis and REVISE it
to incorporate new evidence. Keep the core idea — refine, narrow, or strengthen it.

1. Does the evidence support the hypothesis? Narrow or broaden scope as needed.
2. Which claims now have strong evidence? Which are still unsupported?
3. Should the hypothesis become more specific based on what we've learned?
4. If reviewer feedback is provided, address the critiques directly.

STABILITY IS OK: If progress is good and evidence supports the current direction, keep the
hypothesis similar or identical. Only make substantive changes when evidence clearly calls for
them — e.g., contradictory results, fundamental reviewer critiques, or findings that refine scope.

You must also classify two kinds of edges in the research trace:

(A) The H↔H edge — how does this revised hypothesis relate to the previous one?
    Set `relation_type` (Moulines's structuralist typology) to one of:
    - "evolution": refining specialised claims, same conceptual frame
    - "embedding": previous hypothesis is now a special case of a broader frame
    - "replacement": rejecting the previous frame entirely (Kuhnian shift)
    Set `relation_rationale` to a brief justification (≤120 chars).

(B) The A↔A edges — for each artifact created THIS iteration, classify each of its
    `in_dependencies` (predecessor → dependent) using MultiCite's citation-function
    typology (Lauscher et al., NAACL 2022) — emit one entry in `artifact_relations`
    per (predecessor, dependent) pair. Predecessors are ALWAYS artifacts from EARLIER
    iterations — artifacts within one iteration run in parallel and cannot depend on
    each other, so never emit a relation between two same-iteration artifacts (it
    will be dropped):
    - "background": predecessor is treated as background context
    - "motivation": predecessor motivated this artifact's research
    - "uses": this artifact uses the predecessor's data, method, or output
    - "extends": this artifact extends the predecessor
    - "similarities": this artifact's results agree with the predecessor's
    - "differences": this artifact's results disagree with the predecessor's
    Each `relation_rationale` must be ≤120 characters.

Output the COMPLETE revised hypothesis (with the H↔H relation fields) AND the full
list of A↔A `artifact_relations` for this iteration's new artifacts.
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
    "ArtifactRelation": {
      "description": "One typed A\u2194A edge between a dependent artifact and one of its in_dependencies.\n\nMultiCite citation-function typology (Lauscher et al., NAACL 2022),\nreduced to 6 plain-English types.",
      "properties": {
        "from_id": {
          "description": "ID of the predecessor artifact (the one being depended on)",
          "title": "From Id",
          "type": "string"
        },
        "to_id": {
          "description": "ID of the dependent artifact (the new artifact this iteration)",
          "title": "To Id",
          "type": "string"
        },
        "relation_type": {
          "description": "MultiCite citation-function type for the predecessor\u2192dependent edge: 'background' \u2014 predecessor is treated as background context; 'motivation' \u2014 predecessor motivated this artifact's research; 'uses' \u2014 this artifact uses the predecessor's data, method, or output; 'extends' \u2014 this artifact extends the predecessor; 'similarities' \u2014 this artifact's results agree with the predecessor's; 'differences' \u2014 this artifact's results disagree with the predecessor's.",
          "enum": [
            "background",
            "motivation",
            "uses",
            "extends",
            "similarities",
            "differences"
          ],
          "title": "Relation Type",
          "type": "string"
        },
        "relation_rationale": {
          "description": "Brief rationale for this relation type (one short line, max 120 characters).",
          "maxLength": 120,
          "title": "Relation Rationale",
          "type": "string"
        }
      },
      "required": [
        "from_id",
        "to_id",
        "relation_type",
        "relation_rationale"
      ],
      "title": "ArtifactRelation",
      "type": "object"
    }
  },
  "description": "Revised hypothesis after reviewing iteration results.\n\nOutput matches the hypothesis dict structure so it can replace the\noriginal hypothesis in subsequent iterations.",
  "properties": {
    "title": {
      "description": "Revised hypothesis title (may be unchanged if still accurate)",
      "title": "Title",
      "type": "string"
    },
    "hypothesis": {
      "description": "Revised hypothesis statement \u2014 what we now believe based on evidence",
      "title": "Hypothesis",
      "type": "string"
    },
    "relation_rationale": {
      "description": "Brief rationale for the H\u2194H revision type (one short line, max 120 characters).",
      "maxLength": 120,
      "title": "Relation Rationale",
      "type": "string"
    },
    "confidence_delta": {
      "description": "How confidence changed: 'increased', 'decreased', or 'unchanged'",
      "title": "Confidence Delta",
      "type": "string"
    },
    "key_changes": {
      "description": "Bullet list of specific changes made to the hypothesis",
      "items": {
        "type": "string"
      },
      "title": "Key Changes",
      "type": "array"
    },
    "relation_type": {
      "description": "Moulines's structuralist typology of this hypothesis revision: 'evolution' \u2014 refining specialised claims while keeping the same conceptual frame; 'embedding' \u2014 the previous hypothesis is now a special case of a broader frame; 'replacement' \u2014 rejecting the previous frame entirely (incommensurable, Kuhnian revolution).",
      "enum": [
        "evolution",
        "embedding",
        "replacement"
      ],
      "title": "Relation Type",
      "type": "string"
    },
    "artifact_relations": {
      "description": "Typed A\u2194A edges for this iteration's new artifacts. Emit one entry per (predecessor \u2192 dependent) edge for every in_dependency on each artifact produced this iteration.",
      "items": {
        "$ref": "#/$defs/ArtifactRelation"
      },
      "title": "Artifact Relations",
      "type": "array"
    }
  },
  "required": [
    "title",
    "hypothesis",
    "relation_rationale",
    "confidence_delta",
    "key_changes",
    "relation_type"
  ],
  "title": "RevisedHypothesis",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-06-22 12:47:38 UTC

```
Direction: Computational Linguistics — Dependency Distance Minimization Across UD Treebanks. Something genuinely novel and groundbreaking that measures dependency-distance distributions across UD treebanks, investigates whether spoken language minimizes more than written, characterizes how typology interacts with the pattern, and identifies families that deviate. MUST use commul/universal_dependencies on HuggingFace.

Ambition: level 3 of 5 — phenomenological science: surface and rigorously characterize a new empirical regularity or anomaly in the data, even before a full theoretical explanation exists.

Reviewer: I am Kaja Dobrovoljc (JSI / University of Ljubljana). Calibrate from my existing papers. Cross-domain methods (information theory, mixed-effects models, sequence models) welcome — but keep them close to what I already know, not too far from my background.

Submission/Goal: a paper for ACL, EMNLP, or the Computational Linguistics journal. Audience: computational linguists and quantitative typologists. Tone: empirically rigorous, careful with linguistic detail, reproducible on public UD.
```

### [3] SYSTEM-USER prompt · 2026-06-22 12:48:32 UTC

```
<validation-feedback>
Attempt 1 failed validation.

Schema validation found 1 problem — fix ALL of them at once:
  - at `relation_rationale`: 'Same frame, narrowed from two-way to three-way pattern; asymmetry reframed as directional-not-confirmed; modifier lengthening elevated.' is too long (at most 120 characters, got 135)
Every required field must be present and every field type must match the schema.

Please use the Write tool to overwrite `.terminal_claude_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```

### [4] SYSTEM-USER prompt · 2026-06-22 12:48:36 UTC

```
[Your previous response had no visible output. Please continue and produce a user-visible response.]
```
