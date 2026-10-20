# Predictive mixed longitudinal-transverse intermittency exponents

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

Rare intense fluctuations govern turbulent mixing and dissipation. Their longitudinal and transverse statistics need a joint predictive account rather than separate fitted scaling curves.

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-495%3A+Predictive+mixed+longitudinal-transverse+intermittency+exponents&target=Q-MODEL-495) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-495%3A+Predictive+mixed+longitudinal-transverse+intermittency+exponents&target=Q-MODEL-495)

[At a glance](#at-a-glance) · [The task](#problem) · [Resources and verification](#verification) · [Evidence and context](#evidence) · [AI trial assessment](#assessment) · [Research records](#audit-trail)

<a id="at-a-glance"></a>

## At a glance

| Field | Summary |
| --- | --- |
| Primary field | [Fluid and plasma theory](../domains/phys.md#phys-fluid) |
| Related fields | [Statistical and nonequilibrium physics](../domains/phys.md#phys-stat) |
| Task origin | [Literature-origin question](../evidence-policy.md) |
| Current status | [Open after a scoped check](../evidence-policy.md) · checked 2026-10-20 |
| AI suitability | [Exploratory](../ai-assessment.md) · Untested forecast |
| Scientific review | Pending |

<a id="problem"></a>

## The task

### Precise statement

Develop a predictive description of the mixed longitudinal-transverse structure-function exponents in statistically stationary homogeneous isotropic incompressible turbulence, consistent with exact moment relations and the connection between inertial-range increments and dissipative-range gradients. State moment conventions, scaling ranges and the Reynolds-number limit.

**Required output:** An explicit predictive account of the mixed-exponent family, or a clearly delimited partial result.

**Scope:** A statistical prediction problem for mixed velocity increments and gradients; not a proof of Navier-Stokes global regularity.

### Assumptions

- Three-dimensional incompressible Navier-Stokes dynamics; specify forcing, stationarity, homogeneity and isotropy.
- For separation r e, let delta u_L=[u(x+r e)-u(x)] dot e and delta u_T be one perpendicular component. Define absolute mixed moments S_p,q(r)=E[|delta u_L|^p |delta u_T|^q] for nonnegative orders with finite moments, and their inertial-range exponents by S_p,q(r)~r^zeta_p,q. Signed moments have separate conventions and may vanish by symmetry.
- State the inertial-range and high-Reynolds-number assumptions; identify any additional closure or multifractal hypothesis.

### Success criteria

1. Define which moments and parameter range the result covers, including symmetry-forced zero moments.
2. Recover the applicable signed third-moment identities without substituting absolute moments for them; distinguish proved relations from modeled closures.
3. For empirical claims, compare independent statistics with uncertainty and finite-Reynolds-number controls.

### Background needed

- Incompressible turbulence, structure functions and multifractal modeling.
- Statistical convergence, Reynolds-number scaling and numerical resolution.

<a id="verification"></a>

## Resources and verification

### Resource requirements

**Computing:** Symbolic checks and analysis of selected statistics may be modest; new well-resolved high-Reynolds-number DNS is a major computing task. No costs or runtimes are measured.

**Data:** The cited DNS data are available upon reasonable request and were not publicly deposited; access has not been obtained.

**Experiments:** No new experiment is required for analytical work. Empirical validation requires suitable numerical or measured evidence.

**Theory and model requirements:** The declared flow class, moment definitions, scaling limit and any statistical closure must remain explicit.

**Validation modes:** Proof, Numerical evidence.

### Verification steps

1. Check increment conventions and exact low-order identities against the published version.
2. List each additional statistical hypothesis and where it enters.
3. Separate fitting data from validation data and examine resolution, sampling, anisotropy and scaling-window sensitivity.
4. Retain uncertainty and alternative extrapolations rather than certifying universality from finite data.

**Statement alignment:** A successful fit or conditional closure is not a general derivation of turbulence exponents.

**Human review difficulty:** High: statistical and fluid-dynamical assumptions require specialist assessment.

### Formal validity and empirical support

**What the formal task can establish:** Separate exact identities from results conditional on a multifractal or closure model.

**Empirical support and limits:** The sources report finite-Reynolds-number comparisons. No new validation or asymptotic universality claim is supplied here.

### Methods and obstacles

**Proposed methods:**

- Statistical model analysis
- Moment-identity checks
- Controlled comparison with numerical statistics

**Expected obstacles:**

- Finite scaling windows can imitate asymptotic exponents.
- Rare-event moments converge slowly.
- Model assumptions can be mistaken for consequences of Navier-Stokes dynamics.

### Checks still needed

- Confirm access, rights and suitability of any validation data.
- A low-order subproblem is Curator-proposed; pending review and a focused novelty check.

<a id="evidence"></a>

## Evidence and context

**Status basis:** The September 2026 published paper retains the missing full mixed-exponent description; the review identifies the same need. Targeted searches found no later complete resolution.

[Dated literature checks and remaining limits](../candidates/Q-MODEL-495.md#literature-checks). These are editorial evidence checks, not signed expert reviews.

**Exact problem / theorem locator:** Buaria, Physical Review Fluids 11 L092601, conclusions pp.6-7 and Appendix C; Buaria and Pumir, section 9.1.

### Sources

- [Joint multifractal description of small-scale turbulence: Unifying longitudinal and transverse velocity intermittency](../sources.md#src-phys-009). Dhawal Buaria. 2026. [Read source](https://journals.aps.org/prfluids/pdf/10.1103/24bv-jqps).
  - **Relevant sections:** Physical Review Fluids 11, L092601, published 2026-09-18; conclusions pp.6-7, data availability p.7, Appendix C p.9; equations (18)-(19).
  - **Source limitations:** The underlying DNS data were not publicly deposited; access requires a separate request. The published one-transverse-component relation uses 4/15, correcting the older arXiv:2601.12528v1 wording. Finite-Reynolds-number agreement is not an asymptotic proof.
- [Turbulence intermittency and velocity gradients](../sources.md#src-phys-010). Dhawal Buaria; Alain Pumir. 2026. [Read source](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/83110A5131F55CF9B890415703AA7770/S0022112026114943a.pdf/div-class-title-turbulence-intermittency-and-velocity-gradients-div.pdf).
  - **Relevant sections:** Journal of Fluid Mechanics 1034, P1; published online 2026-05-07; DOI 10.1017/jfm.2026.11494; section 9.1, pp.70-71, and data availability p.78.
  - **Source limitations:** Relevant review sections were inspected. Its underlying data are available upon reasonable request, not assumed accessible to this project.

### Known results and partial progress

- Buaria provides a joint multifractal framework linking increment and gradient statistics, without closing the entire exponent family.
- Published equations (18)-(19) use the 4/5 and one-transverse-component 4/15 relations; the earlier preprint's 4/3 wording should not be copied.
- The paper notes that further changes of exponents at much higher Reynolds numbers cannot be excluded.

**Research value:** A reliable theory would clarify extreme-event statistics relevant to dissipation, mixing and transport. Any improvement to reduced fluid models needs separate demonstration.

### Related problems

No formal dependency or equivalence is asserted.

### Scope of the status check

**Finding:** The published discussion explicitly retains the mixed-exponent closure problem.

**Search limits:** No exhaustive review of every proposed intermittency model; no data access or independent reanalysis.

<details>
<summary>Literature references checked</summary>

**Queries used:**

- "mixed exponents" "intermittency" "2026"
- "Turbulence intermittency and velocity gradients" Buaria Pumir 2026
- "mixed" "exponents" "Buaria" "2026"
- "longitudinal" "transverse" "intermittency" "closed" "2026"
- "mixed structure functions" "2026" turbulence prediction
- "24bv-jqps"

**Sources checked:**

- [Joint multifractal description of small-scale turbulence: Unifying longitudinal and transverse velocity intermittency](../sources.md#src-phys-009)
- [Turbulence intermittency and velocity gradients](../sources.md#src-phys-010)

</details>

<details>
<summary>Previous attempts and public records</summary>

- The cited articles report theoretical frameworks and numerical comparisons; this project has not reproduced them.

</details>

<details>
<summary>Attribution and suggested citation</summary>

**Original authors and credited contributors:**

- Dhawal Buaria
- Alain Pumir

**Suggested citation:** Buaria (2026), Physical Review Fluids 11, L092601, doi:10.1103/24bv-jqps; Buaria and Pumir (2026), Journal of Fluid Mechanics 1034, P1, doi:10.1017/jfm.2026.11494.

**Editorial credit:** Compiled for Theory Research Atlas with Codex assistance.

</details>

<a id="assessment"></a>

## AI trial assessment

**Label:** [Exploratory](../ai-assessment.md). **Evidence:** Untested forecast. **Assessed:** 2026-10-20.

Symbolic consistency checks and comparison of statistical closures offer bounded tasks. Predicting universal exponents requires more than fitting numerical data; this proposed AI role has not been tested.

**Model or capability conditions:** No named model evaluated; assumes a tool-using assistant with source access and specialist human review.

**Uncertainty:** No model has been evaluated; tractability, novelty and resource needs remain uncertain.

Ratings are separate judgments, not a score. High expertise needed or verification difficulty means a larger burden; high method availability or checkability means stronger support.

| Dimension | Rating | Reason |
| --- | --- | --- |
| Statement clarity | Medium | The exponent family is defined after conventions are fixed. |
| Decomposability | Medium | Selected moments offer narrower targets. |
| Methods and literature | High | The literature supplies statistical frameworks. |
| Search / symbolic fit | High | Symbolic consistency and statistics suit tools. |
| Checkability | Medium | Finite evidence cannot settle asymptotics. |
| Expertise needed | High | Fluid dynamics and statistics expertise are necessary. |
| Scholarly significance | High | The question concerns central transport statistics. |
| Verification difficulty | High | Closure validity and rare-event sampling are difficult. |

**Correctness:** No project answer.

Source curation only; no project answer or independent proof audit.

**Novelty:** Not assessed.

Any proposed partial result requires its own literature check.

<details>
<summary>Difficulty and significance</summary>

**Difficulty:** High.

Moment closure, rare-event statistics and the high-Reynolds-number limit remain unresolved; fitting a finite dataset cannot remove those difficulties.

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
| Stable ID | `Q-MODEL-495` |
| Duplicate key | `turbulence-joint-longitudinal-transverse-intermittency-exponents` |
| Original domain label | Fluid and plasma theory |
| Original cross-domain labels | Statistical and nonequilibrium physics |
| Primary domain ID | `PHYS.FLUID` |
| Cross-domain IDs | `PHYS.STAT` |
| Origin code | `literature_open` |
| Status code | `open_after_scoped_check` |
| Curator-designed scope | No |
| Detailed entry | Yes |
| Record level | `C` |
| Human review status | `pending` |
| Trial-label code | `exploratory` |
| Assessment-evidence code | `untested_forecast` |
| Method tags | `model_analysis`, `symbolic_derivation`, `numerical_computation` |
| Validation tags | `pure_proof`, `numerical_evidence` |
| Experimental-dependency tag | `none_for_formal_task` |

[JSON record](../../data/cards/Q-MODEL-495.json)

</details>

[Problem cards](README.md) · [Back to top](#at-a-glance)
