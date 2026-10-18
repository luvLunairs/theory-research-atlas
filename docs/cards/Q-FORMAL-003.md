# Build a bounded exact copy-lemma certificate census

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

Create a tiny, explicitly bounded laboratory for checking information inequalities. The output is a collection of exact derivation certificates, including an honest record if every result is already implied by elementary inequalities.

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-003%3A+Build+a+bounded+exact+copy-lemma+certificate+census&target=Q-FORMAL-003) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-003%3A+Build+a+bounded+exact+copy-lemma+certificate+census&target=Q-FORMAL-003)

[At a glance](#at-a-glance) · [The task](#problem) · [Resources and verification](#verification) · [Evidence and context](#evidence) · [AI trial assessment](#assessment) · [Research records](#audit-trail)

<a id="at-a-glance"></a>

## At a glance

| Field | Summary |
| --- | --- |
| Primary field | [Entropy inequalities and information geometry](../domains/info.md#info-entropy) |
| Related fields | [Optimization and operations research](../domains/math.md#math-opt) |
| Task origin | [Curator-proposed task](../evidence-policy.md) |
| Current status | [Needs further verification](../evidence-policy.md) · checked 2026-10-14 |
| AI suitability | [Preparation needed](../ai-assessment.md) · Untested forecast |
| Scientific review | Pending |

<a id="problem"></a>

## The task

### Precise statement

For five original finite random variables X1,...,X5 and one conditional copy X6 of X1 over (X2,X3), enumerate sums of at most three distinct elemental six-variable Shannon inequalities, each with coefficient 1 or 2. Use exactly the four marginal entropy equalities H(6,S)=H(1,S) for S subset of {2,3}, including the empty set, and I(6;1,4,5|2,3)=0. Determine which sums eliminate all coordinates involving X6 after adding rational combinations of those five equality rows; retain exact certificates and canonical projected inequalities.

**Required output:** An exact census, for the stated finite search, of projected inequalities and derivation certificates. Distinguish trivial, Shannon-implied and potentially non-Shannon consequences; all novelty claims require a separate literature audit.

**Scope:** Curator-proposed, pending peer assessment. A bounded precursor to larger information-inequality exploration; it does not claim to start an unexplored field or solve the full entropy-region problem.

### Assumptions

- All original random variables have finite alphabets; H is ordinary Shannon entropy with H(empty)=0.
- (X6,X2,X3) has the same joint distribution as (X1,X2,X3), and X6 is conditionally independent of (X1,X4,X5) given (X2,X3). No independence or deterministic relationship between X2 and X3 is imposed.
- The search uses exactly six variables, one auxiliary conditional copy, support size at most three and integer weights in {1,2}.
- A proof certificate may add arbitrary rational multiples of exactly the five listed copy equality rows. Any additional equality derived using Shannon inequalities must be expanded into the original rows and counted against the support and coefficient limits.
- No numerical vector is presumed entropic merely because it satisfies Shannon inequalities.

### Success criteria

1. Specify H_T as the joint entropy of the variables indexed by a nonempty subset T of {1,...,6}, with H_empty=0. Generate the elemental rows H(i|{1,...,6} minus {i}) &gt;= 0 and I(i;j|K) &gt;= 0 for i&lt;j and K subset of {1,...,6} minus {i,j}, without duplicates.
2. Use exactly four marginal rows H6-H1=0, H26-H12=0, H36-H13=0, H236-H123=0, and the conditional-independence row H236+H12345-H23-H123456=0. These encode H(6,S)=H(1,S) for all four S subsets of {2,3} and I(6;1,4,5|2,3)=0.
3. For each sum of one, two or three distinct elemental rows with weights 1 or 2, solve exactly whether adding equality rows cancels every coordinate containing 6.
4. Normalize retained nonzero projected integer vectors by positive common factor while preserving the inequality sign; retain exact derivation coefficients.
5. Classify Shannon implication over the original five variables using exact certificates, not floating-point solver status.
6. If the bounded census yields no new inequality, report that limited negative result without extrapolating to deeper copies or larger supports.

### Background needed

- Entropy and conditional mutual information
- Polyhedral cones and rational linear algebra
- Linear programming dual certificates
- Copy-lemma semantics

<a id="verification"></a>

## Resources and verification

### Resource requirements

**Computing:** Six variables produce 63 nonempty entropy coordinates. There are 6 + choose(6,2)*2^4 = 246 elemental Shannon rows; candidate sums grow combinatorially with support. Stream and deduplicate, record exact arithmetic bit growth, and impose a later measured resource cap. No CPU/GPU time or monetary budget is estimated.

**Data:** Mathematical constraints and the cited publications. Public code from the 2026 article is a possible later comparison resource, not an ingested dataset.

**Experiments:** none

**Theory and model requirements:** Finite Shannon entropy, valid conditional-copy extension, nonnegative coefficients on inequalities, unrestricted rational coefficients only on equalities. No claim about quantum entropy or differential entropy.

**Validation modes:** Proof, Exact computation.

### Verification steps

1. Have a reviewer derive the five equality rows from Definition 24 and Lemma 27 with N={1,2,3,4,5}, E={1,4,5}, D={2,3}, A={1} and A'={6}; handle zero-probability conditioning events without division by zero.
2. Confirm that no hidden independence assumption activates Claim 31 and that any derived equality is expanded before checking the fixed support and coefficient limits.
3. Check every original Shannon row and every retained derivation using an independent exact vector checker.
4. Record rejected candidates and completeness of the bounded enumeration.
5. Verify redundancy with rational conic certificates or verified separating vectors.
6. Compare surviving candidates against known inequalities and the 2026 MEM work before suggesting novelty.
7. Report execution logs and measured resource use after an attempt has run.

**Statement alignment:** A certificate proves a universal entropy inequality only when all auxiliary variables are justified by an extension lemma. Failure to derive one in this finite search does not establish independence from Shannon plus arbitrary copies.

**Human review difficulty:** High for semantic alignment and novelty; moderate for exact certificates.

### Formal validity and empirical support

**What the formal task can establish:** The card specifies a mathematical task under its stated assumptions; no project proof or certificate has been checked.

**Empirical support and limits:** No empirical claim is made.

### Methods and obstacles

**Proposed methods:**

- finite search
- exact computation
- symbolic derivation
- classification

**Expected obstacles:**

- A sign error in conditional mutual information invalidates every derived certificate.
- A floating-point LP can mislabel redundancy near a face.
- The finite search may generate only Shannon consequences.
- No result for one copy or one coefficient bound implies a result for all iterated copies.
- Naive enumeration and rational coefficient growth may consume substantial memory.

### Checks still needed

- No proof or certificate establishes whether the three-row coefficient restriction can yield any non-Shannon inequality.
- No novelty comparison of hypothetical output against known five-variable inequalities has been performed.

<a id="evidence"></a>

## Evidence and context

**Status basis:** The copy-lemma encoding is supported by Csirmaz's Definition 24 and Lemma 27. The finite three-row, coefficient-{1,2} search is curator-proposed; neither its novelty nor its ability to yield a non-Shannon consequence has been established. The two-variable conditioning avoids the singleton obstruction only.

[Dated literature checks and remaining limits](../candidates/Q-FORMAL-003.md#literature-checks). These are editorial evidence checks, not signed expert reviews.

**Exact problem / theorem locator:** SRC-FORMAL-004, Section 6, Definition 24 and Lemma 27 (full copy and restriction), Section 6.3 Claims 31-32, and Problem 6; bounded protocol is curator-proposed

### Sources

- [Exploring the entropic region](../sources.md#src-formal-004). Laszlo Csirmaz. 2025. [Read source](https://arxiv.org/html/2509.12439v1).
  - **Relevant sections:** Sections 2, 6 and 9.5; Definition 24; Lemma 27; Claims 31-32; Problems 2, 6, 7
  - **Source limitations:** Problem 6 must be read with the 2026 follow-up SRC-FORMAL-016; listing a question in 2025 does not establish its current status.
- [Information Inequalities for Five Random Variables](../sources.md#src-formal-016). Elod P. Csirmaz; Laszlo Csirmaz. 2026. [Read source](https://arxiv.org/html/2512.23316v2).
  - **Relevant sections:** Introduction; Sections 3–5 and 10
  - **Source limitations:** Preprint first submitted December 2025, inspected revision 3 March 2026. Author code and computed output have not been executed or independently verified.

### Known results and partial progress

- SRC-FORMAL-004, Definition 24 and Lemma 27, licenses this A={1} copy over D={2,3}: construct a full copy of E={1,4,5} conditional on D and restrict to the copy X6 of X1.
- SRC-FORMAL-004, Claim 32, guarantees a polymatroid copy when |D| is 1 or |N|-1, precluding a non-Shannon consequence from those cases. Here |N|=5 and |D|=2, so that claim gives no blanket obstruction.
- SRC-FORMAL-004, Claim 31, still gives an obstruction on the subclass H23=H2+H3: all polymatroids satisfying that extra condition admit the copy. Independence of X2 and X3 is not an assumption of this proposal.
- A 2026 paper already reports systematic five-variable inequalities from a different MEM construction; baseline certificates are not presumed novel.

**Research value:** Potentially useful research infrastructure for separating numerical search from verifiable derivation. Scientific significance of this particular small census is uncertain and requires specialist review.

### Related problems

- **Method preparation for:** [Classify entropic and almost-entropic extremal rays of the five-variable Shannon cone](../candidates.md#q-formal-004). Certificate skills could support exclusions of particular rays, but this finite census does not classify all rays.
- **Related method:** [Compare maximum-entropy and iterated copy-lemma inequality methods](../candidates.md#q-formal-005). A fixed single-copy search says nothing decisive about the unrestricted comparison of MEM and iterated copy methods.

### Scope of the status check

**Finding:** The copy-lemma encoding is supported by Csirmaz's Definition 24 and Lemma 27. The finite three-row, coefficient-{1,2} search is curator-proposed; neither its novelty nor its ability to yield a non-Shannon consequence has been established. The two-variable conditioning avoids the singleton obstruction only.

**Search limits:** No proof or certificate establishes whether the three-row coefficient restriction can yield any non-Shannon inequality. No novelty comparison of hypothetical output against known five-variable inequalities has been performed.

<details>
<summary>Literature references checked</summary>

**Queries used:**

- "Information Inequalities for Five Random Variables" "copy"

**Sources checked:**

- [Exploring the entropic region](../sources.md#src-formal-004)
- [Information Inequalities for Five Random Variables](../sources.md#src-formal-016)

</details>

<details>
<summary>Previous attempts and public records</summary>

- Csirmaz and Csirmaz's 2026 paper reports related five-variable computational and theoretical work. No claim that its algorithm is identical to this bounded protocol.
- No project attempt or model trial has been made.

</details>

<details>
<summary>Attribution and suggested citation</summary>

**Original authors and credited contributors:**

- Zhang and Yeung (origin of the non-Shannon copy construction, as credited in the survey)
- Laszlo Csirmaz
- Elod P. Csirmaz

**Suggested citation:** Csirmaz (2025), Exploring the entropic region, arXiv:2509.12439v1, Definition 24, Lemma 27 and Section 6.3 Claims 31-32; Csirmaz and Csirmaz (2026), Information Inequalities for Five Random Variables, arXiv:2512.23316v2. The bounded census and its conditioning set are curator-proposed.

**Editorial credit:** Compiled for Theory Research Atlas with AI assistance.

</details>

<a id="assessment"></a>

## AI trial assessment

**Label:** [Preparation needed](../ai-assessment.md). **Evidence:** Untested forecast. **Assessed:** 2026-10-13.

The finite specification supports exact checking and automated generation. Usefulness within the stated support and coefficient limits remains unverified; an information theorist should assess these limits and existing coverage before execution.

**Model or capability conditions:** No named model evaluated; assumes tool-using AI can generate rational linear-algebra code and independently check derivation certificates under expert supervision.

**Uncertainty:** High uncertainty about usefulness, output count, runtime and novelty. No theorem or computation establishing a non-Shannon output within support at most three and coefficients in {1,2} has been checked. Claim 31 covers degenerate conditioning subclasses; recent five-variable work also narrows what can count as progress.

Ratings are separate judgments, not a score. High expertise needed or verification difficulty means a larger burden; high method availability or checkability means stronger support.

| Dimension | Rating | Reason |
| --- | --- | --- |
| Statement clarity | High | Variables, constraints, support limit and coefficient set are explicit. |
| Decomposability | High | Separate semantic encoding, enumeration, elimination, normalization and implication checking. |
| Methods and literature | High | Copy-lemma and polyhedral methods are documented. |
| Search / symbolic fit | High | Finite search and rational certificates are the central workflow. |
| Checkability | High | Each retained inequality can be checked by exact vector arithmetic. |
| Expertise needed | High | An expert must verify the extension semantics and distinguish non-Shannon validity from novelty. |
| Scholarly significance | Unknown | The bounded task may generate only elementary consequences; value depends on later review. |
| Verification difficulty | Medium | Certificate arithmetic is mechanical; statement alignment and novelty are harder. |

**Correctness:** No project answer.

The cited literature supports the problem statement. No project answer has been submitted for review.

**Novelty:** Not claimed.

This is a curator-proposed bounded search specification. Neither the packaging nor any potential output is claimed novel; compare future certificates and projected inequalities with known Shannon consequences and existing copy-lemma results before asserting new information.

<details>
<summary>Difficulty and significance</summary>

**Difficulty:** Medium.

The reasons are given in the [AI trial assessment](#assessment).

**Evidence type:** Editorial estimate not measured.

**Significance:** Unknown.

The reasons are given under [research value](#evidence).

</details>

<a id="audit-trail"></a>

## Research records

No project attempts or human reviews have been recorded.

<details>
<summary>Changes to this problem</summary>

| Date | Change |
| --- | --- |
| 2026-10-14 | Compared the statement and status evidence with the dated literature check; updated source references and remaining information gaps. No research attempt or signed review is recorded. |

</details>

<details>
<summary>Record information</summary>

| Field | Recorded value |
| --- | --- |
| Stable ID | `Q-FORMAL-003` |
| Duplicate key | `build-a-bounded-exact-copy-lemma-certificate-census` |
| Original domain label | Information theory |
| Original cross-domain labels | Exact computation; Polyhedral computation |
| Primary domain ID | `INFO.ENTROPY` |
| Cross-domain IDs | `MATH.OPT` |
| Origin code | `curator_proposed` |
| Status code | `unverified` |
| Curator-designed scope | Yes |
| Detailed entry | Yes |
| Record level | `C` |
| Human review status | `pending` |
| Trial-label code | `preparation_required` |
| Assessment-evidence code | `untested_forecast` |
| Method tags | `finite_search`, `exact_computation`, `symbolic_derivation`, `classification`, `certificate_checking` |
| Validation tags | `pure_proof`, `exact_computation` |
| Experimental-dependency tag | `none_for_formal_task` |

[JSON record](../../data/cards/Q-FORMAL-003.json)

</details>

[Problem cards](README.md) · [Back to top](#at-a-glance)
