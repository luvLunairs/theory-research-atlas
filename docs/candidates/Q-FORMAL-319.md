# Distribution-free polynomial-time improper PAC learning of decision trees

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-319 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-319%3A+Distribution-free+polynomial-time+improper+PAC+learning+of+decision+trees&target=Q-FORMAL-319) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-319%3A+Distribution-free+polynomial-time+improper+PAC+learning+of+decision+trees&target=Q-FORMAL-319)

Can Boolean decision trees of size s on n input variables be PAC learned from random labeled examples under arbitrary distributions in time polynomial in n, s, 1/ε and log(1/δ), allowing efficiently evaluable improper hypotheses and no membership queries?

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-10-14.

**Status basis:** The 2026 product-distribution analysis does not settle this unrestricted distribution-free target.

**Statement check:** Source located. **Status check:** Source report only.

**Source date and freshness:** Recorded source years: SRC-FORMAL-307: 2025, SRC-FORMAL-313: 2026. The last-checked date records the scope described in the status basis; it is not a comprehensive literature-search date.

**Scope limits:** The statement and locator identify the candidate. A full assumption set and verification protocol remain to be documented.

**Information still needed**

- Specify the assumptions, candidate methods, resource requirements and independent verification steps for a concrete research task.

**Primary branch:** [Computational learning theory](../domains/cs.md#cs-learn). **Related branches:** [Statistical learning and high-dimensional theory](../domains/stat.md#stat-learn).

**Sources:** [The Probably Approximately Correct Learning Model in Computational Learning Theory](../sources.md#src-formal-307); [Decision Tree Learning on Product Spaces](../sources.md#src-formal-313).

**Exact locator:** Servedio, section 3.1; Moakahr et al., abstract and sections 1.3 and 7.

**Potential difficulty:** Frontier. General improper learning must improve on longstanding quasipolynomial approaches without relying on favorable feature distributions.

**Possible AI role:** Check a candidate splitting criterion on adversarial distributions and audit whether its guarantee extends beyond product measures.

**Verification burden:** High. Distinguish improper learning from finding a small consistent tree, and certify all distributional assumptions.

**Resource expectations:** No physical experiment or external dataset is required. Main cost is specialist proof development and review; finite searches can grow exponentially and need a separately specified limit.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No named model has been evaluated. These are possible research-support roles, not evidence that current AI can resolve the general problem.

**Further work:** define a scoped target, resource requirements and a verification plan before developing a full card. **Human review:** Pending.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
