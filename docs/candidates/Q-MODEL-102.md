# Recover the linear stability threshold of triangular Lagrange points

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MODEL-102 · Full card available.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-102%3A+Recover+the+linear+stability+threshold+of+triangular+Lagrange+points&target=Q-MODEL-102) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-102%3A+Recover+the+linear+stability+threshold+of+triangular+Lagrange+points&target=Q-MODEL-102)

In the planar circular restricted three-body problem with unit primary separation, unit angular speed and mass fractions 1−mu and mu, 0<mu≤1/2, reproduce the linearized characteristic polynomial at L4 and L5: lambda^4+lambda^2+(27/4)mu(1−mu). Establish bounded solutions of the linearized system for 0<mu<mu_R and linear instability for mu_R<mu≤1/2, where mu_R=(1−sqrt(23/27))/2. Exclude mu=mu_R, and do not claim nonlinear stability.

**Origin:** Known-result calibration. **Curator-designed scope:** Yes.

**Current status:** Known result in literature. **Last checked:** 2026-10-14.

**Status basis:** The author text provides the characteristic equation and mass criterion. The card explicitly restricts their interpretation to the nondegenerate linearized planar problem.

**Statement check:** Source located. **Status check:** Source report only.

**Source date and freshness:** Recorded source years: SRC-MODEL-103: date unverified, SRC-MODEL-104: date unverified. The last-checked date records the scope described in the status basis; it is not a comprehensive literature-search date.

**Scope limits:** Use the full card for assumptions and validation limits.

**Information still needed**

- The critical mass case needs a separate repeated-root and Jordan-form analysis if added later.
- No nonlinear stability theorem or observational application has been evaluated.

**Primary branch:** [Celestial dynamics](../domains/astro.md#astro-dyn). **Related branches:** [Dynamical systems and ergodic theory](../domains/math.md#math-dyn), [Classical mechanics and continuum theory](../domains/phys.md#phys-classical).

**Sources:** [Introduction to Celestial Mechanics, 2nd Edition: Stability of Lagrange points](../sources.md#src-model-103); [Introduction to Celestial Mechanics, 2nd Edition: Co-rotating frame](../sources.md#src-model-104).

**Exact locator:** Fitzpatrick, Stability of Lagrange points, equations (9.73)–(9.88); Co-rotating frame, equations (9.22)–(9.30).

**Potential difficulty:** Medium. A small exact matrix calculation is paired with nontrivial interpretation of spectral stability and degenerate cases.

**Possible AI role:** No named model evaluated; assumes tool-using AI with symbolic differentiation, exact polynomial algebra and access to a dynamical-systems reviewer. The symbolic target is short enough for an independent determinant check, while its interpretation tests a frequent overstatement about stability.

**Verification burden:** Medium. The algebra is small, but spectrum, bounded linear motion and nonlinear stability must remain distinct.

**Resource expectations:** Experiment: None for the exact linearization. Assessing real Trojan objects or mission trajectories would require additional forces, initial conditions and observations. Data: No observational catalog; only the stated dimensionless model. Computation: One exact 4-by-4 determinant with an algebraic parameter and quadratic discriminant analysis. A local symbolic environment is a plausible resource class; no runtime or cost has been measured.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No model was tested. Familiarity with the classical result can conceal a wrong sign or an unjustified nonlinear conclusion.

[Read the full card](../cards/Q-MODEL-102.md). **Human review:** Pending.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
