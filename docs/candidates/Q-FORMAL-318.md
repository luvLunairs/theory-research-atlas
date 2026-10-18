# Distribution-free polynomial-time improper PAC learning of DNF

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-318 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-318%3A+Distribution-free+polynomial-time+improper+PAC+learning+of+DNF&target=Q-FORMAL-318) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-318%3A+Distribution-free+polynomial-time+improper+PAC+learning+of+DNF&target=Q-FORMAL-318)

Can s-term DNF on n Boolean variables be learned from independent random labeled examples under every input distribution in time polynomial in n, s, 1/ε and log(1/δ), to error ε with probability at least 1−δ? Allow an efficiently evaluable improper hypothesis; no membership queries.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-10-14.

**Status basis:** The survey retains this learning target; later scoped searches found no general resolution.

**Statement check:** Source located. **Status check:** Source report only.

**Source date and freshness:** Recorded source years: SRC-FORMAL-307: 2025, SRC-FORMAL-322: 2004. The last-checked date records the scope described in the status basis; it is not a comprehensive literature-search date.

**Scope limits:** The statement and locator identify the candidate. A full assumption set and verification protocol remain to be documented.

**Information still needed**

- Specify the assumptions, candidate methods, resource requirements and independent verification steps for a concrete research task.

**Primary branch:** [Computational learning theory](../domains/cs.md#cs-learn). **Related branches:** [Statistical learning and high-dimensional theory](../domains/stat.md#stat-learn).

**Sources:** [The Probably Approximately Correct Learning Model in Computational Learning Theory](../sources.md#src-formal-307); [Learning DNF in Time 2^{O-tilde(n^{1/3})}](../sources.md#src-formal-322).

**Exact locator:** Servedio, section 3.1, DNF discussion; model definitions in section 2. Klivans–Servedio, sections 1.2 and 2.2 (hypothesis evaluation requirement).

**Potential difficulty:** Frontier. Compact representation does not make relevant terms recoverable under arbitrary distributions.

**Possible AI role:** Test a proposed weak learner on exactly specified hard distributions and audit boosting and sampling requirements.

**Verification burden:** High. Proof needs distribution-uniform sample and time bounds, including hypothesis evaluation.

**Resource expectations:** No physical experiment or external dataset is required. Main cost is specialist proof development and review; finite searches can grow exponentially and need a separately specified limit.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No named model has been evaluated. These are possible research-support roles, not evidence that current AI can resolve the general problem.

**Further work:** define a scoped target, resource requirements and a verification plan before developing a full card. **Human review:** Pending.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
