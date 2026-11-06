# Local enforcement of a kinetic-energy upper bound

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MODEL-425 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-425%3A+Local+enforcement+of+a+kinetic-energy+upper+bound&target=Q-MODEL-425) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-425%3A+Local+enforcement+of+a+kinetic-energy+upper+bound&target=Q-MODEL-425)

For zero-temperature orbital-free DFT, determine the provable consequences and validity conditions of imposing t_s(r)≤t_TF(r)+t_vW(r) pointwise as an approximation constraint, with the kinetic-energy-density gauge specified.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Unverified. **Last checked:** 2026-11-06.

**Status basis:** This asks about the consequences of a local approximation constraint. Universal pointwise validity is already contradicted in the positive gradient convention by the examples reported in the cited 2019 paper; the broader consequences remain unverified.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** The 2026-11-06 literature check identifies the versions and passages inspected; original publication dates and earlier checks remain relevant.

**Scope limits:** A formal question about nonrelativistic electronic Hamiltonians or a stated density-functional approximation. Mathematical validity and agreement with molecular measurements are separate tests.

**Information still needed**

- Specify the gauge, approximation class and claimed consequence before attempting a proof.
- Review the complete 2019 examples and subsequent literature before claiming a new local violation.

**Primary branch:** [Quantum chemistry and electronic structure](../domains/chem.md#chem-quant). **Related branches:** [Spectral and operator theory in physics](../domains/mphy.md#mphy-spectral).

**Sources:** [Some Problems in Density Functional Theory](../sources.md#src-model-402); [Upper bound to the gradient-based kinetic energy density of noninteracting electrons in an external potential](../sources.md#src-phys-803).

**Exact locator:** Wrighton et al. (2023), §IV, Question 3.5 and equation (11); Witt et al. (2019), author abstract.

**Potential difficulty:** High. The questions concern unresolved functional-analytic or approximation foundations of electronic-structure theory.

**Possible AI role:** A tool-using AI could track divergence terms and construct gauge-aware comparisons. This is a forecast; no named model has been evaluated on the task.

**Verification burden:** High. Check the density and potential spaces, representability, differentiability and boundary conditions. Benchmark agreement does not establish a functional inequality or a uniqueness theorem.

**Resource expectations:** Proof work and small electronic examples may fit a workstation; accurate correlated-electron reference calculations can be expensive. No general resource bound is established.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** The gauge and target consequence still need specification for an individual attempt. Local and integrated bounds are separate; the entry does not ask for universal local validity.

**Further work:** resolve the statement and status questions above before planning an attempt. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-06

**Coverage:** Statement and later literature. **Statement:** Corrected.

**Recorded status:** Unverified → Unverified.

Make the intended approximation question explicit and avoid presenting a known false local bound as an open universal conjecture.

**Search scope:** Targeted searches and inspection of the cited passages on 2026-11-06; neither an exhaustive literature search nor an independent scientific review.

<details>
<summary>Previous indexed wording</summary>

Determine what follows when the integrated bound in equation (10) is imposed pointwise on kinetic-energy densities as in equation (11).

The current statement appears at the top of this page.
</details>

**Inspected evidence**

- [Some Problems in Density Functional Theory](../sources.md#src-model-402) — §IV, equation (11), Question 3.5 and preceding remark. The question concerns implications of local enforcement and explicitly acknowledges gauge ambiguity and prior violations.
- [Upper bound to the gradient-based kinetic energy density of noninteracting electrons in an external potential](../sources.md#src-phys-803) — Author abstract. The reported violations use the non-negative gradient-based kinetic-energy density.

**Limits and remaining work**

- The 2019 full-text examples were not independently reviewed.
- This does not settle the range of valid approximation consequences.

<details>
<summary>Search queries</summary>

- "Upper bound to the gradient-based kinetic" pdf
- "kinetic energy" "Thomas-Fermi" "Weizsäcker" "conjecture" "2026"


</details>

### 2026-10-14

**Coverage:** Statement only. **Statement:** Needs clarification.

**Recorded status:** Unverified → Unverified.

The historical source matches the indexed question. Targeted keyword searches did not establish a later primary result resolving its full scope; present-day openness remains unverified.

**Search scope:** Original source and recorded targeted searches. No later primary result matching the full target was established; statement-only denotes this evidence limit, not absence of a search.

**Inspected evidence**

- [Some Problems in Density Functional Theory](../sources.md#src-model-402) — §IV, Question 3.5. Original question or research direction located.

**Limits and remaining work**

- Energy-density gauge must be fixed; the source already discusses local violations, so the task is consequences and validity conditions, not universal pointwise truth.
- Only the recorded search terms were covered; later results, different terminology, corrections and exact-scope resolutions may have been missed.

<details>
<summary>Search queries</summary>

- "Thomas-Fermi" "Weizsacker" "upper bound" kinetic 2025


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
