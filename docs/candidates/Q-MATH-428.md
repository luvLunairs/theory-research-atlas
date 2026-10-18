# Positive density of the classical Ulam sequence

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MATH-428 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MATH-428%3A+Positive+density+of+the+classical+Ulam+sequence&target=Q-MATH-428) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MATH-428%3A+Positive+density+of+the+classical+Ulam+sequence&target=Q-MATH-428)

Starting with u1=1,u2=2, choose each subsequent term as the least integer larger than the preceding term that has exactly one representation as the sum of two distinct earlier terms. Does this sequence have positive density?

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Unverified. **Last checked:** 2026-10-15.

**Status basis:** Agama's version 12 claims zero density, but its main argument uses an arbitrary-chain estimate that fails for the chain 1,2,...,N as written. This editorial observation needs specialist confirmation; the separate conditional argument is not audited. The density question remains unverified.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Green's list: December 2025. Agama version 12: 10 March 2026. Selected proof dependencies inspected on 15 October 2026.

**Scope limits:** A concern in a claimed proof does not establish the opposite density conclusion or certify that no other solution exists.

**Information still needed**

- Obtain specialist review of Proposition 3.6 and whether any corrected estimate applies to chains containing an Ulam prefix.
- Check the additional counting hypothesis in Section 6 rather than assuming the alternative argument is unconditional.
- Specify the intended density notion before formalizing a positive answer; the cited negative claim concerns natural density.

**Primary branch:** [Number theory and arithmetic geometry](../domains/math.md#math-num). **Related branches:** None recorded.

**Sources:** [100 Open Problems, December 2025 revision](../sources.md#src-math-302); [Ulam numbers have zero density (version 12)](../sources.md#src-math-409).

**Exact locator:** Green, Problem 7; Agama, version 12, Theorem 5.1.

**Potential difficulty:** Unknown. A claimed resolution is now part of the evidence. Difficulty of the original target and difficulty of checking that claim must be assessed separately; the claim has not been independently verified.

**Possible AI role:** Trace the two claimed density arguments and check their exact hypotheses. For the addition-chain argument, distinguish bounds for shortest chains from bounds for arbitrary chains containing a prescribed Ulam prefix.

**Verification burden:** High. The full proof, its assumptions, and any computational or formal artifacts require independent expert inspection; a matching abstract is insufficient.

**Resource expectations:** No physical experiment or empirical dataset is required. Literature review and proof development are the principal tasks. Any exact search, simulation or symbolic calculation needs an explicit finite scope; its compute and memory requirements have not been estimated.

**Assessment:** 2026-10-15; untested forecast. **Uncertainty:** A concrete concern in one proof dependency is recorded, without a signed expert review or complete assessment of the alternative argument.

**Further work:** resolve the statement and status questions above before planning an attempt. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-10-15

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Unverified.

For the valid chain 1,2,...,N, the length is N-1 and C=(N-1)/(N-1)=1, contradicting the stated uniform growth C >> N/log_2(N). This is a specific editorial concern about Proposition 3.6, not a resolution of the Ulam density problem.

**Search scope:** Read Green's Problem 7 and Agama version 12, focusing on the addition-chain definitions and the dependency of Theorem 5.1 on Proposition 3.6.

**Inspected evidence**

- [100 Open Problems, December 2025 revision](../sources.md#src-math-302) — Problem 7. The source asks whether the classical Ulam sequence has positive density.
- [Ulam numbers have zero density (version 12)](../sources.md#src-math-409) — Definition 3.1; Lemma 3.4; Proposition 3.6; Theorem 5.1. Proposition 3.6 extends a shortest-chain estimate to arbitrary chains; Theorem 5.1 uses that extension.

**Limits and remaining work**

- The observation has no signed specialist review.
- The separate Section 6 argument and its additional hypothesis have not been fully checked.
- No exhaustive later-literature search was performed.

<details>
<summary>Search queries</summary>

- "Ulam numbers have zero density" review Agama error
- "Ulam numbers" "2026" density conjecture


</details>

### 2026-10-14

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Unverified.

The original sequence definition matches Green's Problem 7. Agama's 2026 version 12 claims the opposite density conclusion in Theorem 5.1. The proof and independent acceptance have not been established, so neither openness nor resolution is asserted.

**Search scope:** The original statement and the named later primary result were inspected; the recorded queries delimit the update search.

**Inspected evidence**

- [100 Open Problems, December 2025 revision](../sources.md#src-math-302) — Green, Problem 7; Agama, version 12, Theorem 5.1. The canonical Ulam seed and distinct summands match the question; a later manuscript claims zero natural density.
- [Ulam numbers have zero density (version 12)](../sources.md#src-math-409) — Version 12, Theorem 5.1; definitions in Section 4 and natural density in Section 6. Agama claims zero natural density for the canonical Ulam sequence.

**Limits and remaining work**

- The search is not exhaustive and the later proof was not independently verified.
- No inference of currently open or accepted solved status is justified while this claimed resolution remains unreviewed.

<details>
<summary>Search queries</summary>

- "Ulam numbers have zero density" Agama review 2026


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
