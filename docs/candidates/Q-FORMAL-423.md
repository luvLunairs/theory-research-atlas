# Linear-size universal point sets for planar straight-line drawings

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-423 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-423%3A+Linear-size+universal+point+sets+for+planar+straight-line+drawings&target=Q-FORMAL-423) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-423%3A+Linear-size+universal+point+sets+for+planar+straight-line+drawings&target=Q-FORMAL-423)

For every n, does some O(n)-point planar set support a crossing-free straight-line drawing of every n-vertex planar graph, with graph vertices on a subset of the points?

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-11-06.

**Status basis:** TOPP asks for O(n) universal sets. Gordon's September 2026 preprint reports n exp(O(sqrt(log n))) points and explicitly leaves O(n) open. The new asymptotic claim has not been independently assessed by the project.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** TOPP substantive revision: 2010; Gordon v1: 10 September 2026.

**Scope limits:** Compared the universal straight-line embedding target and its quantifiers with the reported near-linear bound. A bound on point count is separate from coordinate bit length or drawing area.

**Information still needed**

- Independent assessment and later revisions of the near-linear construction.
- An exact O(n) upper bound or superlinear lower bound remains distinct from the reported result.

**Primary branch:** [Computational geometry and topology](../domains/cs.md#cs-geom). **Related branches:** None recorded.

**Sources:** [The Open Problems Project: Problem 45](../sources.md#src-formal-423); [Almost Linear Universal Point Sets for Planar Graphs](../sources.md#src-math-804).

**Exact locator:** TOPP Problem 45, Statement; Gordon, Theorem 1.1 and Appendix A.3

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

Record the substantial reported improvement while keeping the exact linear-size target separate.

**Search scope:** Compared the universal straight-line embedding target and its quantifiers with the reported near-linear bound. A bound on point count is separate from coordinate bit length or drawing area.

**Inspected evidence**

- [The Open Problems Project: Problem 45](../sources.md#src-formal-423) — Statement. Asks whether one O(n)-point set works for every n-vertex planar graph.
- [Almost Linear Universal Point Sets for Planar Graphs](../sources.md#src-math-804) — Theorem 1.1; Appendix A.3. Claims a subpolynomial factor above linear size and explicitly excludes a coordinate-size guarantee.

**Limits and remaining work**

- The search is scoped, not exhaustive.
- No independent proof, numerical replay or formal verification was performed.
- Human review remains pending.

<details>
<summary>Search queries</summary>

- "universal point sets" "2026" "linear"
- "2609.10916" correction OR erratum


</details>

### 2026-10-14

**Coverage:** Statement only. **Statement:** Matched.

**Recorded status:** Unverified → Unverified.

The source supports identifying this question, but does not establish its present unresolved status.

**Search scope:** Inspected the named source statement and its recorded qualifications; no comprehensive citation-chain or specialist database review.

**Inspected evidence**

- [The Open Problems Project: Problem 45](../sources.md#src-formal-423) — TOPP Problem 45: Statement. The source identifies the indexed question or research direction; its original date and any recorded partial results limit what it establishes about present status.

**Limits and remaining work**

- Later universal-point-set bounds; bends and curved edges are excluded.
- Current resolution status was not established by a completed later-literature review.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
