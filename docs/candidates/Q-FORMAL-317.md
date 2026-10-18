# Linear-size sample compression for every binary VC class

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-317 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-317%3A+Linear-size+sample+compression+for+every+binary+VC+class&target=Q-FORMAL-317) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-317%3A+Linear-size+sample+compression+for+every+binary+VC+class&target=Q-FORMAL-317)

Does every binary concept class of finite VC dimension d admit an exact realizable compression scheme storing O(d) original labeled examples plus auxiliary bits, counted together, from which a predictor consistent with the entire sample is reconstructed?

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-10-14.

**Status basis:** The 2025 source reports the conjecture open. A 2026 apparent solution was checked against the current withdrawn record, which identifies an incorrect proof.

**Statement check:** Source located. **Status check:** Source report only.

**Source date and freshness:** Recorded source years: SRC-FORMAL-310: 2025, SRC-FORMAL-311: 2026. The last-checked date records the scope described in the status basis; it is not a comprehensive literature-search date.

**Scope limits:** The statement and locator identify the candidate. A full assumption set and verification protocol remain to be documented.

**Information still needed**

- Specify the assumptions, candidate methods, resource requirements and independent verification steps for a concrete research task.

**Primary branch:** [Statistical learning and high-dimensional theory](../domains/stat.md#stat-learn). **Related branches:** [Computational learning theory](../domains/cs.md#cs-learn).

**Sources:** [Sample Compression Scheme Reductions](../sources.md#src-formal-310); [The No-Clash Teaching Dimension is Bounded by VC Dimension [withdrawn]](../sources.md#src-formal-311).

**Exact locator:** Attias et al., Definition 2.1 and following conjecture; arXiv:2603.23561 withdrawal history.

**Potential difficulty:** Frontier. Known dimension-dependent compression does not establish a universal linear bound.

**Possible AI role:** Enumerate finite concept classes to test a specified compressor, with reconstruction and side-information accounting fixed in advance.

**Verification burden:** High. General proof must work for every class and every finite realizable sample; finite success is not the conjecture.

**Resource expectations:** No physical experiment or external dataset is required. Main cost is specialist proof development and review; finite searches can grow exponentially and need a separately specified limit.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** The withdrawal does not exclude other later solutions. Stronger size-exactly-d and unlabeled versions are distinct. No named model has been evaluated. These are possible research-support roles, not evidence that current AI can resolve the general problem.

**Further work:** define a scoped target, resource requirements and a verification plan before developing a full card. **Human review:** Pending.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
