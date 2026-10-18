# Data selection for linear regression

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-437 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-437%3A+Data+selection+for+linear+regression&target=Q-FORMAL-437) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-437%3A+Data+selection+for+linear+regression&target=Q-FORMAL-437)

Determine the worst-case full-data squared-loss ratio for scalar linear regression in R^d using the minimum-Euclidean-norm fit to n selected examples, in the source's weighted and unweighted selection models. Weighted selected losses are convex combinations; evaluation uses the original equally weighted dataset. Theorem 9 supplies several weighted regimes; the intermediate regime d<n<2d and the unweighted case discussed in Section 5 remain the source's unresolved parts. Apply its zero-denominator and support conventions.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-10-14.

**Status basis:** The 2025 primary paper gives exact weighted-selection results in Theorem 9 and identifies remaining weighted and unweighted cases in Section 5. The original broad regression question is retained with these known cases distinguished; no later resolution was verified.

**Statement check:** Needs clarification. **Status check:** Source report only.

**Source date and freshness:** COLT 2025 problem note.

**Scope limits:** Known regimes remain part of this historical question; the intermediate weighted regime is a specifically identified unresolved component, not a replacement problem.

**Information still needed**

- Check subsequent work on exact intermediate-regime ratios; a full problem card must spell out zero-denominator and support conventions.

**Primary branch:** [Statistical learning and high-dimensional theory](../domains/stat.md#stat-learn). **Related branches:** None recorded.

**Sources:** [Open Problem: Data Selection for Regression Tasks](../sources.md#src-formal-435); [Data Selection for ERMs](../sources.md#src-formal-610).

**Exact locator:** Abstract, linear-regression instance

**Potential difficulty:** Unknown. The source identifies an unresolved research target; its present difficulty has not been independently assessed.

**Possible AI role:** After the statistical model is recovered, help manipulate risk bounds, compare lower-bound constructions and design simulations that challenge proposed assumptions. Simulation does not establish minimax optimality.

**Verification burden:** High. Upper and lower bounds must use identical distribution classes, loss, privacy or oracle conditions and quantifiers; statistical counterexamples need exact arguments.

**Resource expectations:** The formal target needs no new physical experiment. Simulations may use synthetic samples; necessary sample counts and computational costs have not been estimated.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No model has been tested. Current status, useful subcases and feasible computational scale require further review.

**Further work:** define a scoped target, resource requirements and a verification plan before developing a full card. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

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
