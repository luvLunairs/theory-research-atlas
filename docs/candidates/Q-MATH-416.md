# Largest labelled agreement subtree of two coalescent trees

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MATH-416 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MATH-416%3A+Largest+labelled+agreement+subtree+of+two+coalescent+trees&target=Q-MATH-416) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MATH-416%3A+Largest+labelled+agreement+subtree+of+two+coalescent+trees&target=Q-MATH-416)

Generate two independent rooted labelled trees by repeatedly merging a uniformly chosen pair of current lineages. If Cn is their largest common induced labelled subtree size, does E[Cn]=n^(gamma+o(1)) for some gamma<1/2, and what is gamma?

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Unverified. **Last checked:** 2026-11-26.

**Status basis:** For independent Yule–Harding topologies, Bernstein et al. bound the expected agreement size below by order n^(a-epsilon) for every epsilon > 0, with a about 0.344184, and above by O(sqrt(n)). These bounds apply to the coalescent topology and leave the strict exponent conjecture undecided.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Aldous, 2003; Gernhard et al., 2007; Bernstein et al., 2015.

**Scope limits:** Ignore coalescence times and retain the leaf labels on rooted trees. The coalescent law on topologies equals the Yule–Harding law; it differs from the uniform law on cladograms.

**Information still needed**

- Check for sharper bounds specific to independent coalescent trees before selecting a target exponent.

**Primary branch:** [Discrete probability and random structures](../domains/prob.md#prob-discrete). **Related branches:** None recorded.

**Sources:** [Largest common substructures in probabilistic combinatorics](../sources.md#src-math-402); [Maximum Agreement Subtrees and Hölder homeomorphisms between Brownian trees](../sources.md#src-math-603); [Bounds on the Expected Size of the Maximum Agreement Subtree](../sources.md#src-model-904); [Estimating the Relative Order of Speciation or Coalescence Events on a Given Phylogeny](../sources.md#src-model-905).

**Exact locator:** Aldous, Example 3(b); Bernstein et al., Theorems 3.1 and 4.3; Gernhard et al., discussion of ranked tree distributions.

**Potential difficulty:** Unknown. The statement is source-located, but a current difficulty assessment and comparison with the latest partial results have not been completed. A simple formulation is not evidence of tractability.

**Possible AI role:** Work with the Yule–Harding recursion and check any proposed improvement against the published two-sided expectation bounds.

**Verification burden:** High. An asymptotic, distributional or mixing claim needs an analytic proof with the model and limit fixed. Simulations and exact small-instance computations are evidence only.

**Resource expectations:** No physical experiment or empirical dataset is required. Literature review and proof development are the principal tasks. Any exact search, simulation or symbolic calculation needs an explicit finite scope; its compute and memory requirements have not been estimated.

**Assessment:** 2026-11-26; untested forecast. **Uncertainty:** The exact exponent has not been established by the sources examined. Distinct random tree laws have different available bounds.

**Further work:** resolve the statement and status questions above before planning an attempt. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-26

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Unverified.

For independent Yule–Harding topologies, Bernstein et al. bound the expected agreement size below by order n^(a-epsilon) for every epsilon > 0, with a about 0.344184, and above by O(sqrt(n)). These bounds apply to the coalescent topology and leave the strict exponent conjecture undecided.

**Search scope:** Checked the topology correspondence and the Yule–Harding expectation bounds against the original pairwise-merger model.

**Inspected evidence**

- [Largest common substructures in probabilistic combinatorics](../sources.md#src-math-402) — Example 3(b). Defines the process by uniform pairwise mergers.
- [Bounds on the Expected Size of the Maximum Agreement Subtree](../sources.md#src-model-904) — Theorems 3.1 and 4.3. Gives lower and upper bounds in expectation for the Yule–Harding model.
- [Estimating the Relative Order of Speciation or Coalescence Events on a Given Phylogeny](../sources.md#src-model-905) — Model discussion, comparison of the coalescent and Yule models. Identifies the corresponding distributions on ranked binary tree topologies.

**Limits and remaining work**

- The exact exponent has not been established by the sources examined. Distinct random tree laws have different available bounds.

<details>
<summary>Search queries</summary>

- maximum agreement subtree two random Yule Harding trees improved lower bound exponent 2026 independent trees Bernstein Hough Yule


</details>

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
