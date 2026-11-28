# Complexity of planar Euclidean maximum-scatter TSP

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-426 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-426%3A+Complexity+of+planar+Euclidean+maximum-scatter+TSP&target=Q-FORMAL-426) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-426%3A+Complexity+of+planar+Euclidean+maximum-scatter+TSP&target=Q-FORMAL-426)

For a finite set of points in the Euclidean plane, determine the computational complexity of finding a Hamiltonian cycle whose shortest Euclidean edge is as long as possible.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-11-28.

**Status basis:** Kozma and Mömke give a (1−ε)-approximation in fixed doubling dimension, including the Euclidean plane. Their paper explicitly leaves the exact planar problem open and relates it to Hamiltonian cycles in complements of unit disk graphs. This supersedes the directory’s historical note about the lack of geometric approximation bounds.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** The problem statement and references listed in the 28 November 2026 literature check were inspected.

**Scope limits:** TOPP 49, related open problems. Kozma and Mömke, abstract and “Open question,” p. 3.

**Information still needed**

- Check for subsequent exact algorithms or hardness results in the planar case. The published scheme permits a positive relative error.

**Primary branch:** [Computational geometry and topology](../domains/cs.md#cs-geom). **Related branches:** None recorded.

**Sources:** [The Open Problems Project: Problem 49](../sources.md#src-formal-425); [Maximum Scatter TSP in Doubling Metrics](../sources.md#src-math-930).

**Exact locator:** TOPP 49, related open problems. Kozma and Mömke, abstract and “Open question,” p. 3.

**Potential difficulty:** Unknown. The source identifies an unresolved research target; its present difficulty has not been independently assessed.

**Possible AI role:** Study the distance-threshold decision problem or the unit-disk-complement formulation when investigating exact complexity.

**Verification burden:** High. Review geometric degeneracies, exact arithmetic, admissible constructions and model-dependent running time; floating-point drawings alone are not certificates.

**Resource expectations:** No physical experiment or external dataset is intrinsic. Exact geometry and combinatorial enumeration may be expensive; useful instance sizes remain unestimated.

**Assessment:** 2026-11-28; untested forecast. **Uncertainty:** Check for subsequent exact algorithms or hardness results in the planar case. The published scheme permits a positive relative error. Model performance on this task has not been measured.

**Further work:** define a scoped target, resource requirements and a verification plan before developing a full card. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-28

**Coverage:** Statement and later literature. **Statement:** Corrected.

**Recorded status:** Unverified → Source reports open.

Kozma and Mömke give a (1−ε)-approximation in fixed doubling dimension, including the Euclidean plane. Their paper explicitly leaves the exact planar problem open and relates it to Hamiltonian cycles in complements of unit disk graphs. This supersedes the directory’s historical note about the lack of geometric approximation bounds.

**Search scope:** TOPP 49, related open problems. Kozma and Mömke, abstract and “Open question,” p. 3.

<details>
<summary>Previous indexed wording</summary>

Determine the complexity of finding a Hamiltonian tour of a planar point set maximizing its shortest edge length.

The current statement appears at the top of this page.
</details>

**Inspected evidence**

- [The Open Problems Project: Problem 49](../sources.md#src-formal-425) — Problem 49, Related Open Problems. Distinguishes maximizing the shortest Euclidean edge from maximizing the total tour length.
- [Maximum Scatter TSP in Doubling Metrics](../sources.md#src-math-930) — Abstract and the “Open question” on p. 3 of the PDF. Gives an efficient approximation scheme for maximizing the shortest edge in fixed doubling dimension and explicitly leaves exact planar Euclidean optimization open.

**Limits and remaining work**

- Check for subsequent exact algorithms or hardness results in the planar case. The published scheme permits a positive relative error.

<details>
<summary>Search queries</summary>

- Euclidean plane maximum scatter TSP exact complexity NP-complete Kozma Mömke later results


</details>

### 2026-10-14

**Coverage:** Statement only. **Statement:** Matched.

**Recorded status:** Unverified → Unverified.

The source supports identifying this question, but does not establish its present unresolved status.

**Search scope:** Inspected the named source statement and its recorded qualifications; no comprehensive citation-chain or specialist database review.

**Inspected evidence**

- [The Open Problems Project: Problem 49](../sources.md#src-formal-425) — TOPP Problem 49: Related Open Problems. The source identifies the indexed question or research direction; its original date and any recorded partial results limit what it establishes about present status.

**Limits and remaining work**

- Later planar algorithms or hardness for this bottleneck objective.
- Current resolution status was not established by a completed later-literature review.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
