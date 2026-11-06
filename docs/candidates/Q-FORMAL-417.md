# Polynomial separation bounds for sums of square roots

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-417 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-417%3A+Polynomial+separation+bounds+for+sums+of+square+roots&target=Q-FORMAL-417) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-417%3A+Polynomial+separation+bounds+for+sums+of+square+roots&target=Q-FORMAL-417)

Let r(n,k) be the least positive absolute difference between two sums of k square roots of nonnegative integers at most n. Is log(1/r(n,k)) polynomially bounded in k and log n?

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Open after scoped check. **Last checked:** 2026-11-06.

**Status basis:** The 2024 paper retains the separation problem and gives an improved fixed-radicand bound with an ineffective constant. The September 2026 preprint reports an explicit improvement whose exponent still grows exponentially with the number of independent radicals. The scoped search found no accepted uniform polynomial separation bound or disproof.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** TOPP revision: 9 September 2009; SoCG paper: 6 June 2024; inspected arXiv version 2: 21 September 2026.

**Scope limits:** The target is uniform in both k and the radicand bound n. Fixed-radicand constants are insufficient; the 2026 theorem has explicit independence and coefficient hypotheses. A negative separation answer would not by itself rule out every polynomial-time sign algorithm.

**Information still needed**

- Later uniform separation improvements or counterexamples outside the scoped search.
- Independent assessment of the 2026 preprint and any subsequent revisions.

**Primary branch:** [Computational geometry and topology](../domains/cs.md#cs-geom). **Related branches:** None recorded.

**Sources:** [The Open Problems Project: Problem 33](../sources.md#src-formal-417); [An Improved Bound on Sums of Square Roots via the Subspace Theorem](../sources.md#src-math-703); [Quantitative linear independence for square roots](../sources.md#src-math-704).

**Exact locator:** TOPP Problem 33: Statement and Motivation; Eisenbrand et al. (2024), Theorem 6; Aymone et al., version 2 (2026), Theorem 1.1 and Corollary 1.2

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

**Recorded status:** Unverified → Open after scoped check.

Retain the exact uniform separation question, add the newer bounds and their limitations, and record scoped openness rather than treating either improvement as a resolution.

**Search scope:** Compared TOPP's uniform precision question with the full SoCG 2024 paper and the latest displayed arXiv version of the 2026 bound; checked theorem hypotheses, version history and targeted update queries.

**Inspected evidence**

- [The Open Problems Project: Problem 33](../sources.md#src-formal-417) — Statement; Motivation. Defines the uniform separation target and explains its relation, but not equivalence, to polynomial-time sign computation.
- [An Improved Bound on Sums of Square Roots via the Subspace Theorem](../sources.md#src-math-703) — Section 1; Theorem 6, page 54:5. The improved bound contains a radicand-dependent constant; its value is not effective.
- [Quantitative linear independence for square roots](../sources.md#src-math-704) — Theorem 1.1; Corollary 1.2; Proposition 2.2. The strengthened version assumes K >= 8 and nonzero coefficients, retains an exponential exponent, and supplies a weaker bound for smaller K.

**Limits and remaining work**

- No independent proof audit of the cited bounds.
- The search cannot exclude additional or forthcoming results.
- Human review remains pending.

<details>
<summary>Search queries</summary>

- "square roots" "separation" "2026" sums
- sum square roots separation bound 2025 2026 arxiv polynomial
- "2609.14161" correction OR erratum OR revised
- "Quantitative linear independence for square roots" correction


</details>

### 2026-10-14

**Coverage:** Statement only. **Statement:** Matched.

**Recorded status:** Unverified → Unverified.

The source supports identifying this question, but does not establish its present unresolved status.

**Search scope:** Inspected the named source statement and its recorded qualifications; no comprehensive citation-chain or specialist database review.

**Inspected evidence**

- [The Open Problems Project: Problem 33](../sources.md#src-formal-417) — TOPP Problem 33: Statement; Motivation. The source identifies the indexed question or research direction; its original date and any recorded partial results limit what it establishes about present status.

**Limits and remaining work**

- Later separation bounds; a negative answer would not exclude all polynomial-time sign algorithms.
- Current resolution status was not established by a completed later-literature review.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
