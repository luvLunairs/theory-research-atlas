# Thermodynamic pairing order in the stripe regime of the square-lattice Hubbard model

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MODEL-494 · Full card available.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-494%3A+Thermodynamic+pairing+order+in+the+stripe+regime+of+the+square-lattice+Hubbard+model&target=Q-MODEL-494) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-494%3A+Thermodynamic+pairing+order+in+the+stripe+regime+of+the+square-lattice+Hubbard+model&target=Q-MODEL-494)

For the zero-temperature repulsive square-lattice Hubbard model with nearest-neighbor hopping t, on-site repulsion U, t'=0 and hole doping delta=1/6, determine whether superconducting pairing persists in the two-dimensional thermodynamic limit at U/t=10 and at U/t=15, the two stronger-coupling stripe cases studied by Roth et al. Treat the two parameter cases separately.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-10-20.

**Status basis:** Roth et al. explicitly leave persistence of stripe-phase pairing unresolved. Inspected 2026 claims use different doping or hopping parameters; no resolution of this exact target was found.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Primary version and later inspected evidence are dated in the source records; checked on 2026-10-20.

**Scope limits:** Pairing in the source's strong-coupling stripe regime, not a complete phase diagram or a claim about every cuprate.

**Information still needed**

- Independent reproduction
- Raw-data and software availability
- Completeness of later literature and parameter matching

**Primary branch:** [Condensed matter and materials theory](../domains/phys.md#phys-cond). **Related branches:** [Statistical and nonequilibrium physics](../domains/phys.md#phys-stat), [Quantum theory and foundations](../domains/phys.md#phys-quant).

**Sources:** [Superconductivity in the two-dimensional Hubbard model revealed by neural quantum states](../sources.md#src-phys-003); [Superconductivity in the t-t' Hubbard Model from Symmetry-Preserving Neural-Network Quantum States](../sources.md#src-phys-004); [Topological Melting of Magnetic Stripes and the Emergence of Macroscopic d-wave Superconductivity in the 2D Hubbard Model](../sources.md#src-phys-005).

**Exact locator:** SRC-PHYS-003 section IV.3; SRC-PHYS-004 model parameters and discussion; SRC-PHYS-005 pp. 2-3.

**Potential difficulty:** Frontier. Thermodynamic many-body inference and competing orders remain difficult.

**Possible AI role:** AI may help compare methods, implement diagnostics and audit uncertainty; full ground-state inference remains demanding. A model able to inspect primary literature and use scientific code, with specialist oversight; no specific model benchmarked.

**Verification burden:** High. Finite-size pairing or a lower variational energy alone does not prove superconductivity of the exact infinite-system ground state.

**Resource expectations:** Experiment: None for the model calculation. Material-specific relevance needs independent empirical support. Data: Model inputs are specified analytically; reuse numerical data only with documented parameters and provenance. Raw-data availability remains unchecked. Computation: Substantial GPU/HPC resources may be necessary. Source Table 4 reports roughly 500 H200 GPU-hours for one 144-site training case and 10,000 for a 288-site case; these are author estimates, not project measurements or promised budgets. Assumptions: Ground-state conclusions depend on control of variational and extrapolation errors; a trial-state energy is only an upper bound.

**Assessment:** 2026-10-20; untested forecast. **Uncertainty:** No research model has been tested on this task by the project; capability and resource expectations remain provisional.

[Read the full card](../cards/Q-MODEL-494.md). **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-10-20

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Source reports open.

Roth et al. explicitly leave persistence of stripe-phase pairing unresolved. Inspected 2026 claims use different doping or hopping parameters; no resolution of this exact target was found.

**Search scope:** Opened the originating full text and inspected later primary sources for matching assumptions and resolution claims.

**Inspected evidence**

- [Superconductivity in the two-dimensional Hubbard model revealed by neural quantum states](../sources.md#src-phys-003) — arXiv:2511.07566v1, 10 November 2025; section IV.3, section V and Appendix D Table 4. An explicitly unresolved thermodynamic pairing question for the stripe regime at hole doping 1/6 and t'=0.
- [Superconductivity in the t-t' Hubbard Model from Symmetry-Preserving Neural-Network Quantum States](../sources.md#src-phys-004) — arXiv:2608.12465v1, 12 August 2026; model definition, superconducting correlations and discussion. Later superconductivity evidence at hole doping 1/8, U/t=8 and t'/t=-0.2.
- [Topological Melting of Magnetic Stripes and the Emergence of Macroscopic d-wave Superconductivity in the 2D Hubbard Model](../sources.md#src-phys-005) — arXiv:2606.07634v2, revised 10 September 2026; abstract and pp. 2-3, equation (1) and parameters. A later broad superconductivity claim was checked against its explicit Hamiltonian parameters.

**Limits and remaining work**

- Targeted search; no independent evaluation of published numerical conclusions.
- Human review is pending; source inspection is not a scientific review verdict.

<details>
<summary>Search queries</summary>

- "Hubbard" "stripe" "thermodynamic" "2026" superconductivity
- "2511.07566" superconductivity 2026
- Hubbard superconductivity one sixth doping stripes 2026 thermodynamic Roth
- "Hubbard" "1/6" "thermodynamic"


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
