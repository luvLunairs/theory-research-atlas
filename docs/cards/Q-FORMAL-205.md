# A complete graphical criterion for the front-door formula

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

The front-door formula can identify an intervention effect even with hidden confounding, but its familiar sufficient graphical conditions do not describe every graph where the formula works. The task is to find a complete graph-based rule for this specific formula.

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-205%3A+A+complete+graphical+criterion+for+the+front-door+formula&target=Q-FORMAL-205) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-205%3A+A+complete+graphical+criterion+for+the+front-door+formula&target=Q-FORMAL-205)

[At a glance](#at-a-glance) · [The task](#problem) · [Resources and verification](#verification) · [Evidence and context](#evidence) · [AI trial assessment](#assessment) · [Research records](#audit-trail)

<a id="at-a-glance"></a>

## At a glance

| Field | Summary |
| --- | --- |
| Primary field | [Causal inference and identifiability](../domains/stat.md#stat-causal) |
| Related fields | [Algorithms and data structures](../domains/cs.md#cs-alg) |
| Task origin | [Literature-origin question](../evidence-policy.md) |
| Current status | [Source reports open](../evidence-policy.md) · checked 2026-10-14 |
| AI suitability | [Preparation needed](../ai-assessment.md) · Untested forecast |
| Scientific review | Pending |

<a id="problem"></a>

## The task

### Precise statement

Characterize causal DAGs, allowing latent variables, and disjoint observed variable sets X, M and Y on which the unadjusted front-door functional Σ_m P(m|x*) Σ_x P(y|m,x)P(x) equals P(y|do(x*)) for every compatible causal model whose joint distribution over all observed variables is strictly positive. Here x, m and y denote joint values of the corresponding sets. The target is validity of this particular functional, not identifiability by some other formula.

**Required output:** Obtain an exact small countermodel to a proposed graphical extension, or a proved new sufficient graph pattern. The long-term target remains a necessary-and-sufficient criterion for universal validity.

**Scope:** Curator-proposed first milestone, pending review: examine at most 200 acyclic graphs on three observed binary variables X,M,Y and at most two latent binary variables, up to isomorphism fixing the observed roles. For graphs outside the cited sufficient criterion, either give a positive rational countermodel or prove the formula identically for that binary parameterization. These size and cardinality restrictions are exploratory, not literature-certified open subcases.

### Assumptions

- A causal directed acyclic graph is supplied, with observed and latent nodes distinguished.
- The general question allows disjoint observed variable sets X, M and Y; summation is over their joint values.
- Compatible models obey the graph's causal factorization and intervention semantics.
- Following the source's standing assumption, P(v)&gt;0 for every joint assignment v of all observed variables. The bounded initial task imposes the stronger sufficient condition of strictly positive local conditional probability tables.

### Success criteria

1. A countermodel includes the graph, positive rational conditional tables, the observational marginal, the intervention distribution and an exact nonzero discrepancy.
2. A symbolic identity must be proved as a rational-function identity with denominator conditions, and labelled with its binary/cardinality restrictions.
3. A proposed graphical criterion requires both sufficiency and necessity proofs over the stated full model class. Finite tests or general identifiability by another formula are insufficient.
4. Stop at 200 graphs or the symbolic-resource ceiling. Any unresolved identity or failed search remains unclassified.

### Background needed

- Causal DAGs, latent variables and intervention by truncated factorization.
- Conditional independence, d-separation and identification versus formula validity.
- Exact marginalization and symbolic rational-function identities.

<a id="verification"></a>

## Resources and verification

### Resource requirements

**Computing:** With at most five binary nodes, a single full joint table has at most 32 assignments. Symbolic expression growth can still be substantial. Proposed ceilings are 200 graphs, 100 rational parameter assignments per graph, 50,000 expanded polynomial terms per identity, 1 GiB memory and four elapsed hours. Stop at the first ceiling and retain an unresolved label. No runtime or cost has been measured.

**Data:** Synthetic rational conditional tables and explicit graphs only; observational data alone does not establish the assumed causal graph.

**Experiments:** No experiment is needed to prove a statement about a supplied causal model. Establishing that a real system satisfies the graph is a separate empirical task.

**Theory and model requirements:** The general target retains strict positivity of the full observed joint distribution. The finite milestone fixes binary cardinalities and strictly positive local tables. A binary symbolic identity does not by itself establish universal validity for arbitrary cardinalities, additional latent variables or a real causal system.

**Validation modes:** Exact computation, Proof.

### Verification steps

1. Check graph acyclicity, observed roles, probability normalization and strict positivity.
2. Independently compute the joint and observed distributions from the local conditional tables.
3. Compute the intervention distribution by replacing the X mechanism, and separately evaluate the front-door expression.
4. For a countermodel, compare exact rationals; for an identity, verify the cleared-denominator polynomial and all denominator assumptions.
5. Have a causal-inference reviewer check the model class and whether a proof transfers beyond the binary milestone.

**Statement alignment:** The question concerns universal validity of one fixed functional under the source's observed-distribution positivity assumption. A proof in the small binary family or identification by another functional is a narrower result.

**Human review difficulty:** Moderate for a small countermodel; high for necessary-and-sufficient graph criteria and cardinality-independent proofs.

### Formal validity and empirical support

**What the formal task can establish:** Formula validity is conditional on the supplied causal graph, model class and strict positivity of the full observed joint distribution.

**Empirical support and limits:** Neither a symbolic proof nor a synthetic countermodel establishes the causal graph or intervention effect in a real population.

### Methods and obstacles

**Proposed methods:**

- Graph enumeration preserving observed and latent roles.
- Exact rational countermodels via causal factorization.
- Symbolic marginalization with explicit positivity conditions.
- Do-calculus or other sound identification arguments for sufficient cases.

**Expected obstacles:**

- Agreement on many distributions does not prove agreement on all compatible models.
- A complete general identifiability algorithm may produce another functional and thus not answer the stated question.
- Cardinality-restricted identities can be mistaken for graphical theorems.
- Finite observational fits do not validate a causal graph.

### Checks still needed

- Check whether later work on functional equivalence already supplies a complete criterion.
- Clarify any desired restriction on treatment, mediator or outcome sets before extending the initial single-variable milestone.
- Verify that any proposed new graph pattern lies outside the paper's full sufficient theorem and equivalent known criteria.

<a id="evidence"></a>

## Evidence and context

**Status basis:** The April 2026 primary preprint explicitly leaves a necessary-and-sufficient graphical criterion open and gives examples outside its sufficient criterion. A scoped subsequent-literature search found no complete resolution; latent-variable and positivity conventions still require specialist review.

**Exact problem / theorem locator:** Wu–Robeva, §2.1.1 standing positivity assumption; §6, 'Concluding Remarks and Further Questions', Figure 4; Theorems 1.1, 3.5 and 3.6.

### Sources

- [Generalization of Pearl's Front-Door Criterion](../sources.md#src-formal-107). Carol Wu; Elina Robeva. 2026. [Read source](https://arxiv.org/html/2604.15288v1).
  - **Relevant sections:** Theorem 2.5 and Figure 1(b) for the classical criterion; Section 2.1.1 for strict observational positivity; Theorems 1.1, 3.5 and 3.6; Section 6 and Figure 4 for the remaining completeness question.
  - **Source limitations:** The classical criterion is used for calibration; the completeness question is indexed separately. The newer proofs have not been independently verified. Strict positivity of the observed joint distribution is a standing assumption. Original credit for the classical result belongs to Judea Pearl.

### Known results and partial progress

- Wu and Robeva give a sufficient criterion weaker than the classical front-door criterion.
- Their §6 explicitly calls that new criterion incomplete and asks for necessary and sufficient graphical conditions.
- They give a graph violating one of their sufficient conditions where the same front-door functional nevertheless remains valid.

**Research value:** A complete criterion would make the applicability of a common causal formula more transparent. Small exact models can separate plausible graph rules before an ambitious general proof.

### Related problems

- **Calibrated by:** [Reproduce front-door identification in a latent-confounded mediator graph](../candidates.md#q-formal-105). The existing classical front-door calibration supplies background; it is not itself an open target or a substitute for the complete criterion.

### Scope of the status check

**Finding:** The primary preprint explicitly leaves completeness open. No later complete criterion was identified in the scoped search.

**Search limits:** The open-state judgment rests on the dated preprint and a limited follow-up search, not an exhaustive review of all graphical-functional-equivalence literature.

<details>
<summary>Literature references checked</summary>

**Sources checked:**

- [Generalization of Pearl's Front-Door Criterion](../sources.md#src-formal-107)

</details>

<details>
<summary>Previous attempts and public records</summary>

- Wu and Robeva's 2026 paper gives a generalized sufficient criterion, a necessity result and an explicit remaining gap. Its new theorems have not been independently verified here.

</details>

<details>
<summary>Attribution and suggested citation</summary>

**Original authors and credited contributors:**

- Carol Wu
- Elina Robeva
- Judea Pearl

**Suggested citation:** Wu and Robeva, Generalization of Pearl's Front-Door Criterion, arXiv:2604.15288v1 (2026), §6. The classical front-door result is due to Judea Pearl.

**Editorial credit:** Compiled for Theory Research Atlas with AI assistance.

</details>

<a id="assessment"></a>

## AI trial assessment

**Label:** [Preparation needed](../ai-assessment.md). **Evidence:** Untested forecast. **Assessed:** 2026-10-14.

Exact small models and symbolic discrepancies are inspectable, but causal semantics and universal quantifiers need a specialist before any claimed graphical theorem.

**Model or capability conditions:** No named model evaluated; assumes a tool-using AI can manipulate small causal models and exact algebra, with causal-inference review and an independent arithmetic checker.

**Uncertainty:** The open question is based on a recent preprint and may overlap specialized functional-equivalence results. The bounded graph class may be completely covered by existing methods; no novelty or AI success is assumed.

Ratings are separate judgments, not a score. High expertise needed or verification difficulty means a larger burden; high method availability or checkability means stronger support.

| Dimension | Rating | Reason |
| --- | --- | --- |
| Statement clarity | High | The target functional is explicit and distinct from generic identifiability. |
| Decomposability | High | Graphs and countermodels can be considered one at a time. |
| Methods and literature | High | Causal factorization, do-calculus and symbolic marginalization are available. |
| Search / symbolic fit | High | Positive rational binary models support exact counterexample searches. |
| Checkability | Medium | A countermodel is compact; universal graphical claims require deeper reasoning. |
| Expertise needed | High | Latent-variable and intervention semantics need causal-inference expertise. |
| Scholarly significance | High | The result would clarify the scope of a standard causal functional. |
| Verification difficulty | High | Changing variable cardinalities, positivity or the model class can change what has been proved. |

**Correctness:** No project answer.

No graph was classified and no countermodel was computed here.

**Novelty:** Requires future literature review.

The general question is explicitly sourced; all proposed restricted milestones and future outcomes need separate novelty review.

<details>
<summary>Difficulty and significance</summary>

**Difficulty:** High.

Small models are tractable, but complete graphical criteria require substantial causal theory.

**Evidence type:** Editorial estimate not measured.

**Significance:** High.

A complete applicability rule would improve interpretation of a widely used causal functional.

</details>

<a id="audit-trail"></a>

## Research records

No project attempts or human reviews have been recorded.

<details>
<summary>Record information</summary>

| Field | Recorded value |
| --- | --- |
| Stable ID | `Q-FORMAL-205` |
| Duplicate key | `a-complete-graphical-criterion-for-the-front-door-formula` |
| Original domain label | Causal inference and identifiability |
| Original cross-domain labels | Algorithms and data structures |
| Primary domain ID | `STAT.CAUSAL` |
| Cross-domain IDs | `CS.ALG` |
| Origin code | `literature_open` |
| Status code | `source_reports_open` |
| Curator-designed scope | No |
| Detailed entry | Yes |
| Record level | `C` |
| Human review status | `pending` |
| Trial-label code | `preparation_required` |
| Assessment-evidence code | `untested_forecast` |
| Method tags | `model_analysis`, `counterexample`, `symbolic_derivation`, `finite_search`, `proof` |
| Validation tags | `exact_computation`, `pure_proof` |
| Experimental-dependency tag | `none_for_formal_task` |

[JSON record](../../data/cards/Q-FORMAL-205.json)

</details>

[Problem cards](README.md) · [Back to top](#at-a-glance)
