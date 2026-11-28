# Optimal adaptation cost in heavy-tailed bandits

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-441 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-441%3A+Optimal+adaptation+cost+in+heavy-tailed+bandits&target=Q-FORMAL-441) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-441%3A+Optimal+adaptation+cost+in+heavy-tailed+bandits&target=Q-FORMAL-441)

For stochastic bandit rewards with absolute moments of order 1+epsilon bounded by u, with epsilon and u unknown, determine the best possible regret without additional distributional assumptions.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Unverified. **Last checked:** 2026-11-26.

**Status basis:** The original authors report a resolution of the assumption-free rate and algorithm questions up to logarithmic factors. Their results describe trade-offs between guarantees, including a lower bound across moment orders. The preprint awaits independent assessment here.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** COLT 2025; arXiv:2607.29460v1, 31 July 2026.

**Scope limits:** Each arm has a bounded absolute raw moment of order 1+epsilon, with 0 < epsilon <= 1. Distinguish distribution-dependent and worst-case regret. Sublinear regret at each fixed epsilon differs from uniform sublinearity over all positive epsilon.

**Information still needed**

- Check the matching bounds and the endpoint guarantee used in Theorems 7–8 before treating the reported resolution as settled.

**Primary branch:** [Statistical learning and high-dimensional theory](../domains/stat.md#stat-learn). **Related branches:** None recorded.

**Sources:** [Open Problem: Regret Minimization in Heavy-Tailed Bandits with Unknown Distributional Parameters](../sources.md#src-formal-439); [Parameter-Free Heavy-Tailed Bandits](../sources.md#src-model-900).

**Exact locator:** COLT Definition 1 and Open Questions 1–2; Genalti and Metelli (2026), Sections 4–7.

**Potential difficulty:** Unknown. A published problem statement and a matching preprint claim make proof and scope review the immediate task.

**Possible AI role:** Compare the rate normalizations and quantifiers in the COLT questions with the July theorems before pursuing a new bound.

**Verification burden:** High. Upper and lower bounds must use identical distribution classes, loss, privacy or oracle conditions and quantifiers; statistical counterexamples need exact arguments.

**Resource expectations:** The formal target needs no new physical experiment. Simulations may use synthetic samples; necessary sample counts and computational costs have not been estimated.

**Assessment:** 2026-11-26; untested forecast. **Uncertainty:** The later proof was not independently audited. Logarithmic terms and horizon knowledge matter when choosing a sharper target.

**Further work:** resolve the statement and status questions above before planning an attempt. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-26

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Unverified.

The original authors report a resolution of the assumption-free rate and algorithm questions up to logarithmic factors. Their results describe trade-offs between guarantees, including a lower bound across moment orders. The preprint awaits independent assessment here.

**Search scope:** Compared the original full paper with the July preprint's upper and lower bounds and conclusion. Checked the arXiv version record.

**Inspected evidence**

- [Open Problem: Regret Minimization in Heavy-Tailed Bandits with Unknown Distributional Parameters](../sources.md#src-formal-439) — Definition 1 and Open Questions 1–2. Asks for attainable regret and an algorithm without knowledge of either moment parameter.
- [Parameter-Free Heavy-Tailed Bandits](../sources.md#src-model-900) — Sections 4–7, Theorems 7–8 and Corollary 9. Gives matching scale trade-offs up to logarithms and compares performance at different fixed moment orders.

**Limits and remaining work**

- The later proof was not independently audited. Logarithmic terms and horizon knowledge matter when choosing a sharper target.

<details>
<summary>Search queries</summary>

- 2026 heavy-tailed bandits Genalti adaptation price 2025 COLT open problem tail assumptions Pareto regret frontier heavy tailed bandits


</details>

### 2026-10-14

**Coverage:** Access limited. **Statement:** Needs clarification.

**Recorded status:** Unverified → Unverified.

The source supports identifying this question, but does not establish its present unresolved status.

**Search scope:** Read the publisher's abstract and bibliographic record. The full formal problem note was not successfully inspected; targeted discovery did not establish a later resolution.

**Inspected evidence**

- [Open Problem: Regret Minimization in Heavy-Tailed Bandits with Unknown Distributional Parameters](../sources.md#src-formal-439) — Abstract, first open question. The source identifies the indexed question or research direction; its original date and any recorded partial results limit what it establishes about present status.

**Limits and remaining work**

- The uniformity of the adaptation benchmark and later upper/lower bounds require checking.
- No exhaustive search for subsequent resolutions was completed.
- Full-text model assumptions and quantitative targets remain unverified; an abstract alone is insufficient for a complete statement check.

<details>
<summary>Search queries</summary>

- "Regret Minimization in Heavy-Tailed Bandits with Unknown" solution


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
