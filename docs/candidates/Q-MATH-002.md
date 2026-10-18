# Audit exact union-closed-family certificates on at most four elements

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MATH-002 · Full card available.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MATH-002%3A+Audit+exact+union-closed-family+certificates+on+at+most+four+elements&target=Q-MATH-002) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MATH-002%3A+Audit+exact+union-closed-family+certificates+on+at+most+four+elements&target=Q-MATH-002)

Curator-proposed, pending peer assessment: enumerate every family F subseteq P({1,2,3,4}) with F nonempty, union(F) nonempty, and A union B in F for all A,B in F; for each eligible F record an element x in union(F) such that 2*|{A in F:x in A}| >= |F|. Deliver a completeness argument and an independently implemented verifier. Unused ground elements are allowed; repeated sets are not.

**Origin:** Curator proposal. **Curator-designed scope:** Yes.

**Current status:** Known result in literature. **Last checked:** 2026-10-13.

**Status basis:** The four-element mathematical property is a special case of the source's reported twelve-element theorem. The certificate/benchmark packaging is a curator proposal; no claim of mathematical novelty or project execution.

**Statement check:** Source located. **Status check:** Source report only.

**Source date and freshness:** Recorded source years: SRC-MATH-002: 2013. The last-checked date records the scope described in the status basis; it is not a comprehensive literature-search date.

**Scope limits:** Use the full card for assumptions and validation limits.

**Information still needed**

- Review existing public enumeration resources before attributing infrastructure novelty.
- Choose certificate schema and independent verifier implementations.
- Counts by family size and active-universe size remain unmeasured.
- The general union-closed conjecture's present status is outside this card's verification scope.

**Primary branch:** [Extremal and Ramsey theory](../domains/math.md#math-comb-ext). **Related branches:** [Algorithms and data structures](../domains/cs.md#cs-alg).

**Sources:** [The journey of the union-closed sets conjecture](../sources.md#src-math-002).

**Exact locator:** Introduction for definitions; section 5 Theorem 17 for the already-known finite-case context.

**Potential difficulty:** Medium. The task has fully bounded enumeration, a local exact witness, and cheap independent verification. Its purpose is to test careful formalization and tooling, not to suggest the general conjecture is easy.

**Possible AI role:** No named model evaluated; assumes tool-using AI with exact bitset programming and basic combinatorics.

**Verification burden:** Low. Most difficulty is proving coverage and avoiding correlated implementation errors.

**Resource expectations:** Experiment: None; purely finite mathematics. Data: No empirical or private data. Generated finite families and witnesses become the future artifact. Computation: Estimated ordinary CPU and small memory. There are exactly 2^16=65,536 input family masks before filtering; this size justifies a conservative laptop-scale planning assumption but is not a timing measurement.

**Assessment:** 2026-10-13; untested forecast. **Uncertainty:** No implementation was run. Independent novelty of this packaging is not asserted; existing enumerations may already provide equivalent data.

[Read the full card](../cards/Q-MATH-002.md). **Human review:** Pending.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
