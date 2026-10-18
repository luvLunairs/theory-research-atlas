# Dwell-time dependence of switched-system gain

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-CROSS-404 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-CROSS-404%3A+Dwell-time+dependence+of+switched-system+gain&target=Q-CROSS-404) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-CROSS-404%3A+Dwell-time+dependence+of+switched-system+gain&target=Q-CROSS-404)

Determine the worst-case L2 gain as a function of minimum switching dwell time.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Unverified. **Last checked:** 2026-10-14.

**Status basis:** Theorem 25 of the later paper gives a gain-finiteness criterion, with observability qualifications. It does not compute the full optimal dwell-time/gain curve requested by this entry.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Recorded source years: SRC-CROSS-401: 2002; SRC-CROSS-603: 2015. Later evidence is limited to the passages in the dated literature check; an access date does not refresh a historical claim.

**Scope limits:** Theorem 25 of the later paper gives a gain-finiteness criterion, with observability qualifications. It does not compute the full optimal dwell-time/gain curve requested by this entry.

**Information still needed**

- Check later algorithms for the exact gain curve and boundary cases where uniform observability fails.
- Specialist assessment of the exact formulation and remaining novelty is pending.

**Primary branch:** [Robust design and verification](../domains/eng.md#eng-robust). **Related branches:** None recorded.

**Sources:** [2002 MTNS Problem Book: Open Problems on the Mathematical Theory of Systems](../sources.md#src-cross-401); [A characterization of switched linear control systems with finite L2-gain](../sources.md#src-cross-603).

**Exact locator:** Problem 28, section 28.2, pp. 45–47; João P. Hespanha

**Potential difficulty:** High. The general formulation requires specialist control or operator theory, and local computations do not settle the universal claim.

**Possible AI role:** AI could generate switching certificates and compare rigorous gain bounds. This assumes a system capable of reading the relevant literature, writing reproducible code and exposing its calculations for specialist review.

**Verification burden:** High. Check all hypotheses, global quantifiers and any exact certificates independently; simulated stability alone is insufficient.

**Resource expectations:** No physical experiment or observational dataset is needed for the mathematical claim. Symbolic work and small simulations can start on ordinary hardware; general certification or global optimization may be expensive and has not been budgeted.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No model-specific attempt has been run. Later results, a more precise formulation and expert assessment may substantially change difficulty and relevance.

**Further work:** resolve the statement and status questions above before planning an attempt. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

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
