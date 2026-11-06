# Superpolynomial AC0[2]-Frege lower bounds for known tautologies

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-313 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-313%3A+Superpolynomial+AC0%5B2%5D-Frege+lower+bounds+for+known+tautologies&target=Q-FORMAL-313) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-313%3A+Superpolynomial+AC0%5B2%5D-Frege+lower+bounds+for+known+tautologies&target=Q-FORMAL-313)

Find an explicit tautology family requiring superpolynomial-size AC0[2]-Frege proofs for every fixed bound on the depth of circuits appearing as proof lines. These circuits may use unbounded-fan-in AND, OR and parity gates; circuit depth is distinct from the number of inference steps or the depth of the proof DAG.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-11-06.

**Status basis:** The inspected ITCS paper leaves explicit hard tautologies open. Later preprints claim bounds for unrestricted Res(parity) and for random formulas at depth 2. Neither establishes this entry's explicit-family lower bound at every fixed formula depth; their proofs and formalization claims remain independently unchecked.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** ITCS 2026; Braun arXiv v1: 19 September 2026, manuscript revision 2; Conneryd v1: 29 October 2026.

**Scope limits:** Compared the fixed depth of proof-line circuits with derivation depth, and distinguished an explicit family from a high-probability random-family result. Fragment lower bounds do not automatically transfer to stronger Frege systems.

**Information still needed**

- Independent assessment of both recent preprints and the claimed formalization.
- Check tautologicity, explicit constructibility and the exact Frege rule set for any proposed family.

**Primary branch:** [Proof theory and constructive logic](../domains/logic.md#logic-proof). **Related branches:** [Circuit and algebraic complexity](../domains/cs.md#cs-complex-circuit).

**Sources:** [AC⁰[p]-Frege Cannot Efficiently Prove That Constant-Depth Algebraic Circuit Lower Bounds Are Hard](../sources.md#src-formal-308); [An exponential lower bound for the bit pigeonhole principle in resolution over parities](../sources.md#src-math-805); [Random (log n)-CNF Formulas Are Hard for Depth-2 Frege with Modular Gates](../sources.md#src-math-806).

**Exact locator:** Lu-Santhanam-Tzameret, Sections 1.1-1.3; Braun, Theorem 1.1 and Section 1.3; Conneryd, Corollary 1.2 and Theorem 1.3

**Potential difficulty:** Frontier. Polynomial-method circuit bounds have not transferred to this proof system.

**Possible AI role:** Test a proposed algebraic measure against parity inference rules and check individual encodings of candidate tautologies.

**Verification burden:** High. A hardness proof for an inconsistent or non-tautological candidate is vacuous.

**Resource expectations:** No physical experiment or external dataset is required. Main cost is specialist proof development and review; finite searches can grow exponentially and need a separately specified limit.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No named model has been evaluated. These are possible research-support roles, not evidence that current AI can resolve the general problem.

**Further work:** define a scoped target, resource requirements and a verification plan before developing a full card. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-06

**Coverage:** Statement and later literature. **Statement:** Corrected.

**Recorded status:** Source reports open → Source reports open.

Clarify the depth parameter and add recent partial-result claims without presenting either as the full explicit-family result.

**Search scope:** Compared the fixed depth of proof-line circuits with derivation depth, and distinguished an explicit family from a high-probability random-family result. Fragment lower bounds do not automatically transfer to stronger Frege systems.

<details>
<summary>Previous indexed wording</summary>

Find an explicit tautology family requiring superpolynomial-size AC0[2]-Frege proofs at every fixed proof depth, where proof lines may use unbounded-fan-in AND, OR and parity gates.

The current statement appears at the top of this page.
</details>

**Inspected evidence**

- [AC⁰[p]-Frege Cannot Efficiently Prove That Constant-Depth Algebraic Circuit Lower Bounds Are Hard](../sources.md#src-formal-308) — Abstract; Sections 1.1-1.3. The hard DNF family is not known to consist of tautologies.
- [An exponential lower bound for the bit pigeonhole principle in resolution over parities](../sources.md#src-math-805) — Theorem 1.1; Section 1.3. Claims a lower bound for unrestricted DAG-like resolution over parities, a fragment of the target system.
- [Random (log n)-CNF Formulas Are Hard for Depth-2 Frege with Modular Gates](../sources.md#src-math-806) — Corollary 1.2; Theorem 1.3. Claims depth-2 random-formula lower bounds and identifies a barrier to this route at greater depths.

**Limits and remaining work**

- The search is scoped, not exhaustive.
- No independent proof, numerical replay or formal verification was performed.
- Human review remains pending.

<details>
<summary>Search queries</summary>

- "AC0" "Frege" "2026" "lower bounds"
- "New Polynomial-Depth Res" arxiv


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
