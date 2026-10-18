# Reverse sequential PAV approximation factor

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MODEL-443 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-443%3A+Reverse+sequential+PAV+approximation+factor&target=Q-MODEL-443) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-443%3A+Reverse+sequential+PAV+approximation+factor&target=Q-MODEL-443)

Determine the worst-case PAV-score approximation factor of reverse sequential PAV, relative to an optimal size-k committee.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Unverified. **Last checked:** 2026-10-14.

**Status basis:** A matching September 2026 preprint claim addresses the historical target with fixed-priority tiebreaking. The unrestricted zero guarantee is distinct from positive parameter-restricted bounds. Keep unverified pending independent proof acceptance.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Sources: SRC-MODEL-403: 2022; SRC-MODEL-604: 2026. The 2026-10-14 check covers the scope recorded in the linked literature check.

**Scope limits:** A finite approval-election model with fixed rule and axiom definitions from the book. An axiomatic result does not establish that voter preferences or welfare are represented adequately.

**Information still needed**

- Independent acceptance is missing; a zero ratio across all sizes does not exclude parameter-dependent bounds.

**Primary branch:** [Social choice and collective decisions](../domains/econ.md#econ-social). **Related branches:** [Algorithms and data structures](../domains/cs.md#cs-alg).

**Sources:** [Outlook and Research Directions, in Multi-Winner Voting with Approval Preferences](../sources.md#src-model-403); [Reverse Sequential Proportional Approval Voting Rule: Proportionality and Approximation Guarantees](../sources.md#src-model-604).

**Exact locator:** §7.2, Q17

**Potential difficulty:** High. The target quantifies over unrestricted approval profiles or asks for a general algorithmic guarantee.

**Possible AI role:** A directly relevant resolution claim exists. AI could assist specialist comparison of definitions, dependencies and proof steps; reviewing the claim takes priority over treating the target as untouched.

**Verification burden:** High. Independent expert review of the claim is needed. Abstracts, model confidence, producer checks and publication metadata alone do not verify a proof.

**Resource expectations:** Exact small-election searches may use SAT or integer programming on a workstation. Exhaustive instance size grows quickly; general claims require proofs or independently checked counterexamples.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No named model has been evaluated. This forecasts conditional assistance with literature and proof review, not measured capability or a probability that the claim is correct.

**Further work:** resolve the statement and status questions above before planning an attempt. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-10-14

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Unverified.

A matching September 2026 preprint claim addresses the historical target with fixed-priority tiebreaking. The unrestricted zero guarantee is distinct from positive parameter-restricted bounds. Keep unverified pending independent proof acceptance.

**Search scope:** Original source plus the specifically cited later primary paper, review or claim. Only the recorded queries and inspected locators are covered; this is not a complete bibliographic survey.

**Inspected evidence**

- [Outlook and Research Directions, in Multi-Winner Voting with Approval Preferences](../sources.md#src-model-403) — §7.2, Q17. Original question or research direction located.
- [Reverse Sequential Proportional Approval Voting Rule: Proportionality and Approximation Guarantees](../sources.md#src-model-604) — §1.1; Definitions 2–4; §§3–4. The preprint explicitly claims to answer textbook Q17 negatively: the unrestricted worst-case ratio to optimal PAV score is zero; parameter-restricted bounds are separate.

**Limits and remaining work**

- Independent acceptance is missing; a zero ratio across all sizes does not exclude parameter-dependent bounds.
- Statements were compared; proofs were not independently reproduced or formally verified.

<details>
<summary>Search queries</summary>

- "reverse sequential PAV" approximation factor
- "2609.35331"


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
