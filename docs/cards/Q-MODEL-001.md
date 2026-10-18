# Reproduce the CHSH optimum with an exact certificate

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

Rebuild a standard limit on quantum correlations in a form another person can check exactly. This calibrates statement translation and certificate checking before unfamiliar Bell problems are considered.

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-001%3A+Reproduce+the+CHSH+optimum+with+an+exact+certificate&target=Q-MODEL-001) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-001%3A+Reproduce+the+CHSH+optimum+with+an+exact+certificate&target=Q-MODEL-001)

[At a glance](#at-a-glance) · [The task](#problem) · [Resources and verification](#verification) · [Evidence and context](#evidence) · [AI trial assessment](#assessment) · [Research records](#audit-trail)

<a id="at-a-glance"></a>

## At a glance

| Field | Summary |
| --- | --- |
| Primary field | [Quantum theory and foundations](../domains/phys.md#phys-quant) |
| Related fields | [Quantum information theory](../domains/info.md#info-quant), [Optimization and operations research](../domains/math.md#math-opt) |
| Task origin | [Known-result calibration](../evidence-policy.md) |
| Current status | [Known result in literature](../evidence-policy.md) · checked 2026-10-13 |
| AI suitability | [Priority for a later trial](../ai-assessment.md) · Untested forecast |
| Scientific review | Pending |

<a id="problem"></a>

## The task

### Precise statement

For a bipartite quantum state and local Hermitian observables A0,A1,B0,B1 with eigenvalues in {-1,+1}, reproduce the universal bound |&lt;A0 tensor B0&gt;+&lt;A0 tensor B1&gt;+&lt;A1 tensor B0&gt;-&lt;A1 tensor B1&gt;| &lt;= 2 sqrt(2), including an attaining realization and an exact upper-bound certificate.

**Required output:** A reproducible derivation and independently checkable exact upper- and lower-bound certificates for an already known result.

**Scope:** Universal bound under the stated quantum model; a finite-dimensional attaining example; exact 4 by 4 Gram-matrix certificate. No experimental analysis.

### Assumptions

- A normalized positive quantum state on a tensor-product bipartite Hilbert space.
- Each of two local observables per party is Hermitian and squares to identity; the operators act on their own tensor factors.
- Expectations use the same state and the displayed sign convention; this task adopts the tensor-product formulation.

### Success criteria

1. Define the CHSH expression and all normalization conventions explicitly.
2. Provide an exact feasible Gram matrix and dual witness with matching objective values, or a complete independently checked operator proof plus an attaining construction.
3. Explain why the certificate concerns every allowed state and observable, not only sampled numerical examples.
4. Record any discrepancy between source notation, generated mathematics and checking code.

### Background needed

- Tensor products, density operators and Hermitian matrices.
- Positive semidefinite matrices, Gram matrices and weak duality.
- Exact arithmetic over Q(sqrt(2)) or an equivalent symbolic representation.

<a id="verification"></a>

## Resources and verification

### Resource requirements

**Computing:** A few fixed 4 by 4 exact matrices. A standard local symbolic or rational-algebra environment is a plausible resource class; no runtime or monetary estimate has been measured.

**Data:** No empirical dataset; use the cited mathematical definitions.

**Experiments:** None for the mathematical reproduction. Physical realization and loophole analysis would be separate experimental tasks.

**Theory and model requirements:** Quantum tensor-product model and dichotomic projective observables as stated. A broader measurement or operator-algebra model requires a new alignment check.

**Validation modes:** Proof, Exact computation.

### Verification steps

1. Freeze the precise statement and tensor ordering.
2. Derive the Gram objective and dual using one normalization throughout.
3. Check diagonal constraints and positive semidefiniteness exactly, with a second checking path where possible.
4. Check matching objectives and a valid quantum realization.
5. Have a reviewer compare the certificate theorem with the original physical assumptions.
6. Justify extension from the source pure-state representation to every density operator in the declared scope, or use a direct operator argument that covers the full state class.

**Statement alignment:** A valid SDP calculation proves the original bound only after the representation theorem or direct operator reduction is justified; a finite realization demonstrates attainability.

**Human review difficulty:** Moderate: a linear-algebra reviewer can inspect certificates, but a quantum-information reviewer should confirm statement alignment.

### Formal validity and empirical support

**What the formal task can establish:** The target is a mathematical implication of stated quantum assumptions; a reproduced certificate would support this layer only.

**Empirical support and limits:** The card neither reviews Bell experiments nor concludes that the assumptions describe a particular apparatus. Empirical validity is outside this task.

### Methods and obstacles

**Proposed methods:**

- symbolic derivation
- exact computation
- semidefinite duality
- proof reproduction

**Expected obstacles:**

- Losing a factor of two when translating the quadratic objective.
- Confusing a numerical lower bound with a universal upper bound.
- Using the wrong tensor ordering or silently changing allowed observables.
- A source itself can contain a typographical inconsistency; independent algebra remains necessary.

### Checks still needed

- Inspect the apparent omitted 1/2 in one feasibility sentence on PDF p.5 against the displayed dual and the version of record before creating test calculations.
- Select the exact-checking environment and reviewer; neither has been tested or appointed.
- Compare the apparent PSD-definition and Gram-diagonal transcription anomalies with the original PDF and journal version before copying any formulas into test calculations. These are source-quality flags, not a disproof of the bound.

<a id="evidence"></a>

## Evidence and context

**Status basis:** The inspected source supplies a proof and attaining certificate. The project proposes a reproduction task, not a new bound.

**Exact problem / theorem locator:** Wehner Section 2, PDF pp.4-5

### Sources

- [Tsirelson bounds for generalized Clauser-Horne-Shimony-Holt inequalities](../sources.md#src-model-004). Stephanie Wehner. 2006. [Read source](https://arxiv.org/pdf/quant-ph/0510076).
  - **Relevant sections:** Section 1 Theorem 1; Section 2 (PDF pp. 4-5); Section 3 Theorem 2
  - **Source limitations:** arXiv v2 dated 2006; generated PDF front matter also shows 2018. Use journal metadata Phys. Rev. A 73,022110 (2006). Apparent missing factor 1/2 in one feasibility sentence on PDF p.5 must be checked against the displayed dual.

### Known results and partial progress

- Wehner Section 2 proves the optimum 2 sqrt(2) by semidefinite duality; Section 3 extends the method to a family of chained inequalities.
- The result is a known theorem, so reproduction success has no mathematical novelty.

**Research value:** Useful as a compact calibration of proof-certificate discipline and normalization handling. Its scientific value here is workflow reliability, not a new quantum bound.

### Related problems

- **Method bridge to:** [Four mutually unbiased bases in dimension six](../candidates.md#q-model-007). Both use exact Gram constraints, but MUB existence is a different and much harder problem; calibration success supplies no evidence that it is easy.

### Scope of the status check

**Finding:** Inspected full Section 2 and arXiv journal/version metadata; known-result reproduction, not an open-status claim.

**Search limits:** No independent recreation, code execution or proof validation was performed.

<details>
<summary>Literature references checked</summary>

**Sources checked:**

- [Tsirelson bounds for generalized Clauser-Horne-Shimony-Holt inequalities](../sources.md#src-model-004)

</details>

<details>
<summary>Previous attempts and public records</summary>

- Published proof: Stephanie Wehner (2006), Section 2. This is a literature record, not an AI attempt or a project experiment.

</details>

<details>
<summary>Attribution and suggested citation</summary>

**Original authors and credited contributors:**

- Boris S. Tsirelson (original bound, credited by the inspected paper)
- Stephanie Wehner (inspected SDP exposition)

**Suggested citation:** Wehner, S. (2006). Tsirelson bounds for generalized Clauser-Horne-Shimony-Holt inequalities. Physical Review A 73, 022110. https://doi.org/10.1103/PhysRevA.73.022110

**Editorial credit:** Compiled for Theory Research Atlas with AI assistance.

</details>

<a id="assessment"></a>

## AI trial assessment

**Label:** [Priority for a later trial](../ai-assessment.md). **Evidence:** Untested forecast. **Assessed:** 2026-10-13.

A fixed operator-proof calibration with an attaining construction is a useful priority trial. If the alternative SDP route is chosen, first resolve the documented source transcription hazards and normalization alignment. No trial results have been recorded.

**Model or capability conditions:** No named model evaluated; assumes tool-using AI with literature retrieval, exact algebra or rational linear algebra, code generation, and access to a human domain reviewer.

**Uncertainty:** No model was tested. Memorization may dominate reproduction, so success must not be advertised as novel reasoning or frontier capability.

Ratings are separate judgments, not a score. High expertise needed or verification difficulty means a larger burden; high method availability or checkability means stronger support.

| Dimension | Rating | Reason |
| --- | --- | --- |
| Statement clarity | High | Objective and operator assumptions can be fixed completely. |
| Decomposability | High | Separate formulation, witness construction, exact checking and interpretation. |
| Methods and literature | High | The opened paper provides an explicit proof route. |
| Search / symbolic fit | High | Small algebraic matrices fit symbolic checking; no large search is required. |
| Checkability | High | Exact feasibility and objective equality can be inspected independently. |
| Expertise needed | Medium | Quantum notation and SDP duality need a qualified reviewer. |
| Scholarly significance | Medium | Strong calibration value but no new theorem is sought. |
| Verification difficulty | Medium | Numerical agreement is easy; the universal-to-finite certificate translation needs careful review. |

**Correctness:** No project answer.

The cited literature supports the problem statement. No project answer has been submitted for review.

**Novelty:** Not claimed.

The target is a known result; no originality is claimed for the selected scope. Any later novelty claim requires a literature check.

<details>
<summary>Difficulty and significance</summary>

**Difficulty:** Low to medium.

Exact small certificates make errors inspectable, and the literature supplies a clear target. Priority is only for a future calibration trial after human review.

**Evidence type:** Editorial estimate not measured.

**Significance:** Medium.

The reasons are given under [research value](#evidence).

</details>

<a id="audit-trail"></a>

## Research records

No project attempts or human reviews have been recorded.

<details>
<summary>Record information</summary>

| Field | Recorded value |
| --- | --- |
| Stable ID | `Q-MODEL-001` |
| Duplicate key | `chsh-tsirelson-exact-reproduction` |
| Original domain label | Quantum foundations |
| Original cross-domain labels | Optimization; Quantum information |
| Primary domain ID | `PHYS.QUANT` |
| Cross-domain IDs | `INFO.QUANT`, `MATH.OPT` |
| Origin code | `known_result_calibration` |
| Status code | `known_result` |
| Curator-designed scope | Yes |
| Detailed entry | Yes |
| Record level | `C` |
| Human review status | `pending` |
| Trial-label code | `priority_trial` |
| Assessment-evidence code | `untested_forecast` |
| Method tags | `proof`, `symbolic_derivation`, `exact_computation`, `certificate_checking` |
| Validation tags | `pure_proof`, `exact_computation` |
| Experimental-dependency tag | `none_for_formal_task` |

[JSON record](../../data/cards/Q-MODEL-001.json)

</details>

[Problem cards](README.md) · [Back to top](#at-a-glance)
