# Thermodynamic pairing order in the stripe regime of the square-lattice Hubbard model

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

Electron stripes and superconducting pairing compete or coexist in the Hubbard model. Pairing on a finite cluster may disappear as both dimensions grow; the source leaves this limit unresolved.

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-494%3A+Thermodynamic+pairing+order+in+the+stripe+regime+of+the+square-lattice+Hubbard+model&target=Q-MODEL-494) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-494%3A+Thermodynamic+pairing+order+in+the+stripe+regime+of+the+square-lattice+Hubbard+model&target=Q-MODEL-494)

[At a glance](#at-a-glance) · [The task](#problem) · [Resources and verification](#verification) · [Evidence and context](#evidence) · [AI trial assessment](#assessment) · [Research records](#audit-trail)

<a id="at-a-glance"></a>

## At a glance

| Field | Summary |
| --- | --- |
| Primary field | [Condensed matter and materials theory](../domains/phys.md#phys-cond) |
| Related fields | [Statistical and nonequilibrium physics](../domains/phys.md#phys-stat), [Quantum theory and foundations](../domains/phys.md#phys-quant) |
| Task origin | [Literature-origin question](../evidence-policy.md) |
| Current status | [Source reports open](../evidence-policy.md) · checked 2026-10-20 |
| AI suitability | [Exploratory](../ai-assessment.md) · Untested forecast |
| Scientific review | Pending |

<a id="problem"></a>

## The task

### Precise statement

For the zero-temperature repulsive square-lattice Hubbard model with nearest-neighbor hopping t, on-site repulsion U, t'=0 and hole doping delta=1/6, determine whether superconducting pairing persists in the two-dimensional thermodynamic limit at U/t=10 and at U/t=15, the two stronger-coupling stripe cases studied by Roth et al. Treat the two parameter cases separately.

**Required output:** Determine whether long-range superconducting order survives, with controlled treatment of finite-size and method errors.

**Scope:** Pairing in the source's strong-coupling stripe regime, not a complete phase diagram or a claim about every cuprate.

### Assumptions

- H=-t sum_&lt;ij&gt;,sigma (c†_i,sigma c_j,sigma+h.c.) +U sum_i n_i,up n_i,down on the square lattice; t&gt;0, no next-nearest hopping, and delta=1-N_e/N_sites=1/6. Consider zero temperature and U/t=10 and 15 separately.
- Specify lattice shape, boundaries and particle-number convention before comparing results.
- The two-dimensional limit requires both linear dimensions to grow; a fixed-width cylinder has a different limit.

### Success criteria

1. Specify a singlet-pair observable and long-range-order criterion, and assess its limit alongside stripe correlations. Explain how particle-number conservation and boundary pinning enter the estimator.
2. Report competing states and uncertainty from geometry, ansatz, optimization and sampling.
3. Identify numerical evidence as such; a rigorous theorem requires a separate proof.

### Background needed

- Fermionic many-body Hamiltonians
- Pair correlations and symmetry breaking
- Variational Monte Carlo or tensor-network methods
- Finite-size scaling and error analysis

<a id="verification"></a>

## Resources and verification

### Resource requirements

**Computing:** Substantial GPU/HPC resources may be necessary. Source Table 4 reports roughly 500 H200 GPU-hours for one 144-site training case and 10,000 for a 288-site case; these are author estimates, not project measurements or promised budgets.

**Data:** Model inputs are specified analytically; reuse numerical data only with documented parameters and provenance. Raw-data availability remains unchecked.

**Experiments:** None for the model calculation. Material-specific relevance needs independent empirical support.

**Theory and model requirements:** Ground-state conclusions depend on control of variational and extrapolation errors; a trial-state energy is only an upper bound.

**Validation modes:** Numerical evidence, Proof.

### Verification steps

1. Match hopping signs, doping, interaction strength, boundary conditions and observable normalization.
2. Benchmark small instances independently; retain convergence data, seeds and error estimates.
3. Compare more than one geometry and initial state; report limitations of the chosen state family.
4. Check the two-dimensional limit and distinguish pair formation from long-range order.

**Statement alignment:** Finite-size pairing or a lower variational energy alone does not prove superconductivity of the exact infinite-system ground state.

**Human review difficulty:** High: review requires many-body expertise and access to reproducible numerical evidence.

### Formal validity and empirical support

**What the formal task can establish:** A theorem needs exact assumptions; simulations provide evidence with stated systematic and statistical errors.

**Empirical support and limits:** A Hubbard-model result alone does not establish the mechanism of a particular material.

### Methods and obstacles

**Proposed methods:**

- Published neural-state and variational approaches
- Independent correlation estimators
- Comparison across geometries and numerical methods

**Expected obstacles:**

- Fermionic sign problem and variational bias
- Nearly competing states
- Finite clusters may not resolve pairing length scales
- Large independent calculations can be costly

### Checks still needed

- Independent reproduction
- Raw-data and software availability
- Completeness of later literature and parameter matching

<a id="evidence"></a>

## Evidence and context

**Status basis:** Roth et al. explicitly leave persistence of stripe-phase pairing unresolved. Inspected 2026 claims use different doping or hopping parameters; no resolution of this exact target was found.

[Dated literature checks and remaining limits](../candidates/Q-MODEL-494.md#literature-checks). These are editorial evidence checks, not signed expert reviews.

**Exact problem / theorem locator:** SRC-PHYS-003 section IV.3; SRC-PHYS-004 model parameters and discussion; SRC-PHYS-005 pp. 2-3.

### Sources

- [Superconductivity in the two-dimensional Hubbard model revealed by neural quantum states](../sources.md#src-phys-003). Christopher Roth; Ao Chen; Anirvan Sengupta; Antoine Georges. 2025. [Read source](https://arxiv.org/html/2511.07566v1).
  - **Relevant sections:** arXiv:2511.07566v1, 10 November 2025; section IV.3, section V and Appendix D Table 4.
  - **Source limitations:** Variational numerical results; the reported finite-cluster pairing does not establish thermodynamic long-range order.
- [Superconductivity in the t-t' Hubbard Model from Symmetry-Preserving Neural-Network Quantum States](../sources.md#src-phys-004). Riccardo Rende; Luciano Loris Viteritti; Antoine Georges. 2026. [Read source](https://arxiv.org/html/2608.12465v1).
  - **Relevant sections:** arXiv:2608.12465v1, 12 August 2026; model definition, superconducting correlations and discussion.
  - **Source limitations:** Different parameters from the indexed 1/6-doped, t'=0 target; variational evidence is not an exact ground-state proof.
- [Topological Melting of Magnetic Stripes and the Emergence of Macroscopic d-wave Superconductivity in the 2D Hubbard Model](../sources.md#src-phys-005). Jin Hyung Cho. 2026. [Read source](https://arxiv.org/pdf/2606.07634v2).
  - **Relevant sections:** arXiv:2606.07634v2, revised 10 September 2026; abstract and pp. 2-3, equation (1) and parameters.
  - **Source limitations:** The inspected setup uses U/t=6 and nonzero t'/t, unlike the indexed target. Its broad conclusions were not independently evaluated.

### Known results and partial progress

- SRC-PHYS-003 reports pairing in a 144-site stripe state and explicitly leaves the thermodynamic question open.
- SRC-PHYS-004 reports later superconductivity evidence at delta=1/8, U/t=8, t'/t=-0.2; these parameters differ.
- SRC-PHYS-005 makes broad resolution claims but uses U/t=6 and nonzero t'/t in the inspected setup.

**Research value:** Clarifying intertwined orders in a central interacting-electron model would improve theoretical understanding of correlated superconductivity.

### Related problems

No formal dependency or equivalence is asserted.

### Scope of the status check

**Finding:** Inspected later claims do not match the indexed parameters.

**Search limits:** Targeted search; no independent evaluation of published numerical conclusions.

<details>
<summary>Literature references checked</summary>

**Queries used:**

- "Hubbard" "stripe" "thermodynamic" "2026" superconductivity
- "2511.07566" superconductivity 2026
- Hubbard superconductivity one sixth doping stripes 2026 thermodynamic Roth
- "Hubbard" "1/6" "thermodynamic"

**Sources checked:**

- [Superconductivity in the two-dimensional Hubbard model revealed by neural quantum states](../sources.md#src-phys-003)
- [Superconductivity in the t-t' Hubbard Model from Symmetry-Preserving Neural-Network Quantum States](../sources.md#src-phys-004)
- [Topological Melting of Magnetic Stripes and the Emergence of Macroscopic d-wave Superconductivity in the 2D Hubbard Model](../sources.md#src-phys-005)

</details>

<details>
<summary>Previous attempts and public records</summary>

- Published simulations in SRC-PHYS-003 and related work provide context; no project attempt has been run.

</details>

<details>
<summary>Attribution and suggested citation</summary>

**Original authors and credited contributors:**

- Christopher Roth
- Ao Chen
- Anirvan Sengupta
- Antoine Georges

**Suggested citation:** Roth, Chen, Sengupta and Georges, Superconductivity in the two-dimensional Hubbard model revealed by neural quantum states, arXiv:2511.07566v1 (2025), section IV.3; cite the related studies separately when used.

**Editorial credit:** Compiled for Theory Research Atlas with Codex assistance.

</details>

<a id="assessment"></a>

## AI trial assessment

**Label:** [Exploratory](../ai-assessment.md). **Evidence:** Untested forecast. **Assessed:** 2026-10-20.

AI may help compare methods, implement diagnostics and audit uncertainty; full ground-state inference remains demanding.

**Model or capability conditions:** A model able to inspect primary literature and use scientific code, with specialist oversight; no specific model benchmarked.

**Uncertainty:** No research model has been tested on this task by the project; capability and resource expectations remain provisional.

Ratings are separate judgments, not a score. High expertise needed or verification difficulty means a larger burden; high method availability or checkability means stronger support.

| Dimension | Rating | Reason |
| --- | --- | --- |
| Statement clarity | High | Hamiltonian, doping and two parameter cases are fixed; each attempt must state which case and order criterion it addresses. |
| Decomposability | Medium | Geometry, estimator and optimization checks can be separated. |
| Methods and literature | High | Several established numerical approaches provide comparison points. |
| Search / symbolic fit | Medium | Code and algebra help, while unrestricted many-body optimization remains difficult. |
| Checkability | Low | Independent large-system checks may themselves be expensive. |
| Expertise needed | High | Specialists must assess competing orders and systematic errors. |
| Scholarly significance | High | The question addresses correlated superconductivity in a widely studied model. |
| Verification difficulty | High | Close energies and different finite-size limits complicate review. |

**Correctness:** Not assessed.

No candidate solution supplied.

**Novelty:** Not assessed.

Newness depends on exact parameters and future literature checks.

<details>
<summary>Difficulty and significance</summary>

**Difficulty:** High.

Thermodynamic many-body inference and competing orders remain difficult.

**Evidence type:** Source's explicit limit question and reported numerical cost..

**Significance:** High.

Intertwined electronic orders are central to correlated superconductivity.

</details>

<a id="audit-trail"></a>

## Research records

No project attempts or human reviews have been recorded.

<details>
<summary>Changes to this problem</summary>

| Date | Change |
| --- | --- |
| 2026-10-20 | Recorded the thermodynamic target and distinguished later claims with different parameters. |

</details>

<details>
<summary>Record information</summary>

| Field | Recorded value |
| --- | --- |
| Stable ID | `Q-MODEL-494` |
| Duplicate key | `phys:hubbard-square:tprime0:doping1-6:stripe-pairing-thermodynamic` |
| Original domain label | Condensed matter theory |
| Original cross-domain labels | Statistical physics; Quantum theory |
| Primary domain ID | `PHYS.COND` |
| Cross-domain IDs | `PHYS.STAT`, `PHYS.QUANT` |
| Origin code | `literature_open` |
| Status code | `source_reports_open` |
| Curator-designed scope | No |
| Detailed entry | Yes |
| Record level | `C` |
| Human review status | `pending` |
| Trial-label code | `exploratory` |
| Assessment-evidence code | `untested_forecast` |
| Method tags | `model_analysis`, `numerical_computation`, `bounds` |
| Validation tags | `numerical_evidence`, `pure_proof` |
| Experimental-dependency tag | `none_for_formal_task` |

[JSON record](../../data/cards/Q-MODEL-494.json)

</details>

[Problem cards](README.md) · [Back to top](#at-a-glance)
