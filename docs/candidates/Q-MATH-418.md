# Limiting cost of an online random-weight spanning tree

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MATH-418 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MATH-418%3A+Limiting+cost+of+an+online+random-weight+spanning+tree&target=Q-MATH-418) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MATH-418%3A+Limiting+cost+of+an+online+random-weight+spanning+tree&target=Q-MATH-418)

Reveal the edges of Kn in uniformly random order with independent Uniform[0,1] weights. Each edge must be accepted or rejected irrevocably when seen, and accepted edges must ultimately form a spanning tree. Does the minimum expected total cost over admissible policies converge as n grows, and what is its limit?

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-10-14.

**Status basis:** The undirected random-order limit question is still unspecified by the inspected 2018 follow-up and its 2021 correction. The exactly determined directed-arborescence constant concerns a different feasible structure. The source-reported gap is retained with the limited date coverage stated.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Inspected source years: SRC-MATH-403: 2008, SRC-MATH-604: 2018, SRC-MATH-605: 2021. Checked on 2026-10-14 within the scope recorded in the literature check.

**Scope limits:** The undirected random-order limit question is still unspecified by the inspected 2018 follow-up and its 2021 correction. The exactly determined directed-arborescence constant concerns a different feasible structure. The source-reported gap is retained with the limited date coverage stated. One explicitly stated stochastic model or separately posed question is indexed; related models do not share a result automatically.

**Information still needed**

- This is a scope check, not an independent proof verification or exhaustive literature review.
- The mathematical proof or counterexample, if proposed, still requires expert review.

**Primary branch:** [Discrete probability and random structures](../domains/prob.md#prob-discrete). **Related branches:** None recorded.

**Sources:** [Online Random Weight Minimal Spanning Trees and a Stochastic Coalescent](../sources.md#src-math-403); [Online purchasing under uncertainty](../sources.md#src-math-604); [Corrigendum to Online purchasing under uncertainty](../sources.md#src-math-605).

**Exact locator:** Pages 1–2: online combinatorial model and limiting-cost question.

**Potential difficulty:** Unknown. The statement is source-located, but a current difficulty assessment and comparison with the latest partial results have not been completed. A simple formulation is not evidence of tractability.

**Possible AI role:** After checking current status, AI with the relevant mathematical background and tools could compare policy recurrences and rigorously justified bounds for the optimal expected cost. Specialist review remains necessary; no named model has been evaluated.

**Verification burden:** High. An asymptotic, distributional or mixing claim needs an analytic proof with the model and limit fixed. Simulations and exact small-instance computations are evidence only.

**Resource expectations:** No physical experiment or empirical dataset is required. Literature review and proof development are the principal tasks. Any exact search, simulation or symbolic calculation needs an explicit finite scope; its compute and memory requirements have not been estimated.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** Current resolution status, practical resource needs and AI usefulness remain unmeasured. The 2008 draft is incomplete; later results and admissible-policy conventions need checking.

**Further work:** define a scoped target, resource requirements and a verification plan before developing a full card. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-10-14

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Source reports open.

The undirected random-order limit question is still unspecified by the inspected 2018 follow-up and its 2021 correction. The exactly determined directed-arborescence constant concerns a different feasible structure. The source-reported gap is retained with the limited date coverage stated.

**Search scope:** The original statement and the named later primary results were inspected; searches were limited to the recorded queries.

**Inspected evidence**

- [Online Random Weight Minimal Spanning Trees and a Stochastic Coalescent](../sources.md#src-math-403) — Pages 1–2, online combinatorial model. The policy makes irrevocable decisions on a random edge order and seeks an undirected spanning tree.
- [Online purchasing under uncertainty](../sources.md#src-math-604) — Theorem 1.6 and following paragraph; Section 7.1. The authors obtain bounded random-order costs but explicitly do not determine the asymptotic constant.
- [Corrigendum to Online purchasing under uncertainty](../sources.md#src-math-605) — Correction text, page 288. Only adversarial-order upper claims are withdrawn, not the random-order bounds.

**Limits and remaining work**

- This is a scope check, not an independent proof verification or exhaustive literature review.

<details>
<summary>Search queries</summary>

- "online" "random weight" "spanning" "Aldous"
- "online purchasing under uncertainty" spanning tree limit cost random order


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
