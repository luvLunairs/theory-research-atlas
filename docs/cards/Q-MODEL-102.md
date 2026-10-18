# Recover the linear stability threshold of triangular Lagrange points

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

Reproduce the textbook mass-ratio threshold at which small planar disturbances of the triangular Lagrange equilibria cease to remain bounded in the linearized model. The task deliberately stops before nonlinear or real-system stability.

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-102%3A+Recover+the+linear+stability+threshold+of+triangular+Lagrange+points&target=Q-MODEL-102) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-102%3A+Recover+the+linear+stability+threshold+of+triangular+Lagrange+points&target=Q-MODEL-102)

[At a glance](#at-a-glance) · [The task](#problem) · [Resources and verification](#verification) · [Evidence and context](#evidence) · [AI trial assessment](#assessment) · [Research records](#audit-trail)

<a id="at-a-glance"></a>

## At a glance

| Field | Summary |
| --- | --- |
| Primary field | [Celestial dynamics](../domains/astro.md#astro-dyn) |
| Related fields | [Dynamical systems and ergodic theory](../domains/math.md#math-dyn), [Classical mechanics and continuum theory](../domains/phys.md#phys-classical) |
| Task origin | [Known-result calibration](../evidence-policy.md) |
| Current status | [Known result in literature](../evidence-policy.md) · checked 2026-10-14 |
| AI suitability | [Priority for a later trial](../ai-assessment.md) · Untested forecast |
| Scientific review | Pending |

<a id="problem"></a>

## The task

### Precise statement

In the planar circular restricted three-body problem with unit primary separation, unit angular speed and mass fractions 1−mu and mu, 0&lt;mu≤1/2, reproduce the linearized characteristic polynomial at L4 and L5: lambda^4+lambda^2+(27/4)mu(1−mu). Establish bounded solutions of the linearized system for 0&lt;mu&lt;mu_R and linear instability for mu_R&lt;mu≤1/2, where mu_R=(1−sqrt(23/27))/2. Exclude mu=mu_R, and do not claim nonlinear stability.

**Required output:** An exact Jacobian, determinant certificate and parameter analysis distinguishing bounded linearized motion from exponential linear instability.

**Scope:** Planar, infinitesimal disturbances of the triangular equilibria in an ideal circular restricted model, away from the critical mass. No collision dynamics, eccentric primary orbits or nonlinear perturbation theorem.

### Assumptions

- Two point-mass primaries follow circular orbits, while the third body has negligible mass and does not influence them.
- Use a uniformly rotating planar frame, separation 1, angular speed 1 and total normalized primary mass 1; the masses are 1−mu and mu with 0&lt;mu≤1/2.
- The primaries are at (−mu,0) and (1−mu,0). Define r_1^2=(x+mu)^2+y^2 and r_2^2=(x−1+mu)^2+y^2.
- Omega=(x^2+y^2)/2+(1−mu)/r_1+mu/r_2, with x_ddot−2y_dot=Omega_x and y_ddot+2x_dot=Omega_y.
- L4 and L5 are (1/2−mu, ±sqrt(3)/2); the critical parameter mu_R is excluded from the stability assertion.

### Success criteria

1. Verify both equilibrium coordinates directly in the rotating equations.
2. Construct the first-order 4-by-4 linearization in a declared state order and derive its characteristic polynomial exactly.
3. Use q=lambda^2 to establish two distinct negative q roots below the threshold and the unstable spectrum above it.
4. Explain why distinct imaginary eigenvalues yield bounded solutions of this linear system; do not infer nonlinear Lyapunov stability.
5. State explicitly that equality at mu_R is excluded because repeated eigenvalues require additional analysis.

### Background needed

- Linearization of autonomous differential equations and exact determinants.
- Eigenvalues, diagonalizability and the distinction between linear and nonlinear stability.
- Rotating-frame Newtonian mechanics.

<a id="verification"></a>

## Resources and verification

### Resource requirements

**Computing:** One exact 4-by-4 determinant with an algebraic parameter and quadratic discriminant analysis. A local symbolic environment is a plausible resource class; no runtime or cost has been measured.

**Data:** No observational catalog; only the stated dimensionless model.

**Experiments:** None for the exact linearization. Assessing real Trojan objects or mission trajectories would require additional forces, initial conditions and observations.

**Theory and model requirements:** Newtonian point masses, circular prescribed primaries, zero-mass third body, planar motion and infinitesimal perturbations.

**Validation modes:** Proof, Exact computation.

### Verification steps

1. Translate the source notation mu_2=mu, mu_1=1−mu and Omega=−U.
2. Differentiate the declared potential, check each equilibrium and form the 4-by-4 matrix.
3. Independently expand det(lambda I−A) and compare its coefficients with the stated polynomial.
4. Check discriminant signs, nonzero roots and diagonalizability in the strict stable interval.
5. Review every stability sentence for its linear, planar and model-conditional scope.

**Statement alignment:** The certificate concerns bounded solutions of the linearized equation for strict parameter intervals. It is not a theorem about nonlinear trajectories or a real astronomical system.

**Human review difficulty:** Moderate: the determinant is easy to reproduce, while precise stability implications require dynamical-systems knowledge.

### Formal validity and empirical support

**What the formal task can establish:** The target follows from linearizing the explicitly stated circular restricted model. A valid determinant establishes only that mathematical model's local linear behavior.

**Empirical support and limits:** No real system is validated. Eccentricity, finite secondary effects, non-gravitational forces and observations matter before any physical stability inference.

### Methods and obstacles

**Proposed methods:**

- Exact linearization in rotating coordinates
- Symbolic determinant calculation
- Parameter-dependent spectral analysis

**Expected obstacles:**

- Mixing Omega with the source's negative potential U, or reversing a Coriolis sign.
- Treating imaginary eigenvalues alone as sufficient in a repeated-eigenvalue case.
- Reporting nonlinear or indefinitely stable physical trajectories from a linear calculation.

### Checks still needed

- The critical mass case needs a separate repeated-root and Jordan-form analysis if added later.
- No nonlinear stability theorem or observational application has been evaluated.

<a id="evidence"></a>

## Evidence and context

**Status basis:** The author text provides the characteristic equation and mass criterion. The card explicitly restricts their interpretation to the nondegenerate linearized planar problem.

**Exact problem / theorem locator:** Fitzpatrick, Stability of Lagrange points, equations (9.73)–(9.88); Co-rotating frame, equations (9.22)–(9.30).

### Sources

- [Introduction to Celestial Mechanics, 2nd Edition: Stability of Lagrange points](../sources.md#src-model-103). Richard Fitzpatrick. Year not verified. [Read source](https://farside.ph.utexas.edu/teaching/celestial/Celestial/node86.html).
  - **Relevant sections:** Chapter 9, equations (9.73)–(9.88), especially the triangular-point characteristic equation (9.87)
  - **Source limitations:** The relevant calculation is a linear stability calculation. It does not establish nonlinear stability, realistic-system longevity, or the degenerate critical-mass case. No publication date is displayed on the inspected page.
- [Introduction to Celestial Mechanics, 2nd Edition: Co-rotating frame](../sources.md#src-model-104). Richard Fitzpatrick. Year not verified. [Read source](https://farside.ph.utexas.edu/teaching/celestial/Celestial/node83.html).
  - **Relevant sections:** Chapter 9, equations (9.22)–(9.36): rotating equations, effective potential, Jacobi integral and allowed regions
  - **Source limitations:** Circular primary orbits and a massless test body are model assumptions. An allowed position need not be reached by a specified orbit. No publication date is displayed on the inspected page.

### Known results and partial progress

- Fitzpatrick's equation (9.87) gives the triangular-point spectral polynomial and equation (9.88) gives the mass criterion.
- The linear calculation alone does not control nonlinear resonances, finite disturbances or neglected forces.

**Research value:** A manageable continuous-dynamics calibration for sign conventions, parameter inequalities and the scope of a stability theorem. It supports careful celestial-model reasoning without claiming a new orbit or astrophysical prediction.

### Related problems

- **Related method:** [Verify Jacobi conservation and certified forbidden regions](../candidates.md#q-model-105). Both use the same rotating restricted model. The Jacobi integral checks a conserved quantity rather than local equilibrium stability.

### Scope of the status check

**Finding:** The opened author text derives the known characteristic equation and strict mass criterion; the task is a reproduction.

**Search limits:** No independent symbolic derivation was run. The source's broader prose is not used as evidence for nonlinear stability.

<details>
<summary>Literature references checked</summary>

**Sources checked:**

- [Introduction to Celestial Mechanics, 2nd Edition: Stability of Lagrange points](../sources.md#src-model-103)
- [Introduction to Celestial Mechanics, 2nd Edition: Co-rotating frame](../sources.md#src-model-104)

</details>

<details>
<summary>Previous attempts and public records</summary>

- Fitzpatrick's author-maintained text derives the classical triangular-equilibrium linear stability criterion.

</details>

<details>
<summary>Attribution and suggested citation</summary>

**Original authors and credited contributors:**

- Richard Fitzpatrick (inspected exposition)

**Suggested citation:** Fitzpatrick, R. Introduction to Celestial Mechanics, 2nd Edition, Chapter 9: Co-rotating frame and Stability of Lagrange points. University of Texas at Austin, undated online text. https://farside.ph.utexas.edu/teaching/celestial/Celestial/node86.html.

**Editorial credit:** Compiled for Theory Research Atlas with AI assistance.

</details>

<a id="assessment"></a>

## AI trial assessment

**Label:** [Priority for a later trial](../ai-assessment.md). **Evidence:** Untested forecast. **Assessed:** 2026-10-14.

The symbolic target is short enough for an independent determinant check, while its interpretation tests a frequent overstatement about stability.

**Model or capability conditions:** No named model evaluated; assumes tool-using AI with symbolic differentiation, exact polynomial algebra and access to a dynamical-systems reviewer.

**Uncertainty:** No model was tested. Familiarity with the classical result can conceal a wrong sign or an unjustified nonlinear conclusion.

Ratings are separate judgments, not a score. High expertise needed or verification difficulty means a larger burden; high method availability or checkability means stronger support.

| Dimension | Rating | Reason |
| --- | --- | --- |
| Statement clarity | High | Equations, coordinates, parameter domain and excluded threshold are explicit. |
| Decomposability | High | Equilibrium substitution, Jacobian construction and spectral reasoning are separable. |
| Methods and literature | High | The author text provides the reference linearization and threshold. |
| Search / symbolic fit | High | Exact differentiation and determinants avoid a numerical eigenvalue sweep. |
| Checkability | High | A polynomial identity and elementary inequalities can be checked independently. |
| Expertise needed | Medium | A mechanics or dynamical-systems reviewer must check coordinate conventions and stability language. |
| Scholarly significance | Medium | Useful for disciplined model analysis, with no new celestial result sought. |
| Verification difficulty | Medium | The algebra is small, but spectrum, bounded linear motion and nonlinear stability must remain distinct. |

**Correctness:** No project answer.

The cited sources support the mathematical target. No project answer has been submitted or independently reviewed.

**Novelty:** Not claimed.

A known-result calibration with curator-selected checks; no new theorem or empirical finding is claimed.

<details>
<summary>Difficulty and significance</summary>

**Difficulty:** Medium.

A small exact matrix calculation is paired with nontrivial interpretation of spectral stability and degenerate cases.

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
| Stable ID | `Q-MODEL-102` |
| Duplicate key | `cr3bp-l4-l5-linear-threshold-calibration` |
| Original domain label | Celestial dynamics |
| Original cross-domain labels | Dynamical systems; Classical mechanics |
| Primary domain ID | `ASTRO.DYN` |
| Cross-domain IDs | `MATH.DYN`, `PHYS.CLASSICAL` |
| Origin code | `known_result_calibration` |
| Status code | `known_result` |
| Curator-designed scope | Yes |
| Detailed entry | Yes |
| Record level | `C` |
| Human review status | `pending` |
| Trial-label code | `priority_trial` |
| Assessment-evidence code | `untested_forecast` |
| Method tags | `symbolic_derivation`, `exact_computation`, `proof`, `model_analysis` |
| Validation tags | `pure_proof`, `exact_computation` |
| Experimental-dependency tag | `none_for_formal_task` |

[JSON record](../../data/cards/Q-MODEL-102.json)

</details>

[Problem cards](README.md) · [Back to top](#at-a-glance)
