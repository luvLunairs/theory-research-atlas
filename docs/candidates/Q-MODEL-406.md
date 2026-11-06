# Trace-class endpoint for perturbed spectral distances

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MODEL-406 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-406%3A+Trace-class+endpoint+for+perturbed+spectral+distances&target=Q-MODEL-406) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-406%3A+Trace-class+endpoint+for+perturbed+spectral+distances&target=Q-MODEL-406)

Let A be bounded and self-adjoint on a Hilbert space, and let K be an arbitrary trace-class perturbation. Can the estimates Σ_{λ∈σd(A+K)} dist(λ,σ(A))^(1+ε) ≤ C(ε)||K||_(1+ε)^(1+ε), for every ε>0, yield Σ_{λ∈σd(A+K)} dist(λ,σ(A)) ≤ C||K||_1 with C independent of A and K? Count discrete eigenvalues with algebraic multiplicity.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Unverified. **Last checked:** 2026-11-06.

**Status basis:** The accessible 2015 problem and 2013 theorem specify the endpoint target. The latter covers p>1 and records a p=1 special case for interval spectra; the general endpoint's current status remains unverified.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** The 2026-11-06 literature check identifies the versions and passages inspected; original publication dates and earlier checks remain relevant.

**Scope limits:** An operator-theoretic question under the stated domains and boundary conditions; it does not establish that the operator is an empirically adequate physical model.

**Information still needed**

- Find a later primary result deciding the uniform trace-class endpoint for general self-adjoint spectra.
- Distinguish distance to the spectrum from distance to the closed numerical range; control the constants as ε tends to zero.

**Primary branch:** [Spectral and operator theory in physics](../domains/mphy.md#mphy-spectral). **Related branches:** [Quantum theory and foundations](../domains/phys.md#phys-quant).

**Sources:** [Mathematical aspects of physics with non-self-adjoint operators: list of open problems](../sources.md#src-model-401); [Variation of discrete spectra for non-selfadjoint perturbations of selfadjoint operators](../sources.md#src-phys-801); [Tensor trick for perturbed operators](../sources.md#src-phys-807).

**Exact locator:** Hansmann, Tensor trick for perturbed operators (2015), one-page problem; Hansmann (2013), Introduction and Corollary 1.

**Potential difficulty:** High. Non-selfadjoint spectral claims require control of infinite-dimensional operator domains, asymptotics or basis properties.

**Possible AI role:** A tool-using AI could inspect endpoint interpolation and candidate finite-rank obstructions. This is a forecast; no named model has been evaluated on the task.

**Verification burden:** High. A proposed proof needs operator-domain and limiting-argument review. Finite spectral calculations require an independent implementation and cannot certify an infinite-dimensional claim.

**Resource expectations:** Analytic work may use a workstation for symbolic or spectral exploration. Numerical spectra cannot establish infinite-dimensional or uniform bounds.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** The uniform constant and eigenvalue multiplicity are now explicit. Known numerical-range and interval-spectrum estimates do not settle the general endpoint; a specialist status check remains necessary.

**Further work:** resolve the statement and status questions above before planning an attempt. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-06

**Coverage:** Statement and later literature. **Statement:** Corrected.

**Recorded status:** Unverified → Unverified.

Clarify the quantifiers and scope without asserting a new current-open verdict.

**Search scope:** Targeted searches and inspection of the cited passages on 2026-11-06; neither an exhaustive literature search nor an independent scientific review.

<details>
<summary>Previous indexed wording</summary>

Does the family of Schatten-(1+ε) estimates in §8.1 imply a trace-class bound Σdist(λ,σ(A))≤C||K||1 for bounded self-adjoint A?

The current statement appears at the top of this page.
</details>

**Inspected evidence**

- [Tensor trick for perturbed operators](../sources.md#src-phys-807) — Complete one-page problem. States the trace-class perturbation and the proposed passage from every Schatten-(1+ε) estimate to the endpoint.
- [Variation of discrete spectra for non-selfadjoint perturbations of selfadjoint operators](../sources.md#src-phys-801) — Introduction, pp. 1–3; Corollary 1. Uses algebraic multiplicities and constants independent of the operators for p>1; explains the numerical-range distinction and interval-spectrum exception.

**Limits and remaining work**

- No complete later-literature or proof audit was performed.
- The newly accessible individual problem sheet does not replace other questions in the inaccessible AIM collection.

<details>
<summary>Search queries</summary>

- Hansmann eigenvalues non selfadjoint perturbations selfadjoint operators p=1 counterexample
- "trace class" "Hansmann" "spectral" conjecture
- "Mathematical aspects of physics with non-self-adjoint operators" "problems" pdf


</details>

### 2026-10-14

**Coverage:** Statement only. **Statement:** Matched.

**Recorded status:** Unverified → Unverified.

The historical source matches the indexed question. Targeted keyword searches did not establish a later primary result resolving its full scope; present-day openness remains unverified.

**Search scope:** Original source and recorded targeted searches. No later primary result matching the full target was established; statement-only denotes this evidence limit, not absence of a search.

**Inspected evidence**

- [Mathematical aspects of physics with non-self-adjoint operators: list of open problems](../sources.md#src-model-401) — §8.1, Marcel Hansmann. Original question or research direction located.

**Limits and remaining work**

- Clarify uniformity in A and constants C(ε), eigenvalue multiplicities and later endpoint results.
- Only the recorded search terms were covered; later results, different terminology, corrections and exact-scope resolutions may have been missed.

<details>
<summary>Search queries</summary>

- Hansmann trace class endpoint eigenvalues distance spectrum selfadjoint perturbation p=1 counterexample
- non self adjoint AIM 2015 open problems status Almog Boulton


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
