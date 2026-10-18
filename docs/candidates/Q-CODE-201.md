# Binary length-12 covering codes of radius three

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-CODE-201 · Full card available.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-CODE-201%3A+Binary+length-12+covering+codes+of+radius+three&target=Q-CODE-201) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-CODE-201%3A+Binary+length-12+covering+codes+of+radius+three&target=Q-CODE-201)

Determine K_2(12,3), the smallest size of a set C in {0,...,1}^12 such that every word has Hamming distance at most 3 from some member of C. No linearity or symmetry restriction is imposed. The inspected sources report 19 <= K_2(12,3) <= 28; a certified improvement of either bound is a meaningful partial result.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-10-14.

**Status basis:** The most recent located primary bounds leave the interval [19,28] nontrivial. A targeted search for these parameters and subsequent improvements did not locate an exact value. This is a source-based gap, not an exhaustive certification of open status.

**Statement check:** Source located. **Status check:** Source report only.

**Source date and freshness:** Recorded source years: SRC-CODE-201: 2026. The last-checked date records the scope described in the status basis; it is not a comprehensive literature-search date.

**Scope limits:** Use the full card for assumptions and validation limits.

**Information still needed**

- Confirm that no later construction or lower-bound improvement changes this exact parameter cell.
- Audit the source lower-bound certificate if it is needed in a future proof of optimality.
- Retrieve and independently validate any published starting construction before relying on it.

**Primary branch:** [Coding theory](../domains/info.md#info-codes). **Related branches:** [Extremal and Ramsey theory](../domains/math.md#math-comb-ext).

**Sources:** [Semidefinite lower bounds for covering codes](../sources.md#src-code-201).

**Exact locator:** Table 1, row n=12, R=3

**Potential difficulty:** High. Discovery and optimality remain difficult; witness verification is much easier than finding a better code.

**Possible AI role:** No named model evaluated; assumes a tool-using model able to implement finite search and integer checkers, with human review of problem encoding and novelty. An explicit finite witness is cheap to inspect and the target is precise, making bounded construction search a reasonable first trial. The search itself may still be difficult.

**Verification burden:** Low. Low for an explicit covering witness; substantially higher for a nonexistence or optimality proof.

**Resource expectations:** Experiment: No physical experiment. Data: Generate the 4,096 words directly. Existing code constructions can be starting points if their provenance and version are recorded; no external empirical dataset is needed. Computation: A direct witness check for 27 codewords uses at most 1,327,104 coordinate comparisons. This is an operation bound, not a measured runtime. A direct binary set-cover formulation has 4,096 variables and 4,096 covering constraints. Proposed initial ceiling: 4 CPU-hours and 8 GiB RAM, stopping sooner on a verified improvement. This is a curator-chosen exploration cap, not an estimate of the resources needed to solve the problem; no run or cost measurement has been made.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No model has been evaluated on this task. A small universe and an inexpensive witness checker do not imply that a better cover is easy to find or exists at the selected target size.

[Read the full card](../cards/Q-CODE-201.md). **Human review:** Pending.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
