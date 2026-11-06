# Mismatch-capacity formula

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-454 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-454%3A+Mismatch-capacity+formula&target=Q-FORMAL-454) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-454%3A+Mismatch-capacity+formula&target=Q-FORMAL-454)

Find a general single-letter characterization of the capacity of a discrete memoryless channel under a prescribed additive decoding metric when the decoder selects a maximum-metric codeword. State the error criterion and tie convention; stochastic likelihood decoding is a different problem.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-11-06.

**Status basis:** The October 2026 revision explicitly retains the lack of a general single-letter formula for maximum-metric mismatch capacity. Its stochastic-decoder results concern a different decision rule and do not resolve that target.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Original problem source: 2022; inspected primary revision: 30 October 2026.

**Scope limits:** Checked the distinction between selecting a maximizing codeword and sampling a message in proportion to its metric. A multi-letter limit is not a single-letter characterization.

**Information still needed**

- Fix the source's error criterion and tie convention for a concrete theorem.
- Check later versions before asserting a new general formula.

**Primary branch:** [Classical information theory](../domains/info.md#info-shannon). **Related branches:** None recorded.

**Sources:** [New Mathematical Techniques in Information Theory](../sources.md#src-formal-445); [Mismatch Capacity under Stochastic Decoding](../sources.md#src-formal-614); [Mismatch Capacity under Stochastic Decoding](../sources.md#src-math-809).

**Exact locator:** MFO 2022 report, p. 699; Molina-Guillén i Fàbregas v2, Section I, equations (1)-(2)

**Potential difficulty:** Unknown. The source identifies an unresolved research target; its present difficulty has not been independently assessed.

**Possible AI role:** After operational conventions are fixed, explore small-alphabet examples, compare inner and outer bounds and assist with entropy calculations. Numerical optimization cannot establish a capacity formula.

**Verification burden:** High. Achievability and converse arguments must match channel, coding, error and asymptotic conventions; local numerical extrema are insufficient.

**Resource expectations:** No physical channel experiment is required for the formal question. Alphabet optimization and symbolic calculations may be costly; no resource bound is established.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No model has been tested. Current status, useful subcases and feasible computational scale require further review.

**Further work:** define a scoped target, resource requirements and a verification plan before developing a full card. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-06

**Coverage:** Statement and later literature. **Statement:** Corrected.

**Recorded status:** Source reports open → Source reports open.

Make the decoder restriction explicit and retain both source versions.

**Search scope:** Checked the distinction between selecting a maximizing codeword and sampling a message in proportion to its metric. A multi-letter limit is not a single-letter characterization.

<details>
<summary>Previous indexed wording</summary>

Find a single-letter characterization of discrete memoryless channel capacity under a prescribed additive decoding metric.

The current statement appears at the top of this page.
</details>

**Inspected evidence**

- [Mismatch Capacity under Stochastic Decoding](../sources.md#src-math-809) — Section I, equations (1)-(2) and following discussion. Maximum-metric capacity remains unresolved in single-letter form; the stochastic likelihood rule is introduced separately.

**Limits and remaining work**

- The search is scoped, not exhaustive.
- No independent proof, numerical replay or formal verification was performed.
- Human review remains pending.

<details>
<summary>Search queries</summary>

- "2604.17964" mismatch capacity correction


</details>

### 2026-10-14

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Source reports open.

The inspected 2026 paper explicitly says the general single-letter expression for maximum-metric mismatch capacity remains unavailable. Its new stochastic-decoder formula concerns a different decoding rule.

**Search scope:** Read the two decoding definitions and the introduction's explicit status discussion.

**Inspected evidence**

- [New Mathematical Techniques in Information Theory](../sources.md#src-formal-445) — p. 699, Anelia Somekh-Baruch. The source identifies the indexed question or research direction; its original date and any recorded partial results limit what it establishes about present status.
- [Mismatch Capacity under Stochastic Decoding](../sources.md#src-formal-614) — Introduction, equations (1)–(2). The positive stochastic-decoder result does not solve general maximum-metric mismatch capacity.

**Limits and remaining work**

- Review later work after the inspected 2026 manuscript; retain the decoder and tie-breaking conventions.

<details>
<summary>Search queries</summary>

- "mismatched decoding" "capacity" "2026" "open"


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
