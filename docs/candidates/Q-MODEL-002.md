# Certify deficiency-zero hypotheses for small reaction networks

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MODEL-002 · Full card available.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-002%3A+Certify+deficiency-zero+hypotheses+for+small+reaction+networks&target=Q-MODEL-002) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-002%3A+Certify+deficiency-zero+hypotheses+for+small+reaction+networks&target=Q-MODEL-002)

For a finite supplied network of mass-action reactions, compute delta = number_of_complexes - number_of_linkage_classes - rank(stoichiometric_matrix), test weak reversibility, and issue a traceable applicability certificate for the deficiency-zero theorem. Begin with at most four species, six complexes and ten reactions; these limits are curator chosen.

**Origin:** Known-result calibration. **Curator-designed scope:** Yes.

**Current status:** Known result in literature. **Last checked:** 2026-10-13.

**Status basis:** The theorem and hypotheses are verified in the opened sources. The finite input limits and certificate task are curator-designed calibration work.

**Statement check:** Source located. **Status check:** Source report only.

**Source date and freshness:** Recorded source years: SRC-MODEL-005: date unverified, SRC-MODEL-006: 2012, SRC-MODEL-016: 2010. The last-checked date records the scope described in the status basis; it is not a comprehensive literature-search date.

**Scope limits:** Use the full card for assumptions and validation limits.

**Information still needed**

- Approve the small input format and example network before execution.
- Check the version of any theorem used for an expanded global-convergence claim; this card deliberately makes no such claim.
- The empirical validity of any future supplied network requires independent review.

**Primary branch:** [Reaction-network and kinetics theory](../domains/chem.md#chem-reaction). **Related branches:** [Systems biology and biological networks](../domains/bio.md#bio-systems), [Dynamical systems and ergodic theory](../domains/math.md#math-dyn), [Combinatorics and discrete mathematics](../domains/math.md#math-comb).

**Sources:** [Chemical Reaction Network Theory](../sources.md#src-model-005); [Network Theory Part 24](../sources.md#src-model-006); [Product-form stationary distributions for deficiency zero chemical reaction networks](../sources.md#src-model-016).

**Exact locator:** ACK Definitions 2.1-2.4 and Theorem 3.1; Baez theorem

**Potential difficulty:** Medium. The structural part is well suited to generated code and exact certificates, but a reviewer must first approve representation conventions and the limited theorem conclusion.

**Possible AI role:** No named model evaluated; assumes tool-using AI with literature retrieval, exact algebra or rational linear algebra, code generation, and access to a human domain reviewer.

**Verification burden:** Medium. Structural checks are modest; scope errors in stability claims are more subtle.

**Resource expectations:** Experiment: None for the graph-and-theorem certificate. Validating rates, well-mixing and the proposed mechanism requires separate data or experiments. Data: A complete reaction list with species ordering and kinetic convention. No new empirical data for this calibration. Computation: Small exact integer matrices and graph traversals under the declared input bounds. Local laptop-class work is an untested planning assumption; larger symbolic equilibrium computations are outside scope.

**Assessment:** 2026-10-13; untested forecast. **Uncertainty:** No AI or implementation has been tested. Small input bounds are chosen for inspectability and do not estimate success rates.

[Read the full card](../cards/Q-MODEL-002.md). **Human review:** Pending.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
