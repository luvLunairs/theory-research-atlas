# Verify the Ornstein–Uhlenbeck transition law and equilibrium

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

Check a standard random process that is pulled toward the origin while experiencing noise. Its exact probability distribution offers a controlled way to verify stochastic equations, stationary distributions and equilibrium claims.

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-103%3A+Verify+the+Ornstein%E2%80%93Uhlenbeck+transition+law+and+equilibrium&target=Q-MODEL-103) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-103%3A+Verify+the+Ornstein%E2%80%93Uhlenbeck+transition+law+and+equilibrium&target=Q-MODEL-103)

[At a glance](#at-a-glance) · [The task](#problem) · [Resources and verification](#verification) · [Evidence and context](#evidence) · [AI trial assessment](#assessment) · [Research records](#audit-trail)

<a id="at-a-glance"></a>

## At a glance

| Field | Summary |
| --- | --- |
| Primary field | [Statistical and nonequilibrium physics](../domains/phys.md#phys-stat) |
| Related fields | [Stochastic processes and stochastic analysis](../domains/prob.md#prob-process), [Molecular statistical mechanics](../domains/chem.md#chem-stat) |
| Task origin | [Known-result calibration](../evidence-policy.md) |
| Current status | [Known result in literature](../evidence-policy.md) · checked 2026-10-14 |
| AI suitability | [Priority for a later trial](../ai-assessment.md) · Untested forecast |
| Scientific review | Pending |

<a id="problem"></a>

## The task

### Precise statement

For the one-dimensional Itô process dX_t=−a X_t dt+sqrt(2D)dW_t, with a,D&gt;0 and deterministic X_0=x_0, reproduce the Gaussian transition law with mean x_0 exp(−at) and variance (D/a)(1−exp(−2at)). Verify its Fokker–Planck equation, normalization, weak initial limit, Gaussian composition law and stationary density proportional to exp(−a x^2/(2D)). Check zero stationary probability current and detailed balance.

**Required output:** A matched SDE and density derivation, plus explicit checks of normalization, the weak initial condition, composition, stationarity and detailed balance.

**Scope:** The exact scalar Ornstein–Uhlenbeck model with additive Gaussian noise. No interacting-particle model, colored noise, parameter fitting or physical measurement.

### Assumptions

- W_t is standard one-dimensional Brownian motion and the SDE uses the Itô convention.
- a and D are fixed positive real constants; x_0 is deterministic; time is nonnegative and space is the entire real line.
- The drift is restoring, −a x, and the noise coefficient is sqrt(2D); there are no boundaries, absorbing states or time-dependent parameters.
- Use p_t(y|x) for the transition density from x to y; detailed balance means pi(x)p_t(y|x)=pi(y)p_t(x|y) for the stationary density pi.

### Success criteria

1. Recover the mean and variance from the integrating-factor representation and the Itô isometry.
2. Verify ∂_t p=a ∂_y(y p)+D ∂_yy p for t&gt;0, with the same drift and noise normalization as the SDE.
3. Show normalization, nonnegative density, weak convergence to delta_x at t down to zero and Gaussian kernel composition for positive times.
4. Normalize the stationary Gaussian with variance D/a, check zero current j(y)=−a y pi(y)−D pi'(y), and verify detailed balance.
5. Explain that agreement with the mathematical equilibrium distribution does not validate a physical noise model.

### Background needed

- Gaussian densities and convolution.
- Basic Itô integration, deterministic integrating factors and the Itô isometry.
- Fokker–Planck equations, probability current and weak convergence.

<a id="verification"></a>

## Resources and verification

### Resource requirements

**Computing:** Symbolic differentiation, Gaussian integration and a few exact identities. A local computer algebra environment is a plausible resource class; no simulation campaign, runtime or cost measurement is required or reported.

**Data:** No empirical observations. All inputs are symbolic model constants and initial conditions.

**Experiments:** None for the stochastic theorem. A physical Brownian-motion interpretation would require measurements and justification of the noise and overdamped approximations.

**Theory and model requirements:** Standard Brownian increments, Itô dynamics, constant positive coefficients and an unbounded state space with Gaussian decay.

**Validation modes:** Proof, Exact computation.

### Verification steps

1. Derive the stochastic integrating-factor solution and compute its first two moments.
2. Insert the resulting Gaussian into the forward equation and check normalization analytically.
3. Prove the weak initial limit against bounded continuous test functions and verify the Gaussian composition identity.
4. Compute the normalized stationary density, boundary decay and current.
5. Verify detailed balance by comparing both sides as functions of the two positions and time.
6. Have a reviewer compare all conventions with the source SDE and its Appendix A.2, rather than relying on imperfect extracted formula text.

**Statement alignment:** The verified kernel must belong to the exact SDE written here. Numerical paths or moment agreement alone do not establish the density, semigroup or equilibrium interpretation.

**Human review difficulty:** Moderate: formulas are explicit, but the probability-space assumptions and weak limit need a reviewer familiar with stochastic processes.

### Formal validity and empirical support

**What the formal task can establish:** The result is an exact theorem about the declared scalar Itô process and its transition density.

**Empirical support and limits:** No claim is made that a physical particle, molecule or measurement follows this SDE; such use requires independent evidence about drift, noise and time scales.

### Methods and obstacles

**Proposed methods:**

- Integrating factors and Itô isometry
- Fokker–Planck verification
- Gaussian convolution
- Stationary-current and reversibility checks

**Expected obstacles:**

- Losing the factor of two in the noise coefficient or using an anti-restoring drift.
- Confusing standard deviation with variance in the Gaussian normalization.
- Treating a delta initial condition as a pointwise limit of densities.
- Inferring physical fluctuation–dissipation relations from arbitrary a and D without a model interpretation.

### Checks still needed

- Select a symbolic checker and specify which analytic steps remain for human review.
- If a physical application is proposed, separately identify mobility, temperature and the evidence supporting the noise model.

<a id="evidence"></a>

## Evidence and context

**Status basis:** The transition and equilibrium formulas are established results in the cited lectures. The verification checklist is a curator-selected calibration task.

**Exact problem / theorem locator:** Bazant lecture 14, pp.4–5 and Appendix A.1–A.2, pp.7–8; Tong, Section 3.2.2, equations (3.28)–(3.31).

### Sources

- [Lecture 14: Applications in Statistical Mechanics](../sources.md#src-model-105). Martin Z. Bazant (lecturer); Kirill Titievsky (scribe); Geraint Jones (Appendix A.2). 2005. [Read source](https://ocw.mit.edu/courses/18-366-random-walks-and-diffusion-fall-2006/0a8bdd9c04730a715ad5d54640a3702a_lec14.pdf).
  - **Relevant sections:** Dated March 29, 2005; pp.4–5, harmonic potential; Appendix A.1–A.2, pp.7–8; hosted in MIT 18.366 Fall 2006
  - **Source limitations:** The lecture file predates its hosting course. Some extracted formula text has damaged symbols, so the positive diffusion and restoring-drift conventions must be checked against the displayed SDE and Appendix A.2.
- [Kinetic Theory: Stochastic Processes](../sources.md#src-model-106). David Tong. 2012. [Read source](https://www.damtp.cam.ac.uk/user/tong/kintheory/three.pdf).
  - **Relevant sections:** Section 3.1.3, equation (3.12); Section 3.2.2, equations (3.28)–(3.31), printed pp.66–67; Section 3.2.3
  - **Source limitations:** Normalizability, boundary conditions and applicability of the overdamped approximation require separate checks. An equilibrium density does not itself give barrier-crossing times. The author's course page dates the notes to 2012.

### Known results and partial progress

- The inspected MIT lecture gives the transition mean and variance through both Fourier methods and a stochastic integrating factor.
- The current form of the Fokker–Planck equation connects conservative drift with an equilibrium density under the stated boundary assumptions.

**Research value:** A continuous stochastic benchmark with several independent checks. It tests equation translation and equilibrium reasoning that also appear in molecular models, while leaving physical adequacy to separate evidence.

### Related problems

- **Method preparation for:** [Verify equilibrium for an overdamped quartic potential](../candidates.md#q-model-106). The harmonic restoring drift provides a reference before checking the equilibrium current for a nonlinear quartic potential. Its explicit transition kernel does not transfer to that nonlinear case.

### Scope of the status check

**Finding:** The transition law and equilibrium relation are established in the opened lecture texts. This is a calibration target, with no open-problem status.

**Search limits:** No project derivation, symbolic verification or stochastic simulation has been performed. The model's empirical validity was not assessed.

<details>
<summary>Literature references checked</summary>

**Sources checked:**

- [Lecture 14: Applications in Statistical Mechanics](../sources.md#src-model-105)
- [Kinetic Theory: Stochastic Processes](../sources.md#src-model-106)

</details>

<details>
<summary>Previous attempts and public records</summary>

- MIT lecture 14 contains the known Fokker–Planck and stochastic-integral derivations; Appendix A.2 credits Geraint Jones.
- Tong's kinetic-theory notes develop the probability-current and equilibrium interpretation.

</details>

<details>
<summary>Attribution and suggested citation</summary>

**Original authors and credited contributors:**

- Martin Z. Bazant (lecturer)
- Kirill Titievsky (scribe)
- Geraint Jones (stochastic derivation)
- David Tong (supporting exposition)

**Suggested citation:** Bazant, M. Z., lecture 14, Applications in Statistical Mechanics, notes by K. Titievsky, March 29, 2005, Appendix A.2 by G. Jones, March 30, 2005; MIT OpenCourseWare 18.366 Fall 2006. Tong, D. (2012). Kinetic Theory, Section 3: Stochastic Processes.

**Editorial credit:** Compiled for Theory Research Atlas with AI assistance.

</details>

<a id="assessment"></a>

## AI trial assessment

**Label:** [Priority for a later trial](../ai-assessment.md). **Evidence:** Untested forecast. **Assessed:** 2026-10-14.

The closed-form kernel can be checked by both stochastic and differential-equation routes. The main value is whether a generated derivation keeps its conventions and limiting statements consistent.

**Model or capability conditions:** No named model evaluated; assumes tool-using AI with symbolic algebra, basic stochastic calculus and human review of probability arguments.

**Uncertainty:** No AI trial was run. Correctly recalling a Gaussian formula is weaker than satisfying the full verification checklist.

Ratings are separate judgments, not a score. High expertise needed or verification difficulty means a larger burden; high method availability or checkability means stronger support.

| Dimension | Rating | Reason |
| --- | --- | --- |
| Statement clarity | High | The SDE, parameters, initial condition and required identities are explicit. |
| Decomposability | High | Moments, density, initial limit, stationarity and reversibility have separate checks. |
| Methods and literature | High | The opened lectures provide two derivations and equilibrium background. |
| Search / symbolic fit | High | Symbolic differentiation and Gaussian integral identities are a strong fit. |
| Checkability | High | The main checks reduce to explicit formulas, with a short analytic argument for the weak limit. |
| Expertise needed | Medium | A stochastic-analysis reviewer should check the Itô and limiting arguments. |
| Scholarly significance | Medium | A useful continuous-model calibration, not a new stochastic theorem. |
| Verification difficulty | Medium | Algebra is compact; weak convergence and detailed balance cannot be replaced by plotted densities. |

**Correctness:** No project answer.

The cited sources support the mathematical target. No project answer has been submitted or independently reviewed.

**Novelty:** Not claimed.

A known-result calibration with curator-selected checks; no new theorem or empirical finding is claimed.

<details>
<summary>Difficulty and significance</summary>

**Difficulty:** Medium.

The closed form is elementary, but the full checklist spans stochastic integrals, a PDE, weak convergence and reversibility.

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
| Stable ID | `Q-MODEL-103` |
| Duplicate key | `ou-restoring-diffusion-kernel-equilibrium-calibration` |
| Original domain label | Statistical physics |
| Original cross-domain labels | Stochastic processes; Molecular statistical mechanics |
| Primary domain ID | `PHYS.STAT` |
| Cross-domain IDs | `PROB.PROCESS`, `CHEM.STAT` |
| Origin code | `known_result_calibration` |
| Status code | `known_result` |
| Curator-designed scope | Yes |
| Detailed entry | Yes |
| Record level | `C` |
| Human review status | `pending` |
| Trial-label code | `priority_trial` |
| Assessment-evidence code | `untested_forecast` |
| Method tags | `symbolic_derivation`, `proof`, `model_analysis` |
| Validation tags | `pure_proof`, `exact_computation` |
| Experimental-dependency tag | `none_for_formal_task` |

[JSON record](../../data/cards/Q-MODEL-103.json)

</details>

[Problem cards](README.md) · [Back to top](#at-a-glance)
