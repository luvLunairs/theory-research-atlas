# Enumerate equilibria of a supplied rational bimatrix game

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MODEL-003 · Full card available.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-003%3A+Enumerate+equilibria+of+a+supplied+rational+bimatrix+game&target=Q-MODEL-003) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-003%3A+Enumerate+equilibria+of+a+supplied+rational+bimatrix+game&target=Q-MODEL-003)

Given rational m by n payoff matrices with m,n <= 3 and a certified nondegeneracy assumption, reproduce support enumeration and output every Nash equilibrium with exact best-response certificates. Degenerate inputs must be flagged for a separate full-set treatment.

**Origin:** Known-result calibration. **Curator-designed scope:** Yes.

**Current status:** Known result in literature. **Last checked:** 2026-10-13.

**Status basis:** The opened author survey gives support enumeration and explains its nondegeneracy requirement. The <=3 restriction is a curator-selected calibration scope.

**Statement check:** Source located. **Status check:** Source report only.

**Source date and freshness:** Recorded source years: SRC-MODEL-007: 2021. The last-checked date records the scope described in the status basis; it is not a comprehensive literature-search date.

**Scope limits:** Use the full card for assumptions and validation limits.

**Information still needed**

- Set an input numerator/denominator bit-length bound before benchmarking resource use.
- Select and review the independent nondegeneracy check.
- A future extension to degenerate games must represent equilibrium continua and cite the relevant full-set method.

**Primary branch:** [Game and equilibrium theory](../domains/econ.md#econ-game). **Related branches:** [Algorithms and data structures](../domains/cs.md#cs-alg), [Optimization and operations research](../domains/math.md#math-opt).

**Sources:** [Finding Nash Equilibria of Two-Player Games](../sources.md#src-model-007).

**Exact locator:** von Stengel Section 2, Definition 2, Propositions 1 and 3, Algorithm 4; Section 7

**Potential difficulty:** Medium. A finite support search and exact certificates permit independent checking. The source's fully specified example makes the trial transferable without inventing new economic claims.

**Possible AI role:** No named model evaluated; assumes tool-using AI with literature retrieval, exact algebra or rational linear algebra, code generation, and access to a human domain reviewer.

**Verification burden:** Medium. Checking one equilibrium is simple; certifying the whole list and rejecting degenerate inputs is harder.

**Resource expectations:** Experiment: None for equilibrium computation. Behavioral interpretation requires a separate empirical study. Data: Only declared payoff matrices; no personal, market or experimental data are needed. Computation: At most 3 by 3 matrices with a declared bit-length bound to be set in the trial. Small support enumeration is a plausible local workload; no time, cost or success measurements exist.

**Assessment:** 2026-10-13; untested forecast. **Uncertainty:** No named model or solver was run. Reproducing familiar examples may reflect memorization. General bimatrix complexity cannot be inferred from the small trial.

[Read the full card](../cards/Q-MODEL-003.md). **Human review:** Pending.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
