# Connectivity of geometric tetrahedralization flip graphs

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-415 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-415%3A+Connectivity+of+geometric+tetrahedralization+flip+graphs&target=Q-FORMAL-415) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-415%3A+Connectivity+of+geometric+tetrahedralization+flip+graphs&target=Q-FORMAL-415)

For every finite point set in R^3 with no four coplanar, is its tetrahedralization graph connected by geometric 2-to-3 and 3-to-2 bistellar flips without adding or deleting vertices?

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-11-06.

**Status basis:** TOPP's 2008 entry reports the general fixed-point Euclidean question as open. Khoury's September 2026 preprint reports connectivity for four through eight points. Benway's October 2026 revision concerns cusped hyperbolic manifolds, a different setting. An accepted resolution for arbitrary finite Euclidean point sets was not established.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** TOPP revision: 22 December 2008; Khoury version 1: 13 September 2026; Benway version 2: 19 October 2026.

**Scope limits:** All points and coordinates remain fixed, with only geometric 2-to-3 and 3-to-2 moves. Hyperbolic ideal triangulations and abstract topological triangulations have different hypotheses.

**Information still needed**

- Independent assessment of Khoury's eight-point result and any later revisions.
- Further results for arbitrary finite Euclidean point sets, beyond the inspected small-cardinality case.

**Primary branch:** [Computational geometry and topology](../domains/cs.md#cs-geom). **Related branches:** None recorded.

**Sources:** [The Open Problems Project: Problem 28](../sources.md#src-formal-415); [On Isolated Geometric Triangulations](../sources.md#src-math-702); [Flip Graphs for Eight Points in Three Dimensions Are Connected](../sources.md#src-math-705).

**Exact locator:** TOPP Problem 28: Statement and Partial and Related Results; Khoury (2026), Theorem 1; Benway, version 2 (2026), Section 1 and Corollary 4.2

**Potential difficulty:** Unknown. The source identifies an unresolved research target; its present difficulty has not been independently assessed.

**Possible AI role:** After the computational model and current status are checked, generate small geometric instances, inspect exact witnesses and assist with combinatorial or algebraic lemmas. Finite tests do not establish asymptotic complexity or universal existence.

**Verification burden:** High. Review geometric degeneracies, exact arithmetic, admissible constructions and model-dependent running time; floating-point drawings alone are not certificates.

**Resource expectations:** No physical experiment or external dataset is intrinsic. Exact geometry and combinatorial enumeration may be expensive; useful instance sizes remain unestimated.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No model has been tested. Current status, useful subcases and feasible computational scale require further review.

**Further work:** define a scoped target, resource requirements and a verification plan before developing a full card. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-06

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Source reports open.

Add the directly relevant eight-point claim and distinguish the hyperbolic result. Retain the historical source-reported open status for the general Euclidean target.

**Search scope:** Checked TOPP's point-set formulation, a new small-cardinality preprint, and a similarly named hyperbolic result; inspected arXiv version histories and searched for updates.

**Inspected evidence**

- [The Open Problems Project: Problem 28](../sources.md#src-formal-415) — Statement; Partial and Related Results. Asks about arbitrary general-position Euclidean point sets, while distinguishing regular and topological cases.
- [Flip Graphs for Eight Points in Three Dimensions Are Connected](../sources.md#src-math-705) — Theorem 1; Section 1.1. Claims fixed-coordinate, full-vertex connectivity only for four through eight points, without Steiner points or 1-to-4 moves.
- [On Isolated Geometric Triangulations](../sources.md#src-math-702) — Section 1; Theorem 3.4 and Corollary 4.2. The reported disconnected graphs are for ideal triangulations of cusped hyperbolic 3-manifolds.

**Limits and remaining work**

- The recent preprint's proof and acceptance were not independently checked.
- The search does not establish a complete current bibliography for arbitrary point counts.
- Human review remains pending.

<details>
<summary>Search queries</summary>

- tetrahedralizations "flip graph" "disconnected" "2025"
- "tetrahedralizations" "flip graph" connected 2026
- "2609.14797" correction OR revised OR theorem


</details>

### 2026-10-14

**Coverage:** Statement only. **Statement:** Matched.

**Recorded status:** Unverified → Unverified.

The source supports identifying this question, but does not establish its present unresolved status.

**Search scope:** Inspected the named source statement and its recorded qualifications; no comprehensive citation-chain or specialist database review.

**Inspected evidence**

- [The Open Problems Project: Problem 28](../sources.md#src-formal-415) — TOPP Problem 28: Statement; Partial and Related Results. The source identifies the indexed question or research direction; its original date and any recorded partial results limit what it establishes about present status.

**Limits and remaining work**

- Later geometric results, distinguished from topological complexes and regular triangulations.
- Current resolution status was not established by a completed later-literature review.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
