# Are linear-size Boolean circuits possible for integer multiplication?

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-304 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-304%3A+Are+linear-size+Boolean+circuits+possible+for+integer+multiplication%3F&target=Q-FORMAL-304) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-304%3A+Are+linear-size+Boolean+circuits+possible+for+integer+multiplication%3F&target=Q-FORMAL-304)

Do circuits over bounded-fan-in AND, OR and NOT multiply two n-bit integers with O(n) gates, outputting the full product?

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-10-14.

**Status basis:** Source-reported open; later searches did not identify a resolution for this unrestricted gate model.

**Statement check:** Source located. **Status check:** Source report only.

**Source date and freshness:** Recorded source years: SRC-FORMAL-301: 2019. The last-checked date records the scope described in the status basis; it is not a comprehensive literature-search date.

**Scope limits:** The statement and locator identify the candidate. A full assumption set and verification protocol remain to be documented.

**Information still needed**

- Specify the assumptions, candidate methods, resource requirements and independent verification steps for a concrete research task.

**Primary branch:** [Circuit and algebraic complexity](../domains/cs.md#cs-complex-circuit). **Related branches:** [Algorithms and data structures](../domains/cs.md#cs-alg).

**Sources:** [Mathematics and Computation](../sources.md#src-formal-301).

**Exact locator:** Wigderson, section 5.2.1, discussion immediately following Open Problem 5.8.

**Potential difficulty:** Frontier. Even a superlinear bound for this explicit function would exceed present general circuit techniques.

**Possible AI role:** Verify small multiplier constructions or audit the gate accounting in an asymptotic proposed design.

**Verification burden:** High. A finite circuit is exhaustively checkable, but a universal upper or lower bound needs an independent proof.

**Resource expectations:** No physical experiment or external dataset is required. Main cost is specialist proof development and review; finite searches can grow exponentially and need a separately specified limit.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** Recent multiplication claims require careful separation of arithmetic-operation, bit-operation and Boolean-gate models. No named model has been evaluated. These are possible research-support roles, not evidence that current AI can resolve the general problem.

**Further work:** define a scoped target, resource requirements and a verification plan before developing a full card. **Human review:** Pending.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
