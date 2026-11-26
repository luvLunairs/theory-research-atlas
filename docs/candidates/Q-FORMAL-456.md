# General broadcast-channel capacity

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-456 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-456%3A+General+broadcast-channel+capacity&target=Q-FORMAL-456) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-456%3A+General+broadcast-channel+capacity&target=Q-FORMAL-456)

Determine the capacity region of an arbitrary two-receiver discrete memoryless broadcast channel with independent private messages and vanishing average error.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-11-26.

**Status basis:** Huang, Liu and Liu describe the general capacity region as open and report a finite channel where coding over two uses improves the one-letter Marton sum rate. Their counterexample concerns the inner bound and leaves the general characterization open.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** The 2011 ISIT tutorial sets out the problem. The new preprint was posted on 20 August 2026.

**Scope limits:** The target is the full region for two receivers with independent private messages. A strict gain in an achievable sum rate need not determine the boundary of that region.

**Information still needed**

- Independent replication of the preprint's certificate and a characterization of the general region.

**Primary branch:** [Classical information theory](../domains/info.md#info-shannon). **Related branches:** None recorded.

**Sources:** [Elements of Network Information Theory: ISIT 2011 tutorial](../sources.md#src-formal-446); [Sub-optimality of Marton's Inner Bound for the Two-Receiver Broadcast Channel](../sources.md#src-math-906).

**Exact locator:** El Gamal–Kim, broadcast channel slides, and Huang–Liu–Liu, introduction and section III

**Potential difficulty:** Unknown. The source identifies an unresolved research target; its present difficulty has not been independently assessed.

**Possible AI role:** After operational conventions are fixed, explore small-alphabet examples, compare inner and outer bounds and assist with entropy calculations. Numerical optimization cannot establish a capacity formula.

**Verification burden:** High. Achievability and converse arguments must match channel, coding, error and asymptotic conventions; local numerical extrema are insufficient.

**Resource expectations:** No physical channel experiment is required for the formal question. Alphabet optimization and symbolic calculations may be costly; no resource bound is established.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No model has been tested. Current status, useful subcases and feasible computational scale require further review.

**Further work:** define a scoped target, resource requirements and a verification plan before developing a full card. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-26

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Source reports open.

Huang, Liu and Liu describe the general capacity region as open and report a finite channel where coding over two uses improves the one-letter Marton sum rate. Their counterexample concerns the inner bound and leaves the general characterization open.

**Search scope:** The target is the full region for two receivers with independent private messages. A strict gain in an achievable sum rate need not determine the boundary of that region.

**Inspected evidence**

- [Elements of Network Information Theory: ISIT 2011 tutorial](../sources.md#src-formal-446) — Broadcast channel: model and capacity region, PDF pp. 38–39 (Stanford copy). Defines achievability for two private messages and records the historical general problem.
- [Sub-optimality of Marton's Inner Bound for the Two-Receiver Broadcast Channel](../sources.md#src-math-906) — Introduction and section III, especially III-C. Reports strict nonadditivity of the one-letter Marton sum rate for an unconstrained finite channel.

**Limits and remaining work**

- Independent replication of the preprint's certificate and a characterization of the general region.
- This is a literature check. The cited proofs and computational certificates have not been independently reproduced.

<details>
<summary>Search queries</summary>

- general discrete memoryless broadcast channel Marton private messages capacity remains open 2026


</details>

### 2026-10-14

**Coverage:** Statement only. **Statement:** Matched.

**Recorded status:** Unverified → Unverified.

The source supports identifying this question, but does not establish its present unresolved status.

**Search scope:** Inspected the named source statement and its recorded qualifications; no comprehensive citation-chain or specialist database review. The listed targeted searches were exploratory; no verified later source establishing current resolution status was obtained.

**Inspected evidence**

- [Elements of Network Information Theory: ISIT 2011 tutorial](../sources.md#src-formal-446) — PDF pp. 37–38. The source identifies the indexed question or research direction; its original date and any recorded partial results limit what it establishes about present status.

**Limits and remaining work**

- Review later capacity theorems; establish which channel classes remain unresolved.
- Current resolution status was not established by a completed later-literature review.

<details>
<summary>Search queries</summary>

- "general broadcast channel" "capacity" "2025" "open"


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
