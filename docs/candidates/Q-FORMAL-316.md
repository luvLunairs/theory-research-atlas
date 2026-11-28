# Existence of a p-optimal proof system for true quantified Boolean formulas

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-316 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-316%3A+Existence+of+a+p-optimal+proof+system+for+true+quantified+Boolean+formulas&target=Q-FORMAL-316) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-316%3A+Existence+of+a+p-optimal+proof+system+for+true+quantified+Boolean+formulas&target=Q-FORMAL-316)

For the language of true quantified Boolean formulas, is there a polynomial-time computable proof system onto that language such that every other such system has a polynomial-time algorithm translating its proofs to proofs of the same formulas?

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-11-28.

**Status basis:** Egidy asks about ordinary true quantified Boolean formulas. Under one oracle with an infinite polynomial hierarchy all PSPACE languages have p-optimal systems; under another none of the PSPACE languages outside NP has an optimal system. This gives opposite relativized outcomes for the complete quantified-formula problem while leaving the unrelativized question open in the cited work.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** The problem statement and references listed in the 28 November 2026 literature check were inspected.

**Scope limits:** Egidy, Q2 and Section 1.2.2. Egidy and Glaßer, abstract, oracle O₁.

**Information still needed**

- Compare translations for the unrelativized complete language, including how the time bound depends on the system being simulated.

**Primary branch:** [Proof theory and constructive logic](../domains/logic.md#logic-proof). **Related branches:** [Computational complexity](../domains/cs.md#cs-complex).

**Sources:** [The SPARSE-Relativization Framework and Applications to Optimal Proof Systems](../sources.md#src-formal-309); [Optimal Proof Systems for Complex Sets are Hard to Find](../sources.md#src-math-927).

**Exact locator:** Egidy, Q2 and Section 1.2.2. Egidy and Glaßer, abstract, oracle O₁.

**Potential difficulty:** Frontier. The target concerns a PSPACE-complete language and universal translation among all its proof systems.

**Possible AI role:** Check that proposed proof translations are uniform algorithms for each simulated system and distinguish relativized formulas from the ordinary language.

**Verification burden:** High. Check the exact language, total proof-system range and polynomial translation bounds.

**Resource expectations:** No physical experiment or external dataset is required. Main cost is specialist proof development and review; finite searches can grow exponentially and need a separately specified limit.

**Assessment:** 2026-11-28; untested forecast. **Uncertainty:** Compare translations for the unrelativized complete language, including how the time bound depends on the system being simulated. Model performance on this task has not been measured.

**Further work:** define a scoped target, resource requirements and a verification plan before developing a full card. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-28

**Coverage:** Statement and later literature. **Statement:** Corrected.

**Recorded status:** Source reports open → Source reports open.

Egidy asks about ordinary true quantified Boolean formulas. Under one oracle with an infinite polynomial hierarchy all PSPACE languages have p-optimal systems; under another none of the PSPACE languages outside NP has an optimal system. This gives opposite relativized outcomes for the complete quantified-formula problem while leaving the unrelativized question open in the cited work.

**Search scope:** Egidy, Q2 and Section 1.2.2. Egidy and Glaßer, abstract, oracle O₁.

<details>
<summary>Previous indexed wording</summary>

Does the language of true quantified Boolean formulas have a polynomial-time proof system that polynomial-time simulates every other proof system for that language?

The current statement appears at the top of this page.
</details>

**Inspected evidence**

- [The SPARSE-Relativization Framework and Applications to Optimal Proof Systems](../sources.md#src-formal-309) — Q2 and Section 1.2.2, oracle O₂. States the unrelativized question and gives an oracle relative to which all PSPACE sets have p-optimal systems.
- [Optimal Proof Systems for Complex Sets are Hard to Find](../sources.md#src-math-927) — Abstract, first oracle. The negative oracle excludes optimal proof systems for PSPACE languages outside NP while the polynomial hierarchy stays infinite.

**Limits and remaining work**

- Compare translations for the unrelativized complete language, including how the time bound depends on the system being simulated.

<details>
<summary>Search queries</summary>

- Egidy Glaßer PSPACE QBF p-optimal proof systems oracle infinite polynomial hierarchy


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
