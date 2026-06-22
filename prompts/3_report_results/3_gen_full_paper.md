# gen_full_paper — report_results

> Phase: `gen_paper_repo` · `gen_full_paper`
> Run: `run_4SjiUyyE35Gi` — Argument-Adjunct Asymmetry in Spoken-Register Dependency Distance Minimization
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_full_paper` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-22 13:17:30 UTC

````
<research_methodology>
Write like an experienced academic. Reviewers judge both the science and the writing.

- Claims must be proportional to evidence. Choose verbs carefully — "demonstrate," "observe," and "hypothesize" mean different things.
- Every result needs: what was measured, on what data, the numbers, and what they mean.
- Methodology must be specific enough to reproduce. Related work must be organized by theme, not a literature dump.
- State limitations honestly. Avoid both overclaiming and excessive hedging.
</research_methodology>

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
Your workspace: `/ai-inventor/aii_data/runs/run_4SjiUyyE35Gi/4_gen_paper_repo/_4_assemble_paper/paper/workspace`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_4SjiUyyE35Gi/4_gen_paper_repo/_4_assemble_paper/paper/workspace/`:
GOOD: `/ai-inventor/aii_data/runs/run_4SjiUyyE35Gi/4_gen_paper_repo/_4_assemble_paper/paper/workspace/file.py`, `/ai-inventor/aii_data/runs/run_4SjiUyyE35Gi/4_gen_paper_repo/_4_assemble_paper/paper/workspace/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>

<task>
Create a publication-ready top-conference LaTeX paper with BibTeX from <paper_text> and <available_figures>, compile to PDF.
</task>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<paper_text>
title: Argument-Adjunct Asymmetry in Spoken-Register Dependency Distance Minimization
abstract: >-
  The principle that human languages minimize dependency distance—the linear distance between syntactically related words—has
  been established as a cross-linguistic universal. Yet the aggregate reduction in mean dependency distance (MDD) observed
  in spoken versus written registers remains unexplained. We demonstrate that this reduction masks a systematic asymmetry:
  argument relations (subject, object, clausal complements) are significantly shorter in spoken than written language, while
  adjunct relations (adverbial clauses, relative clauses) show no reduction and are on average longer in speech. This pattern
  is robust across sentence-level bootstrap resampling and multiple normalization schemes, and holds in two verified spoken-written
  Universal Dependencies treebank pairs (Slovenian and French). The asymmetry aligns with incremental sentence processing
  theory: arguments must be integrated immediately for semantic interpretation and face selection-based pressure for proximity,
  while adjuncts are optional and can be appended after main-clause completion, permitting longer distances. A cross-linguistic
  audit of 14 UD treebanks reveals that most labeled 'spoken' corpora are actually written genres (news, learner text, journalism),
  sharply limiting current claims of cross-linguistic generalization. The argument-adjunct asymmetry represents a previously
  undocumented refinement to the theory of dependency distance minimization, refining our understanding of how cognitive pressures
  of real-time language production shape syntactic structure. We provide an honest assessment of statistical power: replication
  across 12–20 verified spoken-written pairs is required for robust cross-linguistic inference.
paper_text: "# Introduction\n\nThe human language faculty exhibits a remarkable preference for linear word orders that minimize\
  \ the distance between syntactically dependent words. This dependency distance minimization (DDM) principle has been demonstrated\
  \ as a quantitative universal across 37 languages using large parsed corpora [1], holds across diverse language families\
  \ [2], and correlates with processing difficulty in psycholinguistic tasks [3]. The universality is striking: despite vast\
  \ differences in morphology, phonology, and historical origin, languages organize their words according to a common cognitive\
  \ pressure to keep related elements close.\n\nYet a coarser empirical observation—one that has received little theoretical\
  \ attention—shadows this universal: spoken language exhibits systematically shorter mean dependency distances than written\
  \ language [3, 4]. The immediate interpretation is intuitive: speakers minimize distances more aggressively than writers,\
  \ operating under real-time production constraints. However, this interpretation assumes *uniform* minimization across all\
  \ dependency relations. If minimization operates selectively—intensifying on certain relation types while relaxing on others—then\
  \ the aggregate reduction conflates opposing pressures and misattributes the phenomenon's locus.\n\nThis paper demonstrates\
  \ that the spoken-language reduction in MDD is not uniform but reflects a systematic **argument-adjunct asymmetry**. Core\
  \ grammatical relations selected by a predicate (subjects, objects, clausal complements)—hereafter *arguments*—are significantly\
  \ shorter in speech than writing, consistent with incremental processing pressure: these elements must be integrated immediately\
  \ for semantic interpretation. By contrast, optional modifiers and peripheral dependents (adverbial clauses, relative clauses)—hereafter\
  \ *adjuncts*—show no reduction and paradoxically lengthen in spoken language. This pattern is consistent with a **right-adjunction\
  \ strategy**: speakers append adjuncts after the main clause is complete, maximizing locality constraints for arguments\
  \ while tolerating distance for optional elements. A third category, modifiers (nominal and adverbial modifiers of nouns\
  \ and verbs), serves as a within-analysis control and exhibits near-zero register difference, supporting the specificity\
  \ of the argument effect.\n\nWe test this hypothesis using two verified spoken-written Universal Dependencies (UD) treebank\
  \ pairs: Slovenian (sl_sst/sl_ssj, 6,121 spoken sentences; Dobrovoljc et al., 2012) and French (fr_rhapsodie/fr_gsd, 6,032\
  \ spoken sentences; Lacheret et al., 2014). Both corpora represent transcribed natural dialogue in the UD framework, enabling\
  \ precise computation of dependency distances with controlled annotation schemes \\footnote{Code: \\url{https://github.com/AMGrobelnik/ai-invention-033e16-argument-adjunct-asymmetry-in-spoken-reg/tree/main/round-2/dataset-1}}.\
  \ We apply sentence-level analysis with bootstrap confidence intervals and multiple normalization procedures, removing sentence-length\
  \ confounds while preserving register differences. Results confirm argument shortening in both languages (Slovenian: Δ =\
  \ −0.051, 95% CI [−0.082, −0.019]; French: raw Δ = −0.634, p < 10⁻³⁵) and adjunct non-reduction or elongation (Slovenian:\
  \ Δ = −0.010, CI [−0.038, 0.017]; French: Δ = +0.143, p = 0.470) \\footnote{Code: \\url{https://github.com/AMGrobelnik/ai-invention-033e16-argument-adjunct-asymmetry-in-spoken-reg/tree/main/round-2/experiment-1}}.\n\
  \nA critical contribution of this work is methodological transparency: we audited 14 UD treebanks claiming to represent\
  \ 'spoken' language and found that most are actually written genres (newspapers, journalism, learner text, legal documents).\
  \ Only three treebanks qualify as verified spoken corpora: Slovenian (sl_sst), French (fr_rhapsodie), and Italian (it_parlato,\
  \ not yet on HuggingFace). This audit undermines the credibility of claims that the asymmetry generalizes across 14+ languages;\
  \ prior iteration's null results on the 14-language extension are attributable to misidentified treebanks, not to genuine\
  \ cross-linguistic failure \\footnote{Code: \\url{https://github.com/AMGrobelnik/ai-invention-033e16-argument-adjunct-asymmetry-in-spoken-reg/tree/main/round-2/evaluation-1}}.\
  \ A Monte Carlo power analysis reveals that 80% statistical power requires 12–20 verified spoken-written pairs, far exceeding\
  \ the current supply of high-quality UD resources. Thus, the argument-adjunct asymmetry is a well-supported phenomenon in\
  \ Slovenian and French, an exploratory (not yet confirmed) pattern requiring expansion to additional languages.\n\n## Contributions\n\
  \nThis paper makes four contributions:\n\n1. **Phenomena**: We characterize a previously undocumented argument-adjunct asymmetry\
  \ in register-specific dependency distance, showing that the aggregate spoken-language reduction in DDM is not uniform but\
  \ directionally opposite for arguments versus adjuncts and modifiers .\n\n2. **Mechanism**: We ground the asymmetry in incremental\
  \ processing theory and right-adjunction syntax, providing a principled explanation for why arguments shorten but adjuncts\
  \ resist or lengthen in speech.\n\n3. **Methodological rigor**: We demonstrate that most UD treebanks labeled 'spoken' are\
  \ misidentified written genres, and we establish statistical power requirements (12–20 verified pairs) for robust cross-linguistic\
  \ claims .\n\n4. **Honest framing**: We present evidence of the asymmetry in two verified spoken-written language pairs\
  \ as an exploratory finding requiring replication, rather than overstating generality based on flawed cross-linguistic data.\n\
  \n# Related Work\n\n## Dependency Distance Minimization as Universal\n\nDependency distance minimization has become one\
  \ of the most-replicated quantitative universals in linguistics. Futrell, Mahowald, and Gibson [1] tested DDM across 37\
  \ typologically diverse languages using large parsed corpora, finding that all languages organize words such that actual\
  \ dependency lengths are substantially shorter than conservative random baselines. They grounded DDM in working memory constraints:\
  \ holding unresolved syntactic expectations in memory incurs a cost proportional to how long the parser must wait to integrate\
  \ dependent elements. Ferrer-i-Cancho and colleagues [2] extended this line by introducing an optimality score (eta) measuring\
  \ how close each language's word order comes to the theoretical minimum dependency length given its syntactic structure;\
  \ approximately half of 93 languages achieve 70%+ optimization, suggesting DDM is not merely a tendency but an organizational\
  \ principle enforced through grammar.\n\nHowever, these foundational studies aggregate over all dependency relations without\
  \ stratification. The question of whether all relation types equally contribute to the universal remains unanswered—a gap\
  \ this paper addresses.\n\n## Register Variation and Spoken Language Syntax\n\nRegister-specific syntactic variation has\
  \ been documented across phonology, morphology, and lexical richness [5, 6], but systematic analysis of dependency distance\
  \ by register and relation type is sparse. Liu [3] observed that Japanese spoken dialogue exhibits lower mean dependency\
  \ distance than written news but did not stratify by relation type or control for sentence length. Dobrovoljc [4] recently\
  \ compared spoken and written UD treebanks for English and Slovenian using structural inventory methods (delexicalized dependency\
  \ subtree shapes), finding that speech contains fewer diverse syntactic structures than writing; this result aligns with\
  \ intuitions about speech simplification but does not directly measure dependency distance or examine register effects on\
  \ specific relation types. Poiret and Liu [7], in cross-linguistic work on French, compared dependency distances for subject\
  \ and oblique relations in spoken versus written corpora and found arguments are shorter in speech—consistent with our argument\
  \ findings—but they did not systematically test adjunct relations, normalize for sentence length rigorously, or investigate\
  \ cross-linguistic patterns.\n\nThe novelty of this paper lies in the adjunct dimension and the modifier control. Argument\
  \ shortening in spoken language has been suggested before [7]; what is new is the demonstration that adjuncts are not minimized\
  \ equally (and are actually elongated in some contexts), and that nominal/adverbial modifiers serve as a control category\
  \ showing near-zero register effect.\n\n## Morphology, Word Order, and Typology\n\nA substantial body of work connects morphological\
  \ marking to syntactic organization. Sinnemäki and Haakana [8] studied the interaction of head and dependent marking with\
  \ dependency length in possessive noun phrases, finding an inverse relationship between marking types but no significant\
  \ cross-linguistic correlation between dependency length and morphological complexity alone. This suggests morphological\
  \ and syntactic complexity are partially independent dimensions. The hypothesis that case morphology liberates word order\
  \ flexibility for adjuncts is implicit in much typological work [9, 10] but has not been directly tested against register-specific\
  \ dependency distance variation. The current paper reports a Pearson correlation of r = −0.471 (p = 0.688) between case\
  \ richness and adjunct elongation across our three core languages, a null result that contradicts the initial hypothesis;\
  \ this null is preserved in the revised framing as an open empirical question pending a larger verified sample.\n\n## Incremental\
  \ Processing and Working Memory\n\nIncremental processing theory, developed by Gibson [11] and advanced by expectation-based\
  \ accounts (Levy 2008), proposes that language comprehension unfolds in real time, with continuous integration of new words\
  \ into an emerging structure. Storage cost (maintaining unresolved dependencies) and integration cost (linking distant dependents\
  \ to heads) both penalize long-distance dependencies. Critically, incremental pressure should fall more heavily on *obligatory*\
  \ elements: a listener hearing \"The dog ... the cat\" cannot yet form a complete proposition and must hold the incomplete\
  \ dependency in working memory. Adjuncts, by contrast, are semantically optional and can be integrated after core elements\
  \ are complete. This asymmetry in incremental pressure maps directly onto the argument-adjunct distinction we observe.\n\
  \n# Methods\n\n## Data and Treebank Selection\n\nWe extracted dependency arcs from two verified spoken-written Universal\
  \ Dependencies (UD v2.17, HuggingFace commul/universal_dependencies [12]) treebank pairs:\n\n**Slovenian**: sl_sst (spoken,\
  \ Slovenian Spoken Treebank, 6,121 sentences) vs. sl_ssj (written, Slovenian Marked Up Corpus, 13,435 sentences). The sl_sst\
  \ treebank comprises transcribed natural spoken dialogue from the GOS corpus. The sl_ssj treebank contains news text and\
  \ fiction. Both use consistent UD annotation [13].\n\n**French**: fr_rhapsodie (spoken, 6,032 sentences) vs. fr_gsd (written,\
  \ 16,341 sentences). The fr_rhapsodie treebank contains transcribed natural dialogue from French radio broadcasts. The fr_gsd\
  \ treebank comprises web text and news [14].\n\nThese pairs were selected because: (1) both represent transcribed natural\
  \ speech (not elicited, learner, or written approximations); (2) each language offers clear spoken-written annotation in\
  \ UD; (3) Slovenian and French represent different language families and morphological profiles (Slovenian is morphologically\
  \ rich with case marking; French is morphologically reduced with positional constraints); (4) both pairs use the same UD\
  \ annotation scheme, enabling controlled comparison.\n\n## Treebank Audit\n\nIn iteration 1, we reported results on 14 language\
  \ pairs. A post-hoc audit of these treebanks against their official UD documentation (checking source corpus metadata and\
  \ linguistic description) revealed that most 'spoken' treebanks are misidentified written genres:\n\n- **Verified spoken-written\
  \ pairs** (3 total): sl_sst/sl_ssj (Slovenian), fr_rhapsodie/fr_gsd (French), it_parlato/it_isdt (Italian; not yet on HuggingFace\
  \ as of June 2026)\n- **Learner-confounded** (1): en_eslspok/en_ewt (English; en_eslspok is non-native ESL learner speech,\
  \ confounding register with proficiency)\n- **Written-genre pairs or partial** (5+): de_hdt (newspaper), ru_syntagrus (journalistic),\
  \ ar_padt (newswire), zh_cfl (learner compositions), it_vit (legal/administrative text), pt_bosque (newspaper), es_ancora\
  \ (newspaper) \n\nThis audit means claims of 14-language generalization in iteration 1 were based on false positives: 11\
  \ of the 14 treebanks do not represent genuine spoken-versus-written comparisons. The null results on the 14-language extension\
  \ (pooled p = 0.810 for arguments, p = 0.928 for adjuncts) are attributable to this fundamental misidentification, not to\
  \ genuine cross-linguistic failure of the hypothesis.\n\n## Dependency Arc Classification\n\nFor each sentence, we extracted\
  \ all dependency arcs (head-dependent pairs) and classified each arc's UD deprel label into one of three categories:\n\n\
  - **Arguments** (core obligatory participants): nsubj, obj, iobj, ccomp, xcomp, csubj\n- **Adjuncts** (optional peripheral\
  \ modifiers): advcl, acl, acl:relcl\n- **Modifiers** (control category): nmod, amod, advmod, and other nominal/adverbial/adjectival\
  \ modifications\n\nPunctuation tokens and root arcs were excluded. We computed mean dependency distance (MDD) for each arc\
  \ as |head_position − dependent_position| in 1-indexed token positions.\n\n## Sentence-Length Normalization\n\nSpoken sentences\
  \ are typically shorter than written sentences on average, mechanically producing shorter distances. To isolate register\
  \ effects, we performed OLS residualization: for each (language, modality, category) stratum, we fit the model log(MDD)\
  \ ∼ log(sentence_length) using pooled spoken+written data, then retained residuals. This procedure removes the linear relationship\
  \ between sentence length and distance while preserving the spoken-written mean difference in residuals. All statistical\
  \ tests were performed on residualized MDD.\n\n## Statistical Analysis\n\nUnlike iteration 1, which treated 922,399 individual\
  \ arcs as i.i.d. observations (violating independence assumptions and massively deflating p-values), we perform sentence-level\
  \ analysis:\n\n1. **Sentence-level aggregation**: For each sentence and category, we compute mean MDD; sentences without\
  \ at least one arc in a given category are excluded (retaining 6,186/17,686 Slovenian sentences with all three categories).\
  \ This reduces the effective sample size to sentence level, respecting the clustered structure of the data.\n\n2. **Bootstrap\
  \ resampling**: We perform 1,000 unpaired bootstrap resamples (B=1000, seed=42) of the mean residual MDD difference (spoken\
  \ − written) per category, computing 95% confidence intervals and Cohen's d effect sizes .\n\n3. **Per-language inference**:\
  \ With only 2 languages, we compute the asymmetry index (Δ_adjunct − Δ_argument) separately for each language and report\
  \ results with bootstrap confidence intervals. We acknowledge that formal cross-linguistic hypothesis testing (e.g., one-sample\
  \ t-test across languages with df=2) is severely underpowered .\n\n4. **Robustness**: We verified the asymmetry across five\
  \ methodological variants: (i) residualized OLS (iteration 1 baseline), (ii) raw MDD without normalization, (iii) OLS with\
  \ log(sent_len) as covariate, (iv) Huber robust regression, (v) 1% outlier trimming. All five variants confirm the asymmetry\
  \ direction .\n\n# Results\n\n## Main Finding: Argument-Adjunct Asymmetry in Slovenian\n\n[FIGURE:fig1]\n\nSentence-level\
  \ analysis (n=1,313 spoken, n=4,873 written sentences in Slovenian) after length normalization and bootstrap resampling\
  \ reveals a clear asymmetry:\n\n**Arguments** (n_spoken_arcs = 16,820; n_written = 105,125):\n- Mean residual MDD (spoken\
  \ − written): Δ = −0.051 words\n- 95% Bootstrap CI: [−0.082, −0.019]\n- Cohen's d: −0.091 (small effect)\n- **Interpretation**:\
  \ Significantly shorter in spoken (CI excludes zero)\n\n**Adjuncts** (n_spoken = 2,972; n_written = 24,674):\n- Mean residual\
  \ MDD: Δ = −0.010 words  \n- 95% Bootstrap CI: [−0.038, +0.017]\n- Cohen's d: −0.022 (negligible)\n- **Interpretation**:\
  \ No significant difference (CI includes zero); asymmetry confirmed: adjuncts do not minimize as arguments do\n\n**Modifiers**\
  \ (control, n_spoken = 21,087; n_written = 156,218):\n- Mean residual MDD: Δ = +0.114 words\n- 95% Bootstrap CI: [+0.090,\
  \ +0.138]\n- Cohen's d: +0.333 (small-to-medium)\n- **Interpretation**: Paradoxically longer in spoken (unexpected for a\
  \ within-analysis control; see Discussion)\n\n**Asymmetry Index** (Δ_adjunct − Δ_argument):\n- Value: +0.041\n- 95% Bootstrap\
  \ CI: [−0.003, +0.082]\n- **Interpretation**: Near-zero; the asymmetry is driven primarily by argument shortening rather\
  \ than adjunct elongation\n\nThese results hold across all robustness variants , confirming directional stability.\n\n##\
  \ Cross-Language Comparison: Slovenian vs. French (Raw Data)\n\n[FIGURE:fig2]\n\nWe conducted a preliminary analysis of\
  \ French data (6,032 spoken sentences; from iteration 1 artifacts) using raw MDD (without residualization, for comparability)\
  \ to assess generality across the two core languages \\footnote{Code: \\url{https://github.com/AMGrobelnik/ai-invention-033e16-argument-adjunct-asymmetry-in-spoken-reg/tree/main/round-1/experiment-1}}:\n\
  \n**French raw MDD comparison**:\n- **Arguments**: spoken 2.718 vs. written 3.042, Δ = −0.324 (t-test p ≈ 10⁻³⁵)\n- **Adjuncts**:\
  \ spoken 6.578 vs. written 5.975, Δ = +0.603 (t-test p ≈ 10⁻¹⁰)\n- **Asymmetry confirmed**: Arguments minimize (as in Slovenian),\
  \ adjuncts elongate (opposite direction from Slovenian residualized result but consistent with raw direction)\n\nThe raw-data\
  \ French results show the asymmetry is directionally consistent across languages, though effect magnitudes differ (Slovenian\
  \ has smaller effects post-residualization; French effects are larger pre-normalization). This suggests the phenomenon is\
  \ robust but cross-language effect homogeneity cannot be assumed.\n\n## Robustness Across Methodological Variants\n\n[FIGURE:fig3]\n\
  \nWe tested five distinct analysis pipelines to ensure the asymmetry is not an artifact of any single methodological choice\
  \ :\n\n1. **Residualized OLS** (iteration 1 baseline): interaction coef = +0.0125, p = 0.281; asymmetry direction confirmed\n\
  2. **Raw MDD (no normalization)**: arg Δ = −0.324 (p ≈ 10⁻³⁸), adj Δ = +0.603 (p ≈ 10⁻¹⁰); robust, large effects\n3. **OLS\
  \ length covariate**: arg coefficient = +0.083 (written > spoken), adj coef = −0.153 (spoken > written); confirmed\n4. **Huber\
  \ robust regression**: arg Δ = +0.085, adj Δ = −0.109; confirmed despite outlier handling\n5. **1% outlier trimming**: arg\
  \ Δ = −0.299, adj Δ = +0.495; confirmed after removing extreme arcs\n\n**Robustness confirmation rate: 5/5 variants (100%)**\
  \ confirm asymmetry direction. This demonstrates the finding is not sensitive to preprocessing or normalization choices.\n\
  \n## Statistical Power and Cross-Linguistic Generalization\n\nA Monte Carlo power analysis (n_sims = 3,000 per n_languages\
  \ scenario) reveals how many verified spoken-written language pairs are required for 80% power under a mixed-effects model\
  \ :\n\n| Number of Language Pairs | Statistical Power | Reject Null Count |\n|---|---|---|\n| 3 (current) | 0.109 (11%)\
  \ | 328/3000 |\n| 4 | 0.130 (13%) | 390/3000 |\n| 6 | 0.179 (18%) | 537/3000 |\n| 8 | 0.249 (25%) | 747/3000 |\n| 12 | 0.363\
  \ (36%) | 1090/3000 |\n| 20 | 0.526 (53%) | 1578/3000 |\n\nNote: At n=20, power remains only 53%, well below the conventional\
  \ 80% threshold. Mixed-effects model estimates place the required sample at 12–20 verified pairs for adequate power. Since\
  \ only 3 verified spoken-written UD pairs exist (and one is not yet on HuggingFace), cross-linguistic generalization of\
  \ the asymmetry is a priority for future work, not a settled claim.\n\n# Discussion\n\n## Interpretation: Incremental Processing\
  \ and Right-Adjunction\n\nThe argument-adjunct asymmetry aligns well with incremental sentence processing theory. In real-time\
  \ production, speakers begin planning and uttering the main clause (predicate + core arguments) before fully planning adjuncts.\
  \ Arguments must be integrated immediately: a listener hearing \"The dog ... the cat\" cannot yet form a complete proposition\
  \ and must hold the unresolved dependency in working memory. A speaker under time pressure thus has incentive to place arguments\
  \ close to their heads, minimizing storage cost. Adjuncts, by contrast, can be semantically and structurally integrated\
  \ after the main clause is complete: \"The dog chased the cat\" is a complete, interpretable utterance, and appending an\
  \ adjunct (\"in the park\") adds optional information without requiring pre-integration planning.\n\nThis mechanism predicts\
  \ right-adjunction in speech: adverbial clauses, relative clauses, and postverbal nominal modifiers should be systematically\
  \ appended after the main predicate is satisfied, creating longer dependencies. The French raw data support this (adjuncts\
  \ +0.603 words longer in spoken); the Slovenian residualized data show smaller effect magnitudes but directional consistency.\n\
  \n## The Modifier Control: Why Do Modifiers Lengthen in Speech?\n\nThe modifier result (Δ = +0.114, CI [+0.090, +0.138]\
  \ in Slovenian) is unexpected and warrants discussion. We hypothesized modifiers would show near-zero register difference\
  \ (a control category), but instead they lengthen modestly in spoken language. Two explanations merit consideration:\n\n\
  1. **Noun phrase simplification in speech**: Spoken language may deploy fewer embedded nominal phrases but construct them\
  \ differently. When present, post-nominal modifiers (especially relative clauses and complex appositives) may be appended\
  \ to noun phrases as afterthoughts, parallel to the adjunction strategy.\n\n2. **Sentence structure differences**: Spoken\
  \ language may have shorter sentences overall, causing sentence-level length normalization to incompletely remove structure-related\
  \ confounds. The residualization procedure assumes a linear log-log relationship; non-linear dependencies might not be fully\
  \ captured.\n\nWe report this finding as observed but acknowledge it complicates the narrative of a clean argument-adjunct\
  \ control. The core finding—argument shortening combined with adjunct non-reduction—remains robust across all analyses.\n\
  \n## Why Morphological Case Richness Does Not Predict Cross-Linguistic Variance\n\nOur initial hypothesis predicted that\
  \ case-marking languages would show larger adjunct elongation because case morphology decouples grammatical function from\
  \ word order, permitting freer adjunct placement. The correlation across three languages is r = −0.471 (p = 0.688), a clear\
  \ null result contradicting this prediction.\n\nWe propose three explanations:\n\n1. **Word Order Rigidity is Multidimensional**:\
  \ Case morphology is one factor liberating word order, but sentence-type-specific constraints (verb-second in embedded clauses,\
  \ subject-verb-object dominance in some Romance languages) override case-marking patterns. A language with rich case marking\
  \ but strict syntactic constraints may show limited adjunct freedom.\n\n2. **Prosodic Phrasing Dominates Morphology**: Spoken\
  \ language is organized into intonational phrases. Adjuncts may be placed at prosodic phrase boundaries, creating distance\
  \ not because of case marking but due to prosodic constituency. This hypothesis requires prosodic annotation (unavailable\
  \ in standard UD) to test rigorously.\n\n3. **Interaction Dynamics Override Morphology**: Spoken language is interactive,\
  \ with frequent turn-taking and repair. These discourse-pragmatic factors may constrain adjunct placement more strongly\
  \ than morphological typology.\n\nThe null morphological correlation underscores that the argument-adjunct asymmetry is\
  \ not simply a function of gross typological features but depends on more fine-grained structural and pragmatic properties.\n\
  \n## Limitations\n\n1. **Limited Verified Spoken Treebanks**: Only 2 verified spoken-written UD pairs are currently available\
  \ on HuggingFace (Slovenian and French), limiting cross-linguistic inference. Our power analysis shows 12–20 pairs are needed\
  \ for robust hypothesis testing. Until more genuine spoken corpora are annotated in UD, the asymmetry remains an exploratory\
  \ finding specific to these two languages.\n\n2. **Treebank Annotation Heterogeneity**: While UD is a unified standard,\
  \ individual treebanks vary in annotation practices, particularly for borderline cases (e.g., whether certain clauses are\
  \ adverbial or relative). Our large sample sizes at the sentence level should buffer against noise, but heterogeneity could\
  \ introduce bias.\n\n3. **No Experimental Evidence of Processing Difficulty**: We interpret the asymmetry as reflecting\
  \ cognitive pressures of incremental production, but we lack direct psycholinguistic evidence (self-paced reading, eye-tracking,\
  \ fMRI) demonstrating that spoken-adjunct elongation actually reduces comprehension difficulty or production planning load.\
  \ Our evidence is observational and correlational.\n\n4. **Sentence Length Normalization Imperfection**: Residualization\
  \ via OLS assumes a linear log-log relationship; non-linear confounds may remain. The modifier result (unexpected lengthening\
  \ in speech) hints that our normalization does not fully disentangle all sentence-structure effects.\n\n5. **Lack of Prosodic\
  \ Annotation**: Spoken UD treebanks do not include intonational phrase boundaries or prominence information. Analysis incorporating\
  \ prosodic structure might reveal that adjunct placement is driven more by prosodic phrasing than by morphological typology.\n\
  \n## Methodological Lessons for Cross-Linguistic UD Research\n\nThe treebank audit exposed a critical infrastructure problem:\
  \ most UD treebanks labeled 'spoken' are misidentified written genres or non-representative samples (ESL learner text, parliamentary\
  \ speech, etc.). For future work on register-specific phenomena:\n\n1. Verify treebank source material against official\
  \ UD documentation before making claims about 'spoken' language.\n2. Report treebank selection and audit procedures transparently\
  \ in methods sections.\n3. Acknowledge statistical power limitations: n=3 languages provides power ≈ 11% for mixed-effects\
  \ tests.\n4. Treat results from n < 6 verified pairs as exploratory, requiring replication, not as confirmed cross-linguistic\
  \ universals.\n\n# Conclusion\n\nThis paper has identified and rigorously characterized a systematic asymmetry in register-specific\
  \ dependency distance: arguments are significantly shorter in spoken language, while adjuncts are not minimized to the same\
  \ degree and may be longer. This asymmetry reframes the phenomenon of spoken-language DDM reduction: it is not a uniform\
  \ pressure but a selective intensification of argument minimization, driven by incremental processing constraints.\n\nThe\
  \ argument-adjunct asymmetry is robustly demonstrated in two verified spoken-written language pairs (Slovenian and French)\
  \ and stable across five distinct methodological variants. However, formal cross-linguistic generalization is currently\
  \ underpowered: Monte Carlo simulations indicate 12–20 verified spoken-written pairs are required for 80% statistical power.\
  \ Since only 2–3 such pairs exist in current UD resources, the asymmetry should be understood as an exploratory phenomenon\
  \ in two languages, not yet a confirmed universal.\n\nThe work exposes an infrastructure limitation in universal dependencies:\
  \ the term 'spoken' treebank is often misapplied to written genres, journalism, and elicited speech. Future research should\
  \ prioritize annotating high-quality transcribed natural speech in UD and auditing existing resources to distinguish genuine\
  \ spoken corpora from mislabeled written variants.\n\n**Future directions**:\n\n1. **Spoken Treebank Expansion**: Prioritize\
  \ UD annotation of Italian conversational speech (it_parlato), English conversational genres (en_gum subsets), and Swedish\
  \ interviews (sv_talbanken spoken subset).\n\n2. **Psycholinguistic Validation**: Conduct self-paced reading and eye-tracking\
  \ studies on native-speaker minimal pairs varying argument and adjunct distances in both languages, testing whether patterns\
  \ reflect genuine processing difficulty.\n\n3. **Prosodic Analysis**: Re-analyze data with prosodic annotation (intonational\
  \ phrases, prominence) to test whether adjunct placement is driven by prosodic constituency rather than (or in addition\
  \ to) morphological typology.\n\n4. **Discourse Pragmatics**: Stratify spoken corpora by interactional context (monologue,\
  \ dialogue, task-based conversation) to assess whether conversational interaction intensifies or mitigates the adjunct-elongation\
  \ effect.\n\n5. **Formal Computational Modeling**: Develop an incremental production model that generates predictions about\
  \ argument-adjunct distance as a function of cognitive load, morphological flexibility, and prosodic constraints, enabling\
  \ quantitative comparison with observed corpus patterns.\n\nThe argument-adjunct asymmetry in dependency distance is a previously\
  \ uncharacterized empirical regularity. It demonstrates that fundamental principles of linguistic organization—in this case,\
  \ dependency distance minimization—operate heterogeneously across relation types, shaped by immediate cognitive pressures\
  \ of real-time language production.\n\n# References\n\n[1] Futrell, R., Mahowald, K., & Gibson, E. (2015). Large-scale evidence\
  \ of dependency length minimization in 37 languages. *Proceedings of the National Academy of Sciences of the United States\
  \ of America*, 112(33), 10336–10341. https://doi.org/10.1073/pnas.1502134112\n\n[2] Ferrer-i-Cancho, R., Gómez-Rodríguez,\
  \ C., Esteban, J. L., & Alemany-Puig, L. (2022). The optimality of syntactic dependency distances. *Physical Review E*,\
  \ 105(1), 014308. https://doi.org/10.1103/PhysRevE.105.014308\n\n[3] Liu, H. (2008). Dependency distance as a metric of\
  \ language comprehension difficulty. *Journal of Cognitive Science*, 9(2), 159–191.\n\n[4] Dobrovoljc, K. (2025). Counting\
  \ trees: A treebank-driven exploration of syntactic variation in speech and writing across languages. *Corpus Linguistics\
  \ and Linguistic Theory*, 21(1), 46–78. https://doi.org/10.1515/cllt-2025-0046\n\n[5] Biber, D. (1988). *Variation across\
  \ speech and writing*. Cambridge University Press.\n\n[6] Conrad, S., & Biber, D. (2001). Variation in English grammar.\
  \ Studies in Language Variation and Change, 1, 1–21.\n\n[7] Poiret, C., & Liu, H. (2023). Cross-linguistic variations in\
  \ dependency distance minimization. In *Proceedings of the 37th Pacific Asia Conference on Language, Information and Computation*\
  \ (PACLIC 37), Hong Kong (pp. 234–243).\n\n[8] Sinnemäki, K., & Haakana, V. (2023). Head and dependent marking and dependency\
  \ length in possessive noun phrases: A typological study of morphological and syntactic complexity. *Linguistics Vanguard*,\
  \ 9(1), 45–57. https://doi.org/10.1515/lingvan-2021-0074\n\n[9] Hawkins, J. A. (2004). *Efficiency and complexity in grammars*.\
  \ Oxford University Press.\n\n[10] Greenberg, J. H. (1966). *Language universals: With special reference to feature hierarchies*.\
  \ Mouton.\n\n[11] Gibson, E. (1998). Linguistic complexity: Locality of syntactic dependencies. *Cognition*, 68(1), 1–76.\n\
  \n[12] Universal Dependencies contributors. (2024). Universal Dependencies v2.17. Retrieved from https://universaldependencies.org/\n\
  \n[13] Dobrovoljc, K., & Erjavec, T. (2012). The universal dependencies treebank of spoken Slovenian. In *Proceedings of\
  \ the Eighth International Conference on Language Resources and Evaluation (LREC 2012)* (pp. 2891–2898).\n\n[14] Lacheret,\
  \ A., Kahane, S., & Beliao, J. (2014). Rhapsodie: A prosodic-syntactic treebank for spoken French. In *Proceedings of the\
  \ Ninth International Conference on Language Resources and Evaluation (LREC 2014)* (pp. 57–63)."
summary: >-
  This paper demonstrates that the widely documented reduction in mean dependency distance in spoken versus written language
  masks a systematic asymmetry: argument relations (subjects, objects, clausal complements) are significantly shorter in spoken
  language, consistent with incremental processing pressure, while adjunct relations (adverbial and relative clauses) show
  no reduction and are longer in speech, consistent with right-adjunction (afterthought) syntax. The asymmetry is robustly
  demonstrated in two verified spoken-written Universal Dependencies treebank pairs (Slovenian and French) across five methodological
  variants. However, a critical audit of 14 UD treebanks reveals that most 'spoken' corpora are misidentified written genres,
  undermining iteration 1's claim of 14-language generalization. With only 2–3 verified spoken-written pairs currently available,
  the asymmetry represents an exploratory phenomenon requiring replication across 12–20 additional language pairs for 80%
  statistical power. The work refines our understanding of how cognitive pressures of real-time production shape syntactic
  structure and establishes methodological standards for register-specific UD research.
</paper_text>

<available_figures>
--- Item 1 ---
id: fig1
title: 'Argument-Adjunct Asymmetry in Slovenian: Bootstrap Confidence Intervals'
caption: >-
  Sentence-level mean dependency distance difference (spoken minus written) after length normalization in Slovenian (n=1,313
  spoken, n=4,873 written sentences). Bootstrap 95% confidence intervals (1,000 resamples) for three dependency relation categories.
  Arguments show significant shortening in spoken (Δ=−0.051, CI excludes zero); adjuncts show no significant difference (Δ=−0.010,
  CI includes zero); modifiers unexpectedly lengthen (Δ=+0.114, CI excludes zero). Asymmetry index (adjunct minus argument)
  is near-zero (Δ=+0.041), indicating the asymmetry is driven primarily by argument shortening rather than adjunct elongation.
image_gen_detailed_description: >-
  Horizontal bar chart with error bars. Y-axis: three categories (ARGUMENT, ADJUNCT, MODIFIER) with labels. X-axis: mean difference
  in residualized MDD, ranging from -0.15 to +0.15 (words). ARGUMENT bar: center at -0.051, error bars from -0.082 to -0.019,
  color red (shorter in spoken). ADJUNCT bar: center at -0.010, error bars from -0.038 to +0.017, color yellow (no difference,
  CI includes zero). MODIFIER bar: center at +0.114, error bars from +0.090 to +0.138, color blue (longer in spoken). Add
  vertical dashed line at x=0. Title: 'Slovenian: Register-Specific Dependency Distance by Relation Type'. Include legend:
  red=argument (shorter in speech), yellow=adjunct (no difference), blue=modifier (control).
aspect_ratio: '21:9'
summary: >-
  Bootstrap confidence intervals for three dependency relation types in Slovenian spoken vs. written language, showing argument
  shortening and adjunct non-reduction.
figure_path: figures/fig1_v0.jpg

--- Item 2 ---
id: fig2
title: 'Cross-Language Comparison: Raw Mean Dependency Distance (French vs. Slovenian)'
caption: >-
  Raw mean dependency distance (without length normalization) compared between French (fr_rhapsodie spoken vs. fr_gsd written)
  and Slovenian (raw data from iteration 1 analysis). Left panel: Arguments. Right panel: Adjuncts. Both languages show argument
  shortening in spoken (Slovenian and French arrows point downward from written to spoken), but French shows pronounced adjunct
  elongation (+0.603 words) while Slovenian shows near-zero effect. Effect sizes are larger in French (raw, pre-normalization)
  than in Slovenian (post-normalization), suggesting cross-language heterogeneity in effect magnitudes.
image_gen_detailed_description: >-
  Two-panel grouped bar chart. Left panel (ARGUMENTS): X-axis language pair (Slovenian, French). Y-axis: mean MDD in words
  (0-8). Slovenian spoken (red bar) ≈2.7 vs. written (dark red bar) ≈3.0. French spoken (orange bar) ≈2.7 vs. written (dark
  orange bar) ≈3.0. Right panel (ADJUNCTS): Same structure. Slovenian spoken ≈6.6 vs. written ≈6.0 (smaller difference). French
  spoken ≈6.6 vs. written ≈6.0. Add downward arrows under ARGUMENT bars, upward arrows under ADJUNCT bars to indicate direction
  of effect. Title: 'Argument-Adjunct Register Effects: Cross-Language Comparison'. Legend: red/orange = Slovenian/French,
  light=spoken, dark=written.
aspect_ratio: '21:9'
summary: >-
  Two-language comparison of argument and adjunct dependency distances in spoken vs. written registers, showing directional
  consistency but effect magnitude heterogeneity.
figure_path: figures/fig2_v0.jpg

--- Item 3 ---
id: fig3
title: Robustness Across Five Methodological Variants
caption: >-
  Confirmation of argument-adjunct asymmetry across five distinct analysis pipelines. Each variant tests a different normalization
  or statistical approach: (1) residualized OLS (iteration 1 baseline), (2) raw MDD (no length normalization), (3) OLS with
  log(sentence_length) as covariate, (4) Huber robust regression (outlier handling), (5) 1% outlier trimming. All five variants
  confirm the asymmetry direction: argument Δ is negative (shorter in spoken), adjunct Δ is positive or near-zero (not reduced).
  The robustness confirmation rate is 5/5 (100%), demonstrating the finding is stable across preprocessing choices.
image_gen_detailed_description: >-
  Stacked horizontal bar chart or grouped dot plot. Y-axis: five methodological variants (Residualized OLS, Raw MDD, OLS Covariate,
  Huber Regression, 1% Trim). X-axis: coefficient value, ranging from -0.4 to +0.7. Two dots/bars per variant: ARGUMENT (red,
  negative/leftward) and ADJUNCT (blue, positive/rightward). Variant 1 (Residualized): arg≈-0.007, adj≈+0.020. Variant 2 (Raw
  MDD): arg≈-0.324, adj≈+0.603. Variant 3 (Covariate): arg≈-0.083, adj≈+0.153. Variant 4 (Huber): arg≈-0.085, adj≈+0.109.
  Variant 5 (Trim): arg≈-0.299, adj≈+0.495. Title: 'Robustness Check: Asymmetry Direction Across 5 Analysis Variants'. Add
  checkmark or 'CONFIRMED' label next to each variant.
aspect_ratio: '21:9'
summary: >-
  Robustness confirmation showing argument-adjunct asymmetry is stable across five distinct methodological choices, supporting
  reliability of the main finding.
figure_path: figures/fig3_v0.jpg
</available_figures>

<figure_requirements>
CRITICAL: Include ALL figures from <available_figures>. No exceptions.

- Every figure MUST use \includegraphics{figures/filename.jpg}
- Do NOT skip, convert to tables, or describe without inserting
- Each needs: \begin{figure*|figure}[placement], \includegraphics, \caption, \label, \end{...} — pick env + placement by the figure's `aspect_ratio` field (see PLACEMENT below). Constrain every \includegraphics with `width=\linewidth,height=0.4\textheight,keepaspectratio` (single-column) or `width=\textwidth,height=0.45\textheight,keepaspectratio` (figure*). Use exactly these option keys — `max height=` is NOT valid LaTeX
- Use the `caption` field from each figure for \caption{...} — do NOT invent new captions
- Place figures where their [FIGURE:fig_id] markers appear in paper_text
- VERIFICATION: paper.tex MUST have exact same number of \includegraphics as <available_figures>
- Do NOT generate new figure images (no matplotlib, no PIL, no image generation). Use ONLY the pre-generated figures from <available_figures>. They were already created by a previous pipeline step.

PLACEMENT BY ASPECT RATIO (use the `aspect_ratio` field on each figure):
- `21:9` (architecture diagrams / hero figures): \begin{figure*}[!t] (full two-column width, top of page). The hero architecture diagram should appear EARLY in the paper — typically at the top of page 2. Marker placement in paper_text already determines this; preserve it.
- `16:9` (comparisons, multi-panel results): \begin{figure*}[!t] for full-width or \begin{figure}[!htbp] for single-column.
- `4:3` / `1:1` / `3:2` / `3:4` / `9:16`: \begin{figure}[!htbp] (single-column).
</figure_requirements>

<artifact_links>
The paper_text contains \footnote{Code: \url{...}} references linking to artifact source code
on GitHub. Include \usepackage{hyperref} and \usepackage{url}.
Preserve these exactly as-is — do not remove, rewrite, or convert them to plain text.
The URLs will not resolve yet (the repo is deployed after compilation) — do NOT try to verify or fix them.
</artifact_links>

<headings>
NEVER use inline math (``$...$``) inside ``\section{...}`` / ``\subsection{...}`` / ``\subsubsection{...}`` arguments — hyperref's bookmark builder errors out (``Token not allowed in a PDF string``) and the PDF outline breaks. If a section heading needs a math-looking term, use the text equivalent (``d star`` not ``$d^*$``, ``alpha-equivalent`` not ``$\alpha$-equivalent``) or wrap it in ``\texorpdfstring{$math$}{plain}``. Inline math inside body paragraphs is fine.
</headings>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-paper-to-latex, aii-semscholar-bib.
TODO 2. Review <paper_text> and <available_figures>. Copy all figure images into ./figures/ in your workspace. Count figures — MUST include every one. Plan placements per section. Build `./references.bib` via aii_semscholar_bib__fetch — collect DOIs/ArXiv IDs from <paper_text> and batch-fetch all BibTeX in one call. Do NOT fabricate entries.
TODO 3. Create `./paper.tex` per aii-paper-to-latex skill's setup, write ALL sections, insert ALL figures from <available_figures>, include `./references.bib` via \bibliography. Compile to PDF per skill's process. Fix errors.
TODO 4. CRITICAL VERIFICATION: Run `grep -c 'includegraphics' paper.tex`, confirm count equals figures in <available_figures>. If not, add missing figures. Verify `./paper.pdf` was created.
TODO 5. VISUAL REVIEW: Write Python script to convert EVERY page of paper.pdf to PNG at 150 DPI (use pdf2image or pymupdf). Then read ALL page screenshots — each page image costs ~1,600 tokens so a 15-page paper is only ~24K tokens. You MUST read every page. The ONLY exception is if all page images would not fit in your remaining context — in that case, read as many as fit and state which pages you are skipping and why. Check every page for layout issues, overlapping figures, cut-off text, bad spacing, formatting problems. Fix issues and recompile.
TODO 6. FINAL READ: Check page count (`pdfinfo paper.pdf` or pymupdf). Read entire paper.pdf — check for missing sections, unclear explanations, inconsistencies, typos. Fix and recompile. The ONLY exception is if all pages would not fit in your remaining context — in that case, read as many pages as fit and state which pages you are skipping and why.
</todos>

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "FullPaperExpectedFiles": {
      "description": "All expected output files from full paper generation.",
      "properties": {
        "paper_tex_path": {
          "description": "Path to LaTeX source file. Example: 'paper.tex'",
          "title": "Paper Tex Path",
          "type": "string"
        },
        "paper_pdf_path": {
          "description": "Path to compiled PDF. Example: 'paper.pdf'",
          "title": "Paper Pdf Path",
          "type": "string"
        },
        "references_bib_path": {
          "description": "Path to BibTeX bibliography file. Example: 'references.bib'",
          "title": "References Bib Path",
          "type": "string"
        },
        "figure_paths": {
          "description": "Paths to all figure image files. Example: ['figures/fig1_v0.jpg', 'figures/fig2_v0.jpg']",
          "items": {
            "type": "string"
          },
          "title": "Figure Paths",
          "type": "array"
        }
      },
      "required": [
        "paper_tex_path",
        "paper_pdf_path",
        "references_bib_path",
        "figure_paths"
      ],
      "title": "FullPaperExpectedFiles",
      "type": "object"
    }
  },
  "description": "Full paper \u2014 structured output from paper generation.",
  "properties": {
    "title": {
      "description": "Short descriptive title for this paper generation task (roughly 30-90 characters)",
      "maxLength": 90,
      "minLength": 30,
      "title": "Title",
      "type": "string"
    },
    "summary": {
      "description": "Brief summary of the generated paper: sections written, figures included, compilation status",
      "maxLength": 5000,
      "minLength": 500,
      "title": "Summary",
      "type": "string"
    },
    "out_expected_files": {
      "$ref": "#/$defs/FullPaperExpectedFiles",
      "description": "All output files you created. Must include paper.tex, paper.pdf, references.bib, and paths to all figure files."
    }
  },
  "required": [
    "title",
    "summary",
    "out_expected_files"
  ],
  "title": "FullPaper",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-06-22 13:17:30 UTC

```
Direction: Computational Linguistics — Dependency Distance Minimization Across UD Treebanks. Something genuinely novel and groundbreaking that measures dependency-distance distributions across UD treebanks, investigates whether spoken language minimizes more than written, characterizes how typology interacts with the pattern, and identifies families that deviate. MUST use commul/universal_dependencies on HuggingFace.

Ambition: level 3 of 5 — phenomenological science: surface and rigorously characterize a new empirical regularity or anomaly in the data, even before a full theoretical explanation exists.

Reviewer: I am Kaja Dobrovoljc (JSI / University of Ljubljana). Calibrate from my existing papers. Cross-domain methods (information theory, mixed-effects models, sequence models) welcome — but keep them close to what I already know, not too far from my background.

Submission/Goal: a paper for ACL, EMNLP, or the Computational Linguistics journal. Audience: computational linguists and quantitative typologists. Tone: empirically rigorous, careful with linguistic detail, reproducible on public UD.
```

### [3] SKILL-INPUT — aii-paper-to-latex · 2026-06-22 13:17:34 UTC

The agent loaded the **aii-paper-to-latex** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-paper-to-latex
description: LaTeX paper assembly and compilation. Covers document setup, figure inclusion from pre-generated JPEGs, compilation process, and output files. Use when assembling a paper from pre-written text and pre-generated figures into a compiled PDF.
---

## LaTeX Paper Assembly

Assembles a research paper from paper text, pre-generated figure JPEGs, and bibliography into a compiled PDF.

### Document Setup

```latex
\documentclass[11pt,letterpaper]{article}
\usepackage{graphicx, geometry, amsmath, hyperref, natbib, booktabs, xcolor, listings}
\geometry{margin=1in}
\hypersetup{colorlinks=true, linkcolor=black, citecolor=black, urlcolor=black}
```

### Figure Inclusion

CRITICAL: Include ALL figures. Every figure MUST appear in the paper.

```latex
\begin{figure}[!htbp]
  \centering
  \includegraphics[width=0.92\textwidth,keepaspectratio]{figures/filename.jpg}
  \caption{Descriptive caption.}
  \label{fig:label}
\end{figure}
```

Rules:
- ALWAYS use `[!htbp]` float placement (NOT `[t]` or `[h]` alone)
- ALWAYS constrain with `width` and `keepaspectratio` to prevent page takeover
- Every figure needs `\caption`, `\label`, and a `\ref` in the text
- Do NOT convert figures to tables or describe them without inserting the image
- Do NOT skip any figures

### Compilation Process

Run each command separately (do NOT chain with `&&` — pdflatex often exits non-zero on warnings, which would skip bibtex and leave citations as `??`):

```bash
pdflatex -interaction=nonstopmode paper.tex
bibtex paper
pdflatex -interaction=nonstopmode paper.tex
pdflatex -interaction=nonstopmode paper.tex
```

All four commands are required. Skipping bibtex causes `??` in all citations.
Fix any errors between runs. Verify `./paper.pdf` was created.

### Output Files

- `./paper.tex` — LaTeX source
- `./references.bib` — bibliography file
- `./paper.pdf` — compiled PDF
- `./figures/*.jpg` — all figure images (pre-generated, copied into workspace)
````

### [4] SKILL-INPUT — aii-semscholar-bib · 2026-06-22 13:17:36 UTC

The agent loaded the **aii-semscholar-bib** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-semscholar-bib
description: Build bibliographies using Semantic Scholar. Batch-fetch BibTeX for papers by DOI, ArXiv ID, or title. Use when writing papers, generating reference lists, or building .bib files.
---

## Tool: `aii_semscholar_bib__fetch`

Batch-fetch BibTeX entries from Semantic Scholar. Pass all references in a single call — the tool handles batching internally.

### How it works

1. **DOI/ArXiv refs** → batched into POST /paper/batch calls (up to 500 per API call, auto-chunked)
2. **Title-only refs** → individual GET /paper/search/match (1s delay between)
3. **Post-process** → fix entry type, fix citation key (AuthorYYYY), inject DOI

The ability server runs a single worker (`max_threads: 1`). Multiple concurrent tool calls are queued — each runs independently (no cross-request aggregation). Batching happens within each request.

### Input format

```json
{
  "references": [
    {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
    {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
    {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
  ]
}
```

Each reference object can have:
- `doi` — DOI string (ArXiv DOIs like `10.48550/arXiv.XXXX.XXXXX` auto-convert to ArXiv IDs)
- `arxiv` — ArXiv ID (e.g. `"2305.14325"`)
- `title` — Paper title (used for search/match when no DOI/ArXiv)
- `author` — First author last name (for cleaner citation key)
- `year` — Publication year (int, for citation key)

At least one of `doi`, `arxiv`, or `title` is required per reference.

### Output format

```json
{
  "success": true,
  "bib_text": "@inproceedings{Vaswani2017, ...}\n\n@article{Wei2022, ...}",
  "total": 3,
  "found": 3,
  "failed_count": 0,
  "entries": [{"citation_key": "Vaswani2017", "bibtex": "...", "title": "...", "doi": "...", "arxiv": ""}],
  "failed": []
}
```

### Workflow

1. Collect DOIs, ArXiv IDs, or titles for all papers you need to cite
2. Call `aii_semscholar_bib__fetch` with the full list in **one call**
3. Save `bib_text` from the response to your `references.bib` file
4. Check `failed` — for any missed papers, follow the **fallback procedure** below

### Fallback for failed references (MANDATORY)

NEVER fabricate BibTeX. For each failed reference:
1. **WebSearch** for `"Title" author year` (try `site:arxiv.org` too)
2. **WebFetch** the paper page → extract title, authors, year, venue, DOI/ArXiv ID
3. If DOI/ArXiv found → retry `aii_semscholar_bib__fetch` with it
4. Last resort: write BibTeX by hand using **only verified info from the actual paper page**

---

### CLI (for manual use / debugging)

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-semscholar-bib" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_semscholar_bib__fetch.py --refs '[
  {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
  {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
  {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
]'
```

`--json, -j` — output raw JSON instead of .bib text

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````
