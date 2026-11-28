# Critical versus subcritical heat-kernel decay

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MODEL-416 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-416%3A+Critical+versus+subcritical+heat-kernel+decay&target=Q-MODEL-416) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-416%3A+Critical+versus+subcritical+heat-kernel+decay&target=Q-MODEL-416)

On a connected open set Ω in Euclidean space, let H₊ and H₀ be self-adjoint elliptic differential operators on L²(Ω) with spectral bottom zero and well-defined heat kernels. Assume H₊ admits a strictly positive Hardy weight and subtracting any nonzero nonnegative smooth compactly supported potential from H₀ makes its spectral bottom negative. Does k₊(t,x,y)/k₀(t,x,y) tend to zero as t tends to infinity, locally uniformly on Ω × Ω?

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Unverified. **Last checked:** 2026-11-26.

**Status basis:** The 2015 source distinguishes this heat-kernel question from its weighted semigroup counterpart. The 2010 sheet records a positive answer for a symmetric critical operator perturbed by a nonzero nonnegative potential. The general pair in Conjecture 2 need not have this form.

**Statement check:** Source located. **Status check:** Source report only.

**Source date and freshness:** The author sheets date to 2010 and 2015. The present check confirms the formulation and the scope of an earlier theorem.

**Scope limits:** The indexed 2015 statement is the self-adjoint heat-kernel version. Its elliptic realizations must admit the kernels and comparison in the conjecture.

**Information still needed**

- Check later work for the locally uniform ratio for general pairs under the same hypotheses.
- Specify coefficient regularity, operator domains and positivity of the kernels for any restricted case.

**Primary branch:** [Spectral and operator theory in physics](../domains/mphy.md#mphy-spectral). **Related branches:** [Quantum theory and foundations](../domains/phys.md#phys-quant).

**Sources:** [Mathematical aspects of physics with non-self-adjoint operators: list of open problems](../sources.md#src-model-401); [Large-time behavior of the heat equation: subcriticality versus criticality](../sources.md#src-phys-908); [The large-time behaviour of the heat kernel: subcriticality versus criticality](../sources.md#src-phys-909).

**Exact locator:** Krejčiřík's 2015 AIM sheet, Conjecture 2 and preceding hypotheses. His 2010 workshop sheet, Theorem 1.

**Potential difficulty:** High. Non-selfadjoint spectral claims require control of infinite-dimensional operator domains, asymptotics or basis properties.

**Possible AI role:** A tool-using AI could test model domains and organize positive-solution comparison arguments. This is a forecast; no named model has been evaluated on the task.

**Verification burden:** High. A proposed proof needs operator-domain and limiting-argument review. Finite spectral calculations require an independent implementation and cannot certify an infinite-dimensional claim.

**Resource expectations:** Analytic work may use a workstation for symbolic or spectral exploration. Numerical spectra cannot establish infinite-dimensional or uniform bounds.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** Coefficient regularity and common domain must match the conjecture; later ratio-limit results require checking.

**Further work:** resolve the statement and status questions above before planning an attempt. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-26

**Coverage:** Statement only. **Statement:** Corrected.

**Recorded status:** Unverified → Unverified.

Clarify the hypotheses and a known special case. The available dated formulations leave the contemporary general status unverified.

**Search scope:** The indexed 2015 statement is the self-adjoint heat-kernel version. Its elliptic realizations must admit the kernels and comparison in the conjecture.

<details>
<summary>Previous indexed wording</summary>

Under §21.1's zero spectral-bottom and critical/subcritical elliptic hypotheses, does the subcritical-to-critical heat-kernel ratio tend locally uniformly to zero?

The current statement appears at the top of this page.
</details>

**Inspected evidence**

- [Large-time behavior of the heat equation: subcriticality versus criticality](../sources.md#src-phys-908) — Conjecture 2 and preceding assumptions. States the locally uniform ratio for a pair of self-adjoint elliptic operators, separately from Conjecture 1 on operator norms.
- [The large-time behaviour of the heat kernel: subcriticality versus criticality](../sources.md#src-phys-909) — Conjecture 1 and Theorem 1. Includes the special case P₊ = P₀ + V with nonzero V ≥ 0 and symmetric P₀.

**Limits and remaining work**

- No post-2015 source settling or reaffirming the general formulation was verified.

<details>
<summary>Search queries</summary>

- Yehuda Pinchover critical subcritical heat kernel ratio conjecture heat kernels tend zero locally uniformly current results Pinchover Fraas Krejcirik 2024 2025 proof
- "subcritical" "critical" "heat kernels" ratio limit 2020 2021 2022 2023 2024 2025 Pinchover critical subcritical ratio heat kernels conjecture counterexample Kozma same manifold


</details>

### 2026-10-14

**Coverage:** Statement only. **Statement:** Needs clarification.

**Recorded status:** Unverified → Unverified.

The historical source matches the indexed question. Targeted keyword searches did not establish a later primary result resolving its full scope; present-day openness remains unverified.

**Search scope:** Original source and recorded targeted searches. No later primary result matching the full target was established; statement-only denotes this evidence limit, not absence of a search.

**Inspected evidence**

- [Mathematical aspects of physics with non-self-adjoint operators: list of open problems](../sources.md#src-model-401) — §21.1, Conjecture 2, David Krejčiřík. Original question or research direction located.

**Limits and remaining work**

- Coefficient regularity and common domain must match the conjecture; later ratio-limit results require checking.
- Only the recorded search terms were covered; later results, different terminology, corrections and exact-scope resolutions may have been missed.

<details>
<summary>Search queries</summary>

- critical subcritical heat kernel ratio conjecture Fraas Krejcirik Pinchover 2025
- non self adjoint AIM 2015 open problems status Almog Boulton


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
