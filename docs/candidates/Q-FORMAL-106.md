# Reproduce the LRU paging competitive bound with explicit initial-state terms

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-106 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-106%3A+Reproduce+the+LRU+paging+competitive+bound+with+explicit+initial-state+terms&target=Q-FORMAL-106) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-106%3A+Reproduce+the+LRU+paging+competitive+bound+with+explicit+initial-state+terms&target=Q-FORMAL-106)

In uniform-cost demand paging with cache capacity k >= 1, reproduce the equal-capacity specialization of Sleator and Tarjan's Theorem 6: LRU incurs at most k times the optimal offline fault count plus a constant depending only on initial cache states. Specify a common initially empty convention and derive its startup term rather than assume it vanishes. Explain why finite trace tests do not prove the all-sequence guarantee.

**Origin:** Known-result calibration. **Curator-designed scope:** Yes.

**Current status:** Known result in literature. **Last checked:** 2026-10-14.

**Status basis:** The primary paper proves the cache-size-dependent bound and discusses its additive initial-state term. This is an established-result calibration, not a guarantee for other paging models.

**Statement check:** Source located. **Status check:** Source report only.

**Source date and freshness:** Recorded source years: SRC-FORMAL-108: 1985. The last-checked date records the scope described in the status basis; it is not a comprehensive literature-search date.

**Scope limits:** The statement and locator identify the candidate. A full assumption set and verification protocol remain to be documented.

**Information still needed**

- Specify the assumptions, candidate methods, resource requirements and independent verification steps for a concrete research task.

**Primary branch:** [Randomized, online and distributed algorithms](../domains/cs.md#cs-random). **Related branches:** [Algorithms and data structures](../domains/cs.md#cs-alg).

**Sources:** [Amortized Efficiency of List Update and Paging Rules](../sources.md#src-formal-108).

**Exact locator:** Section 4, Theorem 6 and following initial-cache discussion

**Potential difficulty:** Unknown. No separate difficulty review of this exact statement is recorded. Its origin or current status does not establish tractability.

**Possible AI role:** A tool-using mathematical assistant could compare hypotheses, locate relevant results and propose a narrower proof, construction or counterexample task; a specialist must first select and check that task.

**Verification burden:** Unknown. The statement and source need a task-specific proof or certificate plan before an attempt.

**Resource expectations:** No run estimate is available. Decide data, computation and experiment requirements after selecting a concrete approach.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No named model has been evaluated on this target; AI usefulness and success probability remain unmeasured.

**Further work:** examine the cited result or develop a clearly labeled reproduction. Any new variant needs its own statement and relation to this record. **Human review:** Pending.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
