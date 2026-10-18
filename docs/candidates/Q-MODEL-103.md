# Verify the Ornstein–Uhlenbeck transition law and equilibrium

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MODEL-103 · Full card available.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-103%3A+Verify+the+Ornstein%E2%80%93Uhlenbeck+transition+law+and+equilibrium&target=Q-MODEL-103) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-103%3A+Verify+the+Ornstein%E2%80%93Uhlenbeck+transition+law+and+equilibrium&target=Q-MODEL-103)

For the one-dimensional Itô process dX_t=−a X_t dt+sqrt(2D)dW_t, with a,D>0 and deterministic X_0=x_0, reproduce the Gaussian transition law with mean x_0 exp(−at) and variance (D/a)(1−exp(−2at)). Verify its Fokker–Planck equation, normalization, weak initial limit, Gaussian composition law and stationary density proportional to exp(−a x^2/(2D)). Check zero stationary probability current and detailed balance.

**Origin:** Known-result calibration. **Curator-designed scope:** Yes.

**Current status:** Known result in literature. **Last checked:** 2026-10-14.

**Status basis:** The transition and equilibrium formulas are established results in the cited lectures. The verification checklist is a curator-selected calibration task.

**Statement check:** Source located. **Status check:** Source report only.

**Source date and freshness:** Recorded source years: SRC-MODEL-105: 2005, SRC-MODEL-106: 2012. The last-checked date records the scope described in the status basis; it is not a comprehensive literature-search date.

**Scope limits:** Use the full card for assumptions and validation limits.

**Information still needed**

- Select a symbolic checker and specify which analytic steps remain for human review.
- If a physical application is proposed, separately identify mobility, temperature and the evidence supporting the noise model.

**Primary branch:** [Statistical and nonequilibrium physics](../domains/phys.md#phys-stat). **Related branches:** [Stochastic processes and stochastic analysis](../domains/prob.md#prob-process), [Molecular statistical mechanics](../domains/chem.md#chem-stat).

**Sources:** [Lecture 14: Applications in Statistical Mechanics](../sources.md#src-model-105); [Kinetic Theory: Stochastic Processes](../sources.md#src-model-106).

**Exact locator:** Bazant lecture 14, pp.4–5 and Appendix A.1–A.2, pp.7–8; Tong, Section 3.2.2, equations (3.28)–(3.31).

**Potential difficulty:** Medium. The closed form is elementary, but the full checklist spans stochastic integrals, a PDE, weak convergence and reversibility.

**Possible AI role:** No named model evaluated; assumes tool-using AI with symbolic algebra, basic stochastic calculus and human review of probability arguments. The closed-form kernel can be checked by both stochastic and differential-equation routes. The main value is whether a generated derivation keeps its conventions and limiting statements consistent.

**Verification burden:** Medium. Algebra is compact; weak convergence and detailed balance cannot be replaced by plotted densities.

**Resource expectations:** Experiment: None for the stochastic theorem. A physical Brownian-motion interpretation would require measurements and justification of the noise and overdamped approximations. Data: No empirical observations. All inputs are symbolic model constants and initial conditions. Computation: Symbolic differentiation, Gaussian integration and a few exact identities. A local computer algebra environment is a plausible resource class; no simulation campaign, runtime or cost measurement is required or reported.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No AI trial was run. Correctly recalling a Gaussian formula is weaker than satisfying the full verification checklist.

[Read the full card](../cards/Q-MODEL-103.md). **Human review:** Pending.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
