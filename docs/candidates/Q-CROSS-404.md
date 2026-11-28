# Dwell-time dependence of switched-system gain

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-CROSS-404 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-CROSS-404%3A+Dwell-time+dependence+of+switched-system+gain&target=Q-CROSS-404) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-CROSS-404%3A+Dwell-time+dependence+of+switched-system+gain&target=Q-CROSS-404)

Given continuous-time switched linear realizations with Hurwitz mode matrices, start at zero state and allow all piecewise-constant signals with minimum time τ between consecutive switches. Determine the induced L² gain g(τ), the supremum of the output-to-input L² norm ratio over these signals and nonzero inputs, allowing infinite gain.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Unverified. **Last checked:** 2026-11-28.

**Status basis:** Hespanha gives a method for the slow-switching limit, which can exceed the largest single-mode gain. Chitour, Mason and Sigalotti give a finiteness criterion under their hypotheses and prove right-continuity of the gain for bounded mode families with output y = Cx. These results leave computation of the full finite-dwell-time curve unresolved in the inspected sources.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** The 28 November 2026 check covers the works and passages listed in the literature record.

**Scope limits:** The original realizations may contain direct feedthrough. Proposition 32 is stated for y = Cx with bounded mode triples. The slow-switching limit, a bound at one dwell time and the exact curve are distinct objectives.

**Information still needed**

- Check any proposed algorithm on the original class, including the allowed output feedthrough and cases of infinite gain.

**Primary branch:** [Robust design and verification](../domains/eng.md#eng-robust). **Related branches:** None recorded.

**Sources:** [2002 MTNS Problem Book: Open Problems on the Mathematical Theory of Systems](../sources.md#src-cross-401); [A characterization of switched linear control systems with finite L2-gain](../sources.md#src-cross-603); [Root-Mean-Square Gains of Switched Linear Systems](../sources.md#src-phys-921).

**Exact locator:** Hespanha, MTNS Problem 28, sections 28.1–28.2. Chitour, Mason and Sigalotti, Theorem 25 and Proposition 32. Hespanha, slow-switching report.

**Potential difficulty:** High. The general formulation requires specialist control or operator theory, and local computations do not settle the universal claim.

**Possible AI role:** AI could generate switching certificates and compare rigorous gain bounds. This assumes a system capable of reading the relevant literature, writing reproducible code and exposing its calculations for specialist review.

**Verification burden:** High. Check all hypotheses, global quantifiers and any exact certificates independently; simulated stability alone is insufficient.

**Resource expectations:** No physical experiment or observational dataset is needed for the mathematical claim. Symbolic work and small simulations can start on ordinary hardware; general certification or global optimization may be expensive and has not been budgeted.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No model-specific attempt has been run. Later results, a more precise formulation and expert assessment may substantially change difficulty and relevance.

**Further work:** resolve the statement and status questions above before planning an attempt. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-28

**Coverage:** Statement and later literature. **Statement:** Corrected.

**Recorded status:** Unverified → Unverified.

Hespanha gives a method for the slow-switching limit, which can exceed the largest single-mode gain. Chitour, Mason and Sigalotti give a finiteness criterion under their hypotheses and prove right-continuity of the gain for bounded mode families with output y = Cx. These results leave computation of the full finite-dwell-time curve unresolved in the inspected sources.

**Search scope:** The original realizations may contain direct feedthrough. Proposition 32 is stated for y = Cx with bounded mode triples. The slow-switching limit, a bound at one dwell time and the exact curve are distinct objectives.

<details>
<summary>Previous indexed wording</summary>

Determine the worst-case L2 gain as a function of minimum switching dwell time.

The current statement appears at the top of this page.
</details>

**Inspected evidence**

- [2002 MTNS Problem Book: Open Problems on the Mathematical Theory of Systems](../sources.md#src-cross-401) — Problem 28, sections 28.1–28.2, equations (28.1)–(28.2). Specifies Hurwitz mode matrices, zero initial state, arbitrary square-integrable inputs and the minimum time between switches.
- [Root-Mean-Square Gains of Switched Linear Systems](../sources.md#src-phys-921) — Report dated 24 September 2002, abstract and sections 1 and 5. Provides a procedure for the slow-switching limit and relates it to the gain for a single switch.
- [A characterization of switched linear control systems with finite L2-gain](../sources.md#src-cross-603) — Theorem 25 and section IV-C, Proposition 32. Treats finiteness under additional hypotheses and proves right-continuity of the extended-valued gain for the stated bounded mode triples.

**Limits and remaining work**

- Check any proposed algorithm on the original class, including the allowed output feedthrough and cases of infinite gain.

<details>
<summary>Search queries</summary>

- Hespanha switched systems induced L2 gain minimum dwell time exact gain curve slow switching right continuity Proposition 32


</details>

### 2026-10-14

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Unverified.

Theorem 25 of the later paper gives a gain-finiteness criterion, with observability qualifications. It does not compute the full optimal dwell-time/gain curve requested by this entry.

**Search scope:** Compared the original MTNS formulation with targeted name-and-model searches; inspected the later passages listed below. This is a bounded literature check.

**Inspected evidence**

- [2002 MTNS Problem Book: Open Problems on the Mathematical Theory of Systems](../sources.md#src-cross-401) — Problem 28, section 28.2, pp. 45–47; João P. Hespanha. Identifies the historical target.
- [A characterization of switched linear control systems with finite L2-gain](../sources.md#src-cross-603) — Theorem 25 and Example 31; journal version IEEE TAC 62 (2017), DOI 10.1109/TAC.2016.2593678. Relates finite gain to growth of a minimal realization, with a special role for uniform observability.

**Limits and remaining work**

- Check later algorithms for the exact gain curve and boundary cases where uniform observability fails.
- This check is not an independent proof audit or an exhaustive review of all later literature.

<details>
<summary>Search queries</summary>

- "dwell time" "L2 gain" switched systems "open" Hespanha


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
