# Existence and uniqueness in the TDDFT force equation

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MODEL-431 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-431%3A+Existence+and+uniqueness+in+the+TDDFT+force+equation&target=Q-MODEL-431) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-431%3A+Existence+and+uniqueness+in+the+TDDFT+force+equation&target=Q-MODEL-431)

For a prescribed time-dependent density n(r,t) and compatible initial state, under what hypotheses does the continuum force-balance equation (22) admit a potential w(r,t) that is unique once its purely time-dependent gauge freedom is fixed? Specify the boundary conditions and the spaces of admissible densities and potentials.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Unverified. **Last checked:** 2026-11-28.

**Status basis:** Ruggenthaler and van Leeuwen recast the inversion as an iteration on potentials. The problem collection asks which function space and bounds justify contraction in its continuum formulation. For a two-particle spin-singlet Hubbard dimer, Cancès and Duez report global representability with nonunique effective potentials at singular times. That finite-lattice result leaves the continuum question unsettled.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** The 28 November 2026 check covers the works and passages listed in the literature record.

**Scope limits:** The continuum question requires compatible initial data, a choice of gauge, boundary conditions and control of the response. The dimer preprint treats a two-site system.

**Information still needed**

- Identify the density and potential spaces in which the response estimate holds and address possible zero modes after gauge fixing.

**Primary branch:** [Quantum chemistry and electronic structure](../domains/chem.md#chem-quant). **Related branches:** [Spectral and operator theory in physics](../domains/mphy.md#mphy-spectral).

**Sources:** [Some Problems in Density Functional Theory](../sources.md#src-model-402); [Global fixed point proof of time-dependent density-functional theory](../sources.md#src-phys-925); [V-Representability Beyond Singular Times in Time-Dependent Density Functional Theory: The Hubbard Dimer Case](../sources.md#src-phys-926).

**Exact locator:** Wrighton and coauthors, section VII, equation (22), Question 8.2 and Issue 9. Ruggenthaler and van Leeuwen, fixed-point argument. Cancès and Duez, Hubbard-dimer abstract.

**Potential difficulty:** High. The questions concern unresolved functional-analytic or approximation foundations of electronic-structure theory.

**Possible AI role:** A tool-using AI could audit contraction estimates and potential-to-density consistency. This is a forecast; no named model has been evaluated on the task.

**Verification burden:** High. Check the density and potential spaces, representability, differentiability and boundary conditions. Benchmark agreement does not establish a functional inequality or a uniqueness theorem.

**Resource expectations:** Proof work and small electronic examples may fit a workstation; accurate correlated-electron reference calculations can be expensive. No general resource bound is established.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** Specify density positivity, boundaries, stress-functional regularity and gauge; assess the cited proposed proof rather than assume no answer exists.

**Further work:** resolve the statement and status questions above before planning an attempt. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-28

**Coverage:** Statement and later literature. **Statement:** Corrected.

**Recorded status:** Unverified → Unverified.

Ruggenthaler and van Leeuwen recast the inversion as an iteration on potentials. The problem collection asks which function space and bounds justify contraction in its continuum formulation. For a two-particle spin-singlet Hubbard dimer, Cancès and Duez report global representability with nonunique effective potentials at singular times. That finite-lattice result leaves the continuum question unsettled.

**Search scope:** The continuum question requires compatible initial data, a choice of gauge, boundary conditions and control of the response. The dimer preprint treats a two-site system.

<details>
<summary>Previous indexed wording</summary>

Prove suitable existence and uniqueness results for the density-to-potential force equation (22), accounting for the proposed fixed-point answer discussed in §VII A.

The current statement appears at the top of this page.
</details>

**Inspected evidence**

- [Some Problems in Density Functional Theory](../sources.md#src-model-402) — Section VII, Question 8.2 and Issue 9. Asks for a proof for equation (22) and identifies the missing choice of space and contraction bounds in the proposed answer.
- [Global fixed point proof of time-dependent density-functional theory](../sources.md#src-phys-925) — Abstract and existence argument in the manuscript, including the uniform bound for the iteration. Formulates density-to-potential inversion as a fixed-point problem and gives an iterative argument subject to bounds on the response.
- [V-Representability Beyond Singular Times in Time-Dependent Density Functional Theory: The Hubbard Dimer Case](../sources.md#src-phys-926) — Abstract, October 2026, two-particle spin-singlet Hubbard dimer. The authors obtain global representability in the conventional and geometric dimer formulations and report nonuniqueness of the effective potential at singular times.

**Limits and remaining work**

- Identify the density and potential spaces in which the response estimate holds and address possible zero modes after gauge fixing.

<details>
<summary>Search queries</summary>

- TDDFT density potential inverse force equation continuum fixed point contraction singular times Hubbard dimer Cancès Duez


</details>

### 2026-10-14

**Coverage:** Statement only. **Statement:** Needs clarification.

**Recorded status:** Unverified → Unverified.

The historical source matches the indexed question. Targeted keyword searches did not establish a later primary result resolving its full scope; present-day openness remains unverified.

**Search scope:** Original source and recorded targeted searches. No later primary result matching the full target was established; statement-only denotes this evidence limit, not absence of a search.

**Inspected evidence**

- [Some Problems in Density Functional Theory](../sources.md#src-model-402) — §VII, Question 8.2 and section VII A. Original question or research direction located.

**Limits and remaining work**

- Assess the cited fixed-point answer in its precise function spaces, density positivity, boundary and gauge assumptions.
- Only the recorded search terms were covered; later results, different terminology, corrections and exact-scope resolutions may have been missed.

<details>
<summary>Search queries</summary>

- "TDDFT" "force equation" "uniqueness" 2025


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
