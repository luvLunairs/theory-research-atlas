# Shellability of the ranked tree-child network poset

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MODEL-484 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-484%3A+Shellability+of+the+ranked+tree-child+network+poset&target=Q-MODEL-484) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-484%3A+Shellability+of+the+ranked+tree-child+network+poset&target=Q-MODEL-484)

Is the source-defined poset (T(X), ≼) of cluster systems associated with ranked tree-child networks shellable?

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-11-06.

**Status basis:** The 2026 cactus paper proves EL-shellability for its smaller poset and explicitly repeats the shellability question for the ranked tree-child poset T(X). The embedding identifies a useful related result without resolving the indexed question.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Published tree-child paper, September 2025; cactus preprint v1, 7 June 2026.

**Scope limits:** The cactus poset P(X) embeds into T(X), but shellability is not asserted to follow for the latter. This is a finite combinatorial question about a family of network spaces.

**Information still needed**

- Preserve the exact order on T(X) and its order-complex convention when comparing with the cactus poset.
- The June 2026 paper explicitly retains this question; subsequent work was not exhaustively reviewed.

**Primary branch:** [Evolution, population genetics and phylogenetics](../domains/bio.md#bio-evol). **Related branches:** [Combinatorics and discrete mathematics](../domains/math.md#math-comb).

**Sources:** [Spaces of ranked tree-child networks](../sources.md#src-model-408); [Spaces of ranked tree-child networks](../sources.md#src-model-614); [EL-Shellability of the poset of ranked cactuses](../sources.md#src-model-801).

**Exact locator:** Spaces of ranked tree-child networks, Section 7 and definitions in Sections 4-5; EL-Shellability of the poset of ranked cactuses, Theorem 4.2 and final paragraph of Section 5.

**Potential difficulty:** High. The source asks for a uniform algorithmic or combinatorial result on an entire family of network spaces.

**Possible AI role:** Compare the published T(X) definition with the cactus labeling and isolate which proof steps use cactus structure before proposing a tree-child labeling or obstruction.

**Verification burden:** High. Use the source's exact move or poset definitions. Independently check finite witnesses and algorithm steps; polynomial complexity or shellability across leaf counts requires proof.

**Resource expectations:** Small exact graph instances can be explored on a workstation; distances and poset size may grow rapidly. General algorithmic or shellability claims require proof, not exhaustive checks at a few leaf counts.

**Assessment:** 2026-11-06; untested forecast. **Uncertainty:** A related 2026 theorem is available, but its proof does not supply a tree-child answer. No model-specific capability test or proof audit has been run.

**Further work:** define a scoped target, resource requirements and a verification plan before developing a full card. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-06

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Source reports open → Source reports open.

The 2026 cactus paper proves EL-shellability for its smaller poset and explicitly repeats the shellability question for the ranked tree-child poset T(X). The embedding identifies a useful related result without resolving the indexed question.

**Search scope:** Reopened the published tree-child discussion and inspected the later cactus theorem, embedding and explicit retained question; checked the arXiv version record.

**Inspected evidence**

- [Spaces of ranked tree-child networks](../sources.md#src-model-614) — Section 7. Asks shellability for the ranked tree-child poset.
- [EL-Shellability of the poset of ranked cactuses](../sources.md#src-model-801) — Theorem 4.2; final paragraph of Section 5. Proves cactus EL-shellability, then explicitly leaves T(X) shellability as a question.

**Limits and remaining work**

- The later preprint was inspected for statement and scope, not independently verified in full.

<details>
<summary>Search queries</summary>

- "ranked tree-child" shellability 2026
- "EL-Shellability" "ranked cactuses"


</details>

### 2026-10-14

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Source reports open.

The September 2025 published version explicitly retains this question. No complete later-literature review was performed; the status is the source's report.

**Search scope:** Original source plus the specifically cited later primary paper, review or claim. Only the recorded queries and inspected locators are covered; this is not a complete bibliographic survey.

**Inspected evidence**

- [Spaces of ranked tree-child networks](../sources.md#src-model-408) — §7, shellability question, p. 16; poset and chain construction in §§4–5. Original question or research direction located.
- [Spaces of ranked tree-child networks](../sources.md#src-model-614) — §7; §§2–5 definitions. Explicitly asks whether the source-defined network poset is shellable.

**Limits and remaining work**

- Use the source poset and its order complex; shellability of other network orders does not transfer automatically.
- The later source reports this question as unresolved; subsequent literature was not exhaustively reviewed.
- Statements were compared; proofs were not independently reproduced or formally verified.

<details>
<summary>Search queries</summary>

- "ranked tree-child" "shellable"


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
