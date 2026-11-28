# Distribution-independent statistical queries versus dimension complexity

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-444 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-444%3A+Distribution-independent+statistical+queries+versus+dimension+complexity&target=Q-FORMAL-444) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-444%3A+Distribution-independent+statistical+queries+versus+dimension+complexity&target=Q-FORMAL-444)

Does distribution-independent statistical-query learnability imply low dimension complexity, under the formal definitions in Feldman, Kamath and Srebro's problem note?

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Unverified. **Last checked:** 2026-11-28.

**Status basis:** Patel reports a Boolean class with efficient distribution-free SQ learning at fixed error and superpolynomial exact dimension complexity. Mausberg reports a separate separation covering several approximation conventions. These claims directly address the SQ implication; the broader neural-network question has different hypotheses.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Feldman, Kamath and Srebro, COLT 2026, SQ question. Patel, September 2026, main theorem. Mausberg, October 2026 preprint record.

**Scope limits:** Patel reports a Boolean class with efficient distribution-free SQ learning at fixed error and superpolynomial exact dimension complexity. Mausberg reports a separate separation covering several approximation conventions. These claims directly address the SQ implication; the broader neural-network question has different hypotheses.

**Information still needed**

- The two separation arguments and their accuracy and dimension conventions have not been independently reviewed here.

**Primary branch:** [Statistical learning and high-dimensional theory](../domains/stat.md#stat-learn). **Related branches:** None recorded.

**Sources:** [Invited Open Problem: Is the Power of Deep Learning over Linear Models Inherently Distribution Dependent?](../sources.md#src-formal-441); [A Separation Between Distribution-Free SQ Learning and Dimension Complexity](../sources.md#src-model-922); [Distribution-independent SQ learning does not imply low dimension complexity](../sources.md#src-model-923).

**Exact locator:** Feldman, Kamath and Srebro, COLT 2026, SQ question. Patel, September 2026, main theorem. Mausberg, October 2026 preprint record.

**Potential difficulty:** Unknown. Assessing the two reported separations requires specialist review of the statistical-query and representation models.

**Possible AI role:** Compare the learning error, query tolerance and choice of deterministic or random feature maps in the two separation claims.

**Verification burden:** High. Upper and lower bounds must use identical distribution classes, loss, privacy or oracle conditions and quantifiers; statistical counterexamples need exact arguments.

**Resource expectations:** The formal target needs no new physical experiment. Simulations may use synthetic samples; necessary sample counts and computational costs have not been estimated.

**Assessment:** 2026-11-28; untested forecast. **Uncertainty:** The two separation arguments and their accuracy and dimension conventions have not been independently reviewed here.

**Further work:** resolve the statement and status questions above before planning an attempt. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-28

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Unverified.

Patel reports a Boolean class with efficient distribution-free SQ learning at fixed error and superpolynomial exact dimension complexity. Mausberg reports a separate separation covering several approximation conventions. These claims directly address the SQ implication; the broader neural-network question has different hypotheses.

**Search scope:** Compared the indexed question with the passages and later records listed below.

**Inspected evidence**

- [Invited Open Problem: Is the Power of Deep Learning over Linear Models Inherently Distribution Dependent?](../sources.md#src-formal-441) — COLT 2026 abstract, first question. Asks for a link between distribution-independent SQ learning and dimension complexity.
- [A Separation Between Distribution-Free SQ Learning and Dimension Complexity](../sources.md#src-model-922) — Version 1, introduction, main theorem and Section 2.1. For a Boolean class on n-bit inputs, the paper reports efficient distribution-free SQ learning to error 0.01 alongside superpolynomial exact dimension complexity.
- [Distribution-independent SQ learning does not imply low dimension complexity](../sources.md#src-model-923) — Author’s October 8 preprint record, abstract and linked release citation. The author reports a separation on a domain of size 2N³, with logarithmically many queries at fixed error and linear dimension for the stated deterministic and probabilistic variants.

**Limits and remaining work**

- The two separation arguments and their accuracy and dimension conventions have not been independently reviewed here.

<details>
<summary>Search queries</summary>

- distribution-independent SQ learnability dimension complexity Patel Mausberg Feldman Kamath Srebro separation


</details>

### 2026-10-14

**Coverage:** Access limited. **Statement:** Needs clarification.

**Recorded status:** Unverified → Unverified.

The source supports identifying this question, but does not establish its present unresolved status.

**Search scope:** Read the publisher's abstract and bibliographic record. The full formal problem note was not successfully inspected; targeted discovery did not establish a later resolution.

**Inspected evidence**

- [Invited Open Problem: Is the Power of Deep Learning over Linear Models Inherently Distribution Dependent?](../sources.md#src-formal-441) — Abstract, first question. The source identifies the indexed question or research direction; its original date and any recorded partial results limit what it establishes about present status.

**Limits and remaining work**

- Quantitative definitions of low dimension and SQ resources need full-statement extraction; no equivalence with a generic deep-learning claim is assumed.
- No exhaustive search for subsequent resolutions was completed.
- Full-text model assumptions and quantitative targets remain unverified; an abstract alone is insufficient for a complete statement check.

<details>
<summary>Search queries</summary>

- "Is the Power of Deep Learning over Linear Models"


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
