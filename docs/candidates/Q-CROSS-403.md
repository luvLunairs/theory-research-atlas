# Regular feedback implementability of behaviors

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-CROSS-403 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-CROSS-403%3A+Regular+feedback+implementability+of+behaviors&target=Q-CROSS-403) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-CROSS-403%3A+Regular+feedback+implementability+of+behaviors&target=Q-CROSS-403)

Given a linear differential plant behavior on variables (w,c) and a desired behavior K on w, characterize controllers on c whose partial interconnection projects to K and satisfies both output-cardinality additivity and McMillan-degree additivity.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Unverified. **Last checked:** 2026-10-14.

**Status basis:** The original problem allows only partial interconnection. The 2010 paper solves the full-interconnection case and gives qualified partial-interconnection results; a general resolution of the original target has not been established here.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Recorded source years: SRC-CROSS-401: 2002; SRC-CROSS-602: 2010. Later evidence is limited to the passages in the dated literature check; an access date does not refresh a historical claim.

**Scope limits:** The original problem allows only partial interconnection. The 2010 paper solves the full-interconnection case and gives qualified partial-interconnection results; a general resolution of the original target has not been established here.

**Information still needed**

- Determine whether later work gives a complete test for the desired projected behavior under partial interconnection.
- Specialist assessment of the exact formulation and remaining novelty is pending.

**Primary branch:** [Control, estimation and systems theory](../domains/eng.md#eng-control). **Related branches:** None recorded.

**Sources:** [2002 MTNS Problem Book: Open Problems on the Mathematical Theory of Systems](../sources.md#src-cross-401); [Impulse free interconnection of dynamical systems](../sources.md#src-cross-602).

**Exact locator:** Problem 69, section 69.1, pp. 9–12; H. L. Trentelman

**Potential difficulty:** High. The general formulation requires specialist control or operator theory, and local computations do not settle the universal claim.

**Possible AI role:** AI could derive elimination conditions and check candidate counterexamples by polynomial algebra. This assumes a system capable of reading the relevant literature, writing reproducible code and exposing its calculations for specialist review.

**Verification burden:** High. Check all hypotheses, global quantifiers and any exact certificates independently; simulated stability alone is insufficient.

**Resource expectations:** No physical experiment or observational dataset is needed for the mathematical claim. Symbolic work and small simulations can start on ordinary hardware; general certification or global optimization may be expensive and has not been budgeted.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No model-specific attempt has been run. Later results, a more precise formulation and expert assessment may substantially change difficulty and relevance.

**Further work:** resolve the statement and status questions above before planning an attempt. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-10-14

**Coverage:** Statement and later literature. **Statement:** Corrected.

**Recorded status:** Unverified → Unverified.

The original problem allows only partial interconnection. The 2010 paper solves the full-interconnection case and gives qualified partial-interconnection results; a general resolution of the original target has not been established here.

**Search scope:** Compared the original MTNS formulation with targeted name-and-model searches; inspected the later passages listed below. This is a bounded literature check.

<details>
<summary>Previous indexed wording</summary>

Which linear differential behaviors can a given plant realize through regular feedback interconnection?

The current statement appears at the top of this page.
</details>

**Inspected evidence**

- [2002 MTNS Problem Book: Open Problems on the Mathematical Theory of Systems](../sources.md#src-cross-401) — Problem 69, section 69.1, pp. 9–12; H. L. Trentelman. Identifies the historical target.
- [Impulse free interconnection of dynamical systems](../sources.md#src-cross-602) — Theorem 4.2, sections 4.1 and 6–7, and concluding discussion on p. 658; Linear Algebra and its Applications 432, 637–660. The conclusion explicitly leaves necessary and sufficient conditions for partial interconnection for further investigation.

**Limits and remaining work**

- Determine whether later work gives a complete test for the desired projected behavior under partial interconnection.
- This check is not an independent proof audit or an exhaustive review of all later literature.

<details>
<summary>Search queries</summary>

- "regular feedback implementability" solved


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
