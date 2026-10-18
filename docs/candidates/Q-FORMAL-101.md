# Check common quadratic Lyapunov certificates for small matrix polytopes

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-101 · Full card available.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-101%3A+Check+common+quadratic+Lyapunov+certificates+for+small+matrix+polytopes&target=Q-FORMAL-101) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-101%3A+Check+common+quadratic+Lyapunov+certificates+for+small+matrix+polytopes&target=Q-FORMAL-101)

Given 1-4 rational matrices A_i of a common dimension d <= 4, a rational symmetric P, and rational alpha > 0, verify exactly that P and every residual -(A_i^T P + P A_i + 2 alpha P) are positive definite. If accepted, supply the conditional exponential-decay certificate for xdot = A(t)x with arbitrary measurable A(t) in their convex hull. Rejection does not imply instability. The input bounds and strict-residual convention define a curator-proposed calibration.

**Origin:** Known-result calibration. **Curator-designed scope:** Yes.

**Current status:** Known result in literature. **Last checked:** 2026-10-14.

**Status basis:** The common-quadratic criterion and decay implication are established in the opened monograph. This task checks supplied witnesses, without claiming a new theorem or complete stability decision procedure.

**Statement check:** Source located. **Status check:** Source report only.

**Source date and freshness:** Recorded source years: SRC-FORMAL-101: 1994, SRC-FORMAL-102: 1989. The last-checked date records the scope described in the status basis; it is not a comprehensive literature-search date.

**Scope limits:** Use the full card for assumptions and validation limits.

**Information still needed**

- Choose and record actual certificate fixtures before a trial.
- Have a control reviewer confirm the positivity convention and norm estimate.

**Primary branch:** [Control, estimation and systems theory](../domains/eng.md#eng-control). **Related branches:** [Robust design and verification](../domains/eng.md#eng-robust), [Optimization and operations research](../domains/math.md#math-opt).

**Sources:** [Linear Matrix Inequalities in System and Control Theory](../sources.md#src-formal-101); [Structured and Simultaneous Lyapunov Functions for System Stability Problems](../sources.md#src-formal-102).

**Exact locator:** Boyd et al., Section 5.1, equations (5.8) and (5.17)

**Potential difficulty:** Medium. A finite exact acceptance test separates algebra from theorem application. Priority refers to a possible calibration trial, not demonstrated AI performance.

**Possible AI role:** No named model evaluated; assumes a tool-using AI that can read mathematical sources, produce inspectable symbolic work and code, and work with a human domain reviewer.

**Verification burden:** Medium. The algebra is compact; confusing quadratic stability with general stability is a material risk.

**Resource expectations:** Experiment: None for the conditional certificate. Evidence that a physical plant stays inside the uncertainty set requires separate measurements. Data: Rational vertex matrices, a proposed P and positive alpha; no observational dataset. Computation: Exact determinants of matrices of order at most four with bounded rational inputs. Laptop-class execution is an untested planning assumption; larger dimensions and certificate synthesis may be much harder.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No model, solver or supplied certificate has been tested. Exact arithmetic does not establish empirical adequacy.

[Read the full card](../cards/Q-FORMAL-101.md). **Human review:** Pending.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
