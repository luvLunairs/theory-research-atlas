# Time-optimal steering with bounded angular acceleration

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-CROSS-412 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-CROSS-412%3A+Time-optimal+steering+with+bounded+angular+acceleration&target=Q-CROSS-412) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-CROSS-412%3A+Time-optimal+steering+with+bounded+angular+acceleration&target=Q-CROSS-412)

For x-dot=cos(theta), y-dot=sin(theta), theta-dot=omega and omega-dot=u, |u|<=1, construct global time-optimal steering to a fixed state.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Unverified. **Last checked:** 2026-10-14.

**Status basis:** The source system bounds angular acceleration, not curvature alone. A Dubins or Reeds–Shepp synthesis cannot be transferred without proving equivalence. No global solution of this exact system was confirmed.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Recorded source years: SRC-CROSS-401: 2002. Later evidence is limited to the passages in the dated literature check; an access date does not refresh a historical claim.

**Scope limits:** The source system bounds angular acceleration, not curvature alone. A Dubins or Reeds–Shepp synthesis cannot be transferred without proving equivalence. No global solution of this exact system was confirmed.

**Information still needed**

- Check the role of singular arcs and chattering, and specify the angular-state convention and terminal state.
- Specialist assessment of the exact formulation and remaining novelty is pending.

**Primary branch:** [Control, estimation and systems theory](../domains/eng.md#eng-control). **Related branches:** None recorded.

**Sources:** [2002 MTNS Problem Book: Open Problems on the Mathematical Theory of Systems](../sources.md#src-cross-401).

**Exact locator:** Problem 9, section 9.1, pp. 147–149; Ugo Boscain and Benedetto Piccoli

**Potential difficulty:** High. The general formulation requires specialist control or operator theory, and local computations do not settle the universal claim.

**Possible AI role:** AI could search extremals and verify symbolic necessary conditions, with human review of global optimality. This assumes a system capable of reading the relevant literature, writing reproducible code and exposing its calculations for specialist review.

**Verification burden:** High. Check all hypotheses, global quantifiers and any exact certificates independently; simulated stability alone is insufficient.

**Resource expectations:** No physical experiment or observational dataset is needed for the mathematical claim. Symbolic work and small simulations can start on ordinary hardware; general certification or global optimization may be expensive and has not been budgeted.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No model-specific attempt has been run. Later results, a more precise formulation and expert assessment may substantially change difficulty and relevance.

**Further work:** resolve the statement and status questions above before planning an attempt. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-10-14

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Unverified.

The source system bounds angular acceleration, not curvature alone. A Dubins or Reeds–Shepp synthesis cannot be transferred without proving equivalence. No global solution of this exact system was confirmed.

**Search scope:** Compared the original MTNS formulation with targeted name-and-model searches; inspected the later passages listed below. This is a bounded literature check.

**Inspected evidence**

- [2002 MTNS Problem Book: Open Problems on the Mathematical Theory of Systems](../sources.md#src-cross-401) — Problem 9, section 9.1, pp. 147–149; Ugo Boscain and Benedetto Piccoli. Identifies the historical target.

**Limits and remaining work**

- Check the role of singular arcs and chattering, and specify the angular-state convention and terminal state.
- This check is not an independent proof audit or an exhaustive review of all later literature.

<details>
<summary>Search queries</summary>

- "Boscain" "Piccoli" "angular acceleration" optimal synthesis


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
