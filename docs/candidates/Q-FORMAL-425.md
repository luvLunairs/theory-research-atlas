# Complexity of planar Euclidean maximum TSP

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-425 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-425%3A+Complexity+of+planar+Euclidean+maximum+TSP&target=Q-FORMAL-425) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-425%3A+Complexity+of+planar+Euclidean+maximum+TSP&target=Q-FORMAL-425)

Determine the exact computational complexity of finding a maximum-total-length Hamiltonian tour of a planar Euclidean point set.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-11-28.

**Status basis:** The Open Problems Project lists the exact planar Euclidean problem as open. Barvinok and coauthors prove hardness in Euclidean dimensions at least three and exact algorithms for fixed polyhedral norms. Shenmaier obtains an efficient approximation scheme for total length in fixed doubling dimension. Kozma and Mömke explicitly distinguish the sum-of-distances precision issue from the shortest-edge problem.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** The problem statement and references listed in the 28 November 2026 literature check were inspected.

**Scope limits:** TOPP 49, statement and status. Barvinok et al., abstract. Kozma and Mömke, p. 3. Shenmaier, abstract.

**Information still needed**

- A new exact algorithm or reduction must specify how Euclidean lengths and their sums are represented and compared.

**Primary branch:** [Computational geometry and topology](../domains/cs.md#cs-geom). **Related branches:** None recorded.

**Sources:** [The Open Problems Project: Problem 49](../sources.md#src-formal-425); [The Geometric Maximum Traveling Salesman Problem](../sources.md#src-math-928); [Efficient PTAS for the Maximum Traveling Salesman Problem in a Metric Space of Fixed Doubling Dimension](../sources.md#src-math-929); [Maximum Scatter TSP in Doubling Metrics](../sources.md#src-math-930).

**Exact locator:** TOPP 49, statement and status. Barvinok et al., abstract. Kozma and Mömke, p. 3. Shenmaier, abstract.

**Potential difficulty:** Unknown. The source identifies an unresolved research target; its present difficulty has not been independently assessed.

**Possible AI role:** Review whether an exact reduction or running-time claim assumes real arithmetic or exact comparisons of sums of radicals.

**Verification burden:** High. Review geometric degeneracies, exact arithmetic, admissible constructions and model-dependent running time; floating-point drawings alone are not certificates.

**Resource expectations:** No physical experiment or external dataset is intrinsic. Exact geometry and combinatorial enumeration may be expensive; useful instance sizes remain unestimated.

**Assessment:** 2026-11-28; untested forecast. **Uncertainty:** A new exact algorithm or reduction must specify how Euclidean lengths and their sums are represented and compared. Model performance on this task has not been measured.

**Further work:** define a scoped target, resource requirements and a verification plan before developing a full card. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-28

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Source reports open.

The Open Problems Project lists the exact planar Euclidean problem as open. Barvinok and coauthors prove hardness in Euclidean dimensions at least three and exact algorithms for fixed polyhedral norms. Shenmaier obtains an efficient approximation scheme for total length in fixed doubling dimension. Kozma and Mömke explicitly distinguish the sum-of-distances precision issue from the shortest-edge problem.

**Search scope:** TOPP 49, statement and status. Barvinok et al., abstract. Kozma and Mömke, p. 3. Shenmaier, abstract.

**Inspected evidence**

- [The Open Problems Project: Problem 49](../sources.md#src-formal-425) — Problem 49, Statement and Status. Poses maximum total Euclidean length in the plane and labels the exact problem open.
- [The Geometric Maximum Traveling Salesman Problem](../sources.md#src-math-928) — 2003 revision, abstract, results on polyhedral norms and dimensions greater than two. Provides exact algorithms for polyhedral norms in fixed dimension and Euclidean NP-hardness in dimension at least three.
- [Efficient PTAS for the Maximum Traveling Salesman Problem in a Metric Space of Fixed Doubling Dimension](../sources.md#src-math-929) — First posted in 2020, version 5 revised in 2021, abstract and introduction. Gives an efficient approximation scheme for maximum total tour length in metrics of fixed doubling dimension.
- [Maximum Scatter TSP in Doubling Metrics](../sources.md#src-math-930) — p. 3, paragraph following “Open question”. Distinguishes exact MaxTSP and the difficulty of comparing sums of square roots.

**Limits and remaining work**

- A new exact algorithm or reduction must specify how Euclidean lengths and their sums are represented and compared.

<details>
<summary>Search queries</summary>

- planar Euclidean maximum TSP exact computational complexity polynomial NP-hard
- maximum TSP EPTAS fixed doubling dimension Shenmaier


</details>

### 2026-10-14

**Coverage:** Statement only. **Statement:** Matched.

**Recorded status:** Unverified → Unverified.

The source supports identifying this question, but does not establish its present unresolved status.

**Search scope:** Inspected the named source statement and its recorded qualifications; no comprehensive citation-chain or specialist database review. The listed targeted searches were exploratory; no verified later source establishing current resolution status was obtained.

**Inspected evidence**

- [The Open Problems Project: Problem 49](../sources.md#src-formal-425) — TOPP Problem 49: Statement. The source identifies the indexed question or research direction; its original date and any recorded partial results limit what it establishes about present status.

**Limits and remaining work**

- Later exact complexity and bit-model results.
- Current resolution status was not established by a completed later-literature review.

<details>
<summary>Search queries</summary>

- "Euclidean maximum TSP" "2025"
- "Euclidean maximum TSP" "open"


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
