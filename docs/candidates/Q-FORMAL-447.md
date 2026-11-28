# Optimal private stochastic full-information regret

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-447 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-447%3A+Optimal+private+stochastic+full-information+regret&target=Q-FORMAL-447) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-447%3A+Optimal+private+stochastic+full-information+regret&target=Q-FORMAL-447)

For stochastic full-information online learning with K actions, independent and identically distributed loss vectors in [0,1]^K and a unique best action, determine the optimal horizon-uniform gap-dependent rate of expected pseudo-regret under pure event-level ε-differential privacy. Express the rate in K, ε and the gap Δ between the smallest and second-smallest mean loss.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Reported resolved. **Last checked:** 2026-11-28.

**Status basis:** Cesari and Colomboni establish the sharp horizon-uniform rate up to constants, (log K)/Δ + (log K)/ε. Their upper bound holds for every horizon and matches the known worst-case lower bound in its regime. SIAM lists the paper as accepted for SODA 2027.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Hu and Mehta, Section 1 and Definition 1. Cesari and Colomboni, Theorem 1 and the matching lower-bound discussion. SIAM, SODA 2027 accepted-papers list.

**Scope limits:** Cesari and Colomboni establish the sharp horizon-uniform rate up to constants, (log K)/Δ + (log K)/ε. Their upper bound holds for every horizon and matches the known worst-case lower bound in its regime. SIAM lists the paper as accepted for SODA 2027.

**Information still needed**

- This is a literature resolution of the unique-best-action problem. The bound does not assert that this much regret is necessary at every horizon or on each individual instance.

**Primary branch:** [Statistical learning and high-dimensional theory](../domains/stat.md#stat-learn). **Related branches:** None recorded.

**Sources:** [Open Problem: Optimal Rates for Stochastic Decision-Theoretic Online Learning Under Differentially Privacy](../sources.md#src-formal-443); [Optimal Gap-Dependent Regret for Private Stochastic Decision-Theoretic Online Learning](../sources.md#src-model-924); [SODA27 Accepted Papers](../sources.md#src-model-925).

**Exact locator:** Hu and Mehta, Section 1 and Definition 1. Cesari and Colomboni, Theorem 1 and the matching lower-bound discussion. SIAM, SODA 2027 accepted-papers list.

**Potential difficulty:** Unknown. The literature gives matching upper and lower rates. The difficulty of independently reproducing the upper-bound argument has not been assessed.

**Possible AI role:** Reproduce the theorem and the lower-bound parameter regime when using this historical question as a benchmark.

**Verification burden:** High. Upper and lower bounds must use identical distribution classes, loss, privacy or oracle conditions and quantifiers; statistical counterexamples need exact arguments.

**Resource expectations:** The formal target needs no new physical experiment. Simulations may use synthetic samples; necessary sample counts and computational costs have not been estimated.

**Assessment:** 2026-11-28; untested forecast. **Uncertainty:** This is a literature resolution of the unique-best-action problem. The bound does not assert that this much regret is necessary at every horizon or on each individual instance.

**Further work:** examine the cited result or develop a clearly labeled reproduction. Any new variant needs its own statement and relation to this record. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-28

**Coverage:** Statement and later literature. **Statement:** Corrected.

**Recorded status:** Unverified → Reported resolved.

Cesari and Colomboni establish the sharp horizon-uniform rate up to constants, (log K)/Δ + (log K)/ε. Their upper bound holds for every horizon and matches the known worst-case lower bound in its regime. SIAM lists the paper as accepted for SODA 2027.

**Search scope:** Compared the indexed question with the passages and later records listed below.

<details>
<summary>Previous indexed wording</summary>

Determine matching gap-dependent pseudo-regret bounds for stochastic full-information online learning with K actions, losses in [0,1], horizon T and pure epsilon-differential privacy, as a function of the minimum positive mean-loss gap.

The current statement appears at the top of this page.
</details>

**Inspected evidence**

- [Open Problem: Optimal Rates for Stochastic Decision-Theoretic Online Learning Under Differentially Privacy](../sources.md#src-formal-443) — Section 1 and Definition 1. Specifies a unique optimal action, stochastic losses, full loss-vector observations and pure privacy.
- [Optimal Gap-Dependent Regret for Private Stochastic Decision-Theoretic Online Learning](../sources.md#src-model-924) — Version 1, Theorem 1 and the comparison with the known lower bound immediately afterward. The pure event-level private algorithm attains worst-case gap-dependent pseudo-regret of order (log K)/Δ + (log K)/ε uniformly in the horizon, matching the cited lower bound in its applicable regime.
- [SODA27 Accepted Papers](../sources.md#src-model-925) — Accepted-papers list, entry under the title of the Cesari–Colomboni paper. SIAM lists the matching title and both authors among papers accepted at SODA 2027.

**Limits and remaining work**

- This is a literature resolution of the unique-best-action problem. The bound does not assert that this much regret is necessary at every horizon or on each individual instance.

<details>
<summary>Search queries</summary>

- optimal gap-dependent regret private stochastic decision-theoretic online learning Cesari Colomboni Hu Mehta SODA 2027 accepted papers


</details>

### 2026-10-14

**Coverage:** Statement only. **Statement:** Matched.

**Recorded status:** Unverified → Unverified.

The source supports identifying this question, but does not establish its present unresolved status.

**Search scope:** Inspected the named source statement and its recorded qualifications; no comprehensive citation-chain or specialist database review. The listed targeted searches were exploratory; no verified later source establishing current resolution status was obtained.

**Inspected evidence**

- [Open Problem: Optimal Rates for Stochastic Decision-Theoretic Online Learning Under Differentially Privacy](../sources.md#src-formal-443) — Introduction; section 3. The source identifies the indexed question or research direction; its original date and any recorded partial results limit what it establishes about present status.

**Limits and remaining work**

- Later matching rates and exact privacy adjacency conventions.
- Current resolution status was not established by a completed later-literature review.

<details>
<summary>Search queries</summary>

- "Optimal Rates" "Stochastic" "Hu" "Mehta" privacy 2025 2026


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
