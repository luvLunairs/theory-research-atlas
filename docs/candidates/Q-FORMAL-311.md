# A strongly polynomial algorithm for general linear programming

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-311 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-311%3A+A+strongly+polynomial+algorithm+for+general+linear+programming&target=Q-FORMAL-311) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-311%3A+A+strongly+polynomial+algorithm+for+general+linear+programming&target=Q-FORMAL-311)

Does rational linear programming admit an algorithm with a number of arithmetic operations polynomial only in the numbers of variables and constraints, and with all intermediate encodings polynomial in the input length?

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-10-14.

**Status basis:** The survey explicitly reports the general problem open. Later searches found strongly polynomial restricted LP/MDP results, not the general algorithm.

**Statement check:** Source located. **Status check:** Source report only.

**Source date and freshness:** Recorded source years: SRC-FORMAL-307: 2025. The last-checked date records the scope described in the status basis; it is not a comprehensive literature-search date.

**Scope limits:** The statement and locator identify the candidate. A full assumption set and verification protocol remain to be documented.

**Information still needed**

- Specify the assumptions, candidate methods, resource requirements and independent verification steps for a concrete research task.

**Primary branch:** [Optimization and operations research](../domains/math.md#math-opt). **Related branches:** [Algorithms and data structures](../domains/cs.md#cs-alg).

**Sources:** [The Probably Approximately Correct Learning Model in Computational Learning Theory](../sources.md#src-formal-307).

**Exact locator:** Servedio, section 3.1 footnote 3.

**Potential difficulty:** Frontier. Ordinary polynomial-time algorithms can depend on numeric bit lengths or conditioning.

**Possible AI role:** Audit pivot or potential arguments for hidden dependence on coefficient magnitudes and construct exact adversarial small inputs.

**Verification burden:** High. Both arithmetic-operation count and bit growth must be bounded; empirical speed does not establish strong polynomiality.

**Resource expectations:** No physical experiment or external dataset is required. Main cost is specialist proof development and review; finite searches can grow exponentially and need a separately specified limit.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No named model has been evaluated. These are possible research-support roles, not evidence that current AI can resolve the general problem.

**Further work:** define a scoped target, resource requirements and a verification plan before developing a full card. **Human review:** Pending.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
