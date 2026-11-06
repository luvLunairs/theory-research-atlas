# Winner computation on voter-interval approval domains

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MODEL-444 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-444%3A+Winner+computation+on+voter-interval+approval+domains&target=Q-MODEL-444) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-444%3A+Winner+computation+on+voter-interval+approval+domains&target=Q-MODEL-444)

On voter-interval approval profiles, can an optimal size-k committee be computed in polynomial time for (a) Thiele rules with specified nonnegative, nonincreasing scoring weights and (b) Monroe's rule? These are separate parts of the historical question: a 2026 polynomial-time algorithm covers part (a); the cited result does not cover part (b).

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Unverified. **Last checked:** 2026-11-06.

**Status basis:** Manurangsi and Sornat give a polynomial-time algorithm for generalized Thiele winner computation on voter-interval profiles. Their institutional record lists NeurIPS 2026, and Dong independently cites the algorithm. The historical entry also asks about Monroe's rule, which is outside the inspected result; its current status remains unverified.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Historical Q19; algorithm preprint v1, 7 April 2026; later September citation and institutional NeurIPS 2026 listing.

**Scope limits:** Voter interval means that candidates' supporter sets are intervals in one voter order; it differs from candidate interval. The algorithm permits voter-specific rational weights encoded in binary; it does not establish Monroe winner computation.

**Information still needed**

- A current primary result or reliable retained open-question statement for the Monroe component.
- The final conference version and any corrections to the Thiele algorithm were not inspected.

**Primary branch:** [Social choice and collective decisions](../domains/econ.md#econ-social). **Related branches:** [Algorithms and data structures](../domains/cs.md#cs-alg).

**Sources:** [Outlook and Research Directions, in Multi-Winner Voting with Approval Preferences](../sources.md#src-model-403); [Polynomial-Time Algorithm for Thiele Voting Rules with Voter Interval Preferences](../sources.md#src-model-805); [Polynomial-Time Algorithm for Thiele Voting Rules on Voter Interval Domain](../sources.md#src-model-806); [Jointly Satisfying Pareto Optimality and Justified Representation is NP-Hard in Approval-Based Multiwinner Voting](../sources.md#src-model-603).

**Exact locator:** Lackner and Skowron, Section 7.2, Q19; Manurangsi and Sornat, Sections 2 and 4; Dong, Related Work; Google Research publication record.

**Potential difficulty:** Unknown. The Thiele component has a polynomial-time algorithm. A difficulty estimate for the separate Monroe target requires a current status review.

**Possible AI role:** Start from the existing Thiele algorithm and its exact domain assumptions. Treat algorithm reproduction as known-result work and review the separate Monroe literature before claiming a new solution.

**Verification burden:** High. Separate the two voting rules, verify interval recognition and weight encoding, and compare any proposed algorithm against the existing generalized-Thiele result.

**Resource expectations:** Exact small-election searches may use SAT or integer programming on a workstation. Exhaustive instance size grows quickly; general claims require proofs or independently checked counterexamples.

**Assessment:** 2026-11-06; untested forecast. **Uncertainty:** The Thiele component has an explicit algorithm and later scholarly uptake. The Monroe component and complete algorithm proof remain outside this curation check; no project model test was run.

**Further work:** resolve the statement and status questions above before planning an attempt. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-06

**Coverage:** Statement and later literature. **Statement:** Corrected.

**Recorded status:** Unverified → Unverified.

Manurangsi and Sornat give a polynomial-time algorithm for generalized Thiele winner computation on voter-interval profiles. Their institutional record lists NeurIPS 2026, and Dong independently cites the algorithm. The historical entry also asks about Monroe's rule, which is outside the inspected result; its current status remains unverified.

**Search scope:** Inspected the original combined question, the 2026 algorithm's model and algorithm section, a later independent citation and the institutional publication listing. Searched separately for Monroe on voter-interval profiles.

<details>
<summary>Previous indexed wording</summary>

Can Thiele methods and Monroe's rule be computed in polynomial time on the voter-interval domain?

The current statement appears at the top of this page.
</details>

**Inspected evidence**

- [Outlook and Research Directions, in Multi-Winner Voting with Approval Preferences](../sources.md#src-model-403) — Section 7.2, Q19. The historical question includes both Thiele and Monroe.
- [Polynomial-Time Algorithm for Thiele Voting Rules with Voter Interval Preferences](../sources.md#src-model-805) — Sections 2 and 4; Section 5. Gives the generalized-Thiele polynomial-time algorithm and records human-AI research provenance; no Monroe result is stated.
- [Jointly Satisfying Pareto Optimality and Justified Representation is NP-Hard in Approval-Based Multiwinner Voting](../sources.md#src-model-603) — Related Work. Independently cites the Thiele voter-interval algorithm.
- [Polynomial-Time Algorithm for Thiele Voting Rules on Voter Interval Domain](../sources.md#src-model-806) — Venue line and abstract. Lists the algorithm work at NeurIPS 2026.

**Limits and remaining work**

- Do not mark the combined historical question resolved. Conference metadata and later citation are not an independent project proof audit.

<details>
<summary>Search queries</summary>

- "Monroe" "voter interval" "2026"
- "Polynomial-time Algorithm for Thiele Voting Rules"


</details>

### 2026-10-14

**Coverage:** Statement only. **Statement:** Needs clarification.

**Recorded status:** Unverified → Unverified.

The historical source matches the indexed question. Targeted keyword searches did not establish a later primary result resolving its full scope; present-day openness remains unverified.

**Search scope:** Original source and recorded targeted searches. No later primary result matching the full target was established; statement-only denotes this evidence limit, not absence of a search.

**Inspected evidence**

- [Outlook and Research Directions, in Multi-Winner Voting with Approval Preferences](../sources.md#src-model-403) — §7.2, Q19; section 5.2.4. Original question or research direction located.

**Limits and remaining work**

- The weight sequence representation and supplied interval ordering matter; later algorithms may settle subclasses.
- Only the recorded search terms were covered; later results, different terminology, corrections and exact-scope resolutions may have been missed.

<details>
<summary>Search queries</summary>

- "voter interval" "Thiele" "Monroe" 2024 2025 2026
- "voter interval" "Monroe" polynomial time solved


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
