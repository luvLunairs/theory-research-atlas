# Relaxation time of the polygon triangulation flip walk

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MATH-413 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MATH-413%3A+Relaxation+time+of+the+polygon+triangulation+flip+walk&target=Q-MATH-413) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MATH-413%3A+Relaxation+time+of+the+polygon+triangulation+flip+walk&target=Q-MATH-413)

On the triangulations of a convex n-gon, choose an internal diagonal uniformly and flip it to the other diagonal of its quadrilateral. Is the relaxation time O(n^(3/2)) as n tends to infinity?

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Open after scoped check. **Last checked:** 2026-10-14.

**Status basis:** The original walk matches the 2026 ICALP treatment. Its explicitly stated Aldous conjecture remains beyond the paper's bound. A targeted update search and direct theorem-scope comparison support a scoped open assessment as of 2026-10-14.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Inspected source years: SRC-MATH-401: 2003, SRC-MATH-602: 2026. Checked on 2026-10-14 within the scope recorded in the literature check.

**Scope limits:** The original walk matches the 2026 ICALP treatment. Its explicitly stated Aldous conjecture remains beyond the paper's bound. A targeted update search and direct theorem-scope comparison support a scoped open assessment as of 2026-10-14. One explicitly stated stochastic model or separately posed question is indexed; related models do not share a result automatically.

**Information still needed**

- This is a scope check, not an independent proof verification or exhaustive literature review.
- The mathematical proof or counterexample, if proposed, still requires expert review.

**Primary branch:** [Markov chains, mixing and interacting systems](../domains/prob.md#prob-mix). **Related branches:** None recorded.

**Sources:** [Mixing Times for the Branch-Rotation Chain on Cladograms (or the Triangulation Walk)](../sources.md#src-math-401); [Faster Triangulation Mixing via Transport Flows](../sources.md#src-math-602).

**Exact locator:** Pages 1–2: triangulation walk and PROBLEM.

**Potential difficulty:** Unknown. The statement is source-located, but a current difficulty assessment and comparison with the latest partial results have not been completed. A simple formulation is not evidence of tractability.

**Possible AI role:** After checking current status, AI with the relevant mathematical background and tools could compare canonical-path or coupling arguments with exact small transition matrices. Specialist review remains necessary; no named model has been evaluated.

**Verification burden:** High. An asymptotic, distributional or mixing claim needs an analytic proof with the model and limit fixed. Simulations and exact small-instance computations are evidence only.

**Resource expectations:** No physical experiment or empirical dataset is required. Literature review and proof development are the principal tasks. Any exact search, simulation or symbolic calculation needs an explicit finite scope; its compute and memory requirements have not been estimated.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** Current resolution status, practical resource needs and AI usefulness remain unmeasured. Check whether post-2003 work settles the stated exponent; relaxation time is not identical to total-variation mixing time.

**Further work:** define a scoped target, resource requirements and a verification plan before developing a full card. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-10-14

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Open after scoped check.

The original walk matches the 2026 ICALP treatment. Its explicitly stated Aldous conjecture remains beyond the paper's bound. A targeted update search and direct theorem-scope comparison support a scoped open assessment as of 2026-10-14.

**Search scope:** The original statement and the named later primary results were inspected; searches were limited to the recorded queries.

**Inspected evidence**

- [Mixing Times for the Branch-Rotation Chain on Cladograms (or the Triangulation Walk)](../sources.md#src-math-401) — Pages 1–2, triangulation walk and PROBLEM. The relaxation target is n^(3/2) for the single-diagonal flip chain.
- [Faster Triangulation Mixing via Transport Flows](../sources.md#src-math-602) — Introduction, The Aldous conjecture; Theorem 1 and Corollary 2. The 2026 ICALP paper retains the n^(3/2) conjecture and gives an improved upper bound at the n^2 scale up to logarithms.

**Limits and remaining work**

- This is a scope check, not an independent proof verification or exhaustive literature review.

<details>
<summary>Search queries</summary>

- "Aldous" "triangulation" relaxation time 2025 2026


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
