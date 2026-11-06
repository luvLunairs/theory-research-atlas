# Logarithmic-time fully dynamic planar nearest neighbors

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-430 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-430%3A+Logarithmic-time+fully+dynamic+planar+nearest+neighbors&target=Q-FORMAL-430) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-430%3A+Logarithmic-time+fully+dynamic+planar+nearest+neighbors&target=Q-FORMAL-430)

Can a data structure maintain planar Euclidean points under insertions, deletions and exact nearest-neighbor queries in O(log n) time per operation? State worst-case, amortized and randomization guarantees.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-11-06.

**Status basis:** TOPP records the fully dynamic logarithmic target as open. The inspected SoCG 2025 theorem achieves O(log n) queries with O(log^3 n) amortized insertions, but has no deletion operation. The scoped search did not establish a resolution of the original all-operation target.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** TOPP: 24 January 2006; conference paper: SoCG 2025.

**Scope limits:** Compared TOPP's exact planar Euclidean target with the published insertion-only theorem. Approximate, incremental and fully dynamic data structures answer different questions.

**Information still needed**

- Check later full-version tradeoffs and choose deterministic/randomized and worst-case/amortized guarantees before an attempt.

**Primary branch:** [Computational geometry and topology](../domains/cs.md#cs-geom). **Related branches:** None recorded.

**Sources:** [The Open Problems Project: Problem 63](../sources.md#src-formal-429); [Incremental Planar Nearest Neighbor Queries with Optimal Query Time](../sources.md#src-math-803).

**Exact locator:** TOPP Problem 63, Statement; Iacono-Nekrich, Theorem 12

**Potential difficulty:** Unknown. The source identifies an unresolved research target; its present difficulty has not been independently assessed.

**Possible AI role:** After the computational model and current status are checked, generate small geometric instances, inspect exact witnesses and assist with combinatorial or algebraic lemmas. Finite tests do not establish asymptotic complexity or universal existence.

**Verification burden:** High. Review geometric degeneracies, exact arithmetic, admissible constructions and model-dependent running time; floating-point drawings alone are not certificates.

**Resource expectations:** No physical experiment or external dataset is intrinsic. Exact geometry and combinatorial enumeration may be expensive; useful instance sizes remain unestimated.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No model has been tested. Current status, useful subcases and feasible computational scale require further review.

**Further work:** define a scoped target, resource requirements and a verification plan before developing a full card. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-06

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Source reports open.

Add the published partial result without conflating insertion-only operation with the fully dynamic target.

**Search scope:** Compared TOPP's exact planar Euclidean target with the published insertion-only theorem. Approximate, incremental and fully dynamic data structures answer different questions.

**Inspected evidence**

- [The Open Problems Project: Problem 63](../sources.md#src-formal-429) — Statement. Requires insertion, deletion and exact nearest-neighbor queries.
- [Incremental Planar Nearest Neighbor Queries with Optimal Query Time](../sources.md#src-math-803) — Theorem 12. Gives logarithmic queries with amortized cubic-logarithmic insertions and no deletions.

**Limits and remaining work**

- The search is scoped, not exhaustive.
- No independent proof, numerical replay or formal verification was performed.
- Human review remains pending.

<details>
<summary>Search queries</summary>

- "logarithmic-time" "fully dynamic" "nearest" 2026
- "fully dynamic" "nearest neighbor" "2026" logarithmic


</details>

### 2026-10-14

**Coverage:** Statement only. **Statement:** Matched.

**Recorded status:** Unverified → Unverified.

The source supports identifying this question, but does not establish its present unresolved status.

**Search scope:** Inspected the named source statement and its recorded qualifications; no comprehensive citation-chain or specialist database review.

**Inspected evidence**

- [The Open Problems Project: Problem 63](../sources.md#src-formal-429) — TOPP Problem 63: Statement. The source identifies the indexed question or research direction; its original date and any recorded partial results limit what it establishes about present status.

**Limits and remaining work**

- Later tradeoffs and the exact intended time guarantee.
- Current resolution status was not established by a completed later-literature review.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
