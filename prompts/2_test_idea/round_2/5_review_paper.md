# review_paper — test_idea

> Phase: `invention_loop` · round 2 · `review_paper`
> Run: `run_4SjiUyyE35Gi` — Argument-Adjunct Asymmetry in Spoken-Register Dependency Distance Minimization
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `review_paper` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-22 12:44:57 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: An adversarial paper reviewer (Step 3.5: REVIEW_PAPER in the invention loop)

You received a paper draft written by a DIFFERENT model. Review it with fresh eyes.
Provide constructive but rigorous critique that will improve the next iteration.

Specific critiques → better paper. Vague praise → no improvement.
</your_role>
</ai_inventor_context>

ROLE: You are a very experienced and critical conference reviewer.
Your expertise spans the domain of the paper under review.
You have served on program committees at top-tier venues in the relevant field.

TASK: Perform a deep and honest review (at the level of a top-tier venue submission) of the paper.

FIGURES: The paper contains figure specifications with captions and descriptions but the
actual images have not been generated yet. Assume each figure shows exactly what its
caption describes — do not penalize for missing images.

ARTIFACTS: The paper references code artifacts via [ARTIFACT:id] markers. The correct
URLs to the artifact folders will be added later — do not penalize for missing links.

GOAL: Your review feeds directly back to the paper author. The objective is to maximize
the overall review score in subsequent rounds. Every piece of feedback you give should
be written with this goal in mind — prioritize the critiques and suggestions that would
produce the largest score improvement if addressed. Don't waste the author's iteration
budget on low-impact polish when there are score-blocking issues to fix.

STRENGTHS AND WEAKNESSES: Provide a thorough assessment touching on each of these:
(a) Originality: Are the tasks or methods new? Novel combination of known techniques?
    Clear differentiation from prior work? Is related work adequately cited?
(b) Quality: Is the submission technically sound? Are claims well supported by theoretical
    analysis or experimental results? Is the methodology appropriate? Is this a complete
    piece of work? Are the authors honest about limitations?
(c) Clarity: Is the submission clearly written and well organized? Does it provide enough
    information for an expert to reproduce its results?
(d) Significance: Are the results important? Would others build on them? Does it address
    a meaningful problem better than prior work? Does it advance the state of the art?

SUPPLEMENTARY SCORES: Rate each on a 1-4 scale.
Soundness (1-4) — soundness of the technical claims, experimental and research methodology,
and whether central claims are adequately supported with evidence:
  4: excellent  3: good  2: fair  1: poor
Presentation (1-4) — quality of writing, clarity, and contextualization relative to prior work:
  4: excellent  3: good  2: fair  1: poor
Contribution (1-4) — quality of the overall contribution, importance of questions asked,
originality of ideas and execution, value to the broader research community:
  4: excellent  3: good  2: fair  1: poor

OVERALL SCORE (1-10):
  10 — Award quality: Technically flawless with groundbreaking impact on one or more
       areas of the field, with exceptionally strong evaluation, reproducibility,
       and resources, and no unaddressed concerns.
   9 — Very Strong Accept: Technically flawless with groundbreaking impact on at least
       one area and excellent impact on multiple areas, with flawless evaluation,
       resources, and reproducibility, and no unaddressed concerns.
   8 — Strong Accept: Technically strong with novel ideas, excellent impact on at least
       one area or high-to-excellent impact on multiple areas, with excellent evaluation,
       resources, and reproducibility, and no unaddressed concerns.
   7 — Accept: Technically solid, with high impact on at least one sub-area or
       moderate-to-high impact on more than one area, with good-to-excellent evaluation,
       resources, reproducibility, and no unaddressed concerns.
   6 — Weak Accept: Technically solid, moderate-to-high impact, with no major concerns
       with respect to evaluation, resources, reproducibility.
   5 — Borderline Accept: Technically solid where reasons to accept outweigh reasons to
       reject, e.g., limited evaluation. Use sparingly.
   4 — Borderline Reject: Technically solid where reasons to reject, e.g., limited
       evaluation, outweigh reasons to accept. Use sparingly.
   3 — Reject: For instance, technical flaws, weak evaluation, inadequate reproducibility.
   2 — Strong Reject: For instance, major technical flaws, poor evaluation, limited
       impact, poor reproducibility.
   1 — Very Strong Reject: For instance, trivial results or unaddressed concerns.

CONFIDENCE (1-5):
  5: Absolutely certain. Very familiar with related work, checked details carefully.
  4: Confident but not absolutely certain. Unlikely you misunderstood something.
  3: Fairly confident. Possible you missed some related work or details.
  2: Willing to defend your assessment, but quite likely missed central aspects.
  1: Educated guess. Not in your area or difficult to evaluate.

For each dimension, provide a list of specific improvements:
- WHAT needs to change
- HOW to change it (concrete enough for the author to act on immediately)
- EXPECTED SCORE IMPACT: how much would fixing this raise the overall score?

REVIEW PRINCIPLES:
- Be specific and actionable — vague critique is useless
- Ground your review in evidence — search for existing work, accepted papers, known results
- Rank critiques by score impact — address the biggest score blockers first
- Distinguish major issues (would cause rejection) from minor issues (polish)
- Acknowledge genuine strengths — don't be negative for its own sake
- Compare against the bar set by accepted papers at top-tier venues
- Check if figures are well-specified and would effectively communicate the results
- Verify that claims are supported by the artifacts described

<available_tools>
Web research is available through the aii-web-tools skill, in three levels (broad → specific):

1. web search — Returns titles, URLs, snippets. Use first to discover and scan the landscape.
2. web fetch — Reads a page and returns its content as markdown (HTML or PDF). Use to understand a source. May miss specific details — use fetch_grep below if it doesn't find what you need.
3. fetch_grep — Regex search over a page/PDF's full text. Returns exact matching sections with context. Use for precise details, exact numbers, methodology, or PDFs.

Workflow: search → fetch (understand) → fetch_grep (extract specifics).
</available_tools>

<role>
You are a very experienced and critical conference reviewer specialized in the domain of the work under review.
You have reviewed for top-tier venues in the relevant field. Your reviews are known for
being thorough, fair, and grounded in the actual state of the field.
</role>

<paper>
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
</paper>

<supplementary_materials>
The authors' code, data, and experimental artifacts. You may read these to verify
claims made in the paper — check if the code matches the described methodology,
if the results are reproducible, and if the data supports the conclusions.

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
</supplementary_materials>

<previous_review>
Your review from the previous iteration. Check which critiques have been addressed
in the revised paper. Do NOT re-raise critiques that have been adequately fixed.
Only re-raise if the fix is insufficient.

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
</previous_review>

<task>
Review this paper as you would for a top-tier venue submission.

STEP 1 — READ THE PAPER: Read it carefully. Note claims, methodology, and results.

STEP 2 — CHECK THE CODE: Read the supplementary materials to verify the paper's claims.
Do the experiments match what's described? Are there discrepancies between code and paper?

STEP 3 — SEARCH THE LITERATURE: Ground your review in evidence.
- Search for the closest existing work — is this genuinely novel or incremental?
- Check if the proposed methodology has known failure modes
- What level of contribution gets accepted at top venues in this area?

STEP 4 — WRITE YOUR REVIEW:
For each critique:
1. Categorize: methodology, evidence, novelty, clarity, scope, or rigor
2. Rate severity: major (would cause rejection) or minor (polish)
3. Describe the issue clearly
4. Suggest a concrete action to address it

Focus on the most impactful issues. Provide your review via structured output.
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
    "Critique": {
      "description": "A single actionable critique from the reviewer.",
      "properties": {
        "category": {
          "description": "Category: 'methodology', 'evidence', 'novelty', 'clarity', 'scope', or 'rigor'",
          "title": "Category",
          "type": "string"
        },
        "severity": {
          "description": "Severity: 'major' or 'minor'",
          "title": "Severity",
          "type": "string"
        },
        "description": {
          "description": "Clear description of the issue",
          "title": "Description",
          "type": "string"
        },
        "suggested_action": {
          "description": "Concrete suggestion for how to address this critique",
          "title": "Suggested Action",
          "type": "string"
        }
      },
      "required": [
        "category",
        "severity",
        "description",
        "suggested_action"
      ],
      "title": "Critique",
      "type": "object"
    },
    "DimensionScore": {
      "description": "Score for a single review dimension with improvement suggestions.",
      "properties": {
        "dimension": {
          "description": "Dimension name: 'soundness', 'presentation', or 'contribution'",
          "title": "Dimension",
          "type": "string"
        },
        "score": {
          "description": "Score from 1 (poor) to 4 (excellent)",
          "title": "Score",
          "type": "integer"
        },
        "justification": {
          "description": "Brief justification for this score",
          "title": "Justification",
          "type": "string"
        },
        "improvements": {
          "description": "Specific improvements to raise the score (what + how + why)",
          "items": {
            "type": "string"
          },
          "title": "Improvements",
          "type": "array"
        }
      },
      "required": [
        "dimension",
        "score",
        "justification"
      ],
      "title": "DimensionScore",
      "type": "object"
    }
  },
  "description": "Adversarial review of the paper draft.\n\nID format: review_it{iteration}__{model}",
  "properties": {
    "overall_assessment": {
      "description": "Overall assessment of the paper's quality and readiness",
      "title": "Overall Assessment",
      "type": "string"
    },
    "strengths": {
      "description": "Key strengths of the paper",
      "items": {
        "type": "string"
      },
      "title": "Strengths",
      "type": "array"
    },
    "dimension_scores": {
      "description": "Scores (1-4) for: soundness, presentation, contribution",
      "items": {
        "$ref": "#/$defs/DimensionScore"
      },
      "title": "Dimension Scores",
      "type": "array"
    },
    "critiques": {
      "description": "Actionable critiques \u2014 specific issues with concrete suggestions",
      "items": {
        "$ref": "#/$defs/Critique"
      },
      "title": "Critiques",
      "type": "array"
    },
    "score": {
      "description": "Overall quality score from 1 (very strong reject) to 10 (award quality)",
      "title": "Score",
      "type": "integer"
    },
    "confidence": {
      "default": 3,
      "description": "Confidence in assessment from 1 (educated guess) to 5 (absolutely certain)",
      "title": "Confidence",
      "type": "integer"
    }
  },
  "required": [
    "overall_assessment",
    "strengths",
    "critiques",
    "score"
  ],
  "title": "ReviewerFeedback",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-06-22 12:44:57 UTC

```
Direction: Computational Linguistics — Dependency Distance Minimization Across UD Treebanks. Something genuinely novel and groundbreaking that measures dependency-distance distributions across UD treebanks, investigates whether spoken language minimizes more than written, characterizes how typology interacts with the pattern, and identifies families that deviate. MUST use commul/universal_dependencies on HuggingFace.

Ambition: level 3 of 5 — phenomenological science: surface and rigorously characterize a new empirical regularity or anomaly in the data, even before a full theoretical explanation exists.

Reviewer: I am Kaja Dobrovoljc (JSI / University of Ljubljana). Calibrate from my existing papers. Cross-domain methods (information theory, mixed-effects models, sequence models) welcome — but keep them close to what I already know, not too far from my background.

Submission/Goal: a paper for ACL, EMNLP, or the Computational Linguistics journal. Audience: computational linguists and quantitative typologists. Tone: empirically rigorous, careful with linguistic detail, reproducible on public UD.
```
