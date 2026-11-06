# Characterize admissible e-processes

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-012 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-012%3A+Characterize+admissible+e-processes&target=Q-FORMAL-012) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-012%3A+Characterize+admissible+e-processes&target=Q-FORMAL-012)

For a specified null distribution class and filtration, characterize e-process admissibility by matching necessary and sufficient conditions under the survey's domination order: dominance almost surely under every null law, with strict improvement of positive probability for some null law at some time. Keep pathwise orders in later nonparametric results distinct when comparing their scope.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-11-06.

**Status basis:** The general survey question is retained, with important partial results. Clerico characterizes the bounded constant-conditional-mean case and later gives a complete class for finitely constrained conditional nulls. The latter explicitly leaves minimal complete classes and admissible elements open; it is not a general admissibility characterization.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** 2023 survey; Clerico author version dated 4 August 2025; 2026 conditional-constraint preprint.

**Scope limits:** The survey uses null-law almost-sure dominance, whereas Clerico makes pathwise comparisons. The bounded conditional-mean result cannot be transferred unchanged to a narrower i.i.d. null.

**Information still needed**

- Choose a specific null, filtration and domination convention beyond the cited characterized case.
- Determine whether a proposed conditional-null subproblem asks for complete-class domination or genuinely for all admissible elements.

**Primary branch:** [Inference and decision theory](../domains/stat.md#stat-infer). **Related branches:** [Stochastic processes and stochastic analysis](../domains/prob.md#prob-process).

**Sources:** [Game-Theoretic Statistics and Safe Anytime-Valid Inference](../sources.md#src-formal-010); [On the optimality of coin-betting for mean estimation](../sources.md#src-model-707); [Sequential testing of conditionally constrained hypotheses](../sources.md#src-model-708).

**Exact locator:** Ramdas et al., Section 2.4 footnote 4 and Section 8.2.3; Clerico (2025), Theorem 3; Clerico (2026), Theorem 1 and Section 5.

**Potential difficulty:** Unknown. No separate difficulty review of this exact statement is recorded. Its origin or current status does not establish tractability.

**Possible AI role:** Compare admissibility orders and known conditional-null classes before proposing a new theorem. A useful narrower target must go beyond the characterized bounded-mean case.

**Verification burden:** High. Verify the null class, filtration, measurability and strict-domination convention. A complete-class result alone does not identify the minimal class of admissible processes.

**Resource expectations:** No run estimate is available. Decide data, computation and experiment requirements after selecting a concrete approach.

**Assessment:** 2026-11-06; untested forecast. **Uncertainty:** The candidate remains a broad literature question. The cited partial results do not establish a comprehensive 2026 classification.

**Further work:** define a scoped target, resource requirements and a verification plan before developing a full card. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-06

**Coverage:** Statement and later literature. **Statement:** Corrected.

**Recorded status:** Source reports open → Source reports open.

The general survey question is retained, with important partial results. Clerico characterizes the bounded constant-conditional-mean case and later gives a complete class for finitely constrained conditional nulls. The latter explicitly leaves minimal complete classes and admissible elements open; it is not a general admissibility characterization.

**Search scope:** Read the original survey definition and open question, the bounded-mean author version at its assumptions and Theorem 3, and the later conditional-constraint preprint at Theorem 1 and its explicit unresolved admissibility discussion.

<details>
<summary>Previous indexed wording</summary>

For a precisely fixed null distribution class and filtration, characterize e-process admissibility by matching necessary and sufficient conditions under the pointwise domination order used in the source.

The current statement appears at the top of this page.
</details>

**Inspected evidence**

- [Game-Theoretic Statistics and Safe Anytime-Valid Inference](../sources.md#src-formal-010) — Section 2.4 footnote 4; Section 8.2.3. Defines null-law almost-sure dominance and the unmatched necessary/sufficient conditions.
- [On the optimality of coin-betting for mean estimation](../sources.md#src-model-707) — Sections 6.2-6.3, Theorem 3. Settles the bounded fixed-conditional-mean subclass and distinguishes the i.i.d. model.
- [Sequential testing of conditionally constrained hypotheses](../sources.md#src-model-708) — Theorem 1; Section 5. Gives a dominating affine-product complete class but explicitly leaves identification of its admissible elements open.

**Limits and remaining work**

- A general necessary-and-sufficient characterization was not established. Results with other domination orders cannot be silently substituted.

<details>
<summary>Search queries</summary>

- "admissible e-processes" characterization 2026
- "On the optimality of coin-betting for mean estimation" Clerico arxiv


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
