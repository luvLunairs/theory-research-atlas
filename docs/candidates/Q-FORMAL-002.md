# Audit finite-sample split likelihood-ratio coverage in a Bernoulli model

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-002 · Full card available.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-002%3A+Audit+finite-sample+split+likelihood-ratio+coverage+in+a+Bernoulli+model&target=Q-FORMAL-002) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-002%3A+Audit+finite-sample+split+likelihood-ratio+coverage+in+a+Bernoulli+model&target=Q-FORMAL-002)

Specialize universal inference to iid Bernoulli(p), a prespecified split of 20 observations into two groups of 10, training estimator q=(K1+1)/12, and alpha=1/20. Reproduce the all-p coverage proof and exact rejection probabilities on p in {1/10,...,9/10}.

**Origin:** Known-result calibration. **Curator-designed scope:** Yes.

**Current status:** Known result in literature. **Last checked:** 2026-10-13.

**Status basis:** The guarantee follows from the published theorem under its assumptions. The finite Bernoulli benchmark is a curator-selected reproduction protocol; no calculation has been run.

**Statement check:** Source located. **Status check:** Source report only.

**Source date and freshness:** Recorded source years: SRC-FORMAL-003: 2020, SRC-FORMAL-010: 2023. The last-checked date records the scope described in the status basis; it is not a comprehensive literature-search date.

**Scope limits:** Use the full card for assumptions and validation limits.

**Information still needed**

- An independent reviewer should confirm whether the benchmark's reproduction depth is sufficient before attempting power optimization.
- Any extension to repeated splits, dependence or misspecification requires a separate problem record and proof.

**Primary branch:** [Inference and decision theory](../domains/stat.md#stat-infer). **Related branches:** [Probability foundations and limit theory](../domains/prob.md#prob-found).

**Sources:** [Universal Inference](../sources.md#src-formal-003); [Game-Theoretic Statistics and Safe Anytime-Valid Inference](../sources.md#src-formal-010).

**Exact locator:** SRC-FORMAL-003, Section 2, Theorem 1; finite parameters chosen for calibration

**Potential difficulty:** Medium. The proof and exact finite audit provide two complementary checks with limited implementation scope. The relevant capability is disciplined conditioning and exact arithmetic, not confidence asserted by a model.

**Possible AI role:** No named model evaluated; assumes tool-using AI capable of elementary probability proofs and exact-arithmetic programming.

**Verification burden:** Medium. Small enumeration is easy, but it cannot replace the proof for all p.

**Resource expectations:** Experiment: none Data: No observed data required. The finite outcome space is specified mathematically. Computation: Small finite enumeration over 121 count pairs at each of nine rational parameter values. Rational bit sizes should be logged; wall time, memory and cost have not been measured.

**Assessment:** 2026-10-13; untested forecast. **Uncertainty:** No implementation, empirical success rate or model comparison exists. A later protocol change, especially repeated split selection, may invalidate the reference guarantee.

[Read the full card](../cards/Q-FORMAL-002.md). **Human review:** Pending.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
