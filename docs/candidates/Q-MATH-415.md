# Largest labelled agreement subtree of two uniform cladograms

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MATH-415 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MATH-415%3A+Largest+labelled+agreement+subtree+of+two+uniform+cladograms&target=Q-MATH-415) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MATH-415%3A+Largest+labelled+agreement+subtree+of+two+uniform+cladograms&target=Q-MATH-415)

Let Cn be the largest number of labels on which two independent uniform rooted binary cladograms on [n] induce identical labelled subtrees, suppressing degree-two vertices. Does E[Cn]=n^(gamma+o(1)) for some gamma<1/2, and what is gamma?

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-11-26.

**Status basis:** Khezeli proves a lower bound for E[Cn] of order n^b for every b below an explicit beta in (0.4464, 0.4465), including rooted trees. The strict sub-square-root upper result and this constructive bound do not determine the existence or value of the limiting exponent.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Aldous, 2003; Khezeli, SIAM Journal on Discrete Mathematics, 2024.

**Scope limits:** Both labelled tree topologies are sampled independently under the uniform law. A construction for uniformly relabelled copies of one shape samples a different pair.

**Information still needed**

- Establish an exponent for the optimum; the proven growth of a particular recursive construction gives only a lower bound.

**Primary branch:** [Discrete probability and random structures](../domains/prob.md#prob-discrete). **Related branches:** None recorded.

**Sources:** [Largest common substructures in probabilistic combinatorics](../sources.md#src-math-402); [Problems involving largest common substructures](../sources.md#src-math-406); [Maximum Agreement Subtrees and Hölder homeomorphisms between Brownian trees](../sources.md#src-math-603); [An Improved Lower Bound on the Largest Common Subtree of Random Leaf-Labeled Binary Trees](../sources.md#src-model-903).

**Exact locator:** Aldous, Example 3(a); Khezeli, Theorems 1.1 and 3.1; Budzinski and Sénizergues, Theorem 1.

**Potential difficulty:** Unknown. The statement is source-located, but a current difficulty assessment and comparison with the latest partial results have not been completed. A simple formulation is not evidence of tractability.

**Possible AI role:** Compare the rooted recursive lower-bound construction to the exact maximum on independently drawn trees.

**Verification burden:** High. An asymptotic, distributional or mixing claim needs an analytic proof with the model and limit fixed. Simulations and exact small-instance computations are evidence only.

**Resource expectations:** No physical experiment or empirical dataset is required. Literature review and proof development are the principal tasks. Any exact search, simulation or symbolic calculation needs an explicit finite scope; its compute and memory requirements have not been estimated.

**Assessment:** 2026-11-26; untested forecast. **Uncertainty:** The proofs were not independently audited; the search did not establish a matching exponent.

**Further work:** define a scoped target, resource requirements and a verification plan before developing a full card. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-26

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Source reports open → Source reports open.

Khezeli proves a lower bound for E[Cn] of order n^b for every b below an explicit beta in (0.4464, 0.4465), including rooted trees. The strict sub-square-root upper result and this constructive bound do not determine the existence or value of the limiting exponent.

**Search scope:** Checked the original model, the author's updates and the published lower-bound theorem with its rooted extension.

**Inspected evidence**

- [Largest common substructures in probabilistic combinatorics](../sources.md#src-math-402) — Example 3(a). Conjectures an exponent below one half under the uniform law.
- [An Improved Lower Bound on the Largest Common Subtree of Random Leaf-Labeled Binary Trees](../sources.md#src-model-903) — Theorems 1.1 and 3.1. Gives a polynomial expectation lower bound for every exponent strictly below the stated threshold.

**Limits and remaining work**

- The proofs were not independently audited; the search did not establish a matching exponent.

<details>
<summary>Search queries</summary>

- maximum agreement subtree two random Yule Harding trees improved lower bound exponent 2026 independent trees Bernstein Hough Yule


</details>

### 2026-10-14

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Source reports open.

The exponent question is retained, with an important partial resolution: Budzinski–Sénizergues prove a strict sub-square-root upper bound. Existence and value of an asymptotic exponent are not established by that theorem. This status reflects the inspected source discussion, not a comprehensive present-day openness claim.

**Search scope:** The original statement and the named later primary results were inspected; searches were limited to the recorded queries.

**Inspected evidence**

- [Largest common substructures in probabilistic combinatorics](../sources.md#src-math-402) — Example 3(a), page 2. The source asks for the exponent and its existence for independent uniform labelled cladograms.
- [Problems involving largest common substructures](../sources.md#src-math-406) — Updates section. The maintained page records lower-bound progress, not an exact exponent.
- [Maximum Agreement Subtrees and Hölder homeomorphisms between Brownian trees](../sources.md#src-math-603) — Theorem 1 and Section 5.2. The upper exponent is strictly below 1/2, including an expectation consequence, but no exact exponent is determined.

**Limits and remaining work**

- This is a scope check, not an independent proof verification or exhaustive literature review.

<details>
<summary>Search queries</summary>

- "largest agreement subtree" random trees 2025 2026


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
