# A triangle-free 40-vertex graph with independence number at most nine

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MATH-202 · Full card available.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MATH-202%3A+A+triangle-free+40-vertex+graph+with+independence+number+at+most+nine&target=Q-MATH-202) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MATH-202%3A+A+triangle-free+40-vertex+graph+with+independence+number+at+most+nine&target=Q-MATH-202)

Does a finite simple undirected graph G on exactly 40 vertices exist with no triangle and no independent set of ten vertices? A positive witness proves R(3,10)=41; a complete impossibility proof proves R(3,10)=40, using the established interval 40 <= R(3,10) <= 41.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Open after scoped check. **Last checked:** 2026-10-14.

**Status basis:** The 2024 theorem and the survey dated 2026-04-24 leave exactly two values. A scoped search for a later resolution found none in authoritative sources as of 2026-10-14.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Recorded source years: SRC-MATH-001: 2026, SRC-MATH-202: 2024, SRC-MATH-206: date unverified. The last-checked date records the scope described in the status basis; it is not a comprehensive literature-search date.

**Scope limits:** Use the full card for assumptions and validation limits.

**Information still needed**

- Identify and validate seed files before a trial.
- Check whether selected neighborhoods have already been exhausted.
- Refresh the survey and primary result before an exact-value claim.

**Primary branch:** [Extremal and Ramsey theory](../domains/math.md#math-comb-ext). **Related branches:** [Algorithms and data structures](../domains/cs.md#cs-alg).

**Sources:** [Small Ramsey Numbers, Dynamic Survey DS1, revision 18](../sources.md#src-math-001); [R(3,10) <= 41](../sources.md#src-math-202); [Ramsey Numbers](../sources.md#src-math-206).

**Exact locator:** DS1 revision 18, Table Ia and Section 2.1(d); Angeltveit, Theorem 1.1 and Section 7.

**Potential difficulty:** High. The unrestricted target is a research frontier; a bounded trial has no assured outcome.

**Possible AI role:** No named model evaluated; assumes tool-using AI with graph algorithms, exact SAT formulations and certificate handling. There is a decisive compact witness, but existing extensive searches make an arbitrary small neighborhood uncertain. Validate the checker and justify seed selection first.

**Verification burden:** Medium. Positive verification is bounded; global nonexistence is much harder.

**Resource expectations:** Experiment: None. Data: Attributed 39-vertex graph files from the author collection or paper records; validate and identify every selected seed. Computation: Proposed cap: 8 CPU-hours and 16 GiB RAM, at most 20 seeds. There are 780 possible edges. Triangle checking is small; excluding independent ten-sets needs exact branch-and-bound or a checked SAT certificate. No runtime guarantee is made.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No model or proposed neighborhood has been tested. Published computations support the relevance of search, not the likelihood of success under this cap.

[Read the full card](../cards/Q-MATH-202.md). **Human review:** Pending.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
