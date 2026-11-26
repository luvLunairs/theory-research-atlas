# Hamiltonian tetrahedralizations of convex polytopes

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-416 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-416%3A+Hamiltonian+tetrahedralizations+of+convex+polytopes&target=Q-FORMAL-416) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-416%3A+Hamiltonian+tetrahedralizations+of+convex+polytopes&target=Q-FORMAL-416)

Does every convex three-dimensional polytope have a tetrahedralization using its vertices whose dual adjacency graph contains a Hamiltonian path?

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-11-26.

**Status basis:** The Open Problems Project labels the unrestricted question open. Chin, Ding and Wang rule out pulling as a universal construction. Escalona, Fabila-Monroy and Urrutia prove a positive case for general-position point sets with at most 20 hull vertices and a broader bound allowing added points.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** The directory records updates through September 2007. The inspected research texts date from 2005 and 2012.

**Scope limits:** A tetrahedron is adjacent to another when they share a face. The requested tetrahedralization may be chosen freely and must use only vertices of the polytope.

**Information still needed**

- A later resolution for arbitrary convex three-dimensional polytopes without additional vertices.

**Primary branch:** [Computational geometry and topology](../domains/cs.md#cs-geom). **Related branches:** None recorded.

**Sources:** [The Open Problems Project: Problem 29](../sources.md#src-formal-416); [On Hamiltonian Tetrahedralizations of Convex Polyhedra](../sources.md#src-math-904); [Hamiltonian Tetrahedralizations with Steiner Points](../sources.md#src-math-905).

**Exact locator:** TOPP Problem 29, Chin–Ding–Wang section 2, and Escalona–Fabila-Monroy–Urrutia Theorem 1 and section 3

**Potential difficulty:** Unknown. The source identifies an unresolved research target; its present difficulty has not been independently assessed.

**Possible AI role:** After the computational model and current status are checked, generate small geometric instances, inspect exact witnesses and assist with combinatorial or algebraic lemmas. Finite tests do not establish asymptotic complexity or universal existence.

**Verification burden:** High. Review geometric degeneracies, exact arithmetic, admissible constructions and model-dependent running time; floating-point drawings alone are not certificates.

**Resource expectations:** No physical experiment or external dataset is intrinsic. Exact geometry and combinatorial enumeration may be expensive; useful instance sizes remain unestimated.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No model has been tested. Current status, useful subcases and feasible computational scale require further review.

**Further work:** define a scoped target, resource requirements and a verification plan before developing a full card. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-26

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Source reports open.

The Open Problems Project labels the unrestricted question open. Chin, Ding and Wang rule out pulling as a universal construction. Escalona, Fabila-Monroy and Urrutia prove a positive case for general-position point sets with at most 20 hull vertices and a broader bound allowing added points.

**Search scope:** A tetrahedron is adjacent to another when they share a face. The requested tetrahedralization may be chosen freely and must use only vertices of the polytope.

**Inspected evidence**

- [The Open Problems Project: Problem 29](../sources.md#src-formal-416) — Statement, status and related results. Asks whether the tetrahedra can be ordered along a Hamiltonian path in the dual graph.
- [On Hamiltonian Tetrahedralizations of Convex Polyhedra](../sources.md#src-math-904) — Abstract and section 2. Its counterexample concerns a particular class of tetrahedralizations.
- [Hamiltonian Tetrahedralizations with Steiner Points](../sources.md#src-math-905) — Theorem 1 and section 3. Under general position, at most 20 hull vertices need no extra points. In general the construction allows interior Steiner points.

**Limits and remaining work**

- A later resolution for arbitrary convex three-dimensional polytopes without additional vertices.
- This is a literature check. The cited proofs and computational certificates have not been independently reproduced.

<details>
<summary>Search queries</summary>

- Hamiltonian tetrahedralizations convex polytopes Chin Ding Wang pulling counterexamples Hamiltonian Steiner points


</details>

### 2026-10-14

**Coverage:** Statement only. **Statement:** Matched.

**Recorded status:** Unverified → Unverified.

The source supports identifying this question, but does not establish its present unresolved status.

**Search scope:** Inspected the named source statement and its recorded qualifications; no comprehensive citation-chain or specialist database review.

**Inspected evidence**

- [The Open Problems Project: Problem 29](../sources.md#src-formal-416) — TOPP Problem 29: Statement; Partial and Related Results. The source identifies the indexed question or research direction; its original date and any recorded partial results limit what it establishes about present status.

**Limits and remaining work**

- Later results without Steiner points; allowing Steiner points changes the question.
- Current resolution status was not established by a completed later-literature review.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
