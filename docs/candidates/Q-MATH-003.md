# Determine the four-color triangle Ramsey number R(3,3,3,3)

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MATH-003 · Full card available.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MATH-003%3A+Determine+the+four-color+triangle+Ramsey+number+R%283%2C3%2C3%2C3%29&target=Q-MATH-003) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MATH-003%3A+Determine+the+four-color+triangle+Ramsey+number+R%283%2C3%2C3%2C3%29&target=Q-MATH-003)

Determine the least positive integer N such that every map from the unordered pairs of {1,...,N} to {1,2,3,4} gives some three distinct vertices whose three pair colors are equal.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Open after scoped check. **Last checked:** 2026-10-13.

**Status basis:** The April 2026 author-maintained survey explicitly calls this open and states 51 <= N <= 62. Targeted October 2026 searches found no source establishing an exact value; the inspected recent-sounding multiplicity paper addresses a different quantity. This is a scoped literature check, not proof that no solution exists.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Recorded source years: SRC-MATH-001: 2026, SRC-MATH-013: 2004, SRC-MATH-014: 2023. The last-checked date records the scope described in the status basis; it is not a comprehensive literature-search date.

**Scope limits:** Use the full card for assumptions and validation limits.

**Information still needed**

- Inspect Chung's original lower-bound construction and obtain a corrected machine-readable witness.
- Audit the full upper-bound paper and available code before adopting its implementation.
- Perform a focused citation-forward review after April 2026 in addition to this web search.
- Select a genuinely bounded research subproblem only after expert review; do not treat the full question as the first cheap AI trial.
- Estimate computation and proof-checker storage only after selecting a method.

**Primary branch:** [Extremal and Ramsey theory](../domains/math.md#math-comb-ext). **Related branches:** [Algorithms and data structures](../domains/cs.md#cs-alg), [Optimization and operations research](../domains/math.md#math-opt).

**Sources:** [Small Ramsey Numbers, Dynamic Survey DS1, revision 18](../sources.md#src-math-001); [An Upper Bound of 62 on the Classical Ramsey Number R(3,3,3,3)](../sources.md#src-math-013); [The Four-Color Ramsey Multiplicity of Triangles](../sources.md#src-math-014).

**Exact locator:** DS1.18 section 6.1.1, printed page 56 (PDF page index 55); Fettes–Kramer–Radziszowski abstract; Kiem–Pokutta–Spiegel section 2.

**Potential difficulty:** High. Precise objects and locally verifiable constructions offer a credible role for tool-using AI in literature synthesis, encoding audit, or designing bounded subproblems. The exact unrestricted target requires substantial combinatorial expertise and may exceed available resources.

**Possible AI role:** No named model evaluated; assumes tool-using AI capable of reading advanced combinatorics, writing exact graph code, and working under specialist human review.

**Verification burden:** High. Upper-bound completeness, solver proof artifacts, and symmetry reductions can dominate review.

**Resource expectations:** Experiment: None; a mathematical finite-coloring problem. Data: Public papers and, for a future attempt, existing lower-bound colorings with checked provenance. No empirical dataset required. Computation: Unassessed and potentially substantial. The naive space at N vertices is 4^(N*(N-1)/2). Structural restrictions, solver complexity, certificate storage, and checking cost require separate planning. No hardware, runtime, fee, or affordable-solution promise is made.

**Assessment:** 2026-10-13; untested forecast. **Uncertainty:** No named model or project attempt was evaluated. Public computer-assisted mathematics supports the method family, not a measured AI ability to improve these bounds. A solution newer than the scoped search may exist.

[Read the full card](../cards/Q-MATH-003.md). **Human review:** Pending.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
