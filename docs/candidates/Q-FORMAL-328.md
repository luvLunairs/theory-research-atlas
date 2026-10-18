# Exact capacity of the independent binary deletion channel

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-328 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-328%3A+Exact+capacity+of+the+independent+binary+deletion+channel&target=Q-FORMAL-328) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-328%3A+Exact+capacity+of+the+independent+binary+deletion+channel&target=Q-FORMAL-328)

Determine the Shannon capacity C(d) in bits per input bit of the binary channel that independently deletes each input bit with probability d∈(0,1), preserves the order of surviving bits and does not reveal deletion locations, without feedback.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-10-14.

**Status basis:** The September 2026 source explicitly says exact capacity remains unknown despite its new approximate enclosures.

**Statement check:** Source located. **Status check:** Source report only.

**Source date and freshness:** Recorded source years: SRC-FORMAL-318: 2026. The last-checked date records the scope described in the status basis; it is not a comprehensive literature-search date.

**Scope limits:** The statement and locator identify the candidate. A full assumption set and verification protocol remain to be documented.

**Information still needed**

- Specify the assumptions, candidate methods, resource requirements and independent verification steps for a concrete research task.

**Primary branch:** [Classical information theory](../domains/info.md#info-shannon). **Related branches:** None recorded.

**Sources:** [Binary Deletion Channel Capacity to Within One Hundredth of a Bit](../sources.md#src-formal-318).

**Exact locator:** Papailiopoulos, introduction and capacity definition.

**Potential difficulty:** Frontier. The optimum ranges over input processes with unbounded dependence and requires matching converse and achievability.

**Possible AI role:** Audit finite-window bounds and their rigorous remainder estimates for a fixed deletion probability.

**Verification burden:** High. A good code is only a lower bound; capacity needs a converse valid for arbitrary encoders and vanishing-error asymptotics.

**Resource expectations:** No physical experiment or measured data is required. Finite-channel optimization and certificate storage can become very large; restrict block length before computation.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No named model has been evaluated. These are possible research-support roles, not evidence that current AI can resolve the general problem.

**Further work:** define a scoped target, resource requirements and a verification plan before developing a full card. **Human review:** Pending.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
