# Transfer-matrix calibration for the one-dimensional Ising model

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MATH-103 · Full card available.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MATH-103%3A+Transfer-matrix+calibration+for+the+one-dimensional+Ising+model&target=Q-MATH-103) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MATH-103%3A+Transfer-matrix+calibration+for+the+one-dimensional+Ising+model&target=Q-MATH-103)

For N >= 3 periodic spins s_i in {-1,+1}, finite beta >= 0 and real h, define Z_N = sum_s exp(beta sum_(i=1)^N s_i s_(i+1) + h sum_(i=1)^N s_i), with s_(N+1)=s_1. Reproduce the transfer-matrix formula for Z_N and prove that psi(beta,h) = lim_(N->infinity) N^-1 log Z_N exists and is real-analytic in h for each finite beta. Here beta and h are dimensionless parameters; the task concerns this nearest-neighbor model.

**Origin:** Known-result calibration. **Curator-designed scope:** No.

**Current status:** Known result in literature. **Last checked:** 2026-10-14.

**Status basis:** The theorem and its transfer-matrix proof are present in the inspected author chapter. Reproducing them would be calibration, not a new model solution.

**Statement check:** Source located. **Status check:** Source report only.

**Source date and freshness:** Recorded source years: SRC-MATH-103: 2017. The last-checked date records the scope described in the status basis; it is not a comprehensive literature-search date.

**Scope limits:** Use the full card for assumptions and validation limits.

**Information still needed**

- If the result is formalized, specify the real-analysis library and check the branch and positivity lemmas.
- If physical units are introduced later, document the relation between beta, the coupling energy, temperature and the field parameter.

**Primary branch:** [Rigorous statistical mechanics](../domains/mphy.md#mphy-stat). **Related branches:** [Statistical and nonequilibrium physics](../domains/phys.md#phys-stat), [Discrete probability and random structures](../domains/prob.md#prob-discrete).

**Sources:** [Statistical Mechanics of Lattice Systems: The Ising Model](../sources.md#src-math-103).

**Exact locator:** SRC-MATH-103, Section 3.3, Theorem 3.9 and proof, equations (3.10)-(3.11), pp. 90-92.

**Potential difficulty:** Medium. The symbolic calculation is small but the limiting and analytic claims need careful justification.

**Possible AI role:** No named model evaluated; assumes tool-using AI with symbolic algebra, elementary spectral theory and equilibrium statistical mechanics. The source provides an exact model and a short route to the answer. It offers independently checkable symbolic steps while exposing common errors in boundary conditions and limits.

**Verification burden:** Medium. Choosing a square-root branch and interchanging limits or derivatives can introduce subtle mistakes.

**Resource expectations:** Experiment: None to establish the formal identity. Claims about a particular material would need independent empirical work. Data: No empirical data; the complete model is specified by N, beta and h. Computation: Symbolic manipulation of a two-by-two matrix is sufficient for the proof. Optional finite checks contain 2^N spin assignments for each chosen N; no runtime has been measured.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** The task has not been tested on any model. A correct recalled formula would not demonstrate the ability to reason through the derivation or validate a new model.

[Read the full card](../cards/Q-MATH-103.md). **Human review:** Pending.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
