# Quadratic-time sorting of pairwise sums

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-420 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-420%3A+Quadratic-time+sorting+of+pairwise+sums&target=Q-FORMAL-420) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-420%3A+Quadratic-time+sorting+of+pairwise+sums&target=Q-FORMAL-420)

For two n-element real sets X and Y, can all n^2 sums x+y be sorted in O(n^2) time in a standard real-comparison computation model? A comparison-count bound alone is insufficient.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Unverified. **Last checked:** 2026-11-06.

**Status basis:** TOPP records the historical open target, but Mundhra's April 2025 preprint explicitly claims quadratic total time. Independent validation and acceptance of that claim were not established. The claim is retained for assessment rather than silently treating the older open label as current or recording a resolution.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** TOPP revision: 20 August 2006; the arXiv record displays version 1, submitted 23 April 2025.

**Scope limits:** The target concerns a uniform total-time algorithm. Neither a quadratic comparison-count result nor the presence of a preprint claiming the target establishes its accepted resolution.

**Information still needed**

- Independent evaluation of the claimed quadratic total time, including comparison amortization and data-structure operations.
- Any accepted publication, correction or substantive independent assessment of the preprint.

**Primary branch:** [Computational geometry and topology](../domains/cs.md#cs-geom). **Related branches:** None recorded.

**Sources:** [The Open Problems Project: Problem 41](../sources.md#src-formal-420); [An Explicit and Efficient O(n^2)-Time Algorithm for Sorting Sumsets](../sources.md#src-math-700).

**Exact locator:** TOPP Problem 41: Statement and Partial and Related Results; Mundhra (2025), Theorem 1, Algorithm 1, Theorem 15 and Remark 19

**Potential difficulty:** Unknown. The source identifies an unresolved research target; its present difficulty has not been independently assessed.

**Possible AI role:** After the computational model and current status are checked, generate small geometric instances, inspect exact witnesses and assist with combinatorial or algebraic lemmas. Finite tests do not establish asymptotic complexity or universal existence.

**Verification burden:** High. Review geometric degeneracies, exact arithmetic, admissible constructions and model-dependent running time; floating-point drawings alone are not certificates.

**Resource expectations:** No physical experiment or external dataset is intrinsic. Exact geometry and combinatorial enumeration may be expensive; useful instance sizes remain unestimated.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No model has been tested. Current status, useful subcases and feasible computational scale require further review.

**Further work:** resolve the statement and status questions above before planning an attempt. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-06

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Unverified.

The later resolution claim changes the evidence that a researcher must examine. Keep the original target and unverified status until its correctness and acceptance can be assessed.

**Search scope:** Compared the historical TOPP target with the 2025 preprint's algorithm and stated analysis; checked its arXiv version history and searched for corrections and independent assessment.

**Inspected evidence**

- [The Open Problems Project: Problem 41](../sources.md#src-formal-420) — Statement; Partial and Related Results. Distinguishes quadratic comparisons from quadratic total running time.
- [An Explicit and Efficient O(n^2)-Time Algorithm for Sorting Sumsets](../sources.md#src-math-700) — Theorem 1; Algorithm 1; Theorem 15, Corollary 18 and Remark 19. Claims the exact time target and presents amortized comparison and container-cost arguments requiring independent assessment.

**Limits and remaining work**

- No independent proof verdict, implementation replay or complexity certification.
- No acceptance was established by this limited search; absence from the results is not evidence of rejection.
- Human review remains pending.

<details>
<summary>Search queries</summary>

- "X + Y" sorting "2026"
- "2504.16393" correction error sorting
- "2504.16393" correction OR error OR sorting
- "sumsets" "Mundhra" algorithm correction


</details>

### 2026-10-14

**Coverage:** Statement only. **Statement:** Matched.

**Recorded status:** Unverified → Unverified.

The source supports identifying this question, but does not establish its present unresolved status.

**Search scope:** Inspected the named source statement and its recorded qualifications; no comprehensive citation-chain or specialist database review. The listed targeted searches were exploratory; no verified later source establishing current resolution status was obtained.

**Inspected evidence**

- [The Open Problems Project: Problem 41](../sources.md#src-formal-420) — TOPP Problem 41: Statement; Partial and Related Results. The source identifies the indexed question or research direction; its original date and any recorded partial results limit what it establishes about present status.

**Limits and remaining work**

- Later uniform algorithms; the known quadratic comparison tree does not supply this time bound.
- Current resolution status was not established by a completed later-literature review.

<details>
<summary>Search queries</summary>

- "sorting X+Y" "2025" "2026"


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
