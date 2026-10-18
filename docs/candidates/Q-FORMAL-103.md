# Check twisted-state spectra on Kuramoto cycle networks

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-103 · Full card available.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-103%3A+Check+twisted-state+spectra+on+Kuramoto+cycle+networks&target=Q-FORMAL-103) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-103%3A+Check+twisted-state+spectra+on+Kuramoto+cycle+networks&target=Q-FORMAL-103)

For the simple undirected cycle C_n, n >= 3, consider theta_dot_j = sin(theta_(j-1)-theta_j) + sin(theta_(j+1)-theta_j), with indices modulo n and phases modulo 2 pi. Reproduce the equilibrium and Jacobian spectrum for theta_j = 2 pi q j/n, 0 <= q <= floor(n/2), and classify linear stability modulo uniform rotation. Build an exact sign table only for 3 <= n <= 20. Extra zero eigenvalues must be labeled inconclusive for nonlinear stability. The finite range is curator chosen.

**Origin:** Known-result calibration. **Curator-designed scope:** Yes.

**Current status:** Known result in literature. **Last checked:** 2026-10-14.

**Status basis:** The spectrum is a known result in the opened paper. Later work preserves the distinction between second-order criticality and nonlinear stability. No table or simulation has been produced by this project.

**Statement check:** Source located. **Status check:** Source report only.

**Source date and freshness:** Recorded source years: SRC-FORMAL-104: 2020, SRC-FORMAL-106: 2026. The last-checked date records the scope described in the status basis; it is not a comprehensive literature-search date.

**Scope limits:** Use the full card for assumptions and validation limits.

**Information still needed**

- Select a representation for exact trigonometric signs before implementation.
- Have a reviewer approve terminology for asymptotic stability modulo rotation.

**Primary branch:** [Dynamics on networks and collective behavior](../domains/net.md#net-dynamics). **Related branches:** [Dynamical systems and ergodic theory](../domains/math.md#math-dyn), [Combinatorics and discrete mathematics](../domains/math.md#math-comb).

**Sources:** [Dense networks that do not synchronize and sparse ones that do](../sources.md#src-formal-104); [Benign landscapes for synchronization on spheres via normalized Laplacian matrices](../sources.md#src-formal-106).

**Exact locator:** Townsend et al., equations (4)-(5) and Section II.1; McRae, Section 1.2

**Potential difficulty:** Medium. The known formula and a bounded exact table independently check symbolic reasoning and symmetry handling without relying on trajectories as proof.

**Possible AI role:** No named model evaluated; assumes a tool-using AI that can read mathematical sources, produce inspectable symbolic work and code, and work with a human domain reviewer.

**Verification burden:** Medium. The algebra is compact, but a wrong stability interpretation would overstate the result.

**Resource expectations:** Experiment: None for the idealized ODE calculation. Physical or biological comparisons require separate observations or experiments. Data: Cycle edges, n and q; no empirical time series. Computation: Symbolic differentiation and matrices of order at most twenty for the finite table. Exact trigonometric reasoning avoids numerical optimization. The bounds are chosen for inspectability; no runtime, cost or success rate has been measured.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No model calculation or simulation has been tested. Degenerate cases intentionally receive no nonlinear verdict.

[Read the full card](../cards/Q-FORMAL-103.md). **Human review:** Pending.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
