# Parallel-universe tiebreaking in committee rules

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MODEL-442 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-442%3A+Parallel-universe+tiebreaking+in+committee+rules&target=Q-MODEL-442) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-442%3A+Parallel-universe+tiebreaking+in+committee+rules&target=Q-MODEL-442)

Determine winner-decision complexity when sequential Thiele, Phragmén or equal-share rules return committees obtainable under some tiebreaking order.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Unverified. **Last checked:** 2026-10-14.

**Status basis:** Later results settle important neighboring formulations, but the candidate's unspecified winner-decision variant prevents a full resolution judgment.

**Statement check:** Needs clarification. **Status check:** Later literature checked.

**Source date and freshness:** Sources: SRC-MODEL-403: 2022; SRC-MODEL-606: 2023. The 2026-10-14 check covers the scope recorded in the linked literature check.

**Scope limits:** A finite approval-election model with fixed rule and axiom definitions from the book. An axiomatic result does not establish that voter preferences or welfare are represented adequately.

**Information still needed**

- Specify candidate-membership, committee-membership, uniqueness or counting. The inspected hardness results concern the latter two.

**Primary branch:** [Social choice and collective decisions](../domains/econ.md#econ-social). **Related branches:** [Algorithms and data structures](../domains/cs.md#cs-alg).

**Sources:** [Outlook and Research Directions, in Multi-Winner Voting with Approval Preferences](../sources.md#src-model-403); [Ties in Multiwinner Approval Voting](../sources.md#src-model-606).

**Exact locator:** §7.2, Q15

**Potential difficulty:** High. The target quantifies over unrestricted approval profiles or asks for a general algorithmic guarantee.

**Possible AI role:** A tool-using AI could construct reductions or parameterized search over tie choices. This is a forecast; no named model has been evaluated on the task.

**Verification burden:** High. Check the precise voting axioms, quantifiers, tie handling and input encoding. A counterexample can be checked independently; a rule or complexity claim needs a uniform proof.

**Resource expectations:** Exact small-election searches may use SAT or integer programming on a workstation. Exhaustive instance size grows quickly; general claims require proofs or independently checked counterexamples.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** Each rule is a separate case within this classification question; later results and input/tie representations require review.

**Further work:** resolve the statement and status questions above before planning an attempt. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-10-14

**Coverage:** Statement and later literature. **Statement:** Needs clarification.

**Recorded status:** Unverified → Unverified.

Later results settle important neighboring formulations, but the candidate's unspecified winner-decision variant prevents a full resolution judgment.

**Search scope:** Original source plus the specifically cited later primary paper, review or claim. Only the recorded queries and inspected locators are covered; this is not a complete bibliographic survey.

**Inspected evidence**

- [Outlook and Research Directions, in Multi-Winner Voting with Approval Preferences](../sources.md#src-model-403) — §7.2, Q15. Original question or research direction located.
- [Ties in Multiwinner Approval Voting](../sources.md#src-model-606) — Table 1; §2. Gives coNP-complete uniqueness and hard counting results under parallel-universes ties for several indexed rules.

**Limits and remaining work**

- Specify candidate-membership, committee-membership, uniqueness or counting. The inspected hardness results concern the latter two.
- Statements were compared; proofs were not independently reproduced or formally verified.

<details>
<summary>Search queries</summary>

- "parallel universes" "Phragmen" complexity
- "Ties in Multiwinner Approval Voting" complexity


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
