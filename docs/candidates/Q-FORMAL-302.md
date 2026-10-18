# Deterministic logarithmic space for directed reachability: L versus NL

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-302 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-302%3A+Deterministic+logarithmic+space+for+directed+reachability%3A+L+versus+NL&target=Q-FORMAL-302) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-302%3A+Deterministic+logarithmic+space+for+directed+reachability%3A+L+versus+NL&target=Q-FORMAL-302)

Can directed s–t reachability be decided in deterministic O(log n) work space? This is equivalent to L=NL.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-10-14.

**Status basis:** The source presents L versus NL as open. The later search found no resolution of directed reachability; randomized-space claims are different.

**Statement check:** Source located. **Status check:** Source report only.

**Source date and freshness:** Recorded source years: SRC-FORMAL-301: 2019. The last-checked date records the scope described in the status basis; it is not a comprehensive literature-search date.

**Scope limits:** The statement and locator identify the candidate. A full assumption set and verification protocol remain to be documented.

**Information still needed**

- Specify the assumptions, candidate methods, resource requirements and independent verification steps for a concrete research task.

**Primary branch:** [Computational complexity](../domains/cs.md#cs-complex). **Related branches:** [Algorithms and data structures](../domains/cs.md#cs-alg).

**Sources:** [Mathematics and Computation](../sources.md#src-formal-301).

**Exact locator:** Wigderson, section 14.2, Conjecture 14.8.

**Potential difficulty:** Frontier. Reachability is a central nondeterministic-space complete problem.

**Possible AI role:** Check workspace accounting and uniformity in a proposed restricted-graph reachability algorithm.

**Verification burden:** High. All work tapes, counters and recursion stacks count toward space; successful finite runs do not prove the asymptotic claim.

**Resource expectations:** No physical experiment or external dataset is required. Main cost is specialist proof development and review; finite searches can grow exponentially and need a separately specified limit.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No named model has been evaluated. These are possible research-support roles, not evidence that current AI can resolve the general problem.

**Further work:** define a scoped target, resource requirements and a verification plan before developing a full card. **Human review:** Pending.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
