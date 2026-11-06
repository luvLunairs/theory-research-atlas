# Efficient proportional and Pareto-optimal committees

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MODEL-435 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-435%3A+Efficient+proportional+and+Pareto-optimal+committees&target=Q-MODEL-435) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-435%3A+Efficient+proportional+and+Pareto-optimal+committees&target=Q-MODEL-435)

For every finite approval profile A and target size k, can a polynomial-time rule output a size-k committee satisfying proportional justified representation (PJR) and Pareto optimality under approval-count utilities? This asks for efficient construction; such committees are known to exist.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Unverified. **Last checked:** 2026-11-06.

**Status basis:** Dong's September 2026 preprint states NP-hardness of constructing a committee satisfying even JR and Pareto optimality on unrestricted profiles. Its explicit PJR consequence is conditional on P differing from NP. The full theorem and model are now located, but independent acceptance and correctness of the reduction remain unverified.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Book question, 2022 chapter; Dong arXiv v1, 8 September 2026.

**Scope limits:** Do not conflate constructing a committee, checking Pareto optimality of a supplied committee, and existence of a compatible committee. Restricted-domain positive results do not settle the unrestricted target.

**Information still needed**

- Independent acceptance or a specialist audit of the full search-hardness reduction.

**Primary branch:** [Social choice and collective decisions](../domains/econ.md#econ-social). **Related branches:** [Algorithms and data structures](../domains/cs.md#cs-alg).

**Sources:** [Outlook and Research Directions, in Multi-Winner Voting with Approval Preferences](../sources.md#src-model-403); [Jointly Satisfying Pareto Optimality and Justified Representation is NP-Hard in Approval-Based Multiwinner Voting](../sources.md#src-model-603).

**Exact locator:** Lackner and Skowron, Section 7.1, Q5; Dong (2026), Section 2, Definitions 1-3, and Section 3, Theorem 1 and its PJR consequence.

**Potential difficulty:** High. The target quantifies over unrestricted approval profiles or asks for a general algorithmic guarantee.

**Possible AI role:** A directly relevant resolution claim exists. AI could assist specialist comparison of definitions, dependencies and proof steps; reviewing the claim takes priority over treating the target as untouched.

**Verification burden:** High. Check the X3C reduction as a search-hardness argument for fixed-size committees, the unrestricted profile domain, approval-count Pareto dominance and the PJR-to-JR implication. The author's verification is not independent project review.

**Resource expectations:** Exact small-election searches may use SAT or integer programming on a workstation. Exhaustive instance size grows quickly; general claims require proofs or independently checked counterexamples.

**Assessment:** 2026-11-06; untested forecast. **Uncertainty:** No named model has been evaluated. This forecasts conditional assistance with literature and proof review, not measured capability or a probability that the claim is correct.

**Further work:** resolve the statement and status questions above before planning an attempt. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-06

**Coverage:** Statement and later literature. **Statement:** Corrected.

**Recorded status:** Unverified → Unverified.

Dong's September 2026 preprint states NP-hardness of constructing a committee satisfying even JR and Pareto optimality on unrestricted profiles. Its explicit PJR consequence is conditional on P differing from NP. The full theorem and model are now located, but independent acceptance and correctness of the reduction remain unverified.

**Search scope:** Read the original chapter question, Dong's definitions and Theorem 1 with its explicit consequence, and the arXiv author/provenance and version metadata. Distinguished restricted-domain results from the general target.

<details>
<summary>Previous indexed wording</summary>

Can a polynomial-time rule always produce a committee satisfying proportional justified representation and Pareto optimality?

The current statement appears at the top of this page.
</details>

**Inspected evidence**

- [Outlook and Research Directions, in Multi-Winner Voting with Approval Preferences](../sources.md#src-model-403) — Section 7.1, Q5. Asks for an efficiently computable proportional and Pareto-optimal rule.
- [Jointly Satisfying Pareto Optimality and Justified Representation is NP-Hard in Approval-Based Multiwinner Voting](../sources.md#src-model-603) — Definitions 1-3; Theorem 1 and following paragraph. Claims search hardness already for JR, hence for PJR unless P=NP; compatible committees exist.

**Limits and remaining work**

- No independent reduction audit or external acceptance was established. The question remains unverified rather than being declared solved from a preprint alone.

<details>
<summary>Search queries</summary>

- "committee" "priceability" "Pareto" 2026
- "priceability" "Pareto" "2026" committee


</details>

### 2026-10-14

**Coverage:** Statement and later literature. **Statement:** Needs clarification.

**Recorded status:** Unverified → Unverified.

The claimed hardness would rule out PJR plus Pareto-optimal polynomial-time search unless P=NP. The full reduction and acceptance remain unverified.

**Search scope:** Original source plus the specifically cited later primary paper, review or claim. Only the recorded queries and inspected locators are covered; this is not a complete bibliographic survey.

**Inspected evidence**

- [Outlook and Research Directions, in Multi-Winner Voting with Approval Preferences](../sources.md#src-model-403) — §7.1, Q5, second paragraph. Original question or research direction located.
- [Jointly Satisfying Pareto Optimality and Justified Representation is NP-Hard in Approval-Based Multiwinner Voting](../sources.md#src-model-603) — Abstract. Claims NP-hardness for the weaker combination JR plus Pareto optimality on unrestricted profiles.

**Limits and remaining work**

- The full search-hardness reduction and independent acceptance remain unverified; impossibility is conditional on P differing from NP.
- Statements were compared; proofs were not independently reproduced or formally verified.

<details>
<summary>Search queries</summary>

- "PJR" "Pareto optimality" polynomial 2026
- "Pareto Optimality in Approval-Based Multiwinner Voting"


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
