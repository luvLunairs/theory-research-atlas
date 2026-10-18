# Audit finite-sample split likelihood-ratio coverage in a Bernoulli model

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

Train a probability estimate on one half of a small coin-flip sample and evaluate it on the other half. Check that the resulting confidence set covers the true probability at the promised rate, without replacing exact evidence by simulation.

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-002%3A+Audit+finite-sample+split+likelihood-ratio+coverage+in+a+Bernoulli+model&target=Q-FORMAL-002) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-002%3A+Audit+finite-sample+split+likelihood-ratio+coverage+in+a+Bernoulli+model&target=Q-FORMAL-002)

[At a glance](#at-a-glance) · [The task](#problem) · [Resources and verification](#verification) · [Evidence and context](#evidence) · [AI trial assessment](#assessment) · [Research records](#audit-trail)

<a id="at-a-glance"></a>

## At a glance

| Field | Summary |
| --- | --- |
| Primary field | [Inference and decision theory](../domains/stat.md#stat-infer) |
| Related fields | [Probability foundations and limit theory](../domains/prob.md#prob-found) |
| Task origin | [Known-result calibration](../evidence-policy.md) |
| Current status | [Known result in literature](../evidence-policy.md) · checked 2026-10-13 |
| AI suitability | [Priority for a later trial](../ai-assessment.md) · Untested forecast |
| Scientific review | Pending |

<a id="problem"></a>

## The task

### Precise statement

Specialize universal inference to iid Bernoulli(p), a prespecified split of 20 observations into two groups of 10, training estimator q=(K1+1)/12, and alpha=1/20. Reproduce the all-p coverage proof and exact rejection probabilities on p in {1/10,...,9/10}.

**Required output:** Prove P_p(p in C)&gt;=19/20 for every p in [0,1], where C={theta: q^K0(1-q)^(10-K0)/[theta^K0(1-theta)^(10-K0)] &lt;=20}; report exact rejection probabilities for nine specified rational p values.

**Scope:** Reproduce a known guarantee and create a small exact benchmark. The selected sample size, smoothing rule and evaluation grid are curator choices. No claim of an optimal test, new interval or real-world model adequacy is included.

### Assumptions

- Y1,...,Y20 are iid Bernoulli(p), with p in [0,1].
- The first ten observations form D1 and the remaining ten form D0; the split is fixed before data are seen.
- K1 and K0 are their respective success counts.
- Use q=(K1+1)/12 and alpha=1/20; do not optimize either using the holdout data.
- The ratio on the true distribution's support is well-defined; define endpoint confidence-set behavior explicitly.
- Use the Bernoulli likelihood convention 0^0=1. Set the likelihood ratio to +infinity if its denominator is zero; the smoothed training estimator makes the numerator strictly positive. Retain T&lt;=20 and reject only T&gt;20.

### Success criteria

1. Give the all-p coverage argument with independence and conditioning explicit.
2. Enumerate the 121 pairs (K1,K0) for each grid value using exact arithmetic and exact strict comparison T&gt;20.
3. Report rational probabilities with a reproducible independent checker.
4. Treat endpoint p=0 and p=1 separately rather than silently dividing by zero.
5. Retain this as a calibration result, even if the AI completes it.

### Background needed

- Bernoulli and binomial distributions
- Conditional expectation
- Markov's inequality
- Exact rational arithmetic

<a id="verification"></a>

## Resources and verification

### Resource requirements

**Computing:** Small finite enumeration over 121 count pairs at each of nine rational parameter values. Rational bit sizes should be logged; wall time, memory and cost have not been measured.

**Data:** No observed data required. The finite outcome space is specified mathematically.

**Experiments:** none

**Theory and model requirements:** iid Bernoulli sampling and a prespecified independent holdout split. The theorem's validity does not establish that actual observations obey this model.

**Validation modes:** Proof, Exact computation.

### Verification steps

1. Derive the conditional expectation bound at the true parameter.
2. Verify the sample-count mass formula using binomial coefficients independently.
3. Use exact rational arithmetic to compare the test statistic with 20.
4. Sum rejection masses separately for each specified p and cross-check with a second implementation or manual cases.
5. Review the p=0 and p=1 support cases and document the confidence-set endpoint convention.

**Statement alignment:** Report a fixed-sample guarantee under iid sampling. Do not claim optional-stopping safety or empirical coverage in an unspecified real dataset.

**Human review difficulty:** Moderate; probability review is necessary despite a small program.

### Formal validity and empirical support

**What the formal task can establish:** The card specifies a mathematical task under its stated assumptions; no project proof or certificate has been checked.

**Empirical support and limits:** No empirical claim is made. For statistical models, real-data model adequacy would require separate evidence.

### Methods and obstacles

**Proposed methods:**

- proof reconstruction
- exact computation
- symbolic derivation

**Expected obstacles:**

- Reusing holdout data to choose q breaks the conditioning argument.
- Floating-point comparisons near T=20 can misclassify outcomes.
- Checking nine values of p is not an all-p coverage proof.
- Returning an interval hull is different from returning the exact confidence set.

### Checks still needed

- An independent reviewer should confirm whether the benchmark's reproduction depth is sufficient before attempting power optimization.
- Any extension to repeated splits, dependence or misspecification requires a separate problem record and proof.

<a id="evidence"></a>

## Evidence and context

**Status basis:** The guarantee follows from the published theorem under its assumptions. The finite Bernoulli benchmark is a curator-selected reproduction protocol; no calculation has been run.

**Exact problem / theorem locator:** SRC-FORMAL-003, Section 2, Theorem 1; finite parameters chosen for calibration

### Sources

- [Universal Inference](../sources.md#src-formal-003). Larry Wasserman; Aaditya Ramdas; Sivaraman Balakrishnan. 2020. [Read source](https://arxiv.org/html/1912.11436v4).
  - **Relevant sections:** Section 2, equations (3)–(7), Theorem 1
  - **Source limitations:** Journal year is 2020; arXiv first submission was 2019. No claim that arbitrary data-dependent split choices retain validity. Pin the arXiv v4 identifier when citing; generated HTML front-matter dates need not equal the arXiv revision date.
- [Game-Theoretic Statistics and Safe Anytime-Valid Inference](../sources.md#src-formal-010). Aaditya Ramdas; Peter Grünwald; Vladimir Vovk; Glenn Shafer. 2023. [Read source](https://arxiv.org/html/2210.01948v2).
  - **Relevant sections:** Sections 2.1–2.8, 3.3.1 and 8.2.1–8.2.4
  - **Source limitations:** The arXiv revision record says 17 June 2023; the generated HTML displays an August 2026 document date. Use revision metadata and verify PDF date before bibliographic export.

### Known results and partial progress

- Universal Inference, Theorem 1, provides the finite-sample guarantee.
- The SAVI review places this construction among e-value and e-process methods; fixed-split validity is not unrestricted optional-stopping validity.

**Research value:** Tests the project's ability to distinguish theorem validity, numerical auditing and assumptions about data generation. It can reveal leakage and threshold-convention mistakes before harder statistical research.

### Related problems

No formal dependency or equivalence is asserted.

### Scope of the status check

**Finding:** The exact primary theorem and proof were inspected. The later review identifies the method. This is a known-result specialization.

**Search limits:** No search for every existing Bernoulli implementation or benchmarking protocol; novelty is not asserted.

<details>
<summary>Literature references checked</summary>

**Sources checked:**

- [Universal Inference](../sources.md#src-formal-003)
- [Game-Theoretic Statistics and Safe Anytime-Valid Inference](../sources.md#src-formal-010)

</details>

<details>
<summary>Previous attempts and public records</summary>

- Published universal-inference theorem; no project code, simulations or model attempt have been run.

</details>

<details>
<summary>Attribution and suggested citation</summary>

**Original authors and credited contributors:**

- Larry Wasserman
- Aaditya Ramdas
- Sivaraman Balakrishnan

**Suggested citation:** Wasserman, Ramdas and Balakrishnan (2020), Universal Inference, PNAS 117(29), 16880–16890; arXiv:1912.11436v4, Theorem 1.

**Editorial credit:** Compiled for Theory Research Atlas with AI assistance.

</details>

<a id="assessment"></a>

## AI trial assessment

**Label:** [Priority for a later trial](../ai-assessment.md). **Evidence:** Untested forecast. **Assessed:** 2026-10-13.

The proof and exact finite audit provide two complementary checks with limited implementation scope. The relevant capability is disciplined conditioning and exact arithmetic, not confidence asserted by a model.

**Model or capability conditions:** No named model evaluated; assumes tool-using AI capable of elementary probability proofs and exact-arithmetic programming.

**Uncertainty:** No implementation, empirical success rate or model comparison exists. A later protocol change, especially repeated split selection, may invalidate the reference guarantee.

Ratings are separate judgments, not a score. High expertise needed or verification difficulty means a larger burden; high method availability or checkability means stronger support.

| Dimension | Rating | Reason |
| --- | --- | --- |
| Statement clarity | High | Data model, estimator, threshold, finite grid and endpoint cases are fixed. |
| Decomposability | High | Separate proof, count-pair probabilities, rejection decision and table audit. |
| Methods and literature | High | A primary theorem and a later survey supply the needed framework. |
| Search / symbolic fit | High | Exact arithmetic and symbolic probability are directly useful. |
| Checkability | High | Each finite result has a short rational certificate and a separate general proof. |
| Expertise needed | Medium | A statistician should review leakage, support and coverage arguments. |
| Scholarly significance | Medium | Calibration has methodological value; there is no novelty claim. |
| Verification difficulty | Medium | Small enumeration is easy, but it cannot replace the proof for all p. |

**Correctness:** No project answer.

The cited literature supports the problem statement. No project answer has been submitted for review.

**Novelty:** Not claimed.

The target is a known result; no originality is claimed for the selected scope. Any later novelty claim requires a literature check.

<details>
<summary>Difficulty and significance</summary>

**Difficulty:** Low to medium.

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
| Stable ID | `Q-FORMAL-002` |
| Duplicate key | `audit-finite-sample-split-likelihood-ratio-coverage-in-a-bernoulli-model` |
| Original domain label | Statistical theory |
| Original cross-domain labels | Probability theory; Exact computation |
| Primary domain ID | `STAT.INFER` |
| Cross-domain IDs | `PROB.FOUND` |
| Origin code | `known_result_calibration` |
| Status code | `known_result` |
| Curator-designed scope | Yes |
| Detailed entry | Yes |
| Record level | `C` |
| Human review status | `pending` |
| Trial-label code | `priority_trial` |
| Assessment-evidence code | `untested_forecast` |
| Method tags | `proof`, `exact_computation`, `symbolic_derivation` |
| Validation tags | `pure_proof`, `exact_computation` |
| Experimental-dependency tag | `none_for_formal_task` |

[JSON record](../../data/cards/Q-FORMAL-002.json)

</details>

[Problem cards](README.md) · [Back to top](#at-a-glance)
