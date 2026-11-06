# Three-copy undistillability of the Werner endpoint

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

Can three copies unlock entanglement distillation that a single copy cannot achieve? This finite-copy question probes the limits of entanglement as a communication resource.

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-493%3A+Three-copy+undistillability+of+the+Werner+endpoint&target=Q-MODEL-493) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-493%3A+Three-copy+undistillability+of+the+Werner+endpoint&target=Q-MODEL-493)

[At a glance](#at-a-glance) · [The task](#problem) · [Resources and verification](#verification) · [Evidence and context](#evidence) · [AI trial assessment](#assessment) · [Research records](#audit-trail)

<a id="at-a-glance"></a>

## At a glance

| Field | Summary |
| --- | --- |
| Primary field | [Quantum information theory](../domains/info.md#info-quant) |
| Related fields | [Functional and operator analysis](../domains/math.md#math-anal-func), [Quantum theory and foundations](../domains/phys.md#phys-quant) |
| Task origin | [Literature-origin question](../evidence-policy.md) |
| Current status | [Needs further verification](../evidence-policy.md) · checked 2026-11-06 |
| AI suitability | [Preparation needed](../ai-assessment.md) · Untested forecast |
| Scientific review | Pending |

<a id="problem"></a>

## The task

### Precise statement

For every integer d &gt;= 3, is rho = (I - F/2)/(d^2 - d/2) three-copy undistillable, where F swaps the two C^d factors? Equivalently, is &lt;psi|(rho^Gamma)^(tensor 3)|psi&gt; &gt;= 0 for every unit vector psi of Schmidt rank at most two across A1A2A3:B1B2B3, with Gamma the partial transpose on B?

**Required output:** Prove the displayed nonnegativity for the full domain, or exhibit one admissible vector giving a rigorously negative value.

**Scope:** The target quantifies over every d &gt;= 3. A d=4 study is Curator-proposed; pending review. Its novelty requires a separate check, and a positive answer there is only partial progress.

### Assumptions

- Finite-dimensional complex spaces, d &gt;= 3, and local operations and classical communication (LOCC).
- The bipartition groups all Alice copies against all Bob copies; it is not a three-party problem.
- The endpoint is alpha = -1/2. A coefficient operator need not be Hermitian, positive or normal.
- Under vectorization psi=vec(C), Schmidt rank equals rank(C). The equivalent homogeneous test is q_3(C)=||C||_HS^2 -(1/2) sum_i ||Tr_i C||_HS^2 +(1/4) sum_i&lt;j ||Tr_ij C||_HS^2 -(1/8)|Tr C|^2 &gt;= 0 for every complex rank-at-most-two C on (C^d) tensor 3. Partial traces are unnormalized; their subscripts name the factors removed.

### Success criteria

1. A positive result must cover every permitted Schmidt-rank-two vector and every dimension claimed.
2. A negative result must retain exact vector or coefficient data, rank justification and certified strict negativity.
3. State precisely which dimensions or subclasses remain untreated.

### Background needed

- Partial transpose, Schmidt rank, LOCC and matrix inequalities.
- Tensor indices, unnormalized partial traces and certified arithmetic.

<a id="verification"></a>

## Resources and verification

### Resource requirements

**Computing:** Unmeasured. At d=4 the coefficient matrix has 64 rows and columns; low-rank parameterization reduces storage but does not make global optimization easy. No runtime or cost is forecast.

**Data:** Source definitions and any future exact candidate coefficients.

**Experiments:** None for the formal distillability question.

**Theory and model requirements:** Standard finite-dimensional quantum mechanics and ideal LOCC; all stated complex vectors are allowed.

**Validation modes:** Proof, Exact computation.

### Verification steps

1. Reconstruct the state and the specified bipartition independently.
2. Check vector normalization or homogeneous coefficient conventions and rank exactly.
3. Compare direct contraction with the partial-trace expression.
4. For a proof, audit domain coverage and every imported theorem; for a witness, certify a strict negative margin.
5. Compare with recent claims before asserting novelty.

**Statement alignment:** Normal-only positivity, two-copy results and finite numerical sampling are different claims.

**Human review difficulty:** High for a general proof; an explicit small witness is more localized but still requires statement alignment.

### Formal validity and empirical support

**What the formal task can establish:** Aligned proof or certified counterexample is required; source inspection does not certify either.

**Empirical support and limits:** No claim about laboratory state preparation or experimental distillation is assessed.

### Methods and obstacles

**Proposed methods:**

- Published partial-trace reformulation and support geometry.
- Symbolic identities or exact counterexample checks, with their scope declared.

**Expected obstacles:**

- A restricted ansatz can exclude all difficult cases.
- Floating-point minima near zero are inconclusive.
- A partial trace may increase operator rank.

### Checks still needed

- Obtain a fixed version and assess the new full-scope claim before asserting novelty.
- Inspect the analytic reductions, complete certificates and independent evaluations.
- The earlier qutrit certificate remains uninspected.

<a id="evidence"></a>

## Evidence and context

**Status basis:** Tomar (23 October 2026), Theorems 1.1-1.2, now claims the exact three-copy endpoint for every d&gt;=3. The full proof and certificates have not been independently assessed here.

[Dated literature checks and remaining limits](../candidates/Q-MODEL-493.md#literature-checks). These are editorial evidence checks, not signed expert reviews.

**Exact problem / theorem locator:** Wu and Zou, Section 1.1; Fu et al., Section 4; qutrit candidate description; Tomar, PDF p.2, Theorems 1.1-1.2.

### Sources

- [Sharp Plücker Geometry for Three-Copy Werner Distillation](../sources.md#src-phys-011). Tianhao Wu; Qiran Zou. 2026. [Read source](https://arxiv.org/html/2608.02647v1).
  - **Relevant sections:** arXiv:2608.02647v1, submitted 2026-07-31; Section 1.1, equations (1)-(3), Sections 6-7 and discussion.
  - **Source limitations:** Primary passages and metadata inspected; proofs not independently verified. An October candidate for d=3 is recorded separately.
- [Three-copy undistillability of the boundary qutrit Werner state](../sources.md#src-phys-012). Anonymous. 2026. [Read source](https://zenodo.org/records/23134454).
  - **Relevant sections:** Published 2026-10-04, version 1.1.0-candidate; DOI 10.5281/zenodo.23134454; landing-page description and file inventory.
  - **Source limitations:** Only the landing page was inspected. PDF retrieval failed; the proof, verifier, certificates and review report remain uninspected and unrun. The deposit disclaims journal peer review and an all-copy result.
- [A solution to 2-copy distillability of Werner states](../sources.md#src-formal-604). Jinshi Fu; Li Gao; Sang-Jun Park. 2026. [Read source](https://arxiv.org/html/2607.21367v3).
  - **Relevant sections:** Theorem 1.1; introduction; version 3 dated 5 October 2026
  - **Source limitations:** The statement and proof outline were inspected; no independent proof verification or assessment of subsequent specialist reception was completed.
- [Undistillability of Werner states from three, four and five copies](../sources.md#src-phys-707). Tejasvi Singh Tomar. 2026. [Read source](https://www.mefyi.com/papers/werner-states-copies/werner-states-copies.pdf).
  - **Relevant sections:** PDF p.2, Theorems 1.1-1.2; author landing page /papers/werner-states-copies/, first posted 2026-10-23, inspected 2026-11-06.
  - **Source limitations:** Author labels it unreviewed. Certificates and formalizations were not replayed; the reported Lean coverage is limited and assumes the distillability criterion. The hosted PDF is mutable; no immutable version was retrieved.

### Known results and partial progress

- Wu and Zou report nonnegativity for positive semidefinite and normal rank-two coefficient operators and specified nonnormal support configurations.
- Fu, Gao and Park report the exact two-copy threshold; their theorem does not settle three or arbitrarily many copies.
- The anonymous d=3 deposit is a candidate claim whose certificate has not been inspected here.
- Tomar reports the full three-copy threshold; see SRC-PHYS-707.

**Research value:** The full target is a concrete step toward understanding NPT entanglement. Its significance is foundational; no immediate communications-hardware improvement follows.

### Related problems

- **Related to:** [NPT bound entanglement](../candidates.md#q-model-005). Tests one finite-copy layer of the Werner route to NPT bound entanglement. Neither a three-copy positivity theorem nor a distillation witness for this family settles the unrestricted all-copy existence question.
- **Related to:** [Two-copy distillability of the two-ququart Werner boundary state](../candidates.md#q-model-006). The two-copy boundary is a reported recent advance, retained separately with its unresolved independent-review requirements.

### Scope of the status check

**Finding:** Tomar (23 October 2026), Theorems 1.1-1.2, now claims the exact three-copy endpoint for every d&gt;=3. The full proof and certificates have not been independently assessed here.

**Search limits:** Source inspection only. No certificate replay or independent proof review; the author-hosted PDF has no immutable version retained here.

<details>
<summary>Literature references checked</summary>

**Queries used:**

- "NPT bound entanglement" "2026" solved
- "three-copy" "Werner" "2026" November
- "2607.21367" correction OR withdrawn
- "Undistillability of Werner states from three, four and five copies" correction

**Sources checked:**

- [Sharp Plücker Geometry for Three-Copy Werner Distillation](../sources.md#src-phys-011)
- [Three-copy undistillability of the boundary qutrit Werner state](../sources.md#src-phys-012)
- [A solution to 2-copy distillability of Werner states](../sources.md#src-formal-604)
- [Undistillability of Werner states from three, four and five copies](../sources.md#src-phys-707)

</details>

<details>
<summary>Previous attempts and public records</summary>

- External records: Wu and Zou's sector analysis and the anonymous qutrit candidate. No project attempt.
- External record: Tomar (2026), SRC-PHYS-707; unreviewed here.

</details>

<details>
<summary>Attribution and suggested citation</summary>

**Original authors and credited contributors:**

- Tianhao Wu
- Qiran Zou
- Jinshi Fu
- Li Gao
- Sang-Jun Park
- Tejasvi Singh Tomar

**Suggested citation:** Wu and Zou (2026), arXiv:2608.02647v1; Fu, Gao and Park (2026), arXiv:2607.21367v3. Cite Anonymous, Zenodo 10.5281/zenodo.23134454, version 1.1.0-candidate, only as the reported d=3 claim. Additional claim: Tomar (2026), Undistillability of Werner states from three, four and five copies, SRC-PHYS-707.

**Editorial credit:** Compiled for Theory Research Atlas with Codex assistance.

</details>

<a id="assessment"></a>

## AI trial assessment

**Label:** [Preparation needed](../ai-assessment.md). **Evidence:** Untested forecast. **Assessed:** 2026-11-06.

Assess the new claim before beginning a novelty-oriented attempt.

**Model or capability conditions:** No model evaluated. Assumes tool-using AI able to inspect literature, manipulate mathematical expressions and retain reproducible calculations.

**Uncertainty:** No project AI attempt measured; correctness of the new claim and novelty of further work remain unresolved.

Ratings are separate judgments, not a score. High expertise needed or verification difficulty means a larger burden; high method availability or checkability means stronger support.

| Dimension | Rating | Reason |
| --- | --- | --- |
| Statement clarity | High | The state, copy count and rank quantifier are fixed. |
| Decomposability | Medium | Restricted sectors are possible but may already be solved. |
| Methods and literature | High | Partial-trace and support-geometry approaches are available. |
| Search / symbolic fit | High | Finite coefficient representations support auditable calculations. |
| Checkability | Medium | An exact counterexample is easier to check than global nonnegativity. |
| Expertise needed | High | Quantum-information and matrix-analysis review is needed. |
| Scholarly significance | High | Finite-copy activation bears on the structure of entanglement. |
| Verification difficulty | High | Universal proofs must retain every complex nonnormal case. |

**Correctness:** No project answer.

No answer has been produced or verified.

**Novelty:** Requires future literature review.

Compare against the new full-scope claim and its retained version.

<details>
<summary>Difficulty and significance</summary>

**Difficulty:** High.

The recent full-scope claim needs review; the previous description of remaining sectors is out of date.

**Evidence type:** Editorial estimate not measured.

**Significance:** High.

A finite-copy boundary within the NPT distillability problem.

</details>

<a id="audit-trail"></a>

## Research records

No project attempts or human reviews have been recorded.

<details>
<summary>Changes to this problem</summary>

| Date | Change |
| --- | --- |
| 2026-11-06 | Updated source evidence and outstanding checks; retained the historical target and pending human review. |

</details>

<details>
<summary>Record information</summary>

| Field | Recorded value |
| --- | --- |
| Stable ID | `Q-MODEL-493` |
| Duplicate key | `werner-minus-half-three-copy-all-dimensions` |
| Original domain label | Quantum information |
| Original cross-domain labels | Matrix analysis; Quantum foundations |
| Primary domain ID | `INFO.QUANT` |
| Cross-domain IDs | `MATH.ANAL.FUNC`, `PHYS.QUANT` |
| Origin code | `literature_open` |
| Status code | `unverified` |
| Curator-designed scope | No |
| Detailed entry | Yes |
| Record level | `C` |
| Human review status | `pending` |
| Trial-label code | `preparation_required` |
| Assessment-evidence code | `untested_forecast` |
| Method tags | `proof`, `counterexample`, `symbolic_derivation`, `exact_computation` |
| Validation tags | `pure_proof`, `exact_computation` |
| Experimental-dependency tag | `none_for_formal_task` |

[JSON record](../../data/cards/Q-MODEL-493.json)

</details>

[Problem cards](README.md) · [Back to top](#at-a-glance)
