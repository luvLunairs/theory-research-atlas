# Check common quadratic Lyapunov certificates for small matrix polytopes

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

A proposed stability argument can be checked through a few exact matrices. The useful output is a certificate with explicit assumptions, including an explanation of what an unsuccessful check does not establish.

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-101%3A+Check+common+quadratic+Lyapunov+certificates+for+small+matrix+polytopes&target=Q-FORMAL-101) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-101%3A+Check+common+quadratic+Lyapunov+certificates+for+small+matrix+polytopes&target=Q-FORMAL-101)

[At a glance](#at-a-glance) · [The task](#problem) · [Resources and verification](#verification) · [Evidence and context](#evidence) · [AI trial assessment](#assessment) · [Research records](#audit-trail)

<a id="at-a-glance"></a>

## At a glance

| Field | Summary |
| --- | --- |
| Primary field | [Control, estimation and systems theory](../domains/eng.md#eng-control) |
| Related fields | [Robust design and verification](../domains/eng.md#eng-robust), [Optimization and operations research](../domains/math.md#math-opt) |
| Task origin | [Known-result calibration](../evidence-policy.md) |
| Current status | [Known result in literature](../evidence-policy.md) · checked 2026-10-14 |
| AI suitability | [Priority for a later trial](../ai-assessment.md) · Untested forecast |
| Scientific review | Pending |

<a id="problem"></a>

## The task

### Precise statement

Given 1-4 rational matrices A_i of a common dimension d &lt;= 4, a rational symmetric P, and rational alpha &gt; 0, verify exactly that P and every residual -(A_i^T P + P A_i + 2 alpha P) are positive definite. If accepted, supply the conditional exponential-decay certificate for xdot = A(t)x with arbitrary measurable A(t) in their convex hull. Rejection does not imply instability. The input bounds and strict-residual convention define a curator-proposed calibration.

**Required output:** An independently checkable rational certificate for a sufficient exponential-stability condition, or a precise account of failed certificate conditions.

**Scope:** At most four vertices and dimension at most four. Each input numerator and positive denominator has at most 64 bits. These are proposed limits for readable certificates, not measured performance guarantees. Searching for P or optimizing alpha is outside the required task.

### Assumptions

- Continuous-time homogeneous dynamics on a real finite-dimensional state space, without forcing, resets, delays or stochastic terms.
- A(t) is measurable and belongs to the compact convex hull of the fixed vertex matrices; solutions are interpreted as absolutely continuous.
- One common P and one fixed positive alpha must satisfy every vertex condition.
- Inputs are exact rationals; dimensions, denominators and symmetry are checked first.

### Success criteria

1. Retain the rational input and verify dimensions, denominators and symmetry.
2. Provide exact positive-definiteness witnesses for P and every residual, such as positive leading principal minors.
3. Justify extension from the vertices to every convex combination and to the derivative along a measurable matrix trajectory.
4. State the resulting decay estimate for V(x)=x^T P x and the corresponding Euclidean norm estimate, retaining dependence on the conditioning of P.
5. A failed or non-strict test rejects this supplied certificate; it does not establish instability or rule out another certificate.

### Background needed

- Exact rational arithmetic and positive-definite matrices.
- Lyapunov functions, linear differential inclusions and uniform decay.
- The distinction between a sufficient witness and a complete decision procedure.

<a id="verification"></a>

## Resources and verification

### Resource requirements

**Computing:** Exact determinants of matrices of order at most four with bounded rational inputs. Laptop-class execution is an untested planning assumption; larger dimensions and certificate synthesis may be much harder.

**Data:** Rational vertex matrices, a proposed P and positive alpha; no observational dataset.

**Experiments:** None for the conditional certificate. Evidence that a physical plant stays inside the uncertainty set requires separate measurements.

**Theory and model requirements:** Continuous-time dynamics, the uncertainty set and the common quadratic form are theorem premises, not conclusions inferred from data.

**Validation modes:** Proof, Exact computation.

### Verification steps

1. Compare the uncertainty model and time convention with the source.
2. Independently recompute residuals and positivity witnesses.
3. Review convexity and the almost-everywhere derivative argument.
4. Check the decay estimate and review physical interpretation separately.

**Statement alignment:** Only the declared common-quadratic sufficient condition is certified. No synthesis, optimal decay rate, empirical robustness or general instability result follows.

**Human review difficulty:** Moderate: mechanical algebra checks are short, but a control specialist should approve theorem-to-model alignment.

### Formal validity and empirical support

**What the formal task can establish:** An accepted witness entails a conditional decay guarantee for the specified differential inclusion.

**Empirical support and limits:** The certificate does not establish that a physical system is linear, unforced or contained in the supplied uncertainty set.

### Methods and obstacles

**Proposed methods:**

- Exact matrix arithmetic
- Lyapunov proof application
- Certificate checking

**Expected obstacles:**

- Using floating-point eigenvalues as exact positivity witnesses.
- Checking different P matrices for different vertices.
- Dropping the alpha term, reversing a sign, or silently switching to discrete time.
- Treating certificate rejection as an instability proof.

### Checks still needed

- Choose and record actual certificate fixtures before a trial.
- Have a control reviewer confirm the positivity convention and norm estimate.

<a id="evidence"></a>

## Evidence and context

**Status basis:** The common-quadratic criterion and decay implication are established in the opened monograph. This task checks supplied witnesses, without claiming a new theorem or complete stability decision procedure.

**Exact problem / theorem locator:** Boyd et al., Section 5.1, equations (5.8) and (5.17)

### Sources

- [Linear Matrix Inequalities in System and Control Theory](../sources.md#src-formal-101). Stephen Boyd; Laurent El Ghaoui; Eric Feron; Venkataramanan Balakrishnan. 1994. [Read source](https://stanford.edu/~boyd/lmibook/lmibook.pdf).
  - **Relevant sections:** Chapter 5, Section 5.1, equations (5.4), (5.8); Section 5.1.3, equation (5.17); printed pages 61-66
  - **Source limitations:** The theorem is conditional on the continuous-time model. No solver or physical system was evaluated. The author-hosted book is linked, not redistributed.
- [Structured and Simultaneous Lyapunov Functions for System Stability Problems](../sources.md#src-formal-102). Stephen Boyd; Qinping Yang. 1989. [Read source](https://stanford.edu/~boyd/papers/simul_lyapunov.html).
  - **Relevant sections:** Author bibliographic record; linked PDF Section 2 and convex-hull discussion preceding Theorem 5.2
  - **Source limitations:** Publication year follows the author record; the linked re-typeset PDF has a 2001 title-page date. Broader feedback-system claims are outside the proposed task.

### Known results and partial progress

- The common-quadratic polytopic criterion reduces an inequality over the matrix convex hull to finitely many vertex inequalities.
- If Vdot &lt;= -2 alpha V, then V(x(t)) &lt;= exp(-2 alpha t) V(x(0)).
- General stability does not imply the existence of a common quadratic certificate.

**Research value:** Creates a compact verification baseline for control theory and guards against overclaiming from numerical optimization or failed witness searches.

### Related problems

No formal dependency or equivalence is asserted.

### Scope of the status check

**Finding:** The criterion, vertex reduction and decay-rate condition were checked in the author-hosted monograph; the earlier paper supplies historical context.

**Search limits:** This establishes literature status of the theorem, not correctness of a future certificate. Later certificate families were not exhaustively surveyed.

<details>
<summary>Literature references checked</summary>

**Sources checked:**

- [Linear Matrix Inequalities in System and Control Theory](../sources.md#src-formal-101)
- [Structured and Simultaneous Lyapunov Functions for System Stability Problems](../sources.md#src-formal-102)

</details>

<details>
<summary>Previous attempts and public records</summary>

- The cited authors develop the underlying theory and numerical methods. No project implementation or model trial is recorded.

</details>

<details>
<summary>Attribution and suggested citation</summary>

**Original authors and credited contributors:**

- Stephen Boyd
- Laurent El Ghaoui
- Eric Feron
- Venkataramanan Balakrishnan
- Qinping Yang

**Suggested citation:** Boyd, S., El Ghaoui, L., Feron, E., and Balakrishnan, V. (1994), Linear Matrix Inequalities in System and Control Theory, SIAM, Chapter 5. Related work: Boyd, S., and Yang, Q. (1989), International Journal of Control 49(6), 2215-2240.

**Editorial credit:** Compiled for Theory Research Atlas with AI assistance.

</details>

<a id="assessment"></a>

## AI trial assessment

**Label:** [Priority for a later trial](../ai-assessment.md). **Evidence:** Untested forecast. **Assessed:** 2026-10-14.

A finite exact acceptance test separates algebra from theorem application. Priority refers to a possible calibration trial, not demonstrated AI performance.

**Model or capability conditions:** No named model evaluated; assumes a tool-using AI that can read mathematical sources, produce inspectable symbolic work and code, and work with a human domain reviewer.

**Uncertainty:** No model, solver or supplied certificate has been tested. Exact arithmetic does not establish empirical adequacy.

Ratings are separate judgments, not a score. High expertise needed or verification difficulty means a larger burden; high method availability or checkability means stronger support.

| Dimension | Rating | Reason |
| --- | --- | --- |
| Statement clarity | High | Input matrices and acceptance inequalities are explicit. |
| Decomposability | High | Input checking, matrix certificates and the decay argument can be reviewed separately. |
| Methods and literature | High | Established matrix and Lyapunov methods apply directly. |
| Search / symbolic fit | High | Small rational matrix arithmetic fits symbolic tools; unbounded synthesis is unnecessary. |
| Checkability | High | Every finite witness can be recomputed independently. |
| Expertise needed | Medium | A control reviewer must confirm the uncertainty and time conventions. |
| Scholarly significance | Medium | The contribution is verification practice rather than a new theorem. |
| Verification difficulty | Medium | The algebra is compact; confusing quadratic stability with general stability is a material risk. |

**Correctness:** No project answer.

The cited literature supports the calibration target. No project answer has been submitted for review.

**Novelty:** Not claimed.

This is a known-result calibration. The chosen bounds and presentation are not claims of scientific novelty.

<details>
<summary>Difficulty and significance</summary>

**Difficulty:** Medium.

The reasons are given in the [AI trial assessment](#assessment).

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
| Stable ID | `Q-FORMAL-101` |
| Duplicate key | `small-polytopic-ldi-common-quadratic-certificate` |
| Original domain label | Control, estimation and systems theory |
| Original cross-domain labels | Robust design and verification; Convex optimization |
| Primary domain ID | `ENG.CONTROL` |
| Cross-domain IDs | `ENG.ROBUST`, `MATH.OPT` |
| Origin code | `known_result_calibration` |
| Status code | `known_result` |
| Curator-designed scope | Yes |
| Detailed entry | Yes |
| Record level | `C` |
| Human review status | `pending` |
| Trial-label code | `priority_trial` |
| Assessment-evidence code | `untested_forecast` |
| Method tags | `proof`, `exact_computation`, `certificate_checking`, `model_analysis` |
| Validation tags | `pure_proof`, `exact_computation` |
| Experimental-dependency tag | `none_for_formal_task` |

[JSON record](../../data/cards/Q-FORMAL-101.json)

</details>

[Problem cards](README.md) · [Back to top](#at-a-glance)
