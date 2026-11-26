# Assumptions permitting optimal heavy-tail adaptation

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-442 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-442%3A+Assumptions+permitting+optimal+heavy-tail+adaptation&target=Q-FORMAL-442) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-442%3A+Assumptions+permitting+optimal+heavy-tail+adaptation&target=Q-FORMAL-442)

For stochastic bandits with unknown moment order and bound, can one distributional assumption encompass all instances on which a learner can match the known-parameter regret rate at no additional cost?

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Unverified. **Last checked:** 2026-11-26.

**Status basis:** The COLT question asks whether a single assumption can cover the distributions permitting adaptation at oracle cost. Do and Nguyen give a characterization for an explicit central-moment benchmark. Its dependence on the benchmark and known visibility constants limits a general resolution claim.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** COLT 2025; arXiv:2611.12140v2, 11 November 2026.

**Scope limits:** The structural condition concerns the optimal arm. The upper bound takes the horizon and visibility constants as inputs; the converse constrains strategies with a specified exploration budget.

**Information still needed**

- Compare the 2025 raw-moment oracle guarantees with the central-moment budget in the November preprint, including the allowed side information.

**Primary branch:** [Statistical learning and high-dimensional theory](../domains/stat.md#stat-learn). **Related branches:** None recorded.

**Sources:** [Open Problem: Regret Minimization in Heavy-Tailed Bandits with Unknown Distributional Parameters](../sources.md#src-formal-439); [Visible Tails: Characterizing Adaptation to Unknown Moments in Heavy-Tailed Bandits](../sources.md#src-model-901).

**Exact locator:** COLT Open Question 3; Do and Nguyen (2026), Sections 2–5.

**Potential difficulty:** Unknown. A benchmark-specific preprint supplies both an upper bound and a converse; the scope of the original structural question still needs comparison.

**Possible AI role:** Check which original oracle guarantees the visibility theorem recovers and what side information its learner uses.

**Verification burden:** High. Upper and lower bounds must use identical distribution classes, loss, privacy or oracle conditions and quantifiers; statistical counterexamples need exact arguments.

**Resource expectations:** The formal target needs no new physical experiment. Simulations may use synthetic samples; necessary sample counts and computational costs have not been estimated.

**Assessment:** 2026-11-26; untested forecast. **Uncertainty:** The proof and equivalence of benchmarks have not been independently checked.

**Further work:** resolve the statement and status questions above before planning an attempt. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-26

**Coverage:** Statement and later literature. **Statement:** Corrected.

**Recorded status:** Unverified → Unverified.

The COLT question asks whether a single assumption can cover the distributions permitting adaptation at oracle cost. Do and Nguyen give a characterization for an explicit central-moment benchmark. Its dependence on the benchmark and known visibility constants limits a general resolution claim.

**Search scope:** Compared Question 3 in the proceedings PDF with both arXiv versions; the record follows the revised theorem statements of 11 November.

<details>
<summary>Previous indexed wording</summary>

Characterize distributional assumptions sufficient and necessary to avoid the extra regret cost of adapting to unknown heavy-tail moment order and bound in stochastic bandits.

The current statement appears at the top of this page.
</details>

**Inspected evidence**

- [Open Problem: Regret Minimization in Heavy-Tailed Bandits with Unknown Distributional Parameters](../sources.md#src-formal-439) — Open Question 3. Asks whether a structural assumption can encompass the distributions allowing cost-free adaptation.
- [Visible Tails: Characterizing Adaptation to Unknown Moments in Heavy-Tailed Bandits](../sources.md#src-model-901) — Sections 2–5. States a one-sided visibility criterion, an algorithm informed of its constants and a converse indexed by the exploration budget.

**Limits and remaining work**

- The proof and equivalence of benchmarks have not been independently checked.

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

- [Open Problem: Regret Minimization in Heavy-Tailed Bandits with Unknown Distributional Parameters](../sources.md#src-formal-439) — Abstract, second open question. The source identifies the indexed question or research direction; its original date and any recorded partial results limit what it establishes about present status.

**Limits and remaining work**

- A formal ordering of admissible assumptions and later necessity results are missing.
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
