# Efficient passive initialization of a three-dimensional quantum memory

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

A memory is useful only if information can be loaded into its protected state. This asks whether the proposed passive memory can be initialized without preparation taking prohibitively long.

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-496%3A+Efficient+passive+initialization+of+a+three-dimensional+quantum+memory&target=Q-MODEL-496) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-496%3A+Efficient+passive+initialization+of+a+three-dimensional+quantum+memory&target=Q-MODEL-496)

[At a glance](#at-a-glance) · [The task](#problem) · [Resources and verification](#verification) · [Evidence and context](#evidence) · [AI trial assessment](#assessment) · [Research records](#audit-trail)

<a id="at-a-glance"></a>

## At a glance

| Field | Summary |
| --- | --- |
| Primary field | [Quantum information theory](../domains/info.md#info-quant) |
| Related fields | [Statistical and nonequilibrium physics](../domains/phys.md#phys-stat), [Coding theory](../domains/info.md#info-codes) |
| Task origin | [Literature-origin question](../evidence-policy.md) |
| Current status | [Source reports open](../evidence-policy.md) · checked 2026-10-20 |
| AI suitability | [Exploratory](../ai-assessment.md) · Untested forecast |
| Scientific review | Pending |

<a id="problem"></a>

## The task

### Precise statement

For the main three-dimensional stabilizer-memory family with random embedding of Balasubramanian, Davydova and Lin, can the logical-zero thermal state |0&gt;&lt;0|_L tensor rho_beta be initialized efficiently from an accessible state by the within-sector thermalization route in Section 1.3? Specify allowed initial controls, bath dynamics, temperature, preparation error, logical error and system-size scaling.

**Required output:** Establish an efficient preparation procedure under explicit conditions, or prove a preparation bottleneck for a specified admissible procedure.

**Scope:** The logical-zero preparation route explicitly discussed in the source. The open direction does not prescribe a unique efficiency threshold. Define input preparation, allowed controls and an error metric before an attempt; preparing arbitrary unknown logical states is a further claim.

### Assumptions

- Use the main random-embedding family in Sections 1.2.2 and 3, with the storage analysis in Section 5, and its thermal encoding. Specify the construction parameters and any probability statement over embeddings.
- Declare the bath dynamics and nonzero temperature regime before a quantitative claim.
- Approach the thermal syndrome state while bounding logical errors during preparation. Exact conservation of a logical sector is not assumed; global equilibration that loses the stored information is not success.

### Success criteria

1. Identify the preparation channel, its admissible initial states and the target thermal syndrome state.
2. Give a rigorous accuracy bound with explicit dependence on system size, temperature and tolerance.
3. Bound logical errors during preparation and compare the initialization time with the storage regime. Do not replace metastable protection by an assumed exactly conserved logical sector.
4. Limit any obstruction to the protocols and parameter regime actually proved.

### Background needed

- Stabilizer codes, syndrome sectors and Gibbs states.
- Local thermal dynamics, mixing estimates and asymptotic error bounds.

<a id="verification"></a>

## Resources and verification

### Resource requirements

**Computing:** Unmeasured. Small instances can test definitions, while exact state-space simulation grows rapidly. Analytical bounds may avoid full simulation; no affordable full-scale run is promised.

**Data:** The published code construction, bath assumptions and a fully specified proposed preparation protocol.

**Experiments:** None for a theorem about the prescribed model; physical implementation would require separate experiments.

**Theory and model requirements:** Ideal stabilizer interactions, chosen thermal dynamics and a stated logical-sector encoding. Hardware robustness is a separate claim.

**Validation modes:** Proof, Numerical evidence.

### Verification steps

1. State the physical or mathematical controls allowed during preparation.
2. Match the Hamiltonian, encoding and bath to the cited construction.
3. Check the logical-zero target and quantify leakage or logical errors rather than imposing perfect within-sector conservation without justification.
4. Audit every size-dependent constant, accuracy estimate and temperature restriction.
5. Treat simulations as diagnostics and obtain specialist review of the final asymptotic argument.

**Statement alignment:** Ground-space encoding, mixed thermal encoding, active preparation and passive within-sector relaxation are distinct tasks.

**Human review difficulty:** High: the protocol must fit the code construction while its error and resource estimates remain uniform in the declared limit.

### Formal validity and empirical support

**What the formal task can establish:** A theorem applies only to its stated Hamiltonian and dynamics. Source inspection is not independent validation of the construction.

**Empirical support and limits:** No experimental device, fabrication tolerance or measured memory performance is established by this entry.

### Methods and obstacles

**Proposed methods:**

- Analyze the source's proposed within-sector thermalization route.
- Check the assumptions of applicable mixing and preparation theorems before transferring them.

**Expected obstacles:**

- A lifetime bound does not supply an initialization bound.
- Mixing across logical sectors destroys the desired information.
- A good finite-size simulation need not imply efficient asymptotic preparation.

### Checks still needed

- Choose a precise efficiency target and permitted controls.
- Audit dependencies in the memory theorem before using them.
- Search for subsequent initialization results and compare their models.

<a id="evidence"></a>

## Evidence and context

**Status basis:** Section 1.3 explicitly leaves efficient initialization untreated. The later two-dimensional classical stability result addresses a different task. A focused search found no solution for the stated quantum construction; this is not an exhaustive status determination.

[Dated literature checks and remaining limits](../candidates/Q-MODEL-496.md#literature-checks). These are editorial evidence checks, not signed expert reviews.

**Exact problem / theorem locator:** Balasubramanian, Davydova and Lin, Section 1.3, item 2; later classical result, abstract and Section 1.

### Sources

- [A passive self-correcting quantum memory in three dimensions](../sources.md#src-phys-013). Shankar Balasubramanian; Margarita Davydova; Ting-Chun Lin. 2026. [Read source](https://arxiv.org/html/2605.10943v1).
  - **Relevant sections:** arXiv:2605.10943v1, submitted 2026-05-11; Section 1.3, item 2, and thermal-encoding definition.
  - **Source limitations:** The initialization discussion and metadata were inspected. The long construction and lifetime proof were not independently verified; no physical implementation is established here.
- [A thermally and perturbatively stable classical spin model in two dimensions](../sources.md#src-phys-014). Shankar Balasubramanian; Margarita Davydova; Ting-Chun Lin; Ryan Thorngren. 2026. [Read source](https://arxiv.org/html/2610.22548v1).
  - **Relevant sections:** arXiv:2610.22548v1, submitted 2026-10-15; abstract and Section 1.
  - **Source limitations:** This is not a solution of efficient initialization for the three-dimensional quantum memory. Statement and scope inspected; proof not independently verified.

### Known results and partial progress

- The source reports a storage theorem for its main random-embedding construction using thermal encoding. Efficient initialization is left open.
- Its suggested within-sector route may encounter energetic bottlenecks; a cited rapid-initialization argument has an unmet LDPC metacheck assumption.
- The October follow-up treats two-dimensional classical stability, not this initialization problem.
- The separate explicit-embedding construction in Sections 1.2.4 and 6 does not yet have the complete exponential-lifetime proof in this paper; its preparation cannot simply inherit the main construction's guarantee.

**Research value:** Initialization connects a theoretical storage construction to a usable information-processing procedure. A rigorous obstruction would also clarify what the construction requires.

### Related problems

No formal dependency or equivalence is asserted.

### Scope of the status check

**Finding:** Section 1.3 explicitly leaves efficient initialization untreated. The later two-dimensional classical stability result addresses a different task. A focused search found no solution for the stated quantum construction; this is not an exhaustive status determination.

**Search limits:** Focused later-work searches do not exclude unpublished or newly posted results. The underlying construction was not independently proved.

<details>
<summary>Literature references checked</summary>

**Queries used:**

- "2605.10943" initialization
- "self-correcting quantum memory" "initialization" 2026
- "2605.10943" "initialization" "proof"
- "passive" "memory" "initialization" "Balasubramanian" 2026
- "self-correcting" "initialization" quantum memory September October 2026

**Sources checked:**

- [A passive self-correcting quantum memory in three dimensions](../sources.md#src-phys-013)
- [A thermally and perturbatively stable classical spin model in two dimensions](../sources.md#src-phys-014)

</details>

<details>
<summary>Previous attempts and public records</summary>

- The original outlook proposes a possible preparation route and describes obstacles; no project attempt has been run.

</details>

<details>
<summary>Attribution and suggested citation</summary>

**Original authors and credited contributors:**

- Shankar Balasubramanian
- Margarita Davydova
- Ting-Chun Lin

**Suggested citation:** Balasubramanian, Davydova and Lin (2026), arXiv:2605.10943v1, Section 1.3. The later scope comparison uses Balasubramanian, Davydova, Lin and Thorngren (2026), arXiv:2610.22548v1.

**Editorial credit:** Compiled for Theory Research Atlas with Codex assistance.

</details>

<a id="assessment"></a>

## AI trial assessment

**Label:** [Exploratory](../ai-assessment.md). **Evidence:** Untested forecast. **Assessed:** 2026-10-20.

AI may help track the construction's hypotheses and test local lemmas. The missing asymptotic preparation argument is substantial.

**Model or capability conditions:** No model evaluated. Assumes tool-using AI able to inspect literature, manipulate mathematical expressions and retain reproducible calculations.

**Uncertainty:** No model or protocol tested. Appropriate assumptions and practical resource costs remain unsettled.

Ratings are separate judgments, not a score. High expertise needed or verification difficulty means a larger burden; high method availability or checkability means stronger support.

| Dimension | Rating | Reason |
| --- | --- | --- |
| Statement clarity | Medium | The source identifies the task; efficiency and allowed preparation controls need specification. |
| Decomposability | Medium | Protocol definition, local lemmas and scaling bounds can be separated. |
| Methods and literature | Medium | Mixing-time methods exist, but their hypotheses may fail here. |
| Search / symbolic fit | Medium | Finite calculations can expose obstructions without resolving scaling. |
| Checkability | Medium | A precise theorem is reviewable; full dynamics are costly. |
| Expertise needed | High | Quantum coding and thermal-dynamics expertise are both needed. |
| Scholarly significance | High | Preparation is necessary for using a long-lived memory. |
| Verification difficulty | High | Logical preservation and uniform asymptotic bounds must hold together. |

**Correctness:** No project answer.

No preparation protocol has been proved or tested by this project.

**Novelty:** Requires future literature review.

Any chosen protocol and scaling claim need a focused comparison.

<details>
<summary>Difficulty and significance</summary>

**Difficulty:** High.

Efficient preparation requires control of a large interacting system in a specified logical sector.

**Evidence type:** Editorial estimate not measured.

**Significance:** High.

Preparation determines whether the theoretical protected state is operationally accessible.

</details>

<a id="audit-trail"></a>

## Research records

No project attempts or human reviews have been recorded.

<details>
<summary>Record information</summary>

| Field | Recorded value |
| --- | --- |
| Stable ID | `Q-MODEL-496` |
| Duplicate key | `three-dimensional-passive-quantum-memory-thermal-initialization-bdl2026` |
| Original domain label | Quantum information |
| Original cross-domain labels | Statistical physics; Quantum coding theory |
| Primary domain ID | `INFO.QUANT` |
| Cross-domain IDs | `PHYS.STAT`, `INFO.CODES` |
| Origin code | `literature_open` |
| Status code | `source_reports_open` |
| Curator-designed scope | No |
| Detailed entry | Yes |
| Record level | `C` |
| Human review status | `pending` |
| Trial-label code | `exploratory` |
| Assessment-evidence code | `untested_forecast` |
| Method tags | `proof`, `bounds`, `model_analysis`, `numerical_computation` |
| Validation tags | `pure_proof`, `numerical_evidence` |
| Experimental-dependency tag | `none_for_formal_task` |

[JSON record](../../data/cards/Q-MODEL-496.json)

</details>

[Problem cards](README.md) · [Back to top](#at-a-glance)
