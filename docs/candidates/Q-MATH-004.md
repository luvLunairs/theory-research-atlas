# Determine the two-color Ramsey number R(5,5)

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MATH-004 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MATH-004%3A+Determine+the+two-color+Ramsey+number+R%285%2C5%29&target=Q-MATH-004) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MATH-004%3A+Determine+the+two-color+Ramsey+number+R%285%2C5%29&target=Q-MATH-004)

Determine the least N such that every red/blue coloring of the edges of K_N has a monochromatic K5.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Open after scoped check. **Last checked:** 2026-11-06.

**Status basis:** Radziszowski's April 2026 survey and Angeltveit-McKay v2 give 43 <= R(5,5) <= 46. The scoped update search found no accepted exact value. The conjectured value 43 is not established.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** DS1.18: 24 April 2026, versioned PDF inspected; upper-bound preprint v2: 1 September 2025.

**Scope limits:** Compared the precise two-color target with the primary upper-bound paper and the versioned 2026 survey. A valid coloring is a lower-bound witness; an upper bound requires complete exclusion.

**Information still needed**

- Check all current bounds again before claiming an improvement.
- An exhaustive upper-bound computation needs complete case coverage and independently reproducible certificates.

**Primary branch:** [Extremal and Ramsey theory](../domains/math.md#math-comb-ext). **Related branches:** [Algorithms and data structures](../domains/cs.md#cs-alg).

**Sources:** [Small Ramsey Numbers, Dynamic Survey DS1, revision 18](../sources.md#src-math-001); [R(5,5) <= 46](../sources.md#src-math-802).

**Exact locator:** DS1.18 Section 2.1(e), Table Ib; Angeltveit-McKay v2, Theorem 1.1 and Section 1

**Potential difficulty:** Unknown. No separate difficulty review of this exact statement is recorded. Its origin or current status does not establish tractability.

**Possible AI role:** A tool-using mathematical assistant could compare hypotheses, locate relevant results and propose a narrower proof, construction or counterexample task; a specialist must first select and check that task.

**Verification burden:** Unknown. The statement and source need a task-specific proof or certificate plan before an attempt.

**Resource expectations:** No run estimate is available. Decide data, computation and experiment requirements after selecting a concrete approach.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No named model has been evaluated on this target; AI usefulness and success probability remain unmeasured.

**Further work:** define a scoped target, resource requirements and a verification plan before developing a full card. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-06

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Source reports open → Open after scoped check.

Replace the unspecified gap with a sourced interval; retain openness within the search scope.

**Search scope:** Compared the precise two-color target with the primary upper-bound paper and the versioned 2026 survey. A valid coloring is a lower-bound witness; an upper bound requires complete exclusion.

**Inspected evidence**

- [Small Ramsey Numbers, Dynamic Survey DS1, revision 18](../sources.md#src-math-001) — Revision 18, Section 2.1(e); Table Ib. Retains a nonzero bound gap and distinguishes the conjectured exact value.
- [R(5,5) <= 46](../sources.md#src-math-802) — Theorem 1.1; Section 1. Proves the upper bound 46 and records the lower bound 43.

**Limits and remaining work**

- The search is scoped, not exhaustive.
- No independent proof, numerical replay or formal verification was performed.
- Human review remains pending.

<details>
<summary>Search queries</summary>

- "R(5,5)" "2026" 43
- "R(5,5)" "46" Angeltveit McKay arxiv


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
