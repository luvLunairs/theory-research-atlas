# Optimal acceleration from predetermined gradient-descent stepsizes

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-510 · Full card available.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-510%3A+Optimal+acceleration+from+predetermined+gradient-descent+stepsizes&target=Q-FORMAL-510) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-510%3A+Optimal+acceleration+from+predetermined+gradient-descent+stepsizes&target=Q-FORMAL-510)

For x_t=x_(t-1)-eta_t grad f(x_(t-1)), with positive deterministic stepsizes chosen before the run, determine the sharp asymptotic worst-case last-iterate objective-gap rate on all finite-dimensional convex L-smooth functions admitting a minimizer. Write R_N for the gap normalized by L||x_0-x_*||^2, taking its supremum over dimension, objective, minimizer x_* and initial point x_0 outside the minimizer set. In the known-horizon setting, minimize this supremum over length-N schedules; in the anytime setting, require one infinite schedule to satisfy its guarantee at every stopping time.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-10-20.

**Status basis:** The September 2026 paper leaves the sharp rates unresolved. The scoped later-work search found no matching resolution or correction. Acceleration beyond 1/N is already known in both settings.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Versions and date limitations are recorded in the source catalog. Relevant passages were opened on 2026-10-20.

**Scope limits:** Two related rates are recorded together to prevent conflation. A known-horizon schedule may depend on N; an anytime schedule cannot depend on its future stopping time. Quadratic-only or stochastic-gradient results answer different questions.

**Information still needed**

- Independent audit of the latest lower-bound proof.
- Refresh later literature for the exact setting before making a novelty claim.

**Primary branch:** [Optimization and operations research](../domains/math.md#math-opt). **Related branches:** [Algorithms and data structures](../domains/cs.md#cs-alg).

**Sources:** [Stronger Lower Bounds for (Non-)Anytime Acceleration of Gradient Descent](../sources.md#src-impact-001); [Acceleration by stepsize hedging: Silver Stepsize Schedule for smooth convex optimization](../sources.md#src-impact-002); [Anytime Acceleration of Gradient Descent](../sources.md#src-impact-003).

**Exact locator:** Jung, Cho and Yun, equation (1), Theorems 1.1-1.2 and Section 5; Altschuler and Parrilo, Sections 1-3; Zhang et al., publisher abstract.

**Potential difficulty:** High. The full target requires a general argument beyond the inspected partial results.

**Possible AI role:** No model evaluated; assumes a tool-using assistant able to read the cited mathematics and preserve reproducible evidence.

**Verification burden:** High. High for a new general rate theorem; finite algebraic certificates may be easier to audit.

**Resource expectations:** Experiment: None for the mathematical rate question. Data: The cited schedules, definitions and proof certificates; no empirical training dataset is required. Computation: Unmeasured. Symbolic work and small numerical diagnostics are possible, but global schedule optimization can be expensive. No hardware, runtime or solution-cost estimate is available.

**Assessment:** 2026-10-20; untested forecast. **Uncertainty:** Editorial planning judgment only. No model, search strategy, runtime or success probability has been measured.

[Read the full card](../cards/Q-FORMAL-510.md). **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-10-20

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Source reports open.

The September 2026 paper leaves the sharp rates unresolved. The scoped later-work search found no matching resolution or correction. Acceleration beyond 1/N is already known in both settings.

**Search scope:** Opened the listed source passages and searched exact identifiers and later-result terminology. This is a bounded source check.

**Inspected evidence**

- [Stronger Lower Bounds for (Non-)Anytime Acceleration of Gradient Descent](../sources.md#src-impact-001) — Equation (1), Theorems 1.1-1.2 and Section 5. Records two distinct sharp-rate gaps and the exact anytime limsup obstruction.
- [Acceleration by stepsize hedging: Silver Stepsize Schedule for smooth convex optimization](../sources.md#src-impact-002) — Sections 1-3. Supplies the silver-schedule upper bound.
- [Anytime Acceleration of Gradient Descent](../sources.md#src-impact-003) — Publisher abstract. The earlier question of any acceleration beyond 1/T is resolved; the sharp rate is different.

**Limits and remaining work**

- Bounded title, identifier and terminology searches; unpublished results or different terminology may be missed. No full proof audit.

<details>
<summary>Search queries</summary>

- "gradient descent" "step-size" "1.450" October 2026
- "gradient descent" "stepsize" "October 2026" "lower bound"
- "2609.04032" correction


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
