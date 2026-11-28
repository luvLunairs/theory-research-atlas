# Schauder bases for periodic trigonometric Schrödinger potentials

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MODEL-410 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-410%3A+Schauder+bases+for+periodic+trigonometric+Schr%C3%B6dinger+potentials&target=Q-MODEL-410) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-410%3A+Schauder+bases+for+periodic+trigonometric+Schr%C3%B6dinger+potentials&target=Q-MODEL-410)

For −d²/dx² + V(x) on (0,π) with periodic boundary conditions and V(x) = Σ_{k=−m}^m vₖ exp(2ikx), which complex coefficient tuples (v₋ₘ,…,vₘ) give a Schauder basis of eigenfunctions in L²(0,π)?

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Unverified. **Last checked:** 2026-11-28.

**Status basis:** Mityagin gives an exact test for V(x) = exp(−2ix) + b exp(2ix), namely |b| = 1. Earlier work with Djakov proves that for a exp(−2ix) + B exp(4ix), with a and B nonzero, even the root functions fail to form a basis under periodic boundary conditions. The general coefficient classification has no verified current status here.

**Statement check:** Source located. **Status check:** Source report only.

**Source date and freshness:** The 28 November 2026 check covers the works and passages listed in the literature record.

**Scope limits:** The problem sheet asks about eigenfunctions. Root-function theorems may add generalized eigenvectors at defective eigenvalues.

**Information still needed**

- For any proposed general coefficient criterion, specify how multiple eigenvalues are treated and compare its scope with known root-function criteria.

**Primary branch:** [Spectral and operator theory in physics](../domains/mphy.md#mphy-spectral). **Related branches:** [Quantum theory and foundations](../domains/phys.md#phys-quant).

**Sources:** [Mathematical aspects of physics with non-self-adjoint operators: list of open problems](../sources.md#src-model-401); [Schauder basis for Schrödinger operators with periodic boundary conditions](../sources.md#src-phys-923); [Convergence of spectral decompositions of Hill operators with trigonometric polynomial potentials](../sources.md#src-phys-924).

**Exact locator:** Mityagin, 2015 AIM sheet 23, Open Problem and Known Case. Djakov and Mityagin, abstract, cases (i) and (ii).

**Potential difficulty:** High. Non-selfadjoint spectral claims require control of infinite-dimensional operator domains, asymptotics or basis properties.

**Possible AI role:** A tool-using AI could compare Fourier recurrences against known basis tests. This is a forecast; no named model has been evaluated on the task.

**Verification burden:** High. A proposed proof needs operator-domain and limiting-argument review. Finite spectral calculations require an independent implementation and cannot certify an infinite-dimensional claim.

**Resource expectations:** Analytic work may use a workstation for symbolic or spectral exploration. Numerical spectra cannot establish infinite-dimensional or uniform bounds.

**Assessment:** 2026-11-28; untested forecast. **Uncertainty:** A comparison with root-function criteria must account for any associated functions and multiplicities. The named special cases already have answers.

**Further work:** resolve the statement and status questions above before planning an attempt. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-28

**Coverage:** Statement only. **Statement:** Corrected.

**Recorded status:** Unverified → Unverified.

Mityagin gives an exact test for V(x) = exp(−2ix) + b exp(2ix), namely |b| = 1. Earlier work with Djakov proves that for a exp(−2ix) + B exp(4ix), with a and B nonzero, even the root functions fail to form a basis under periodic boundary conditions. The general coefficient classification has no verified current status here.

**Search scope:** The problem sheet asks about eigenfunctions. Root-function theorems may add generalized eigenvectors at defective eigenvalues.

<details>
<summary>Previous indexed wording</summary>

Characterize coefficients vk in V(x)=Σ|k|≤m vk e^(2ikx) for which the periodic Schrödinger eigensystem on (0,π) is a Schauder basis of L².

The current statement appears at the top of this page.
</details>

**Inspected evidence**

- [Schauder basis for Schrödinger operators with periodic boundary conditions](../sources.md#src-phys-923) — 2015 AIM sheet 23, Open Problem and Known Case. Asks for a coefficient test for eigenfunctions under periodic boundary conditions and identifies a two-term potential with an exact criterion.
- [Convergence of spectral decompositions of Hill operators with trigonometric polynomial potentials](../sources.md#src-phys-924) — Abstract, cases (i)–(iii) and the periodic-boundary conclusion for case (ii). For the potential a exp(−2ix) + B exp(4ix) with both coefficients nonzero, the system of root functions is complete but fails to be a basis under periodic boundary conditions.

**Limits and remaining work**

- For any proposed general coefficient criterion, specify how multiple eigenvalues are treated and compare its scope with known root-function criteria.

<details>
<summary>Search queries</summary>

- Mityagin Schauder basis periodic Schrodinger trigonometric polynomial coefficient classification root functions after 2015


</details>

### 2026-10-14

**Coverage:** Statement only. **Statement:** Matched.

**Recorded status:** Unverified → Unverified.

The historical source matches the indexed question. Targeted keyword searches did not establish a later primary result resolving its full scope; present-day openness remains unverified.

**Search scope:** Original source and recorded targeted searches. No later primary result matching the full target was established; statement-only denotes this evidence limit, not absence of a search.

**Inspected evidence**

- [Mathematical aspects of physics with non-self-adjoint operators: list of open problems](../sources.md#src-model-401) — §13.1, Boris Mityagin. Original question or research direction located.

**Limits and remaining work**

- Root vectors versus eigenvectors and multiple eigenvalues require clarification; subsequent basis criteria need checking.
- Only the recorded search terms were covered; later results, different terminology, corrections and exact-scope resolutions may have been missed.

<details>
<summary>Search queries</summary>

- non self adjoint AIM 2015 open problems status Almog Boulton
- "trigonometric polynomial" "Schauder basis" Mityagin 2025


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
