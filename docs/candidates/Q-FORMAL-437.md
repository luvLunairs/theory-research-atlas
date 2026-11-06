# Data selection for linear regression

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-437 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-437%3A+Data+selection+for+linear+regression&target=Q-FORMAL-437) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-437%3A+Data+selection+for+linear+regression&target=Q-FORMAL-437)

Determine the worst-case full-data squared-loss ratio for scalar linear regression in R^d using the minimum-Euclidean-norm fit under selection budget n, in the original weighted and unweighted selection models. Weighted selected losses are convex combinations; evaluation uses the original equally weighted dataset. Retain the original zero-denominator, repeated-example and effective-support conventions. Distinguish the known weighted regimes and subsequent partial results from the remaining weighted budgets and the separate unweighted-selection question.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-11-06.

**Status basis:** The broad question remains open in part. Subsequent preprints report exact weighted ratios at n=2d-1, (3,4), (4,5), (4,6), (5,6), and throughout ceil(3d/2)<=n<=2d-1. Thus the whole intermediate interval must not be described as untouched. The remaining intermediate budgets and unweighted training selection are distinct unresolved targets.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Original 2025 paper; Zhang v2 dated 2 October 2026; Liu-Wang v1 metadata displays 8 September 2026.

**Scope limits:** Liu-Wang permits nonuniform evaluation weights, but its upper-half lower bound is uniform, so that law also addresses the original evaluation model. Weighted evaluation is not unweighted training selection.

**Information still needed**

- Compare the preprint proofs and any later versions before selecting a remaining budget.
- A full card must retain the minimum-norm tie rule, infimum versus attainment, support budget and zero-loss conventions.
- The later search focused on weighted selection; the current frontier for unweighted training selection needs a dedicated check.

**Primary branch:** [Statistical learning and high-dimensional theory](../domains/stat.md#stat-learn). **Related branches:** None recorded.

**Sources:** [Open Problem: Data Selection for Regression Tasks](../sources.md#src-formal-435); [Data Selection for ERMs](../sources.md#src-formal-610); [Exact Risk Ratios for Weighted Data Selection in Linear Regression](../sources.md#src-model-702); [Weighted Data Selection: Sharp Upper-Half and Five-Dimensional Laws](../sources.md#src-model-703).

**Exact locator:** Hanneke et al., Theorem 9 and Section 5; Zhang v2, Section 2; Liu-Wang v1, Section 2, Theorems 1-2.

**Potential difficulty:** Unknown. The source identifies an unresolved research target; its present difficulty has not been independently assessed.

**Possible AI role:** Compare the remaining weighted-budget cells against the cited frontier, or examine unweighted selection after a separate status check. Preserve rank and minimum-norm conventions in symbolic examples.

**Verification burden:** High. Upper and lower bounds must use identical distribution classes, loss, privacy or oracle conditions and quantifiers; statistical counterexamples need exact arguments.

**Resource expectations:** The formal target needs no new physical experiment. Simulations may use synthetic samples; necessary sample counts and computational costs have not been estimated.

**Assessment:** 2026-11-06; untested forecast. **Uncertainty:** Recent preprints provide partial results, not a verified solution of every original case. Their claimed exact or Lean checks were not rerun.

**Further work:** define a scoped target, resource requirements and a verification plan before developing a full card. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-06

**Coverage:** Statement and later literature. **Statement:** Corrected.

**Recorded status:** Source reports open → Source reports open.

The broad question remains open in part. Subsequent preprints report exact weighted ratios at n=2d-1, (3,4), (4,5), (4,6), (5,6), and throughout ceil(3d/2)<=n<=2d-1. Thus the whole intermediate interval must not be described as untouched. The remaining intermediate budgets and unweighted training selection are distinct unresolved targets.

**Search scope:** Read the original regression theorem and open discussion, then compared two later primary preprints at their model definitions, theorem statements and remaining-frontier discussion. The correction searches located no matching retraction or erratum.

<details>
<summary>Previous indexed wording</summary>

Determine the worst-case full-data squared-loss ratio for scalar linear regression in R^d using the minimum-Euclidean-norm fit to n selected examples, in the source's weighted and unweighted selection models. Weighted selected losses are convex combinations; evaluation uses the original equally weighted dataset. Theorem 9 supplies several weighted regimes; the intermediate regime d<n<2d and the unweighted case discussed in Section 5 remain the source's unresolved parts. Apply its zero-denominator and support conventions.

The current statement appears at the top of this page.
</details>

**Inspected evidence**

- [Data Selection for ERMs](../sources.md#src-formal-610) — Theorem 9; Section 5. Retains separate weighted and unweighted models and the original endpoint conventions.
- [Exact Risk Ratios for Weighted Data Selection in Linear Regression](../sources.md#src-model-702) — Section 2, Theorems 2.1-2.3; Conjecture 7.2. Exact low-dimensional cells and the 2d-1 boundary improve the original weighted frontier.
- [Weighted Data Selection: Sharp Upper-Half and Five-Dimensional Laws](../sources.md#src-model-703) — Section 2, Theorems 1-2 and paragraph after equation (5). The upper-half law has a uniform-data lower bound; other budgets remain a stated target.

**Limits and remaining work**

- No independent proof or Lean check was performed. The unweighted frontier was not comprehensively searched.

<details>
<summary>Search queries</summary>

- "Data Selection for ERMs" regression 2026
- "Data Selection" "linear regression" "2026" "weighted"
- "Data Selection for ERMs" "d<n"
- "2608.28007" correction OR erratum OR withdrawn
- "2610.00101" correction OR erratum OR withdrawn


</details>

### 2026-10-14

**Coverage:** Statement only. **Statement:** Corrected.

**Recorded status:** Unverified → Source reports open.

The 2025 primary paper gives exact weighted-selection results in Theorem 9 and identifies remaining weighted and unweighted cases in Section 5. The original broad regression question is retained with these known cases distinguished; no later resolution was verified.

**Search scope:** Read the weighted selection definition, min-norm rule, theorem regimes, and the following open-case discussion. A later-resolution search was not completed and no independent later status source was inspected.

<details>
<summary>Previous indexed wording</summary>

Determine the attainable regression error when a natural linear-regression rule is fitted to n examples selected from a larger dataset, under the source's data-selection model.

The current statement appears at the top of this page.
</details>

**Inspected evidence**

- [Open Problem: Data Selection for Regression Tasks](../sources.md#src-formal-435) — Abstract, linear-regression instance. The source identifies the indexed question or research direction; its original date and any recorded partial results limit what it establishes about present status.
- [Data Selection for ERMs](../sources.md#src-formal-610) — Weighted Data Selection; Theorem 9; Section 5, Data Selection in Regression. Theorem 9 supplies weighted-selection regimes; Section 5 leaves the intermediate weighted regime and further unweighted cases to be characterized.

**Limits and remaining work**

- Check subsequent work on exact intermediate-regime ratios; a full problem card must spell out zero-denominator and support conventions.
- Current resolution status was not established by a completed later-literature review.

<details>
<summary>Search queries</summary>

- "Data Selection for Regression Tasks" solution
- "Data Selection for ERMs"


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
