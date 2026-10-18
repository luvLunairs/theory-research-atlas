# First-order representations of Markovian PDE behaviors

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-CROSS-401 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-CROSS-401%3A+First-order+representations+of+Markovian+PDE+behaviors&target=Q-CROSS-401) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-CROSS-401%3A+First-order+representations+of+Markovian+PDE+behaviors&target=Q-CROSS-401)

Historical conjecture: for a constant-coefficient linear PDE behavior, does concatenability across every three-way partition of the independent-variable space characterize an equivalent first-order kernel representation in the same manifest variables? The weak-Markovian converse is disproved by Rocha and Willems (2006).

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Disproved. **Last checked:** 2026-10-15.

**Status basis:** Rocha and Willems (2006), section 3, give a smooth finite-dimensional counterexample to the original weak-Markovian equivalence. The historical conjecture is false; strong-Markovian variants are separate questions.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Recorded source years: SRC-CROSS-401: 2002; SRC-CROSS-601: 2006. Later evidence is limited to the passages in the dated literature check; an access date does not refresh a historical claim.

**Scope limits:** The weak-Markovian converse is false. The finite-dimensional strong-Markovian theorem has different hypotheses and must not be presented as a repair of the original statement.

**Information still needed**

- Reconstruct the counterexample's polynomial kernel and check concatenation and nonrepresentability separately.
- Any proposed extension needs its own statement, provenance and current literature check.

**Primary branch:** [Control, estimation and systems theory](../domains/eng.md#eng-control). **Related branches:** [Differential equations and variational analysis](../domains/math.md#math-anal-pde).

**Sources:** [2002 MTNS Problem Book: Open Problems on the Mathematical Theory of Systems](../sources.md#src-cross-401); [Markov properties for systems described by PDEs and first-order representations](../sources.md#src-cross-601).

**Exact locator:** Problem 75, section 75.2.2, pp. 1–3; Jan C. Willems

**Potential difficulty:** Unknown. The historical conjecture is settled negatively. The remaining work is a proof audit whose effort has not been estimated.

**Possible AI role:** Reconstruct the published example, derive its polynomial relations and organize a proof audit. Assistance requires symbolic algebra and a reader familiar with behavioral systems.

**Verification burden:** High. Verify membership in the PDE behavior, the concatenation property and the obstruction to a first-order kernel in the same variables. Checking sample trajectories is insufficient.

**Resource expectations:** No experiment or external dataset is needed. Exact symbolic calculations can support the audit; the main resource is specialist attention to signal spaces and quantifiers.

**Assessment:** 2026-10-15; untested forecast. **Uncertainty:** No reconstruction or formal verification has been carried out. The workload concerns the existing proof, not the prospect of resolving an open conjecture.

**Further work:** examine the cited result or develop a clearly labeled reproduction. Any new variant needs its own statement and relation to this record. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-10-15

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Disproved → Disproved.

The weak-Markovian counterexample and the finite-dimensional strong-Markovian theorem address different properties. The original converse remains disproved.

**Search scope:** Reopened the 2006 paper to compare the two Markov properties and align the verification profile with its counterexample.

**Inspected evidence**

- [Markov properties for systems described by PDEs and first-order representations](../sources.md#src-cross-601) — §§2–3 and §5, Theorem 1. Weak and strong Markov properties are distinct; the former has a counterexample, while the finite-dimensional strong version has a theorem.

**Limits and remaining work**

- No proof was independently reconstructed, and no new general strong-Markovian claim was assessed.

### 2026-10-14

**Coverage:** Statement and later literature. **Statement:** Corrected.

**Recorded status:** Unverified → Disproved.

Rocha and Willems (2006), section 3, give a smooth finite-dimensional counterexample to the original weak-Markovian equivalence. The historical conjecture is false; strong-Markovian variants are separate questions.

**Search scope:** Compared the original MTNS formulation with targeted name-and-model searches; inspected the later passages listed below. This is a bounded literature check.

<details>
<summary>Previous indexed wording</summary>

Does Markovian concatenation characterize first-order kernel representations of constant-coefficient linear PDE behaviors?

The current statement appears at the top of this page.
</details>

**Inspected evidence**

- [2002 MTNS Problem Book: Open Problems on the Mathematical Theory of Systems](../sources.md#src-cross-401) — Problem 75, section 75.2.2, pp. 1–3; Jan C. Willems. Identifies the historical target.
- [Markov properties for systems described by PDEs and first-order representations](../sources.md#src-cross-601) — Section 3, pp. 539–540; DOI 10.1016/j.sysconle.2005.11.003. A finite-dimensional smooth behavior is weak-Markovian but has no first-order kernel representation.

**Limits and remaining work**

- Check the polynomial-kernel encoding of the published counterexample before using it as a calibration.
- This check is not an independent proof audit or an exhaustive review of all later literature.

<details>
<summary>Search queries</summary>

- "Markov properties for systems described by PDEs" pdf


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
