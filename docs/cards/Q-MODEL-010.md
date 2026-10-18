# Reproduce equilibrium branches in an energy-balance climate model

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

Reproduce equilibrium branches of a published low-dimensional climate model and put error bounds around its folds. The exercise illustrates why local sensitivity becomes unreliable near a turning point; it does not estimate a threshold for the Earth's climate.

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-010%3A+Reproduce+equilibrium+branches+in+an+energy-balance+climate+model&target=Q-MODEL-010) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-010%3A+Reproduce+equilibrium+branches+in+an+energy-balance+climate+model&target=Q-MODEL-010)

[At a glance](#at-a-glance) · [The task](#problem) · [Resources and verification](#verification) · [Evidence and context](#evidence) · [AI trial assessment](#assessment) · [Research records](#audit-trail)

<a id="at-a-glance"></a>

## At a glance

| Field | Summary |
| --- | --- |
| Primary field | [Climate dynamics and reduced models](../domains/earth.md#earth-climate) |
| Related fields | [Dynamical systems and ergodic theory](../domains/math.md#math-dyn), [Numerical analysis and scientific computation](../domains/math.md#math-numer) |
| Task origin | [Known-result calibration](../evidence-policy.md) |
| Current status | [Known result in literature](../evidence-policy.md) · checked 2026-10-14 |
| AI suitability | [Preparation needed](../ai-assessment.md) · Untested forecast |
| Scientific review | Pending |

<a id="problem"></a>

## The task

### Precise statement

For the deterministic energy-balance model of Ashwin and von der Heydt, use the decimal parameter values in Table 1 as exact model inputs on T in [260,310] K. Reproduce Gamma(T) in equation (18), isolate every root of R'(T) in this interval with certified error control, classify nondegenerate folds and regular equilibrium stability, and verify S=1/R'(T) wherever R'(T)≠0. State why this local sensitivity formula does not apply at a fold. Noise is set to zero and carbon dioxide is a fixed positive parameter.

**Required output:** A reproducible model specification, certified fold intervals and stable/unstable regular branches, with a precise explanation of local versus finite-change sensitivity.

**Scope:** The deterministic equilibrium curve of the paper's specified scalar model on a fixed temperature interval. No stochastic tipping simulation, parameter estimation, future-emissions scenario or observational climate sensitivity.

### Assumptions

- Use c_T dT/dt=F(T,C)=Q_0(1−alpha(T))+A ln(C/C_0)−epsilon(T)sigma T^4, with fixed C&gt;0 and no stochastic terms.
- Define epsilon(T)=epsilon_1+(epsilon_2−epsilon_1)[1+tanh((T−T_0)/T_epsilon)]/2.
- Define H(z)=[1+tanh(z/T_alpha)]/2, Sigma(T)=(T−T_1)H(T−T_1)H(T_2−T)/(T_2−T_1)+H(T−T_2), and alpha(T)=alpha_1(1−Sigma(T))+alpha_2 Sigma(T).
- Use alpha_1=0.52, alpha_2=0.47, T_1=278 K, T_2=288 K, epsilon_1=0.53, epsilon_2=0.39, T_0=288 K, T_alpha=5 K and T_epsilon=20 K.
- Use A=5.35 W m^−2, C_0=280 ppm, Q_0=342 W m^−2, sigma=5.67×10^−8 W m^−2 K^−4 and c_T=5×10^8 J m^−2 K^−1. Treat these decimal values as exact model inputs, not exact measured constants.
- Restrict the certification to T in [260,310] K. Retain the smooth tanh functions and their tails; do not replace them by discontinuous steps or truncate their derivatives.

### Success criteria

1. Derive R(T)=epsilon(T)sigma T^4−Q_0(1−alpha(T)) and Gamma(T)=C_0 exp(R(T)/A) from F=0.
2. Obtain R' and R'' by independent differentiation of the declared functions; document any disagreement with the source's displayed curvature expression.
3. Isolate every root of R' in [260,310] K, proving existence and uniqueness in each reported interval and excluding roots in the remaining domain; target interval width at most 10^−6 K.
4. At each root, certify nonzero R'' before calling it a nondegenerate fold; bound the corresponding R and Gamma values with outward rounding.
5. Classify regular equilibria from F_T/c_T=−R'/c_T; establish S=dT/dR=1/R' only where the inverse function theorem applies.
6. Compare certified intervals with the paper's rounded illustrative values and report discrepancies without changing parameters to force agreement.

### Background needed

- Scalar equilibrium stability and the inverse function theorem.
- Differentiation of composite smooth functions and physical-unit bookkeeping.
- Interval arithmetic or another rigorous root-isolation method for transcendental functions.

<a id="verification"></a>

## Resources and verification

### Resource requirements

**Computing:** One-dimensional interval subdivision and validated evaluation of tanh and exp. A local validated-numerics environment is a plausible starting resource class, but total subdivisions, precision, runtime and cost are unmeasured and must be reported in any future attempt.

**Data:** The cited equations and Table 1 only; no temperature record, emissions dataset or remote climate simulation.

**Experiments:** None for the model reproduction. Empirical climate adequacy, feedback calibration and real tipping estimates would require observational and modeling evidence beyond this task.

**Theory and model requirements:** A scalar global energy-balance model with prescribed smooth albedo and emissivity, fixed external carbon dioxide, positive heat capacity and exact decimal parameters.

**Validation modes:** Proof, Exact computation, Numerical evidence.

### Verification steps

1. Compare each function and parameter with the original Table 1 and equations (15)–(19), recording units and the zero-noise choice.
2. Differentiate R from its definition by two independently inspectable routes; reconcile the first derivative with equation (21) and flag the curvature discrepancy.
3. Use directed rounding or rigorous analytic enclosures for tanh, exp and their derivatives.
4. Partition the whole temperature interval, certify every retained root interval and account for every excluded part of the domain.
5. Check nondegeneracy, stability signs and propagated forcing/concentration bounds; retain the certificate and checker description.
6. Review the interpretation of S away from folds and explicitly exclude observational predictions.

**Statement alignment:** The deliverable certifies the functions and exact decimals stated here on [260,310] K. It does not certify temperatures outside that interval, alternative climate models, parameter uncertainty or stochastic tipping behavior.

**Human review difficulty:** High relative to the small model: a reviewer must inspect the completeness of numerical enclosures and the distinction between a source reproduction and a real-world claim.

### Formal validity and empirical support

**What the formal task can establish:** A successful certificate would establish equilibria, folds and local sensitivities of this deterministic scalar model at its declared inputs.

**Empirical support and limits:** The model is illustrative. No evidence review is supplied for its feedback functions, parameters or applicability to real climate tipping; model folds are not validated Earth-system thresholds.

### Methods and obstacles

**Proposed methods:**

- Independent symbolic differentiation
- Validated interval root isolation
- Scalar equilibrium and fold analysis
- Dimensional and source-alignment checks

**Expected obstacles:**

- Treating a plotted fold or a floating-point root as proof that all folds have been found.
- Copying the apparent curvature-expression error after equation (21).
- Treating tanh derivatives as exactly zero outside a transition range.
- Confusing exact input decimals with empirical parameter certainty or model certification with climate validation.

### Checks still needed

- Reconcile the unnumbered second-derivative expression after equation (21) with differentiation of equation (19) before implementing fold tests.
- Check Table 1 against a visual copy before a trial if extraction or notation is ambiguous.
- Choose and document a validated arithmetic library whose transcendental enclosures meet the certificate requirements.
- The paper's prose describes transition derivatives as nonzero only in restricted ranges; for the defined smooth tanh model this must be interpreted approximately, not as compact support.

<a id="evidence"></a>

## Evidence and context

**Status basis:** The paper supplies the illustrative model and equilibrium analysis. The temperature interval and certification requirements make the existing reproduction target precise; they do not define a real-world climate threshold.

**Exact problem / theorem locator:** Section 3, equations (15)–(21), Table 1 and Figure 2; Table 1 is on printed p.1540.

### Sources

- [Extreme Sensitivity and Climate Tipping Points](../sources.md#src-model-011). Peter Ashwin; Anna S. von der Heydt. 2020. [Read source](https://link.springer.com/article/10.1007/s10955-019-02425-x).
  - **Relevant sections:** Sections 2-3; equations (15)-(21), the unnumbered curvature expression following (21), and Table 1; Discussion
  - **Source limitations:** Published online 2019, journal volume 2020. The curvature expression and approximate statements about tanh derivative ranges require care; see Q-MODEL-010. Simplified model results do not establish real-world tipping thresholds.

### Known results and partial progress

- The paper displays the equilibrium curve and reports a bistable forcing interval of approximately −1.744 to 3.004 W m^−2, corresponding to roughly 202 to 490 ppm in its illustrative model.
- Equation (21) gives the derivative used for local equilibrium sensitivity; the source separately discusses the difference between local and finite-change sensitivity.
- The curvature expression printed after equation (21) appears inconsistent with direct differentiation of equation (19), and should not be copied as a trusted identity.

**Research value:** A concrete benchmark for separating numerical pictures, certified model conclusions and empirical climate claims. It also tests whether a reproduction can expose and document source inconsistencies.

### Related problems

No formal dependency or equivalence is asserted.

### Scope of the status check

**Finding:** The opened article and its full PDF provide the model, Table 1 and known equilibrium analysis. The task is a bounded reproduction; no unresolved climate conjecture is asserted.

**Search limits:** No roots, certificates or parameter-fit results have been computed. A possible source curvature error remains a documented issue, not evidence that the paper's broader conclusions are false.

<details>
<summary>Literature references checked</summary>

**Sources checked:**

- [Extreme Sensitivity and Climate Tipping Points](../sources.md#src-model-011)

</details>

<details>
<summary>Previous attempts and public records</summary>

- Ashwin and von der Heydt present equilibrium branches and illustrative numerical behavior in Section 3 and Figure 2. Their plotted results are reference values, not a project certificate.

</details>

<details>
<summary>Attribution and suggested citation</summary>

**Original authors and credited contributors:**

- Peter Ashwin
- Anna S. von der Heydt

**Suggested citation:** Ashwin, P. and von der Heydt, A. S. (2020; published online 2019). Extreme Sensitivity and Climate Tipping Points. Journal of Statistical Physics 179, 1531–1552. https://doi.org/10.1007/s10955-019-02425-x.

**Editorial credit:** Compiled for Theory Research Atlas with AI assistance.

</details>

<a id="assessment"></a>

## AI trial assessment

**Label:** [Preparation needed](../ai-assessment.md). **Evidence:** Untested forecast. **Assessed:** 2026-10-14.

The finite interval and explicit functions make a rigorous reproduction feasible to specify. A validated transcendental arithmetic environment and resolution of the source's derivative inconsistency are prerequisites for reliable certificates.

**Model or capability conditions:** No named model evaluated; assumes tool-using AI with symbolic differentiation, validated interval arithmetic for transcendental functions and human review of numerical certificates and model scope.

**Uncertainty:** No trial was run, so the proposed precision and resource class are untested. Source transcription and interval overestimation could require revising the numerical method without altering the target.

Ratings are separate judgments, not a score. High expertise needed or verification difficulty means a larger burden; high method availability or checkability means stronger support.

| Dimension | Rating | Reason |
| --- | --- | --- |
| Statement clarity | High | The functions, parameter values, interval and certificate width are specified. |
| Decomposability | High | Model transcription, differentiation, root isolation and interpretation can be checked separately. |
| Methods and literature | High | The source gives the equilibrium construction; validated root isolation is a standard numerical method. |
| Search / symbolic fit | High | Symbolic differentiation and interval subdivision suit the declared one-dimensional task. |
| Checkability | Medium | Certificates are compact in principle, but completeness requires controlling the full interval, not sampling. |
| Expertise needed | High | A numerical-analysis reviewer and a climate-model reader should check certification and physical scope. |
| Scholarly significance | Medium | It strengthens reproduction and sensitivity interpretation without estimating Earth's actual tipping points. |
| Verification difficulty | High | Reliable exclusion of all additional roots and handling source discrepancies exceed ordinary plotting. |

**Correctness:** No project answer.

The cited sources support the mathematical target. No project answer has been submitted or independently reviewed.

**Novelty:** Not claimed.

A known-result calibration with curator-selected checks; no new theorem or empirical finding is claimed.

<details>
<summary>Difficulty and significance</summary>

**Difficulty:** Medium.

The state space is one-dimensional, but rigorous completeness, transcendental enclosures and source discrepancies make the task more demanding than plotting a curve.

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
| Stable ID | `Q-MODEL-010` |
| Duplicate key | `ashwin-vonderheydt-ebm-equilibrium-calibration` |
| Original domain label | Climate dynamics |
| Original cross-domain labels | Dynamical systems; Numerical analysis |
| Primary domain ID | `EARTH.CLIMATE` |
| Cross-domain IDs | `MATH.DYN`, `MATH.NUMER` |
| Origin code | `known_result_calibration` |
| Status code | `known_result` |
| Curator-designed scope | Yes |
| Detailed entry | Yes |
| Record level | `C` |
| Human review status | `pending` |
| Trial-label code | `preparation_required` |
| Assessment-evidence code | `untested_forecast` |
| Method tags | `symbolic_derivation`, `numerical_computation`, `certificate_checking`, `model_analysis` |
| Validation tags | `pure_proof`, `exact_computation`, `numerical_evidence` |
| Experimental-dependency tag | `none_for_formal_task` |

[JSON record](../../data/cards/Q-MODEL-010.json)

</details>

[Problem cards](README.md) · [Back to top](#at-a-glance)
