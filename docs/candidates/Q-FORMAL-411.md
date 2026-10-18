# Subquadratic minimum-link paths among planar obstacles

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-411 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-411%3A+Subquadratic+minimum-link+paths+among+planar+obstacles&target=Q-FORMAL-411) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-411%3A+Subquadratic+minimum-link+paths+among+planar+obstacles&target=Q-FORMAL-411)

Can a path with the fewest straight segments between specified points among polygonal planar obstacles be found in subquadratic time in the input size?

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Unverified. **Last checked:** 2026-10-14.

**Status basis:** The later Minimum-Link Paths Revisited paper establishes 3SUM-hardness for the exact unrestricted-orientation problem and subquadratic approximation algorithms. This supplies an important conditional barrier but does not by itself settle the literal unconditional algorithmic question; current status remains unverified.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Latest displayed substantive revision: 2001.

**Scope limits:** This is a source-defined research question, not a claim that a solution or a manageable research route is known.

**Information still needed**

- Specify whether subquadratic means o(n^2) or O(n^(2-epsilon)) and the computational model; review newer 3SUM reductions and algorithms.

**Primary branch:** [Computational geometry and topology](../domains/cs.md#cs-geom). **Related branches:** None recorded.

**Sources:** [The Open Problems Project: Problem 22](../sources.md#src-formal-411); [Minimum-Link Paths Revisited](../sources.md#src-formal-612).

**Exact locator:** TOPP Problem 22: Statement

**Potential difficulty:** Unknown. The source identifies an unresolved research target; its present difficulty has not been independently assessed.

**Possible AI role:** After the computational model and current status are checked, generate small geometric instances, inspect exact witnesses and assist with combinatorial or algebraic lemmas. Finite tests do not establish asymptotic complexity or universal existence.

**Verification burden:** High. Review geometric degeneracies, exact arithmetic, admissible constructions and model-dependent running time; floating-point drawings alone are not certificates.

**Resource expectations:** No physical experiment or external dataset is intrinsic. Exact geometry and combinatorial enumeration may be expensive; useful instance sizes remain unestimated.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No model has been tested. Current status, useful subcases and feasible computational scale require further review.

**Further work:** resolve the statement and status questions above before planning an attempt. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-10-14

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Unverified.

The later Minimum-Link Paths Revisited paper establishes 3SUM-hardness for the exact unrestricted-orientation problem and subquadratic approximation algorithms. This supplies an important conditional barrier but does not by itself settle the literal unconditional algorithmic question; current status remains unverified.

**Search scope:** Matched the exact unrestricted-orientation target against the later hardness and approximation claims; did not treat approximation as exact solution.

**Inspected evidence**

- [The Open Problems Project: Problem 22](../sources.md#src-formal-411) — TOPP Problem 22: Statement. The source identifies the indexed question or research direction; its original date and any recorded partial results limit what it establishes about present status.
- [Minimum-Link Paths Revisited](../sources.md#src-formal-612) — Abstract; introduction. Exact link distance is 3SUM-hard; the subquadratic algorithms have approximation guarantees.

**Limits and remaining work**

- Specify whether subquadratic means o(n^2) or O(n^(2-epsilon)) and the computational model; review newer 3SUM reductions and algorithms.

<details>
<summary>Search queries</summary>

- "minimum-link" "subquadratic" 2025 2026
- "minimum-link path" "subquadratic"


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
