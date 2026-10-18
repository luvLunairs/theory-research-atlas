# Certify deficiency-zero hypotheses for small reaction networks

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

Turn a reaction diagram into a checkable explanation of whether a known structural theorem applies. This links chemistry and biology to graph algorithms and exact linear algebra without treating a model as an observed mechanism.

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-002%3A+Certify+deficiency-zero+hypotheses+for+small+reaction+networks&target=Q-MODEL-002) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-002%3A+Certify+deficiency-zero+hypotheses+for+small+reaction+networks&target=Q-MODEL-002)

[At a glance](#at-a-glance) · [The task](#problem) · [Resources and verification](#verification) · [Evidence and context](#evidence) · [AI trial assessment](#assessment) · [Research records](#audit-trail)

<a id="at-a-glance"></a>

## At a glance

| Field | Summary |
| --- | --- |
| Primary field | [Reaction-network and kinetics theory](../domains/chem.md#chem-reaction) |
| Related fields | [Systems biology and biological networks](../domains/bio.md#bio-systems), [Dynamical systems and ergodic theory](../domains/math.md#math-dyn), [Combinatorics and discrete mathematics](../domains/math.md#math-comb) |
| Task origin | [Known-result calibration](../evidence-policy.md) |
| Current status | [Known result in literature](../evidence-policy.md) · checked 2026-10-13 |
| AI suitability | [Preparation needed](../ai-assessment.md) · Untested forecast |
| Scientific review | Pending |

<a id="problem"></a>

## The task

### Precise statement

For a finite supplied network of mass-action reactions, compute delta = number_of_complexes - number_of_linkage_classes - rank(stoichiometric_matrix), test weak reversibility, and issue a traceable applicability certificate for the deficiency-zero theorem. Begin with at most four species, six complexes and ten reactions; these limits are curator chosen.

**Required output:** An exact structural certificate with the theorem's supported conclusion, or a precise report of failed hypotheses.

**Scope:** Curator-chosen inputs up to four species, six complexes and ten directed reactions. Include A+B &lt;-&gt; C and C &lt;-&gt; D as one fully specified example network, with positive rate symbols; this fixture is proposed and has not been run.

### Assumptions

- Finite set of species and distinct nonnegative-integer stoichiometric complexes.
- Deterministic, autonomous mass-action kinetics with strictly positive fixed rate constants.
- The theorem applies on positive stoichiometric compatibility classes; stability is relative to the class.
- Duplicate reactions and self-loops must have an explicitly documented normalization convention.

### Success criteria

1. Produce a canonical complex list, incidence data, stoichiometric matrix and exact rank certificate.
2. Produce connected-component and directed-return-path certificates for linkage count and weak reversibility.
3. Compute deficiency exactly and state the theorem only when all hypotheses apply.
4. If a hypothesis fails, report inapplicability rather than infer instability or nonexistence.
5. Separate structural certification from identifying whether the network represents a real chemical or biological system.

### Background needed

- Directed graphs and strongly connected components.
- Exact rank, conservation laws and stoichiometric subspaces.
- Mass-action ODEs, complex balance and relative local stability.

<a id="verification"></a>

## Resources and verification

### Resource requirements

**Computing:** Small exact integer matrices and graph traversals under the declared input bounds. Local laptop-class work is an untested planning assumption; larger symbolic equilibrium computations are outside scope.

**Data:** A complete reaction list with species ordering and kinetic convention. No new empirical data for this calibration.

**Experiments:** None for the graph-and-theorem certificate. Validating rates, well-mixing and the proposed mechanism requires separate data or experiments.

**Theory and model requirements:** Mass action, positive rates and positive compatibility classes. Does not transfer automatically to delays, spatial PDEs, stochastic dynamics, non-mass-action kinetics or time-varying forcing.

**Validation modes:** Proof, Exact computation.

### Verification steps

1. Review the input reaction semantics and deduplication convention.
2. Compare complex and species matrices with the supplied diagram.
3. Check exact rank and graph witnesses independently.
4. Verify each hypothesis against the cited theorem and retain its positivity and relative-stability clauses.
5. Review any biological or chemical interpretation separately.

**Statement alignment:** The certificate establishes theorem applicability, not global attraction, empirical adequacy, or a complete classification of all possible dynamics.

**Human review difficulty:** Moderate for a CRNT specialist; a graph or linear-algebra reviewer can check only the structural layer.

### Formal validity and empirical support

**What the formal task can establish:** Conditional structural theorem application can be certified under mass-action assumptions.

**Empirical support and limits:** Real chemistry and cell biology may violate ideal mixing, closure, rate and scale assumptions; this task supplies no empirical confirmation.

### Methods and obstacles

**Proposed methods:**

- classification
- exact computation
- graph algorithms
- proof application

**Expected obstacles:**

- Treating species as complexes or counting duplicate complexes twice.
- Floating-point rank errors.
- Confusing reversibility, weak reversibility, detailed balance and complex balance.
- Changing local stability into a global-attraction claim.
- Assuming that theorem inapplicability implies a negative dynamical result.

### Checks still needed

- Approve the small input format and example network before execution.
- Check the version of any theorem used for an expanded global-convergence claim; this card deliberately makes no such claim.
- The empirical validity of any future supplied network requires independent review.

<a id="evidence"></a>

## Evidence and context

**Status basis:** The theorem and hypotheses are verified in the opened sources. The finite input limits and certificate task are curator-designed calibration work.

**Exact problem / theorem locator:** ACK Definitions 2.1-2.4 and Theorem 3.1; Baez theorem

### Sources

- [Chemical Reaction Network Theory](../sources.md#src-model-005). Martin Feinberg; Ohio State University. Year not verified. [Read source](https://cbe.osu.edu/chemical-reaction-network-theory).
  - **Relevant sections:** Lectures; 1.A Early Reviews; 1.C More Mathematical Articles
  - **Source limitations:** Directory coverage is intentionally historical and author centered. Linked works have not all been read.
- [Network Theory Part 24](../sources.md#src-model-006). John Baez. 2012. [Read source](https://math.ucr.edu/home/baez/networks/networks_24.html).
  - **Relevant sections:** The zero deficiency theorem; Deficiency Zero Theorem (Child's Version)
  - **Source limitations:** Expository existence theorem is narrower than the full stability theorem. Do not infer global attraction from this page.
- [Product-form stationary distributions for deficiency zero chemical reaction networks](../sources.md#src-model-016). David F. Anderson; Gheorghe Craciun; Thomas G. Kurtz. 2010. [Read source](https://arxiv.org/html/0803.3042).
  - **Relevant sections:** Section 2 Definitions 2.1-2.4; Section 3.2 Theorems 3.1-3.3; Section 4 Theorems 4.1-4.2
  - **Source limitations:** Use stochastic propensity and volume conventions in the paper; unrestricted independent Poisson claims can be wrong after conditioning on a conserved class.

### Known results and partial progress

- ACK Theorem 3.1 states uniqueness of the equilibrium in each positive compatibility class and local asymptotic stability relative to that class for weakly reversible deficiency-zero mass-action networks.
- Baez gives a complementary existence proof through linear algebra. Feinberg's directory records historical sources and corrections.

**Research value:** Provides a reusable hypothesis-checking baseline for model sciences. It can prevent invalid theorem transfers and supports later comparisons of reaction-network structures.

### Related problems

- **Prerequisite for:** [Reproduce a product-form stationary distribution on a conserved reaction class](../candidates.md#q-model-012). A structural certificate can establish the hypotheses used to obtain a complex-balanced deterministic equilibrium before the stochastic product-form task.
- **Method bridge to:** [Bound structural perturbations in a selected biological model](../candidates.md#q-model-014). Structural perturbation studies need reliable recomputation of graph and rank invariants.

### Scope of the status check

**Finding:** The full theorem statement, structural definitions and author bibliography were opened and compared. It is an established-result calibration.

**Search limits:** No implementation or mathematical experiment was executed. Original 1972 articles were credited through the author directory, not claimed as fully read.

<details>
<summary>Literature references checked</summary>

**Sources checked:**

- [Chemical Reaction Network Theory](../sources.md#src-model-005)
- [Network Theory Part 24](../sources.md#src-model-006)
- [Product-form stationary distributions for deficiency zero chemical reaction networks](../sources.md#src-model-016)

</details>

<details>
<summary>Previous attempts and public records</summary>

- Existing theorem and proofs are documented by Horn, Jackson, Feinberg, Baez and ACK. No project implementation or model trial exists.

</details>

<details>
<summary>Attribution and suggested citation</summary>

**Original authors and credited contributors:**

- Fritz Horn
- Roy Jackson
- Martin Feinberg
- John Baez
- David F. Anderson
- Gheorghe Craciun
- Thomas G. Kurtz

**Suggested citation:** Theorem source: Anderson, D. F., Craciun, G., and Kurtz, T. G. (2010), Product-form stationary distributions for deficiency zero chemical reaction networks, arXiv:0803.3042v4, Section 3.2. Historical references and author credit: Feinberg, Chemical Reaction Network Theory (Ohio State); Baez (2012), Network Theory Part 24.

**Editorial credit:** Compiled for Theory Research Atlas with AI assistance.

</details>

<a id="assessment"></a>

## AI trial assessment

**Label:** [Preparation needed](../ai-assessment.md). **Evidence:** Untested forecast. **Assessed:** 2026-10-13.

The structural part is well suited to generated code and exact certificates, but a reviewer must first approve representation conventions and the limited theorem conclusion.

**Model or capability conditions:** No named model evaluated; assumes tool-using AI with literature retrieval, exact algebra or rational linear algebra, code generation, and access to a human domain reviewer.

**Uncertainty:** No AI or implementation has been tested. Small input bounds are chosen for inspectability and do not estimate success rates.

Ratings are separate judgments, not a score. High expertise needed or verification difficulty means a larger burden; high method availability or checkability means stronger support.

| Dimension | Rating | Reason |
| --- | --- | --- |
| Statement clarity | High | Finite input and the applicable theorem are explicit. |
| Decomposability | High | Parsing, graph structure, rank and theorem matching are separable. |
| Methods and literature | High | Author resources and a primary paper state the required concepts. |
| Search / symbolic fit | High | Exact linear algebra and graph algorithms apply directly. |
| Checkability | High | Certificates can be independently recomputed at the proposed small sizes. |
| Expertise needed | Medium | A CRNT reviewer must distinguish complex balance and detailed balance and assess kinetic assumptions. |
| Scholarly significance | Medium | Reusable verification baseline; no new reaction-network theorem is claimed. |
| Verification difficulty | Medium | Structural checks are modest; scope errors in stability claims are more subtle. |

**Correctness:** No project answer.

The cited literature supports the problem statement. No project answer has been submitted for review.

**Novelty:** Not claimed.

The target is a known result; no originality is claimed for the selected scope. Any later novelty claim requires a literature check.

<details>
<summary>Difficulty and significance</summary>

**Difficulty:** Medium.

The reasons are given in the [AI trial assessment](#assessment).

**Evidence type:** Editorial estimate not measured.

**Significance:** Medium.

The reasons are given under [research value](#evidence).

</details>

<a id="audit-trail"></a>

## Research records

No project attempts or human reviews have been recorded.

<details>
<summary>Record information</summary>

| Field | Recorded value |
| --- | --- |
| Stable ID | `Q-MODEL-002` |
| Duplicate key | `deficiency-zero-applicability-certificate` |
| Original domain label | Chemical reaction network theory |
| Original cross-domain labels | Systems biology; Graph theory; Dynamical systems |
| Primary domain ID | `CHEM.REACTION` |
| Cross-domain IDs | `BIO.SYSTEMS`, `MATH.DYN`, `MATH.COMB` |
| Origin code | `known_result_calibration` |
| Status code | `known_result` |
| Curator-designed scope | Yes |
| Detailed entry | Yes |
| Record level | `C` |
| Human review status | `pending` |
| Trial-label code | `preparation_required` |
| Assessment-evidence code | `untested_forecast` |
| Method tags | `proof`, `exact_computation`, `model_analysis`, `certificate_checking` |
| Validation tags | `pure_proof`, `exact_computation` |
| Experimental-dependency tag | `none_for_formal_task` |

[JSON record](../../data/cards/Q-MODEL-002.json)

</details>

[Problem cards](README.md) · [Back to top](#at-a-glance)
