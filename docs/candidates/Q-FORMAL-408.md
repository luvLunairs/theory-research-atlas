# Counting simple polygonalizations in polynomial time

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-408 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-408%3A+Counting+simple+polygonalizations+in+polynomial+time&target=Q-FORMAL-408) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-408%3A+Counting+simple+polygonalizations+in+polynomial+time&target=Q-FORMAL-408)

Can the number of non-self-intersecting polygonalizations using every point of a planar n-point set as a vertex be computed in polynomial time?

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Open after scoped check. **Last checked:** 2026-11-06.

**Status basis:** TOPP's June 2025 update and Alegría et al. (2025) report general exact counting as open. Eppstein's output-polynomial enumeration result does not give polynomial time in the input size alone. The recorded update search on 2026-11-06 found no accepted resolution of the exact counting target.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** TOPP revision: 18 June 2025; inspected journal papers published 18 July 2024 and 15 March 2025.

**Scope limits:** The target is exact counting in input-polynomial time. Output-polynomial enumeration, approximation of the logarithm of the count and monotone special cases do not settle it.

**Information still needed**

- The scoped search does not exclude a later exact-counting algorithm or hardness result.

**Primary branch:** [Computational geometry and topology](../domains/cs.md#cs-geom). **Related branches:** None recorded.

**Sources:** [The Open Problems Project: Problem 16](../sources.md#src-formal-408); [Non-crossing Hamiltonian Paths and Cycles in Output-Polynomial Time](../sources.md#src-math-701); [Upward Pointset Embeddings of Planar st-Graphs](../sources.md#src-math-706).

**Exact locator:** TOPP Problem 16: Statement and June 2025 update; Eppstein (2024), Sections 1 and 6; Alegría et al. (2025), Section 1

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

**Recorded status:** Unverified → Open after scoped check.

The inspected later results do not resolve the retained exact counting question. Record scoped openness without equating an output-size bound with an input-size bound.

**Search scope:** Compared TOPP Problem 16 with two later journal articles and targeted web searches for counting complexity updates; distinguished counting, listing and monotone restrictions.

**Inspected evidence**

- [The Open Problems Project: Problem 16](../sources.md#src-formal-408) — Statement; Status/Conjectures; 18 June 2025 revision. Poses the exact polynomial-time counting question and labels it open.
- [Non-crossing Hamiltonian Paths and Cycles in Output-Polynomial Time](../sources.md#src-math-701) — Abstract; Sections 1 and 6. Provides output-polynomial listing and discusses the unresolved exact-counting complexity.
- [Upward Pointset Embeddings of Planar st-Graphs](../sources.md#src-math-706) — Section 1, paragraphs after the contribution list. Explicitly retains general polygonalization counting as open and separates its monotone enumeration result.

**Limits and remaining work**

- The update search is not exhaustive.
- No proof or algorithm was independently audited.
- Human review remains pending.

<details>
<summary>Search queries</summary>

- "counting polygonalizations" complexity
- "polygonalizations" counting complexity 2026
- "counting polygonalizations" polynomial 2025 2026


</details>

### 2026-10-14

**Coverage:** Statement only. **Statement:** Matched.

**Recorded status:** Unverified → Unverified.

The source supports identifying this question, but does not establish its present unresolved status.

**Search scope:** Inspected the named source statement and its recorded qualifications; no comprehensive citation-chain or specialist database review.

**Inspected evidence**

- [The Open Problems Project: Problem 16](../sources.md#src-formal-408) — TOPP Problem 16: Statement; June 2025 update. The source identifies the indexed question or research direction; its original date and any recorded partial results limit what it establishes about present status.

**Limits and remaining work**

- Resolutions or hardness results after the June 2025 update.
- Current resolution status was not established by a completed later-literature review.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
