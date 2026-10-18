# A 150-point no-three-in-line configuration on a 75 by 75 grid

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MATH-201 · Full card available.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MATH-201%3A+A+150-point+no-three-in-line+configuration+on+a+75+by+75+grid&target=Q-MATH-201) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MATH-201%3A+A+150-point+no-three-in-line+configuration+on+a+75+by+75+grid&target=Q-MATH-201)

Does there exist S contained in {0,...,74}^2 with |S|=150 such that (x_j-x_i)(y_k-y_i)-(x_k-x_i)(y_j-y_i) is nonzero for every three distinct points of S? A construction attains the row-count upper bound; an impossibility proof must cover all configurations.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Open after scoped check. **Last checked:** 2026-10-14.

**Status basis:** The author-maintained frontier records all sizes 2 through 74 and size 76, but no size 75. Searches for a size-75 construction or impossibility result found no authoritative resolution by 2026-10-14. This is an open-status inference from a dated frontier gap, not an explicit theorem of open status.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Recorded source years: SRC-MATH-201: date unverified. The last-checked date records the scope described in the status basis; it is not a comprehensive literature-search date.

**Scope limits:** Use the full card for assumptions and validation limits.

**Information still needed**

- Refresh the latest table.
- Determine whether the proposed symmetry case has already been exhausted.
- Audit sub-150 records before claiming a lower-count improvement.

**Primary branch:** [Geometry](../domains/math.md#math-geom). **Related branches:** [Extremal and Ramsey theory](../domains/math.md#math-comb-ext), [Algorithms and data structures](../domains/cs.md#cs-alg).

**Sources:** [The No-Three-in-Line Problem](../sources.md#src-math-201).

**Exact locator:** Introduction and maintained frontier entries for n=71,73,74,76; summary-table date 2026-09-11.

**Potential difficulty:** High. The unrestricted target is a research frontier; a bounded trial has no assured outcome.

**Possible AI role:** No named model evaluated; assumes tool-using AI able to implement integer constraints, reason about symmetry and produce inspectable solver inputs. Priority applies to the bounded construction experiment: its output is precise and independently checkable. It does not predict that the frontier target will be solved.

**Verification burden:** Medium. Positive checking is simple; UNSAT needs an encoding proof and certificate audit.

**Resource expectations:** Experiment: None. Data: Self-contained. Optional attributed configurations and encodings come from Flammenkamp's database. Computation: Proposed cap: 8 CPU-hours and 16 GiB RAM. The grid has 5,625 positions. A positive witness needs C(150,3)=551,300 exact triple checks. Full impossibility may require much larger resources.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No model or search has been evaluated. Easy checking gives no estimate of success probability, and the frontier can change quickly.

[Read the full card](../cards/Q-MATH-201.md). **Human review:** Pending.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
