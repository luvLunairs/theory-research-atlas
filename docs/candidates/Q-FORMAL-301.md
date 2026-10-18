# Unconditional polynomial-time derandomization: BPP versus P

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-301 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-301%3A+Unconditional+polynomial-time+derandomization%3A+BPP+versus+P&target=Q-FORMAL-301) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-301%3A+Unconditional+polynomial-time+derandomization%3A+BPP+versus+P&target=Q-FORMAL-301)

Does every bounded-error randomized polynomial-time decision algorithm have a deterministic polynomial-time counterpart; equivalently, is BPP=P?

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-10-14.

**Status basis:** Recent generator results remain conditional. The scoped later-literature search found no unconditional resolution.

**Statement check:** Source located. **Status check:** Source report only.

**Source date and freshness:** Recorded source years: SRC-FORMAL-301: 2019, SRC-FORMAL-302: 2026. The last-checked date records the scope described in the status basis; it is not a comprehensive literature-search date.

**Scope limits:** The statement and locator identify the candidate. A full assumption set and verification protocol remain to be documented.

**Information still needed**

- Specify the assumptions, candidate methods, resource requirements and independent verification steps for a concrete research task.

**Primary branch:** [Randomized, online and distributed algorithms](../domains/cs.md#cs-random). **Related branches:** [Computational complexity](../domains/cs.md#cs-complex).

**Sources:** [Mathematics and Computation](../sources.md#src-formal-301); [Pseudorandomness Beating the Hybrid Argument for Insensitive Algorithms](../sources.md#src-formal-302).

**Exact locator:** Wigderson, Conjecture 7.8; Doron et al., section 1.1.

**Potential difficulty:** Frontier. General derandomization must escape dependence on unproved circuit hardness.

**Possible AI role:** Audit the hypotheses and parameter losses of a proposed hardness-to-randomness reduction, or test a separately bounded generator for a restricted circuit class.

**Verification burden:** High. A proof must establish uniform polynomial running time and worst-case correctness on all input lengths.

**Resource expectations:** No physical experiment or external dataset is required. Main cost is specialist proof development and review; finite searches can grow exponentially and need a separately specified limit.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No named model has been evaluated. These are possible research-support roles, not evidence that current AI can resolve the general problem.

**Further work:** define a scoped target, resource requirements and a verification plan before developing a full card. **Human review:** Pending.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
