# Connecting regularized quasi-densities to physical densities

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MODEL-421 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-421%3A+Connecting+regularized+quasi-densities+to+physical+densities&target=Q-MODEL-421) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-421%3A+Connecting+regularized+quasi-densities+to+physical+densities&target=Q-MODEL-421)

Relate the quasi-densities used to regularize density functional theory systematically to measurable densities and their exact constraints.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Unverified. **Last checked:** 2026-11-26.

**Status basis:** An explicit reconstruction is already available for Moreau–Yosida regularization at fixed potential. The 2026 perspective explains which representability properties belong to the physical density and gives a choice-dependent interpretation of the mixed density. The broader transfer of constraints to approximate functionals remains to be specified.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** The 2026-11-26 literature check identifies the publications, versions and limits covered.

**Scope limits:** For a regularized minimizer x, potential v, parameter ε and the specified duality map J, the physical density is x + εJ⁻¹(v). Positivity and particle-number normalization of the reconstructed density need not hold for x.

**Information still needed**

- Name the density and potential spaces, external potential and exact constraint to be transferred.
- Identify which proposed constraint or approximation goes beyond the published reconstruction and its physical interpretation.

**Primary branch:** [Quantum chemistry and electronic structure](../domains/chem.md#chem-quant). **Related branches:** [Spectral and operator theory in physics](../domains/mphy.md#mphy-spectral).

**Sources:** [Some Problems in Density Functional Theory](../sources.md#src-model-402); [Density-potential inversion from Moreau–Yosida regularization](../sources.md#src-phys-906); [Perspective on Moreau–Yosida regularization in density-functional theory](../sources.md#src-phys-907).

**Exact locator:** Wrighton et al., Question 2.2 and remark. Penz, Csirik and Laestadius (2023), equations (6)–(9). Penz et al. (2026), equation (57) and following discussion.

**Potential difficulty:** High. The questions concern unresolved functional-analytic or approximation foundations of electronic-structure theory.

**Possible AI role:** A tool-using AI could derive maps and track which exact density constraints survive. This is a forecast; no named model has been evaluated on the task.

**Verification burden:** High. Check the density and potential spaces, representability, differentiability and boundary conditions. Benchmark agreement does not establish a functional inequality or a uniqueness theorem.

**Resource expectations:** Proof work and small electronic examples may fit a workstation; accurate correlated-electron reference calculations can be expensive. No general resource bound is established.

**Assessment:** 2026-11-26; untested forecast. **Uncertainty:** The published reconstruction assumes a fixed potential and duality map. Whether an exact constraint can guide a practical approximation still depends on the spaces and functional chosen.

**Further work:** resolve the statement and status questions above before planning an attempt. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-26

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Unverified.

Record the exact reconstruction as known and retain the broader program with unverified overall status.

**Search scope:** For a regularized minimizer x, potential v, parameter ε and the specified duality map J, the physical density is x + εJ⁻¹(v). Positivity and particle-number normalization of the reconstructed density need not hold for x.

**Inspected evidence**

- [Some Problems in Density Functional Theory](../sources.md#src-model-402) — Question 2.2 and its remark. Asks for a systematic connection with physical densities and their properties used in approximate functionals.
- [Density-potential inversion from Moreau–Yosida regularization](../sources.md#src-phys-906) — Equation (9) and following paragraph. Gives the physical density associated with a specified regularized minimizer and potential.
- [Perspective on Moreau–Yosida regularization in density-functional theory](../sources.md#src-phys-907) — Equation (57) and following discussion. Explains which representability conditions can fail for the mixed density and how an electrostatic interpretation depends on the topology.

**Limits and remaining work**

- No comprehensive classification of transferred constraints or experimental test was located.

<details>
<summary>Search queries</summary>

- 2025 2026 Moreau Yosida physical densities quasidensities electron density Legendre regularization Kvaal Wrighton question 2.2 density representability exact constraints Penz
- 2025 2026 density-potential Moreau–Yosida Penz quasi densities physical densities regularization constraints direct physical interpretation 022001


</details>

### 2026-10-14

**Coverage:** Statement only. **Statement:** Needs clarification.

**Recorded status:** Unverified → Unverified.

The historical source matches the indexed question. Targeted keyword searches did not establish a later primary result resolving its full scope; present-day openness remains unverified.

**Search scope:** Original source and recorded targeted searches. No later primary result matching the full target was established; statement-only denotes this evidence limit, not absence of a search.

**Inspected evidence**

- [Some Problems in Density Functional Theory](../sources.md#src-model-402) — §III B, Question 2.2. Original question or research direction located.

**Limits and remaining work**

- Specify regularization, topology and reconstruction error; the paper's cited regularization construction requires closer review.
- Only the recorded search terms were covered; later results, different terminology, corrections and exact-scope resolutions may have been missed.

<details>
<summary>Search queries</summary>

- "quasi-densities" regularized density functional theory 2025


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
