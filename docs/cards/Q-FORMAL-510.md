# Optimal acceleration from predetermined gradient-descent stepsizes

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

How much speed can gradient descent gain by changing only its predetermined step lengths? The answer would identify a basic limit of this widely used optimization method.

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-510%3A+Optimal+acceleration+from+predetermined+gradient-descent+stepsizes&target=Q-FORMAL-510) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-510%3A+Optimal+acceleration+from+predetermined+gradient-descent+stepsizes&target=Q-FORMAL-510)

[At a glance](#at-a-glance) · [The task](#problem) · [Resources and verification](#verification) · [Evidence and context](#evidence) · [AI trial assessment](#assessment) · [Research records](#audit-trail)

<a id="at-a-glance"></a>

## At a glance

| Field | Summary |
| --- | --- |
| Primary field | [Optimization and operations research](../domains/math.md#math-opt) |
| Related fields | [Algorithms and data structures](../domains/cs.md#cs-alg) |
| Task origin | [Literature-origin question](../evidence-policy.md) |
| Current status | [Source reports open](../evidence-policy.md) · checked 2026-10-20 |
| AI suitability | [Preparation needed](../ai-assessment.md) · Untested forecast |
| Scientific review | Pending |

<a id="problem"></a>

## The task

### Precise statement

For x_t=x_(t-1)-eta_t grad f(x_(t-1)), with positive deterministic stepsizes chosen before the run, determine the sharp asymptotic worst-case last-iterate objective-gap rate on all finite-dimensional convex L-smooth functions admitting a minimizer. Write R_N for the gap normalized by L||x_0-x_*||^2, taking its supremum over dimension, objective, minimizer x_* and initial point x_0 outside the minimizer set. In the known-horizon setting, minimize this supremum over length-N schedules; in the anytime setting, require one infinite schedule to satisfy its guarantee at every stopping time.

**Required output:** Close or narrow one of the two source-reported rate gaps, specifying which setting is addressed.

**Scope:** Two related rates are recorded together to prevent conflation. A known-horizon schedule may depend on N; an anytime schedule cannot depend on its future stopping time. Quadratic-only or stochastic-gradient results answer different questions.

### Assumptions

- Exact gradients, Euclidean norm and unconstrained smooth convex minimization; no strong-convexity assumption.
- No momentum, averaging, randomization or adaptation to observations. Stepsizes may exceed 2/L. The normalization uses a minimizer x_* and a starting point x_0 outside the minimizer set.
- The guarantee concerns the final iterate, not the best iterate. Constants must be uniform over the stated function class and dimension.

### Success criteria

1. An upper bound needs a schedule and a uniform proof; a lower bound must quantify over every permitted schedule.
2. State exponents exactly and preserve logarithmic factors, constants, horizon restrictions and limit quantifiers.
3. Finite computations or fitted slopes alone do not establish an asymptotic rate.

### Background needed

- Smooth convex optimization and worst-case oracle complexity.
- Uniform asymptotic estimates and proof certificates for optimization inequalities.

<a id="verification"></a>

## Resources and verification

### Resource requirements

**Computing:** Unmeasured. Symbolic work and small numerical diagnostics are possible, but global schedule optimization can be expensive. No hardware, runtime or solution-cost estimate is available.

**Data:** The cited schedules, definitions and proof certificates; no empirical training dataset is required.

**Experiments:** None for the mathematical rate question.

**Theory and model requirements:** The exact-gradient, deterministic, nonadaptive model in the statement.

**Validation modes:** Proof, Exact computation, Numerical evidence.

### Verification steps

1. Match the algorithm and normalization to equation (1).
2. Audit every inequality and its dimension dependence.
3. Check finite identities with exact or certified arithmetic when applicable.
4. Have an optimization specialist inspect horizon and asymptotic quantifiers.

**Statement alignment:** Distinguish final iterate from best iterate, known horizon from anytime, and general smooth convex objectives from quadratics.

**Human review difficulty:** High for a new general rate theorem; finite algebraic certificates may be easier to audit.

### Formal validity and empirical support

**What the formal task can establish:** Source inspection confirms the recorded formulation, not an independent proof of the cited theorems.

**Empirical support and limits:** A formal answer would not by itself establish practical performance on real training tasks.

### Methods and obstacles

**Proposed methods:**

- Inspect the published recursive multi-step inequalities and checkpoint-based lower bounds.
- Use computations only to examine a precisely stated finite instance before claiming any general theorem.

**Expected obstacles:**

- A successful schedule on selected functions need not control the worst case.
- Interchanging schedule, dimension, instance and horizon quantifiers changes the target.
- Large steps can cause transient growth even when terminal performance improves.

### Checks still needed

- Independent audit of the latest lower-bound proof.
- Refresh later literature for the exact setting before making a novelty claim.

<a id="evidence"></a>

## Evidence and context

**Status basis:** The September 2026 paper leaves the sharp rates unresolved. The scoped later-work search found no matching resolution or correction. Acceleration beyond 1/N is already known in both settings.

[Dated literature checks and remaining limits](../candidates/Q-FORMAL-510.md#literature-checks). These are editorial evidence checks, not signed expert reviews.

**Exact problem / theorem locator:** Jung, Cho and Yun, equation (1), Theorems 1.1-1.2 and Section 5; Altschuler and Parrilo, Sections 1-3; Zhang et al., publisher abstract.

### Sources

- [Stronger Lower Bounds for (Non-)Anytime Acceleration of Gradient Descent](../sources.md#src-impact-001). Minchan Jung; Hanseul Cho; Chulhee Yun. 2026. [Read source](https://arxiv.org/html/2609.04032v2).
  - **Relevant sections:** Version 2, 4 September 2026; equation (1), Theorems 1.1-1.2 and Sections 3-5. Version date checked against the arXiv abstract page.
  - **Source limitations:** The stated lower bounds were read, not independently proved. The anytime theorem is a limsup obstruction, not a pointwise lower bound at every iteration.
- [Acceleration by stepsize hedging: Silver Stepsize Schedule for smooth convex optimization](../sources.md#src-impact-002). Jason M. Altschuler; Pablo A. Parrilo. 2025. [Read source](https://link.springer.com/article/10.1007/s10107-024-02164-2).
  - **Relevant sections:** Mathematical Programming 213, 1105-1118; published online 25 November 2024, issue September 2025; DOI 10.1007/s10107-024-02164-2; Sections 1-3.
  - **Source limitations:** This is an upper-bound construction, not a proof that its rate is optimal. Special terminal iterations and anytime guarantees must be distinguished.
- [Anytime Acceleration of Gradient Descent](../sources.md#src-impact-003). Zihan Zhang; Jason Lee; Simon Du; Yuxin Chen. 2025. [Read source](https://proceedings.mlr.press/v291/zhang25a.html).
  - **Relevant sections:** COLT 2025, PMLR 291:5991-6013; conference 30 June-4 July 2025; publisher abstract and bibliography.
  - **Source limitations:** Publisher abstract inspected; the full proof was not audited. The sharp anytime exponent remains a separate question.

### Known results and partial progress

- Let a=log_2(1+sqrt(2)) and b=log_2(1+sqrt(3)). The silver construction gives O(N^-a) at terminal lengths N=2^k-1; the September 2026 paper records this best-known non-anytime exponent and reports Omega(N^-b) for every length-N schedule.
- For anytime schedules, the published upper exponent is 2a/(1+a). The later barrier is limsup_N N^(2b/(1+b)) R_N &gt;= c for a universal c&gt;0.
- These are different optimization problems; the anytime barrier is not a lower bound at every N.

**Research value:** Determines how much acceleration can come from stepsizes alone. Relevance to optimization theory is direct; benefits for nonconvex training require separate evidence.

### Related problems

No formal dependency or equivalence is asserted.

### Scope of the status check

**Finding:** The September 2026 paper leaves the sharp rates unresolved. The scoped later-work search found no matching resolution or correction. Acceleration beyond 1/N is already known in both settings.

**Search limits:** Bounded title, identifier and terminology searches; unpublished results or different terminology may be missed. No full proof audit.

<details>
<summary>Literature references checked</summary>

**Queries used:**

- "gradient descent" "step-size" "1.450" October 2026
- "gradient descent" "stepsize" "October 2026" "lower bound"
- "2609.04032" correction

**Sources checked:**

- [Stronger Lower Bounds for (Non-)Anytime Acceleration of Gradient Descent](../sources.md#src-impact-001)
- [Acceleration by stepsize hedging: Silver Stepsize Schedule for smooth convex optimization](../sources.md#src-impact-002)
- [Anytime Acceleration of Gradient Descent](../sources.md#src-impact-003)

</details>

<details>
<summary>Previous attempts and public records</summary>

- The cited papers supply upper and lower bounds. No project research attempt has been run.

</details>

<details>
<summary>Attribution and suggested citation</summary>

**Original authors and credited contributors:**

- Jason M. Altschuler
- Pablo A. Parrilo
- Zihan Zhang
- Jason Lee
- Simon Du
- Yuxin Chen
- Minchan Jung
- Hanseul Cho
- Chulhee Yun

**Suggested citation:** Cite the specific bound used: Altschuler and Parrilo, Mathematical Programming 213 (2025), 1105-1118; Zhang et al., COLT 2025, PMLR 291; Jung, Cho and Yun, arXiv:2609.04032v2.

**Editorial credit:** Compiled for Theory Research Atlas with Codex assistance.

</details>

<a id="assessment"></a>

## AI trial assessment

**Label:** [Preparation needed](../ai-assessment.md). **Evidence:** Untested forecast. **Assessed:** 2026-10-20.

The problem is explicit and has reusable published arguments. Assessing a specific AI attempt requires a narrower, independently checked target.

**Model or capability conditions:** No model evaluated; assumes a tool-using assistant able to read the cited mathematics and preserve reproducible evidence.

**Uncertainty:** Editorial planning judgment only. No model, search strategy, runtime or success probability has been measured.

Ratings are separate judgments, not a score. High expertise needed or verification difficulty means a larger burden; high method availability or checkability means stronger support.

| Dimension | Rating | Reason |
| --- | --- | --- |
| Statement clarity | High | The source specifies the objects and quantifiers. |
| Decomposability | Medium | A selected lemma or finite instance can be checked separately; it need not settle the full problem. |
| Methods and literature | High | The cited papers provide concrete methods and known limitations. |
| Search / symbolic fit | Medium | Symbolic or finite computations can assist a declared task, without proving the general claim. |
| Checkability | Medium | Exact certificates help, but the claimed scope still requires proof. |
| Expertise needed | High | Specialist review is needed for a new general result. |
| Scholarly significance | High | Determines how much acceleration can come from stepsizes alone. Relevance to optimization theory is direct; benefits for nonconvex training require separate evidence. |
| Verification difficulty | High | High for a new general rate theorem; finite algebraic certificates may be easier to audit. |

**Correctness:** No project answer.

No project proof, counterexample or research computation is supplied.

**Novelty:** Requires future literature review.

Any new claim needs a focused comparison at the time of submission.

<details>
<summary>Difficulty and significance</summary>

**Difficulty:** High.

The full target requires a general argument beyond the inspected partial results.

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
| Stable ID | `Q-FORMAL-510` |
| Duplicate key | `smooth-convex-gd-predetermined-positive-stepsizes-sharp-last-iterate-rate` |
| Original domain label | Optimization and operations research |
| Original cross-domain labels | Algorithms and data structures |
| Primary domain ID | `MATH.OPT` |
| Cross-domain IDs | `CS.ALG` |
| Origin code | `literature_open` |
| Status code | `source_reports_open` |
| Curator-designed scope | No |
| Detailed entry | Yes |
| Record level | `C` |
| Human review status | `pending` |
| Trial-label code | `preparation_required` |
| Assessment-evidence code | `untested_forecast` |
| Method tags | `proof`, `bounds`, `algorithm`, `symbolic_derivation`, `numerical_computation` |
| Validation tags | `pure_proof`, `exact_computation`, `numerical_evidence` |
| Experimental-dependency tag | `none_for_formal_task` |

[JSON record](../../data/cards/Q-FORMAL-510.json)

</details>

[Problem cards](README.md) · [Back to top](#at-a-glance)
