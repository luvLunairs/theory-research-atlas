# Core committee construction when the core exists

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MODEL-438 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-438%3A+Core+committee+construction+when+the+core+exists&target=Q-MODEL-438) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-438%3A+Core+committee+construction+when+the+core+exists&target=Q-MODEL-438)

Can a committee in the approval-election core be found in polynomial time on instances promised to have a nonempty core?

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Unverified. **Last checked:** 2026-11-26.

**Status basis:** The revised preprint reports a polynomial-time construction at the ordinary Hare quota. Theorem 7.2 has polynomial dependence on the input size and 1/delta, where delta = q - n/(k+1). Its bound does not cover the Droop core+ endpoint delta = 0.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** 2022 book and arXiv:2609.11912v2, 3 November 2026.

**Scope limits:** At the Hare quota q = n/k, delta = n/[k(k+1)] is positive. Finding one core committee and deciding whether a supplied committee belongs to the core are different tasks.

**Information still needed**

- Check the rational linear programs and their size in the search algorithm. The reported Hare existence formalization does not certify the runtime.

**Primary branch:** [Social choice and collective decisions](../domains/econ.md#econ-social). **Related branches:** [Algorithms and data structures](../domains/cs.md#cs-alg).

**Sources:** [Outlook and Research Directions, in Multi-Winner Voting with Approval Preferences](../sources.md#src-model-403); [Existence of the Core in Approval-Based Committee Elections](../sources.md#src-model-602).

**Exact locator:** Lackner and Skowron, Chapter 7, Q11; Becker, Greger and Peters v2, Sections 7–8, Theorem 7.2.

**Potential difficulty:** High. The target quantifies over unrestricted approval profiles or asks for a general algorithmic guarantee.

**Possible AI role:** Audit the polynomial dependence on the quota gap and the input representation for the ordinary Hare search problem.

**Verification burden:** High. Independent expert review of the claim is needed. Abstracts, model confidence, producer checks and publication metadata alone do not verify a proof.

**Resource expectations:** Exact small-election searches may use SAT or integer programming on a workstation. Exhaustive instance size grows quickly; general claims require proofs or independently checked counterexamples.

**Assessment:** 2026-11-26; untested forecast. **Uncertainty:** The algorithm and bit-complexity proof have not been independently verified.

**Further work:** resolve the statement and status questions above before planning an attempt. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-26

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Unverified.

The revised preprint reports a polynomial-time construction at the ordinary Hare quota. Theorem 7.2 has polynomial dependence on the input size and 1/delta, where delta = q - n/(k+1). Its bound does not cover the Droop core+ endpoint delta = 0.

**Search scope:** Checked the book questions, arXiv version history and revised theorem statements; searched for a publication or correction.

**Inspected evidence**

- [Outlook and Research Directions, in Multi-Winner Voting with Approval Preferences](../sources.md#src-model-403) — Chapter 7, Q11 and footnote. Separates search for a core committee from recognition.
- [Existence of the Core in Approval-Based Committee Elections](../sources.md#src-model-602) — Section 7, Theorem 7.2 and its proof; Section 8. Bounds the number of swaps and the size of the rational linear programs; treats the Droop endpoint separately.

**Limits and remaining work**

- The algorithm and bit-complexity proof have not been independently verified.

<details>
<summary>Search queries</summary>

- "Existence of the Core in Approval-Based Committee Elections" Becker Greger Peters 2026 accepted conference November core Droop Hare Theorem


</details>

### 2026-10-14

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Unverified.

The claimed algorithm would answer the historical promised search problem. Keep unverified pending independent acceptance and verification.

**Search scope:** Original source plus the specifically cited later primary paper, review or claim. Only the recorded queries and inspected locators are covered; this is not a complete bibliographic survey.

**Inspected evidence**

- [Outlook and Research Directions, in Multi-Winner Voting with Approval Preferences](../sources.md#src-model-403) — §7.2, Q11 and footnote 1. Original question or research direction located.
- [Existence of the Core in Approval-Based Committee Elections](../sources.md#src-model-602) — §7.1, Theorem 7.1. Claims polynomial-time construction of a core+ committee, hence a core committee, without a non-emptiness promise.

**Limits and remaining work**

- Independent acceptance and bit-complexity details remain unverified; search and recognition of arbitrary core committees are distinct.
- Statements were compared; proofs were not independently reproduced or formally verified.

<details>
<summary>Search queries</summary>

- "core" "committee" "polynomial" "exists" 2025 2026


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
