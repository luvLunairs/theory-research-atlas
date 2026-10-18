# Largest labelled agreement subtree of two coalescent trees

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MATH-416 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MATH-416%3A+Largest+labelled+agreement+subtree+of+two+coalescent+trees&target=Q-MATH-416) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MATH-416%3A+Largest+labelled+agreement+subtree+of+two+coalescent+trees&target=Q-MATH-416)

Generate two independent rooted labelled trees by repeatedly merging a uniformly chosen pair of current lineages. If Cn is their largest common induced labelled subtree size, does E[Cn]=n^(gamma+o(1)) for some gamma<1/2, and what is gamma?

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Unverified. **Last checked:** 2026-10-14.

**Status basis:** The coalescent statement is identifiable in Aldous's 2003 source. The exact exponent remains unverified: recent uniform-cladogram bounds cannot be transferred to the coalescent law without a model comparison.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Inspected source years: SRC-MATH-402: 2003, SRC-MATH-603: 2023. Checked on 2026-10-14 within the scope recorded in the literature check.

**Scope limits:** The coalescent statement is identifiable in Aldous's 2003 source. The exact exponent remains unverified: recent uniform-cladogram bounds cannot be transferred to the coalescent law without a model comparison. One explicitly stated stochastic model or separately posed question is indexed; related models do not share a result automatically.

**Information still needed**

- An explicit equivalence between the relevant labelled rooted tree laws and the Yule–Harding convention is still needed.
- No complete later-literature survey for the coalescent exponent was performed.
- The mathematical proof or counterexample, if proposed, still requires expert review.

**Primary branch:** [Discrete probability and random structures](../domains/prob.md#prob-discrete). **Related branches:** None recorded.

**Sources:** [Largest common substructures in probabilistic combinatorics](../sources.md#src-math-402); [Maximum Agreement Subtrees and Hölder homeomorphisms between Brownian trees](../sources.md#src-math-603).

**Exact locator:** Example 3(b), page 2.

**Potential difficulty:** Unknown. The statement is source-located, but a current difficulty assessment and comparison with the latest partial results have not been completed. A simple formulation is not evidence of tractability.

**Possible AI role:** After checking current status, AI with the relevant mathematical background and tools could develop distributional recurrences using the coalescent structure. Specialist review remains necessary; no named model has been evaluated.

**Verification burden:** High. An asymptotic, distributional or mixing claim needs an analytic proof with the model and limit fixed. Simulations and exact small-instance computations are evidence only.

**Resource expectations:** No physical experiment or empirical dataset is required. Literature review and proof development are the principal tasks. Any exact search, simulation or symbolic calculation needs an explicit finite scope; its compute and memory requirements have not been estimated.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** Current resolution status, practical resource needs and AI usefulness remain unmeasured. The exponent for this law must not be transferred from uniform cladograms.

**Further work:** resolve the statement and status questions above before planning an attempt. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-10-14

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Unverified.

The coalescent statement is identifiable in Aldous's 2003 source. The exact exponent remains unverified: recent uniform-cladogram bounds cannot be transferred to the coalescent law without a model comparison.

**Search scope:** The original statement and the named later primary results were inspected; searches were limited to the recorded queries.

**Inspected evidence**

- [Largest common substructures in probabilistic combinatorics](../sources.md#src-math-402) — Example 3(b), page 2. The coalescent pair-merger law is separately posed from uniform cladograms.
- [Maximum Agreement Subtrees and Hölder homeomorphisms between Brownian trees](../sources.md#src-math-603) — Section 5.2, Yule–Harding discussion. The paper discusses a related tree model; applying its statements to the exact coalescent law requires explicit distributional alignment.

**Limits and remaining work**

- An explicit equivalence between the relevant labelled rooted tree laws and the Yule–Harding convention is still needed.
- No complete later-literature survey for the coalescent exponent was performed.

<details>
<summary>Search queries</summary>

- "common" "coalescent trees" "agreement" asymptotic
- "largest agreement subtree" coalescent "2026"


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
