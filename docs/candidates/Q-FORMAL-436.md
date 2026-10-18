# Data selection for mean estimation

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-436 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-436%3A+Data+selection+for+mean+estimation&target=Q-FORMAL-436) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-436%3A+Data+selection+for+mean+estimation&target=Q-FORMAL-436)

Determine the worst-case mean-selection loss ratio sup_D L_D^*(n)/L_D^* for finite multisets D in R^d, where L_D is average squared Euclidean loss and L_D^*(n) is the best full-data loss attained by the mean of n selected points, using the source's multiplicity and zero-denominator conventions. The exact scalar ratio is known; the remaining question includes finite d>1 and n>1.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-10-14.

**Status basis:** The 2025 primary paper solves the scalar case and explicitly leaves the exact finite higher-dimensional ratio open in Section 5. Both the known case and unresolved part are retained within the original mean-selection question; later resolution status is unchecked.

**Statement check:** Source located. **Status check:** Source report only.

**Source date and freshness:** COLT 2025 problem note.

**Scope limits:** This is a source-defined research question, not a claim that a solution or a manageable research route is known.

**Information still needed**

- Check later literature for an exact d-dimensional ratio and retain the source's multiplicity convention when constructing instances.

**Primary branch:** [Inference and decision theory](../domains/stat.md#stat-infer). **Related branches:** None recorded.

**Sources:** [Open Problem: Data Selection for Regression Tasks](../sources.md#src-formal-435); [Data Selection for ERMs](../sources.md#src-formal-610).

**Exact locator:** Abstract, mean-estimation instance

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

The 2025 primary paper solves the scalar case and explicitly leaves the exact finite higher-dimensional ratio open in Section 5. Both the known case and unresolved part are retained within the original mean-selection question; later resolution status is unchecked.

**Search scope:** Read the scalar theorem and the higher-dimensional question in the authors' full paper; no later source establishing the exact higher-dimensional ratio was inspected. A later-resolution search was not completed and no independent later status source was inspected.

<details>
<summary>Previous indexed wording</summary>

Determine how well the natural mean-estimation rule can perform when trained on n examples selected from a larger dataset, as posed in the source's regression data-selection framework.

The current statement appears at the top of this page.
</details>

**Inspected evidence**

- [Open Problem: Data Selection for Regression Tasks](../sources.md#src-formal-435) — Abstract, mean-estimation instance. The source identifies the indexed question or research direction; its original date and any recorded partial results limit what it establishes about present status.
- [Data Selection for ERMs](../sources.md#src-formal-610) — Section 1.1, Theorem 1; Section 5, High-Dimensional Mean Estimation. Scalar mean selection has an exact result; the finite higher-dimensional ratio is left as a question.

**Limits and remaining work**

- Check later literature for an exact d-dimensional ratio and retain the source's multiplicity convention when constructing instances.
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
