# Parallel complexity of polynomial-time committee rules

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MODEL-445 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-445%3A+Parallel+complexity+of+polynomial-time+committee+rules&target=Q-MODEL-445) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-445%3A+Parallel+complexity+of+polynomial-time+committee+rules&target=Q-MODEL-445)

Classify the parallel complexity of computing the winning committee for AV, SAV, sequential CC/PAV, reverse sequential CC/PAV, sequential Phragmén, Greedy Monroe and MES with the source's tie conventions. For MES, distinguish its first phase from completion by sequential Phragmén. Efficient parallel computation means polylogarithmic time with polynomially many processors.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Reported resolved. **Last checked:** 2026-10-15.

**Status basis:** The source-surveyed family is classified by a published result. P-hardness means absence of efficient parallel algorithms only under P≠NC.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Sources: SRC-MODEL-403: 2022; SRC-MODEL-605: 2026. The 2026-10-14 check covers the scope recorded in the linked literature check.

**Scope limits:** The classification concerns these rules under worst-case asymptotic complexity. It does not prohibit practical parallel speedups, and it does not cover arbitrary MES completion rules.

**Information still needed**

- Independent proof reproduction is pending; record the exact rule and completion convention in any implementation.

**Primary branch:** [Social choice and collective decisions](../domains/econ.md#econ-social). **Related branches:** [Algorithms and data structures](../domains/cs.md#cs-alg), [Computational complexity](../domains/cs.md#cs-complex).

**Sources:** [Outlook and Research Directions, in Multi-Winner Voting with Approval Preferences](../sources.md#src-model-403); [On the Parallelizability of Approval-Based Committee Rules](../sources.md#src-model-605).

**Exact locator:** Lackner–Skowron §7.2, Q20; Fitzsimmons–Hassan–Hemaspaandra, Theorem 1, §2.2 and Appendices A and C in arXiv:2501.15006v2.

**Potential difficulty:** Unknown. The original classification is published. The effort required to audit its logspace algorithms and hardness reductions has not been estimated.

**Possible AI role:** Reconstruct reductions, check arithmetic and relate each theorem to an exact rule definition. This is review of existing results, not a prediction of a new complexity classification.

**Verification burden:** High. Check input encoding, reduction space, output convention and both directions of each reduction. A runtime benchmark cannot prove a complexity-class separation.

**Resource expectations:** No election dataset or new experiment is necessary. Small exact implementations can support proof review; specialist work on complexity and voting rules is the main requirement.

**Assessment:** 2026-10-15; untested forecast. **Uncertainty:** No named model has been evaluated. This forecasts conditional assistance with literature and proof review, not measured capability or a probability that the claim is correct.

**Further work:** examine the cited result or develop a clearly labeled reproduction. Any new variant needs its own statement and relation to this record. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-10-15

**Coverage:** Statement and later literature. **Statement:** Corrected.

**Recorded status:** Reported resolved → Reported resolved.

The classification applies to the stated parallel model and voting rules, with first-phase MES distinguished from completion by sequential Phragmén.

**Search scope:** Followed the published paper's full-version reference and inspected the complexity definitions and appendices, including MES completion.

<details>
<summary>Previous indexed wording</summary>

Classify the parallel complexity of the surveyed polynomial-time approval rules: AV, SAV, sequential CC/PAV, reverse sequential CC/PAV, sequential Phragmén, Greedy Monroe and the Method of Equal Shares, under stated tiebreaking.

The current statement appears at the top of this page.
</details>

**Inspected evidence**

- [On the Parallelizability of Approval-Based Committee Rules](../sources.md#src-model-605) — Full manuscript v2, §2.2, Appendices A, C.4 and C.5. The full version supplies the omitted rule proofs and separates first-phase MES from its Phragmén completion.

**Limits and remaining work**

- The reductions were inspected but not independently reproduced. An asymptotic hardness statement is not a measured performance result.

### 2026-10-14

**Coverage:** Statement and later literature. **Statement:** Corrected.

**Recorded status:** Unverified → Reported resolved.

The source-surveyed family is classified by a published result. P-hardness means absence of efficient parallel algorithms only under P≠NC.

**Search scope:** Original source plus the specifically cited later primary paper, review or claim. Only the recorded queries and inspected locators are covered; this is not a complete bibliographic survey.

<details>
<summary>Previous indexed wording</summary>

Classify polynomial-time approval committee rules by parallel complexity, including P-completeness or efficient parallel algorithms.

The current statement appears at the top of this page.
</details>

**Inspected evidence**

- [Outlook and Research Directions, in Multi-Winner Voting with Approval Preferences](../sources.md#src-model-403) — §7.2, Q20. Original question or research direction located.
- [On the Parallelizability of Approval-Based Committee Rules](../sources.md#src-model-605) — §1.1, Theorem 1; §§3–4. The published paper explicitly answers book question Q20 for its surveyed rules: P-hardness for seven sequential rules and logspace for AV/SAV.

**Limits and remaining work**

- The classification concerns the surveyed rules and their tiebreaking. P-hardness excludes NC algorithms only if P differs from NC.
- Statements were compared; proofs were not independently reproduced or formally verified.

<details>
<summary>Search queries</summary>

- "approval voting" "parallel complexity"
- "multiwinner" "P-complete" parallel


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
