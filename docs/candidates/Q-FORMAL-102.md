# Verify the equal-block language of a locally constrained tree-adjoining grammar

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-102 · Full card available.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-102%3A+Verify+the+equal-block+language+of+a+locally+constrained+tree-adjoining+grammar&target=Q-FORMAL-102) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-102%3A+Verify+the+equal-block+language+of+a+locally+constrained+tree-adjoining+grammar&target=Q-FORMAL-102)

Reproduce the nonempty string-language claim in Vijay-Shankar and Joshi, Example 2.5: the locally constrained TAG generates exactly a^n b^n c^n for integers n >= 1 when empty yields are excluded. Transcribe its elementary trees, preserve null-adjoining restrictions at auxiliary roots and feet, prove both language inclusions, and provide derivations for n = 1,...,6. Record separately whether the initial tree admits the empty word. The finite example range is curator chosen.

**Origin:** Known-result calibration. **Curator-designed scope:** Yes.

**Current status:** Known result in literature. **Last checked:** 2026-10-14.

**Status basis:** The source presents the equal-block construction with local adjoining constraints. This reproduces that construction, not an unrestricted-TAG claim or an empirical claim about language.

**Statement check:** Source located. **Status check:** Source report only.

**Source date and freshness:** Recorded source years: SRC-FORMAL-103: 1985. The last-checked date records the scope described in the status basis; it is not a comprehensive literature-search date.

**Scope limits:** Use the full card for assumptions and validation limits.

**Information still needed**

- A human reader should approve the scanned tree transcription and empty-word convention before implementation.
- Any comparison with a modern TAG library must specify how it encodes local constraints.

**Primary branch:** [Formal language and grammar theory](../domains/cog.md#cog-lang). **Related branches:** [Algorithms and data structures](../domains/cs.md#cs-alg), [Proof theory and constructive logic](../domains/logic.md#logic-proof).

**Sources:** [Some Computational Properties of Tree Adjoining Grammars](../sources.md#src-formal-103).

**Exact locator:** Section 2.1 and Example 2.5, printed pages 84-85

**Potential difficulty:** Medium. Symbolic assistance fits the inductive target and short examples, but a reviewer should first approve transcription of the scanned grammar and its node restrictions.

**Possible AI role:** No named model evaluated; assumes a tool-using AI that can read mathematical sources, produce inspectable symbolic work and code, and work with a human domain reviewer.

**Verification burden:** Medium. A parser may accept sample strings while implementing the wrong constraints.

**Resource expectations:** Experiment: None for language equality. Processing, acceptability and acquisition claims need independent linguistic or cognitive evidence. Data: Original elementary-tree diagrams and local-constraint definitions; no corpus or participant data. Computation: Small symbolic trees and six derivation records; no parser training. Local execution should suffice for this bounded presentation, but nothing has been timed. General grammar induction or exhaustive unrestricted derivation search would be different tasks.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** No transcription, parser or proof has been executed or reviewed. Scanned notation and differing TAG conventions are the main preparation risks.

[Read the full card](../cards/Q-FORMAL-102.md). **Human review:** Pending.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
