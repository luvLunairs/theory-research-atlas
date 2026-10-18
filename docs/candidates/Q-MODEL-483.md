# Computational complexity of ranked tree-child network rNNI* distance

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MODEL-483 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-483%3A+Computational+complexity+of+ranked+tree-child+network+rNNI%2A+distance&target=Q-MODEL-483) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-483%3A+Computational+complexity+of+ranked+tree-child+network+rNNI%2A+distance&target=Q-MODEL-483)

Can the discrete rNNI* distance between two binary ranked tree-child networks on a common finite leaf set X be computed in polynomial time?

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-10-14.

**Status basis:** The September 2025 published version explicitly retains this question. No complete later-literature review was performed; the status is the source's report.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Sources: SRC-MODEL-408: 2024; SRC-MODEL-614: 2025. The 2026-10-14 check covers the scope recorded in the linked literature check.

**Scope limits:** These are finite combinatorial questions about the source-defined ranked tree-child network space. A theorem about that space does not establish that a particular inferred network describes evolutionary history.

**Information still needed**

- Use discrete rNNI* moves; continuous CAT(0) distance and order-membership algorithms do not solve discrete shortest distance.
- The later source reports this question as unresolved; subsequent literature was not exhaustively reviewed.

**Primary branch:** [Evolution, population genetics and phylogenetics](../domains/bio.md#bio-evol). **Related branches:** [Combinatorics and discrete mathematics](../domains/math.md#math-comb).

**Sources:** [Spaces of ranked tree-child networks](../sources.md#src-model-408); [Spaces of ranked tree-child networks](../sources.md#src-model-614).

**Exact locator:** §7, final discussion of rNNI*; definitions in §§2–4

**Potential difficulty:** High. The source asks for a uniform algorithmic or combinatorial result on an entire family of network spaces.

**Possible AI role:** A tool-using AI could implement independent move validators and compare exact small-instance distances to candidate decompositions or hardness reductions. This is a forecast; no named model has been evaluated on the task.

**Verification burden:** High. Use the source's exact move or poset definitions. Independently check finite witnesses and algorithm steps; polynomial complexity or shellability across leaf counts requires proof.

**Resource expectations:** Small exact graph instances can be explored on a workstation; distances and poset size may grow rapidly. General algorithmic or shellability claims require proof, not exhaustive checks at a few leaf counts.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** The operation and network equivalence must match the paper. Efficient continuous CAT(0) distance computation is a different result; later discrete-distance literature needs checking.

**Further work:** define a scoped target, resource requirements and a verification plan before developing a full card. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-10-14

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Source reports open.

The September 2025 published version explicitly retains this question. No complete later-literature review was performed; the status is the source's report.

**Search scope:** Original source plus the specifically cited later primary paper, review or claim. Only the recorded queries and inspected locators are covered; this is not a complete bibliographic survey.

**Inspected evidence**

- [Spaces of ranked tree-child networks](../sources.md#src-model-408) — §7, final discussion of rNNI*; definitions in §§2–4. Original question or research direction located.
- [Spaces of ranked tree-child networks](../sources.md#src-model-614) — §7; §§2–5 definitions. Explicitly asks whether discrete rNNI* distance is polynomial-time computable.

**Limits and remaining work**

- Use discrete rNNI* moves; continuous CAT(0) distance and order-membership algorithms do not solve discrete shortest distance.
- The later source reports this question as unresolved; subsequent literature was not exhaustively reviewed.
- Statements were compared; proofs were not independently reproduced or formally verified.

<details>
<summary>Search queries</summary>

- "ranked tree-child" "distance" complexity 2025 2026


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
