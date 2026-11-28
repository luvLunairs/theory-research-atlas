# General relay-channel capacity

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-457 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-457%3A+General+relay-channel+capacity&target=Q-FORMAL-457) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-457%3A+General+relay-channel+capacity&target=Q-FORMAL-457)

Determine the capacity of an arbitrary discrete memoryless relay channel with a strictly causal relay encoder and vanishing average error.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Conflicting evidence. **Last checked:** 2026-11-26.

**Status basis:** Ponniah claims a general capacity formula. Shiu's 16 September preprint gives a binary channel with a rate exceeding the original proposal. Ponniah's 20 September revision still claims a characterization. Independent adjudication of the revised formula was not located.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** The tutorial dates to 2011. The September 2026 rebuttal appeared between versions 1 and 2 of the proposed formula.

**Scope limits:** The target uses a strictly causal relay in a discrete memoryless channel. The dated objection addresses the proposed characterization, not the underlying capacity question.

**Information still needed**

- A comparison of the revised scheme definitions against Shiu's example and independent assessment.

**Primary branch:** [Classical information theory](../domains/info.md#info-shannon). **Related branches:** None recorded.

**Sources:** [Elements of Network Information Theory: ISIT 2011 tutorial](../sources.md#src-formal-446); [The Capacity of the Relay Channel](../sources.md#src-math-907); [Counterexample to a Proposed Capacity Characterization of the Relay Channel](../sources.md#src-math-908).

**Exact locator:** El Gamal–Kim, relay channel slides, Ponniah v2 Theorem 4, and Shiu sections 2–4

**Potential difficulty:** Unknown. The source identifies an unresolved research target; its present difficulty has not been independently assessed.

**Possible AI role:** Compare both preprint versions against the explicit binary channel before using the proposed formula as a research premise.

**Verification burden:** High. Achievability and converse arguments must match channel, coding, error and asymptotic conventions; local numerical extrema are insufficient.

**Resource expectations:** No physical channel experiment is required for the formal question. Alphabet optimization and symbolic calculations may be costly; no resource bound is established.

**Assessment:** 2026-11-26; untested forecast. **Uncertainty:** A comparison of the revised scheme definitions against Shiu's example and independent assessment. No AI performance has been measured on this task.

**Further work:** resolve the statement and status questions above before planning an attempt. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-26

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Conflicting evidence.

Ponniah claims a general capacity formula. Shiu's 16 September preprint gives a binary channel with a rate exceeding the original proposal. Ponniah's 20 September revision still claims a characterization. Independent adjudication of the revised formula was not located.

**Search scope:** The target uses a strictly causal relay in a discrete memoryless channel. The dated objection addresses the proposed characterization, not the underlying capacity question.

**Inspected evidence**

- [Elements of Network Information Theory: ISIT 2011 tutorial](../sources.md#src-formal-446) — Relay channel: model and capacity, PDF pp. 79–80 (Stanford copy). Introduces the discrete memoryless relay model and its general capacity problem.
- [The Capacity of the Relay Channel](../sources.md#src-math-907) — Version history and v2 Theorem 4. The 14 September claim was revised on 20 September. The latter still proposes a three-scheme formula.
- [Counterexample to a Proposed Capacity Characterization of the Relay Channel](../sources.md#src-math-908) — Sections 2–4, especially section 3.3. Derives an achievable rate above the value of the proposed formula for an explicit binary channel. The manuscript is dated 16 September.

**Limits and remaining work**

- A comparison of the revised scheme definitions against Shiu's example and independent assessment.
- This is a literature check. The cited proofs and computational certificates have not been independently reproduced.

<details>
<summary>Search queries</summary>

- general relay channel Ponniah capacity correction response November 2026 counterexample


</details>

### 2026-10-14

**Coverage:** Statement only. **Statement:** Matched.

**Recorded status:** Unverified → Unverified.

The source supports identifying this question, but does not establish its present unresolved status.

**Search scope:** Inspected the named source statement and its recorded qualifications; no comprehensive citation-chain or specialist database review. The listed targeted searches were exploratory; no verified later source establishing current resolution status was obtained.

**Inspected evidence**

- [Elements of Network Information Theory: ISIT 2011 tutorial](../sources.md#src-formal-446) — PDF pp. 78–79. The source identifies the indexed question or research direction; its original date and any recorded partial results limit what it establishes about present status.

**Limits and remaining work**

- Review later general and special-case results; distinguish this problem from Cover's restricted relay question.
- Current resolution status was not established by a completed later-literature review.

<details>
<summary>Search queries</summary>

- "general relay channel" "capacity" "open" 2025 2026


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
