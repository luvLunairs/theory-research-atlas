# Completeness for slowly growing imaginary potentials

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MODEL-401 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-401%3A+Completeness+for+slowly+growing+imaginary+potentials&target=Q-MODEL-401) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-401%3A+Completeness+for+slowly+growing+imaginary+potentials&target=Q-MODEL-401)

For 0<α≤2/3, is the eigensystem of −d²/dx²+i|x|^α complete on R, or on R+ with a Dirichlet condition?

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Unverified. **Last checked:** 2026-11-06.

**Status basis:** The half-line result extends beyond the previously recorded endpoint: Tumanov gives an α0<2/3 with completeness for α>α0. The remaining original range and the full-line case are not resolved by this inspection.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** The 2026-11-06 literature check identifies the versions and passages inspected; original publication dates and earlier checks remain relevant.

**Scope limits:** An operator-theoretic question under the stated domains and boundary conditions; it does not establish that the operator is an empirically adequate physical model.

**Information still needed**

- Identify the sharp remaining half-line range; the cited corollary supplies no explicit optimal α0.
- Check the full-line realization separately, including the even and odd sectors; do not transfer a Dirichlet theorem to it without justification.

**Primary branch:** [Spectral and operator theory in physics](../domains/mphy.md#mphy-spectral). **Related branches:** [Quantum theory and foundations](../domains/phys.md#phys-quant).

**Sources:** [Mathematical aspects of physics with non-self-adjoint operators: list of open problems](../sources.md#src-model-401); [Completeness theorem for the system of eigenfunctions of the complex Schrödinger operator L=-d²/dx²+cx^(2/3)](../sources.md#src-model-607); [Completeness theorem for the system of eigenfunctions of the complex Schrödinger operator L_c = -d²/dx² + cx^α](../sources.md#src-phys-800); [Open problems in non-self-adjoint spectral theory](../sources.md#src-phys-808).

**Exact locator:** Almog, AIM §1.1; Tumanov (2021), Theorem 1 and Corollary.

**Potential difficulty:** High. Non-selfadjoint spectral claims require control of infinite-dimensional operator domains, asymptotics or basis properties.

**Possible AI role:** A tool-using AI could compare resolvent estimates and test asymptotic constructions. This is a forecast; no named model has been evaluated on the task.

**Verification burden:** High. A proposed proof needs operator-domain and limiting-argument review. Finite spectral calculations require an independent implementation and cannot certify an infinite-dimensional claim.

**Resource expectations:** Analytic work may use a workstation for symbolic or spectral exploration. Numerical spectra cannot establish infinite-dimensional or uniform bounds.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** The previous endpoint-only summary understated the cited progress. Completeness, basis properties and full-line boundary conditions remain distinct; no AI success estimate has been measured.

**Further work:** resolve the statement and status questions above before planning an attempt. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-06

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Unverified.

Retain the original question and its unverified overall status, with the stronger known partial range recorded.

**Search scope:** Targeted searches and inspection of the cited passages on 2026-11-06; neither an exhaustive literature search nor an independent scientific review.

**Inspected evidence**

- [Completeness theorem for the system of eigenfunctions of the complex Schrödinger operator L_c = -d²/dx² + cx^α](../sources.md#src-phys-800) — Introduction; Theorem 1 and Corollary, pp. 2–3. For the defined Dirichlet realization on L²(R+), θ0(α) is continuous and exceeds the earlier angle threshold; the corollary explicitly covers some α below 2/3.

**Limits and remaining work**

- No optimal cutoff or remaining-case classification was established.
- The original AIM collection could not be reopened; its earlier inspection is retained.
- The cited proof was not independently verified.

<details>
<summary>Search queries</summary>

- "Completeness theorem" "Tumanov" "alpha"
- "nonselfadjointproblems.pdf"


</details>

### 2026-10-14

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Unverified.

The 2015 range is no longer wholly open: a later completeness theorem covers the half-line endpoint. The status of the remaining full original target is not established.

**Search scope:** Original source plus the specifically cited later primary paper, review or claim. Only the recorded queries and inspected locators are covered; this is not a complete bibliographic survey.

**Inspected evidence**

- [Mathematical aspects of physics with non-self-adjoint operators: list of open problems](../sources.md#src-model-401) — §1.1, Yaniv Almog. Original question or research direction located.
- [Completeness theorem for the system of eigenfunctions of the complex Schrödinger operator L=-d²/dx²+cx^(2/3)](../sources.md#src-model-607) — Abstract. The Dirichlet half-line endpoint alpha=2/3 is answered positively; the whole original interval and full-line formulation were not settled by the inspected statement.

**Limits and remaining work**

- Determine the remaining range 0<alpha<2/3 separately from the proved Dirichlet endpoint; full-line and half-line realizations must not be identified without proof.
- Statements were compared; proofs were not independently reproduced or formally verified.

<details>
<summary>Search queries</summary>

- Almog completeness imaginary potential alpha 2/3 Schrodinger 2015 2025
- non self adjoint AIM 2015 open problems status Almog Boulton
- "Completeness" "Tumanov" "2/3" Schrödinger
- "Tumanov" "319" "80" "99" completeness
- "Tumanov" "Completeness theorem" "2022"


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
