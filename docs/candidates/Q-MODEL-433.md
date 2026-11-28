# Nonempty core in approval-based committee elections

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MODEL-433 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-433%3A+Nonempty+core+in+approval-based+committee+elections&target=Q-MODEL-433) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-433%3A+Nonempty+core+in+approval-based+committee+elections&target=Q-MODEL-433)

Does every approval election admit a size-k committee unblocked by every coalition entitled to purchase a proportionate-sized alternative committee?

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Unverified. **Last checked:** 2026-11-26.

**Status basis:** The revised preprint retains the ordinary Hare-core existence claim and also gives existence for Droop core+. Its report of formalization specifically covers Hare-quota core existence. The atlas has not independently checked that formalization.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** 2022 book and arXiv:2609.11912v2, 3 November 2026.

**Scope limits:** There are n voters and k seats. Blocking the Hare committee requires an affordable deviation that gives every coalition member strictly more approved winners.

**Information still needed**

- Independently check the formal target and the proof for the stated Hare model.

**Primary branch:** [Social choice and collective decisions](../domains/econ.md#econ-social). **Related branches:** [Algorithms and data structures](../domains/cs.md#cs-alg).

**Sources:** [Outlook and Research Directions, in Multi-Winner Voting with Approval Preferences](../sources.md#src-model-403); [Existence of the Core in Approval-Based Committee Elections](../sources.md#src-model-602).

**Exact locator:** Lackner and Skowron, Chapter 7, Q3; Becker, Greger and Peters v2, Sections 2–3, 6 and 8.

**Potential difficulty:** High. The target quantifies over unrestricted approval profiles or asks for a general algorithmic guarantee.

**Possible AI role:** Check the Hare blocking inequalities against the revised theorem and the exact statement attributed to the Lean project.

**Verification burden:** High. Independent expert review of the claim is needed. Abstracts, model confidence, producer checks and publication metadata alone do not verify a proof.

**Resource expectations:** Exact small-election searches may use SAT or integer programming on a workstation. Exhaustive instance size grows quickly; general claims require proofs or independently checked counterexamples.

**Assessment:** 2026-11-26; untested forecast. **Uncertainty:** The later source is a preprint. Its external formalization was not rerun and no atlas review is recorded.

**Further work:** resolve the statement and status questions above before planning an attempt. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-26

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Unverified.

The revised preprint retains the ordinary Hare-core existence claim and also gives existence for Droop core+. Its report of formalization specifically covers Hare-quota core existence. The atlas has not independently checked that formalization.

**Search scope:** Checked the book questions, arXiv version history and revised theorem statements; searched for a publication or correction.

**Inspected evidence**

- [Outlook and Research Directions, in Multi-Winner Voting with Approval Preferences](../sources.md#src-model-403) — Chapter 7, Q3. Records the historical question of ordinary approval-core existence.
- [Existence of the Core in Approval-Based Committee Elections](../sources.md#src-model-602) — Section 2, Theorem 6.5, and Section 8. Reports existence for Hare core+ and distinguishes the Droop endpoint.

**Limits and remaining work**

- The later source is a preprint. Its external formalization was not rerun and no atlas review is recorded.

<details>
<summary>Search queries</summary>

- "Existence of the Core in Approval-Based Committee Elections" Becker Greger Peters 2026 accepted conference November core Droop Hare Theorem


</details>

### 2026-10-14

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Unverified.

A matching general resolution claim exists; publication/acceptance and the proof or formalization remain to be checked.

**Search scope:** Original source plus the specifically cited later primary paper, review or claim. Only the recorded queries and inspected locators are covered; this is not a complete bibliographic survey.

**Inspected evidence**

- [Outlook and Research Directions, in Multi-Winner Voting with Approval Preferences](../sources.md#src-model-403) — §7.1, Q3; core definition 4.10. Original question or research direction located.
- [Existence of the Core in Approval-Based Committee Elections](../sources.md#src-model-602) — §§2–3 and §6. The September 2026 preprint uses the same strict blocking/Hare-quota definition and claims core non-emptiness for every instance.

**Limits and remaining work**

- Publication or independent acceptance and the proof/formalization of the 2026 claim remain unverified; retain strict blocking and Hare quotas.
- Statements were compared; proofs were not independently reproduced or formally verified.

<details>
<summary>Search queries</summary>

- "approval" "core" "non-empty" 2024 2025 2026 committee


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
