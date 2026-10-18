# A complete graphical criterion for the front-door formula

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-205 · Full card available.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-205%3A+A+complete+graphical+criterion+for+the+front-door+formula&target=Q-FORMAL-205) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-205%3A+A+complete+graphical+criterion+for+the+front-door+formula&target=Q-FORMAL-205)

Characterize causal DAGs, allowing latent variables, and disjoint observed variable sets X, M and Y on which the unadjusted front-door functional Σ_m P(m|x*) Σ_x P(y|m,x)P(x) equals P(y|do(x*)) for every compatible causal model whose joint distribution over all observed variables is strictly positive. Here x, m and y denote joint values of the corresponding sets. The target is validity of this particular functional, not identifiability by some other formula.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-10-14.

**Status basis:** The April 2026 primary preprint explicitly leaves a necessary-and-sufficient graphical criterion open and gives examples outside its sufficient criterion. A scoped subsequent-literature search found no complete resolution; latent-variable and positivity conventions still require specialist review.

**Statement check:** Source located. **Status check:** Source report only.

**Source date and freshness:** Recorded source years: SRC-FORMAL-107: 2026. The last-checked date records the scope described in the status basis; it is not a comprehensive literature-search date.

**Scope limits:** Use the full card for assumptions and validation limits.

**Information still needed**

- Check whether later work on functional equivalence already supplies a complete criterion.
- Clarify any desired restriction on treatment, mediator or outcome sets before extending the initial single-variable milestone.
- Verify that any proposed new graph pattern lies outside the paper's full sufficient theorem and equivalent known criteria.

**Primary branch:** [Causal inference and identifiability](../domains/stat.md#stat-causal). **Related branches:** [Algorithms and data structures](../domains/cs.md#cs-alg).

**Sources:** [Generalization of Pearl's Front-Door Criterion](../sources.md#src-formal-107).

**Exact locator:** Wu–Robeva, §2.1.1 standing positivity assumption; §6, 'Concluding Remarks and Further Questions', Figure 4; Theorems 1.1, 3.5 and 3.6.

**Potential difficulty:** High. Small models are tractable, but complete graphical criteria require substantial causal theory.

**Possible AI role:** No named model evaluated; assumes a tool-using AI can manipulate small causal models and exact algebra, with causal-inference review and an independent arithmetic checker. Exact small models and symbolic discrepancies are inspectable, but causal semantics and universal quantifiers need a specialist before any claimed graphical theorem.

**Verification burden:** High. Changing variable cardinalities, positivity or the model class can change what has been proved.

**Resource expectations:** Experiment: No experiment is needed to prove a statement about a supplied causal model. Establishing that a real system satisfies the graph is a separate empirical task. Data: Synthetic rational conditional tables and explicit graphs only; observational data alone does not establish the assumed causal graph. Computation: With at most five binary nodes, a single full joint table has at most 32 assignments. Symbolic expression growth can still be substantial. Proposed ceilings are 200 graphs, 100 rational parameter assignments per graph, 50,000 expanded polynomial terms per identity, 1 GiB memory and four elapsed hours. Stop at the first ceiling and retain an unresolved label. No runtime or cost has been measured.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** The open question is based on a recent preprint and may overlap specialized functional-equivalence results. The bounded graph class may be completely covered by existing methods; no novelty or AI success is assumed.

[Read the full card](../cards/Q-FORMAL-205.md). **Human review:** Pending.

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
