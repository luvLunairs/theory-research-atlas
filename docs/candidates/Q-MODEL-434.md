# Polynomial-time full justified representation

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MODEL-434 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-434%3A+Polynomial-time+full+justified+representation&target=Q-MODEL-434) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-434%3A+Polynomial-time+full+justified+representation&target=Q-MODEL-434)

Is full justified representation achievable by a polynomial-time approval-based committee rule on unrestricted profiles?

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Reported resolved. **Last checked:** 2026-11-06.

**Status basis:** A polynomial-time FJR rule is given by Frank and Peters. Teh subsequently treats that result as established and supplies a polynomial-time rule for the stronger FJR+ axiom. This independent scholarly uptake and matching construction support a sourced resolution of the historical existence question; journal acceptance and project proof certification are not asserted.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Historical question: 2022. Frank-Peters preprint: August 2026; Teh v1: 11 August 2026.

**Scope limits:** The target is efficient construction of an FJR committee on unrestricted approval profiles, not efficient verification of arbitrary committees. The latter is a different computational question.

**Information still needed**

- Specialist review of the algorithms and any subsequent publication versions remains to be recorded.

**Primary branch:** [Social choice and collective decisions](../domains/econ.md#econ-social). **Related branches:** [Algorithms and data structures](../domains/cs.md#cs-alg).

**Sources:** [Outlook and Research Directions, in Multi-Winner Voting with Approval Preferences](../sources.md#src-model-403); [A Polynomial-Time Rule Satisfying Full Justified Representation](../sources.md#src-model-601); [Strengthening Full Justified Representation: Efficient Verification and Computation](../sources.md#src-model-706).

**Exact locator:** Lackner-Skowron, Section 7.1 Q5 and Definition 4.7; Frank-Peters, Theorem 1; Teh, Theorem 3.5 and Corollary 3.6.

**Potential difficulty:** High. The historical algorithm-existence question has a sourced affirmative resolution; it should no longer be presented as an untouched research target.

**Possible AI role:** Reproduce the published rules, compare FJR and FJR+ guarantees, or identify a separately stated extension with its own novelty check.

**Verification burden:** High. Independent expert review of the claim is needed. Abstracts, model confidence, producer checks and publication metadata alone do not verify a proof.

**Resource expectations:** Exact small-election searches may use SAT or integer programming on a workstation. Exhaustive instance size grows quickly; general claims require proofs or independently checked counterexamples.

**Assessment:** 2026-11-06; untested forecast. **Uncertainty:** No algorithm was run and no independent proof certification was performed. The resolution label records matching literature and subsequent independent uptake.

**Further work:** examine the cited result or develop a clearly labeled reproduction. Any new variant needs its own statement and relation to this record. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-06

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Reported resolved.

A polynomial-time FJR rule is given by Frank and Peters. Teh subsequently treats that result as established and supplies a polynomial-time rule for the stronger FJR+ axiom. This independent scholarly uptake and matching construction support a sourced resolution of the historical existence question; journal acceptance and project proof certification are not asserted.

**Search scope:** Reopened the existing Frank-Peters primary source at its algorithm theorem and inspected the independent Teh follow-up at its attribution, stronger axiom and polynomial-time construction. A targeted correction search found no matching counterexample or erratum.

**Inspected evidence**

- [A Polynomial-Time Rule Satisfying Full Justified Representation](../sources.md#src-model-601) — Section 3, Algorithm 1 and Theorem 1. Provides a polynomial-time construction satisfying the original FJR axiom.
- [Strengthening Full Justified Representation: Efficient Verification and Computation](../sources.md#src-model-706) — Introduction; Theorem 3.5 and Corollary 3.6. Explicitly recognizes preceding FJR constructions and independently provides a stronger polynomial-time guarantee.

**Limits and remaining work**

- Independent uptake is not equivalent to a signed project proof review. No peer-reviewed venue was established in this check.

<details>
<summary>Search queries</summary>

- "full justified representation" polynomial time 2026
- "full justified representation" "2026" erratum OR counterexample


</details>

### 2026-10-14

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Unverified.

A matching resolution claim has been located. Keep unverified pending publication/acceptance and specialist verification, rather than treating the historical target as plainly open.

**Search scope:** Original source plus the specifically cited later primary paper, review or claim. Only the recorded queries and inspected locators are covered; this is not a complete bibliographic survey.

**Inspected evidence**

- [Outlook and Research Directions, in Multi-Winner Voting with Approval Preferences](../sources.md#src-model-403) — §7.1, Q5; FJR definition 4.7. Original question or research direction located.
- [A Polynomial-Time Rule Satisfying Full Justified Representation](../sources.md#src-model-601) — §2, §3 Algorithm 1 and Theorem 1. The August 2026 preprint claims a polynomial-time rule satisfying the same Hare-quota FJR property.

**Limits and remaining work**

- Publication or independent acceptance of the 2026 claim remains unverified; FJR must not be replaced by EJR or EJR+.
- Statements were compared; proofs were not independently reproduced or formally verified.

<details>
<summary>Search queries</summary>

- "full justified representation" polynomial time


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
