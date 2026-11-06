# Time-optimal steering with bounded angular acceleration

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-CROSS-412 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-CROSS-412%3A+Time-optimal+steering+with+bounded+angular+acceleration&target=Q-CROSS-412) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-CROSS-412%3A+Time-optimal+steering+with+bounded+angular+acceleration&target=Q-CROSS-412)

For x-dot=cos(theta), y-dot=sin(theta), theta-dot=omega and omega-dot=u with |u|<=1 on R^2 x S^1 x R, fix a terminal state q_bar and construct a time-optimal trajectory and control from every initial state q to q_bar. Angular velocity is unrestricted; angular acceleration is bounded.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Unverified. **Last checked:** 2026-11-06.

**Status basis:** The original ideal no-skidding model requires a global synthesis, including possible chattering. Bazzi, Shammas and Asmar (2017) instead relax no-skidding and study small skid angles. That altered model does not resolve this target; its present status remains unverified here.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** The original problem is from 2002. The dated literature check identifies the later version inspected; neither access date nor a related theorem establishes current openness.

**Scope limits:** The angle is taken modulo 2 pi, while angular velocity is a real state. A finite collection of extremals, ordinary curvature-bounded Dubins paths or a skidding model does not by itself solve the stated synthesis.

**Information still needed**

- Check later global syntheses for the exact ideal-car dynamics, including singular arcs and chattering.
- A proposed restricted endpoint or control family needs its own provenance and novelty check.

**Primary branch:** [Control, estimation and systems theory](../domains/eng.md#eng-control). **Related branches:** None recorded.

**Sources:** [2002 MTNS Problem Book: Open Problems on the Mathematical Theory of Systems](../sources.md#src-cross-401); [Relaxing Nonholonomic Constraints to Eliminate Chattering From Time-Optimal Control Solutions](../sources.md#src-cross-802).

**Exact locator:** Problem 9, section 9.1, pp. 147–149; Ugo Boscain and Benedetto Piccoli

**Potential difficulty:** High. The general formulation requires specialist control or operator theory, and local computations do not settle the universal claim.

**Possible AI role:** AI could search extremals and verify symbolic necessary conditions, with human review of global optimality. This assumes a system capable of reading the relevant literature, writing reproducible code and exposing its calculations for specialist review.

**Verification burden:** High. Match the state space, endpoint conditions and acceleration constraint, then prove global minimality. Necessary extremal equations and numerically truncated switching sequences are insufficient.

**Resource expectations:** No physical experiment or observational dataset is needed for the mathematical claim. Symbolic work and small simulations can start on ordinary hardware; general certification or global optimization may be expensive and has not been budgeted.

**Assessment:** 2026-11-06; untested forecast. **Uncertainty:** No model-specific attempt has been run. Later results, a more precise formulation and expert assessment may substantially change difficulty and relevance.

**Further work:** resolve the statement and status questions above before planning an attempt. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-06

**Coverage:** Statement and later literature. **Statement:** Corrected.

**Recorded status:** Unverified → Unverified.

The original ideal no-skidding model requires a global synthesis, including possible chattering. Bazzi, Shammas and Asmar (2017) instead relax no-skidding and study small skid angles. That altered model does not resolve this target; its present status remains unverified here.

**Search scope:** Inspected the original formulation in the editor-hosted MTNS collection and the identified later paper. Targeted searches compared model assumptions and the claimed output; this is not an exhaustive status review.

<details>
<summary>Previous indexed wording</summary>

For x-dot=cos(theta), y-dot=sin(theta), theta-dot=omega and omega-dot=u, |u|<=1, construct global time-optimal steering to a fixed state.

The current statement appears at the top of this page.
</details>

**Inspected evidence**

- [2002 MTNS Problem Book: Open Problems on the Mathematical Theory of Systems](../sources.md#src-cross-401) — Problem 9, section 9.1, pp. 147–149; Ugo Boscain and Benedetto Piccoli. Checked the original assumptions and target.
- [Relaxing Nonholonomic Constraints to Eliminate Chattering From Time-Optimal Control Solutions](../sources.md#src-cross-802) — IEEE Robotics and Automation Letters 2(3), 1817-1824; abstract and Sections I-II; DOI 10.1109/LRA.2017.2708162. The abstract and model comparison explicitly change the no-skidding constraint; the small-skid-angle synthesis belongs to that different system.

**Limits and remaining work**

- Check later global syntheses for the exact ideal-car dynamics, including singular arcs and chattering.
- A proposed restricted endpoint or control family needs its own provenance and novelty check.
- No independent proof audit or comprehensive present-status assessment was performed.

<details>
<summary>Search queries</summary>

- "Boscain" "Piccoli" "angular acceleration" optimal synthesis
- "Dubins" "angular acceleration" synthesis chattering 2025
- "Dubins" "angular acceleration" "synthesis" 2026


</details>

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
