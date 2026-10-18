# Improve the lower bound for R(4,6) with a 36-vertex graph

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MATH-204 · Full card available.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MATH-204%3A+Improve+the+lower+bound+for+R%284%2C6%29+with+a+36-vertex+graph&target=Q-MATH-204) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MATH-204%3A+Improve+the+lower+bound+for+R%284%2C6%29+with+a+36-vertex+graph&target=Q-MATH-204)

Does there exist a finite simple undirected graph on exactly 36 vertices having neither a clique of four vertices nor an independent set of six vertices? A witness proves R(4,6) >= 37; ruling out all such graphs would prove R(4,6)=36.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Open after scoped check. **Last checked:** 2026-10-14.

**Status basis:** The 2026 survey gives 36 <= R(4,6) <= 40, with the upper bound in Table Ib rather than the older Table Ia entry. The author collection supplies 35-vertex witnesses. No authoritative later resolution was located in a scoped check on 2026-10-14.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Recorded source years: SRC-MATH-001: 2026, SRC-MATH-203: 2012, SRC-MATH-206: date unverified. The last-checked date records the scope described in the status basis; it is not a comprehensive literature-search date.

**Scope limits:** Use the full card for assumptions and validation limits.

**Information still needed**

- Fetch and independently validate the individual seed files before a trial.
- Check whether four-edge extension neighborhoods have already been exhausted.
- Confirm the live survey bounds before describing a result as an improvement.

**Primary branch:** [Extremal and Ramsey theory](../domains/math.md#math-comb-ext). **Related branches:** [Algorithms and data structures](../domains/cs.md#cs-alg).

**Sources:** [Small Ramsey Numbers, Dynamic Survey DS1, revision 18](../sources.md#src-math-001); [R(4,6) Colorings](../sources.md#src-math-203); [Ramsey Numbers](../sources.md#src-math-206).

**Exact locator:** DS1 revision 18, Table Ia for the lower bound and Table Ib for the improved upper bound; Exoo's R(4,6) collection.

**Potential difficulty:** High. The unrestricted target is a research frontier; a bounded trial has no assured outcome.

**Possible AI role:** No named model evaluated; assumes tool-using AI with exact graph algorithms, SAT encodings and reproducible solver inputs. The proposed bounded construction trial has reusable attributed seeds and a transparent independent checker. The recommendation concerns reviewability and controlled scope, not an expectation of solving the full problem.

**Verification burden:** Low. A positive graph has a transparent exhaustive checker; this rating does not apply to a global impossibility claim.

**Resource expectations:** Experiment: None. Data: The 37 attributed graph files linked by SRC-MATH-203. Their source and content identifiers should accompany any extension result. Computation: Proposed cap: 8 CPU-hours and 16 GiB RAM for all seeds together. The witness has 630 possible edges; independent brute-force verification examines C(36,4)=58,905 four-sets and C(36,6)=1,947,792 six-sets. Search and global nonexistence can be far more expensive.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No model or seed neighborhood has been tested. Existing expert searches may already have covered these neighborhoods, and success within the proposed cap is unknown.

[Read the full card](../cards/Q-MATH-204.md). **Human review:** Pending.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
