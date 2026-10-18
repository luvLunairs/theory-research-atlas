# Almost-consistent equations over Z4

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-500 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-500%3A+Almost-consistent+equations+over+Z4&target=Q-FORMAL-500) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-500%3A+Almost-consistent+equations+over+Z4&target=Q-FORMAL-500)

Is deleting at most k equations ax+by=c over Z4 to obtain consistency fixed-parameter tractable in k or W[1]-hard?

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Reported resolved. **Last checked:** 2026-10-15.

**Status basis:** The exact FPT theorem for prime-power moduli covers Z4 with deletion budget k. The paper is accepted at FOCS 2026, confirmed by the official list and an institutional publication record. This records the literature outcome; the algorithm has not been independently reproduced here.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** PACS question: 7 July 2024. Theorem: April 2026 preprint. FOCS acceptance and institutional advance-publication record checked on 15 October 2026.

**Scope limits:** The original FPT-versus-W[1]-hard question is settled in favor of FPT. An implementation or a sharper bound would need a separately stated objective.

**Information still needed**

- Independent reproduction of the algorithm and its running-time proof remains available as a separate verification task.
- The fixed modulus 4 and parameter k must be preserved in any reproduction.

**Primary branch:** [Algorithms and data structures](../domains/cs.md#cs-alg). **Related branches:** None recorded.

**Sources:** [PACS 2024: Workshop on Parameterized Algorithms and Constraint Satisfaction — Open problems](../sources.md#src-formal-488); [Optimal FPT-Approximability for Modular Linear Equations](../sources.md#src-formal-615); [FOCS 2026 accepted papers](../sources.md#src-review-701); [Optimal FPT-Approximability for Modular Linear Equations — institutional publication record](../sources.md#src-review-702).

**Exact locator:** Question 1

**Potential difficulty:** Unknown. The original question has an accepted conference result. The effort required to reproduce its algorithm or improve its bounds has not been assessed.

**Possible AI role:** Assist with explaining and reproducing the prime-power algorithm, checking small instances, and tracing the parameter dependence. Any proposed improvement should be stated separately from the resolved question.

**Verification burden:** High. Verify correctness and resource bounds under the exact input encoding, parameter and oracle access; observed running time does not prove asymptotic guarantees.

**Resource expectations:** No physical experiment is intrinsic. Small finite instances can be generated, but exhaustive searches may grow exponentially and no budget has been estimated.

**Assessment:** 2026-10-15; untested forecast. **Uncertainty:** Conference acceptance is documented. No implementation, full proof reproduction, or model evaluation has been performed.

**Further work:** examine the cited result or develop a clearly labeled reproduction. Any new variant needs its own statement and relation to this record. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-10-15

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Reported resolved.

The prime-power theorem gives exact fixed-parameter tractability for the modulus-4 deletion problem. Official FOCS acceptance supports its recorded resolution.

**Search scope:** Compared PACS Question 1 with the preprint's Theorem 1 and checked conference acceptance against the official FOCS list and an institutional publication record.

**Inspected evidence**

- [PACS 2024: Workshop on Parameterized Algorithms and Constraint Satisfaction — Open problems](../sources.md#src-formal-488) — Question 1, printed page 1. The target uses equations over Z4 and the number of deletions k.
- [Optimal FPT-Approximability for Modular Linear Equations](../sources.md#src-formal-615) — Introduction, Theorem 1 and the following paragraph. For modulus 4 the approximation ratio is one, giving exact fixed-parameter tractability.
- [FOCS 2026 accepted papers](../sources.md#src-review-701) — Accepted-paper entry with matching title and five authors. Official conference acceptance is confirmed.
- [Optimal FPT-Approximability for Modular Linear Equations — institutional publication record](../sources.md#src-review-702) — Publication status and host-publication fields. The institution lists FOCS 2026 and advance publication on 1 October.

**Limits and remaining work**

- The accepted manuscript download was unavailable; theorem matching used arXiv version 1.
- No independent algorithm implementation or complete proof audit was performed.

<details>
<summary>Search queries</summary>

- "Optimal FPT-Approximability for Modular Linear Equations"
- "Optimal FPT-Approximability" "accepted"


</details>

### 2026-10-14

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Unverified.

Theorem 1 of the April 2026 preprint Optimal FPT-Approximability for Modular Linear Equations claims an FPT approximation ratio omega(m). For fixed m=4, omega(4)=1, so the theorem claims an exact FPT resolution of the indexed question. Independent proof review and reliable confirmation of this recent claim remain outstanding; this is not an ordinary open target.

**Search scope:** Compared PACS Question 1 with the exact prime-power theorem, distinguishing exact FPT from earlier factor-two FPT approximation.

**Inspected evidence**

- [PACS 2024: Workshop on Parameterized Algorithms and Constraint Satisfaction — Open problems](../sources.md#src-formal-488) — Question 1. The source identifies the indexed question or research direction; its original date and any recorded partial results limit what it establishes about present status.
- [Optimal FPT-Approximability for Modular Linear Equations](../sources.md#src-formal-615) — Introduction, Theorem 1; Section 4. The exact FPT result includes modulus 4 and the deletion-budget parameter.

**Limits and remaining work**

- Independent review or reliable published confirmation of the 2026 preprint's exact FPT claim is missing.
- The parameterization must remain the number k of violated equations for fixed modulus 4.

<details>
<summary>Search queries</summary>

- "Min-2-Lin" "Z4" "2025"
- "Min-2-Lin" Z4 parameterized
- "Min-2-Lin" "Z4" "2026"
- "Min-2-Lin" "Z4" "Parameterized Approximability"


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
