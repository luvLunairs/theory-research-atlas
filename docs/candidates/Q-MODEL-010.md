# Reproduce equilibrium branches in an energy-balance climate model

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MODEL-010 · Full card available.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-010%3A+Reproduce+equilibrium+branches+in+an+energy-balance+climate+model&target=Q-MODEL-010) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-010%3A+Reproduce+equilibrium+branches+in+an+energy-balance+climate+model&target=Q-MODEL-010)

For the deterministic energy-balance model of Ashwin and von der Heydt, use the decimal parameter values in Table 1 as exact model inputs on T in [260,310] K. Reproduce Gamma(T) in equation (18), isolate every root of R'(T) in this interval with certified error control, classify nondegenerate folds and regular equilibrium stability, and verify S=1/R'(T) wherever R'(T)≠0. State why this local sensitivity formula does not apply at a fold. Noise is set to zero and carbon dioxide is a fixed positive parameter.

**Origin:** Known-result calibration. **Curator-designed scope:** Yes.

**Current status:** Known result in literature. **Last checked:** 2026-10-14.

**Status basis:** The paper supplies the illustrative model and equilibrium analysis. The temperature interval and certification requirements make the existing reproduction target precise; they do not define a real-world climate threshold.

**Statement check:** Source located. **Status check:** Source report only.

**Source date and freshness:** Recorded source years: SRC-MODEL-011: 2020. The last-checked date records the scope described in the status basis; it is not a comprehensive literature-search date.

**Scope limits:** Use the full card for assumptions and validation limits.

**Information still needed**

- Reconcile the unnumbered second-derivative expression after equation (21) with differentiation of equation (19) before implementing fold tests.
- Check Table 1 against a visual copy before a trial if extraction or notation is ambiguous.
- Choose and document a validated arithmetic library whose transcendental enclosures meet the certificate requirements.
- The paper's prose describes transition derivatives as nonzero only in restricted ranges; for the defined smooth tanh model this must be interpreted approximately, not as compact support.

**Primary branch:** [Climate dynamics and reduced models](../domains/earth.md#earth-climate). **Related branches:** [Dynamical systems and ergodic theory](../domains/math.md#math-dyn), [Numerical analysis and scientific computation](../domains/math.md#math-numer).

**Sources:** [Extreme Sensitivity and Climate Tipping Points](../sources.md#src-model-011).

**Exact locator:** Section 3, equations (15)–(21), Table 1 and Figure 2; Table 1 is on printed p.1540.

**Potential difficulty:** Medium. The state space is one-dimensional, but rigorous completeness, transcendental enclosures and source discrepancies make the task more demanding than plotting a curve.

**Possible AI role:** No named model evaluated; assumes tool-using AI with symbolic differentiation, validated interval arithmetic for transcendental functions and human review of numerical certificates and model scope. The finite interval and explicit functions make a rigorous reproduction feasible to specify. A validated transcendental arithmetic environment and resolution of the source's derivative inconsistency are prerequisites for reliable certificates.

**Verification burden:** High. Reliable exclusion of all additional roots and handling source discrepancies exceed ordinary plotting.

**Resource expectations:** Experiment: None for the model reproduction. Empirical climate adequacy, feedback calibration and real tipping estimates would require observational and modeling evidence beyond this task. Data: The cited equations and Table 1 only; no temperature record, emissions dataset or remote climate simulation. Computation: One-dimensional interval subdivision and validated evaluation of tanh and exp. A local validated-numerics environment is a plausible starting resource class, but total subdivisions, precision, runtime and cost are unmeasured and must be reported in any future attempt.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No trial was run, so the proposed precision and resource class are untested. Source transcription and interval overestimation could require revising the numerical method without altering the target.

[Read the full card](../cards/Q-MODEL-010.md). **Human review:** Pending.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
