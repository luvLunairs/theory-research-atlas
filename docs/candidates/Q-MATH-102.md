# Exact mixing certificates for small positive Markov chains

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MATH-102 · Full card available.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MATH-102%3A+Exact+mixing+certificates+for+small+positive+Markov+chains&target=Q-MATH-102) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MATH-102%3A+Exact+mixing+certificates+for+small+positive+Markov+chains&target=Q-MATH-102)

Given a rational row-stochastic matrix P of order 2 <= n <= 6 with every entry positive and every reduced denominator at most 100, compute its stationary probability row vector pi and tau = max_(i,j) (1/2) sum_k |P_ik-P_jk|. Certify d(t) = max_i ||P^t(i,.)-pi||_TV <= tau^t for every integer t >= 1, and return an integer T >= 1 with tau^T <= 1/100. Supply exact row-coupling certificates and a general argument, not only sampled trajectories.

**Origin:** Known-result calibration. **Curator-designed scope:** Yes.

**Current status:** Known result in literature. **Last checked:** 2026-10-14.

**Status basis:** The cited textbook gives the coupling and submultiplicativity facts from which the stated certificate follows. Matrix-size, denominator and tolerance limits are curator-defined calibration conditions.

**Statement check:** Source located. **Status check:** Source report only.

**Source date and freshness:** Recorded source years: SRC-MATH-102: 2009. The last-checked date records the scope described in the status basis; it is not a comprehensive literature-search date.

**Scope limits:** Use the full card for assumptions and validation limits.

**Information still needed**

- Choose representative matrices, including identical-row and slowly contracting examples, before making performance comparisons.
- Any extension to chains with zero entries needs a new irreducibility, aperiodicity and multi-step analysis.

**Primary branch:** [Markov chains, mixing and interacting systems](../domains/prob.md#prob-mix). **Related branches:** [Stochastic processes and stochastic analysis](../domains/prob.md#prob-process), [Randomized, online and distributed algorithms](../domains/cs.md#cs-random).

**Sources:** [Markov Chains and Mixing Times, first edition](../sources.md#src-math-102).

**Exact locator:** SRC-MATH-102, Proposition 4.7, Lemmas 4.11-4.12 and Corollary 5.3.

**Potential difficulty:** Medium. The task combines finite exact calculations with a uniform probabilistic proof.

**Possible AI role:** No named model evaluated; assumes tool-using AI with finite probability, coupling arguments and exact rational computation. The proof decomposes into established coupling facts and exact arithmetic checks. Small input dimensions allow independent review while retaining an all-time probabilistic claim.

**Verification burden:** Medium. The main risk is mistaking several checked times for an all-time proof or mixing up row and column conventions.

**Resource expectations:** Experiment: No physical experiment or stochastic simulation is required. Data: An explicit rational transition matrix; no observed trajectories or external data. Computation: Rational linear algebra on matrices of order at most 6 and coupling tables of order at most 6 by 6. Rational bit lengths can grow when certifying large T; resource estimates should be recorded for selected inputs before execution.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No model has been tested. A compact matrix does not ensure a sharp bound or small rational intermediates.

[Read the full card](../cards/Q-MATH-102.md). **Human review:** Pending.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
