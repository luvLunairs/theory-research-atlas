# Nonlinear stationary axisymmetric tidal response of Kerr black holes

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

How does a spinning black hole respond beyond first order to a steady surrounding gravitational tide? A complete treatment must connect the spacetime solution with well-defined response coefficients.

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-492%3A+Nonlinear+stationary+axisymmetric+tidal+response+of+Kerr+black+holes&target=Q-MODEL-492) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-492%3A+Nonlinear+stationary+axisymmetric+tidal+response+of+Kerr+black+holes&target=Q-MODEL-492)

[At a glance](#at-a-glance) · [The task](#problem) · [Resources and verification](#verification) · [Evidence and context](#evidence) · [AI trial assessment](#assessment) · [Research records](#audit-trail)

<a id="at-a-glance"></a>

## At a glance

| Field | Summary |
| --- | --- |
| Primary field | [Gravitation and spacetime theory](../domains/phys.md#phys-grav) |
| Related fields | [Mathematical physics](../domains/mphy.md) |
| Task origin | [Literature-origin question](../evidence-policy.md) |
| Current status | [Open after a scoped check](../evidence-policy.md) · checked 2026-10-20 |
| AI suitability | [Preparation needed](../ai-assessment.md) · Untested forecast |
| Scientific review | Pending |

<a id="problem"></a>

## The task

### Precise statement

Determine the nonlinear stationary axisymmetric tidal response of four-dimensional Kerr black holes across multipoles, including matching to a worldline effective field theory. Recover established quadrupolar results and identify the response coefficients accessible within axisymmetry.

**Required output:** A controlled response calculation or theorem with explicit multipole coverage and identifiable coefficients.

**Scope:** The literature gap is multipolar nonlinear response and EFT matching, not the already-studied linear Kerr response.

### Assumptions

- Four-dimensional vacuum general relativity, with a regular Kerr event horizon and stationary axisymmetric external gravitational tides.
- Specify the applied tidal moments, normalization and matching prescription; distinguish nonlinear tidal order from order in black-hole spin.
- Separate conservative static response from dissipation and frequency-dependent response.
- State the spin range explicitly. For subextremal calculations use |a|&lt;M in geometrized units; an extremal limit requires its own boundary analysis.

### Success criteria

1. State which tidal orders, multipoles and spin values are covered.
2. Show that horizon-regular solutions satisfy the field equations and match the declared EFT.
3. Recover established limits and state which coefficients cannot be determined under axisymmetry.

### Background needed

- General-relativistic perturbation theory and horizon boundary conditions.
- Multipole expansions, worldline EFT and symbolic tensor calculation.

<a id="verification"></a>

## Resources and verification

### Resource requirements

**Computing:** A finite-order symbolic calculation may start locally, but expression growth can dominate memory. No runtime or budget has been measured.

**Data:** Published equations and conventions; no observational dataset is required.

**Experiments:** None for a conditional GR calculation; observational tests require additional evidence.

**Theory and model requirements:** Vacuum GR, specified tidal environment and horizon regularity; only response combinations identifiable in the chosen symmetry sector.

**Validation modes:** Proof, Exact computation.

### Verification steps

1. Check source definitions and retained perturbative orders.
2. Substitute derived fields into the equations and inspect horizon and axis regularity.
3. Audit source-response separation and EFT matching independently.
4. Compare the nonrotating and quadrupolar limits with the cited results.

**Statement alignment:** A finite-order calculation establishes only its stated channels and approximation; it is not a complete all-multipole or observational result.

**Human review difficulty:** High: a specialist must inspect gauge choices, operator identifiability and matching.

### Formal validity and empirical support

**What the formal task can establish:** A result would hold under the stated GR and boundary assumptions.

**Empirical support and limits:** No observational test of nonlinear tidal coefficients is supplied by this entry.

### Methods and obstacles

**Proposed methods:**

- Symbolic perturbation theory
- Multipolar expansion
- EFT matching
- Boundary and limiting-case checks

**Expected obstacles:**

- Gauge-dependent tails can be mistaken for physical response.
- Axisymmetry may conceal independent EFT operators.
- All-orders language can exceed the calculation actually established.

### Checks still needed

- Select a finite tidal order and multipole sector; this narrowing is Curator-proposed; pending review.
- Check subsequent literature for that exact sector before claiming novelty.

<a id="evidence"></a>

## Evidence and context

**Status basis:** The review explicitly identifies the incomplete multipolar calculation and EFT matching. The October 2026 Kerr-Newman result concerns linear response. A targeted later-literature search found no closure of this specific gap.

[Dated literature checks and remaining limits](../candidates/Q-MODEL-492.md#literature-checks). These are editorial evidence checks, not signed expert reviews.

**Exact problem / theorem locator:** Rodríguez et al., section 6.3.2, PDF p.112; Gounis et al., section 5.1; Chakraborty et al., introduction and final discussion.

### Sources

- [Love numbers of black holes and compact objects](../sources.md#src-phys-006). María J. Rodríguez; Luca Santoni; Adam R. Solomon. 2026. [Read source](https://arxiv.org/pdf/2604.08653v1).
  - **Relevant sections:** Section 6.3.2, PDF page 112; arXiv:2604.08653v1, submitted 2026-04-09.
  - **Source limitations:** The relevant review passage was inspected, not every cited derivation; it is a preprint review and its status statement is dated.
- [The Vanishing of the Non-linear Static Love Number of Kerr Black Holes and the Role of Symmetries](../sources.md#src-phys-007). L.-R. Gounis; A. Kehagias; A. Riotto. 2025. [Read source](https://arxiv.org/html/2412.08249v1).
  - **Relevant sections:** Section 5.1, equations (41)-(47), and conclusions. Preprint submitted 2024-12-11; JCAP 03 (2025) 002, DOI 10.1088/1475-7516/2025/03/002.
  - **Source limitations:** The later review identifies remaining multipolar and EFT-matching work. No independent audit of the curvature calculation or generality claim was performed.
- [Vanishing Love Numbers of Kerr-Newman Black Holes](../sources.md#src-phys-008). Sumanta Chakraborty; Takuya Katagiri; Paolo Pani; Jun-Xi Shi. 2026. [Read source](https://arxiv.org/html/2610.17179v1).
  - **Relevant sections:** Introduction, static perturbations and final discussion; arXiv:2610.17179v1, submitted 2026-10-12.
  - **Source limitations:** Recent preprint; its linear result is not a solution of the nonlinear Kerr target and has not been independently verified here.

### Known results and partial progress

- Gounis et al. calculate an axisymmetric quadrupolar tidal tail and make a broader vanishing claim; the later review still identifies incomplete multipolar matching.
- The October Kerr-Newman preprint reports a linear conservative Love matrix, leaving beyond-linear response separate.

**Research value:** Response coefficients connect compact-object structure with inspiral modeling. The value of a bounded result depends on its new coverage and interpretation, not merely on another zero coefficient.

### Related problems

No formal dependency or equivalence is asserted.

### Scope of the status check

**Finding:** The scoped gap remains supported by the inspected literature.

**Search limits:** Targeted search, not exhaustive citation tracking or an independent audit of the source proofs.

<details>
<summary>Literature references checked</summary>

**Queries used:**

- "Kerr" "nonlinear Love" "2026" "matching"
- Kerr nonlinear Love numbers stationary axisymmetric EFT matching 2026 multipoles
- "Kerr" "nonlinear" "Love" "October" "2026"
- "nonlinear" "Kerr Love" "2026"
- "non-linear" "Kerr" "EFT" "2026"

**Sources checked:**

- [Love numbers of black holes and compact objects](../sources.md#src-phys-006)
- [The Vanishing of the Non-linear Static Love Number of Kerr Black Holes and the Role of Symmetries](../sources.md#src-phys-007)
- [Vanishing Love Numbers of Kerr-Newman Black Holes](../sources.md#src-phys-008)

</details>

<details>
<summary>Previous attempts and public records</summary>

- The source papers provide relevant calculations; no project research attempt has been run.

</details>

<details>
<summary>Attribution and suggested citation</summary>

**Original authors and credited contributors:**

- María J. Rodríguez
- Luca Santoni
- Adam R. Solomon
- L.-R. Gounis
- A. Kehagias
- A. Riotto

**Suggested citation:** Rodríguez, Santoni and Solomon (2026), arXiv:2604.08653v1, section 6.3.2; Gounis, Kehagias and Riotto, JCAP 03 (2025) 002. Credit each additional result used.

**Editorial credit:** Compiled for Theory Research Atlas with Codex assistance.

</details>

<a id="assessment"></a>

## AI trial assessment

**Label:** [Preparation needed](../ai-assessment.md). **Evidence:** Untested forecast. **Assessed:** 2026-10-20.

Symbolic tensor manipulation can assist finite-order field equations and matching checks. Choosing an informative sector and interpreting its coefficients require GR and EFT expertise; no AI trial has been run.

**Model or capability conditions:** No named model evaluated; assumes a tool-using assistant with source access and specialist human review.

**Uncertainty:** No model has been evaluated; tractability, novelty and resource needs remain uncertain.

Ratings are separate judgments, not a score. High expertise needed or verification difficulty means a larger burden; high method availability or checkability means stronger support.

| Dimension | Rating | Reason |
| --- | --- | --- |
| Statement clarity | Medium | The gap is identifiable; a first sector needs selection. |
| Decomposability | Medium | Finite orders separate calculation and matching. |
| Methods and literature | High | The sources provide established perturbative tools. |
| Search / symbolic fit | High | Tensor algebra offers a concrete assistance role. |
| Checkability | Medium | Substitution helps, but matching needs judgment. |
| Expertise needed | High | GR and EFT expertise are necessary. |
| Scholarly significance | High | Response structure supports gravitational theory. |
| Verification difficulty | High | Gauge and operator ambiguities complicate review. |

**Correctness:** No project answer.

Source curation only; no project answer or independent proof audit.

**Novelty:** Not assessed.

Any proposed partial result requires its own literature check.

<details>
<summary>Difficulty and significance</summary>

**Difficulty:** High.

Nonlinear multipole coupling, gauge choices and EFT matching must be controlled together; symbolic expression growth is an additional burden.

**Evidence type:** Editorial estimate not measured.

**Significance:** High.

The reasons are given under [research value](#evidence).

</details>

<a id="audit-trail"></a>

## Research records

No project attempts or human reviews have been recorded.

<details>
<summary>Record information</summary>

| Field | Recorded value |
| --- | --- |
| Stable ID | `Q-MODEL-492` |
| Duplicate key | `kerr-nonlinear-stationary-axisymmetric-multipolar-eft-response` |
| Original domain label | Gravitation and spacetime theory |
| Original cross-domain labels | Mathematical physics |
| Primary domain ID | `PHYS.GRAV` |
| Cross-domain IDs | `MPHY` |
| Origin code | `literature_open` |
| Status code | `open_after_scoped_check` |
| Curator-designed scope | No |
| Detailed entry | Yes |
| Record level | `C` |
| Human review status | `pending` |
| Trial-label code | `preparation_required` |
| Assessment-evidence code | `untested_forecast` |
| Method tags | `symbolic_derivation`, `proof`, `model_analysis` |
| Validation tags | `pure_proof`, `exact_computation` |
| Experimental-dependency tag | `none_for_formal_task` |

[JSON record](../../data/cards/Q-MODEL-492.json)

</details>

[Problem cards](README.md) · [Back to top](#at-a-glance)
