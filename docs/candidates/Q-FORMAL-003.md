# Build a bounded exact copy-lemma certificate census

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-003 · Full card available.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-003%3A+Build+a+bounded+exact+copy-lemma+certificate+census&target=Q-FORMAL-003) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-003%3A+Build+a+bounded+exact+copy-lemma+certificate+census&target=Q-FORMAL-003)

For five original finite random variables X1,...,X5 and one conditional copy X6 of X1 over (X2,X3), enumerate sums of at most three distinct elemental six-variable Shannon inequalities, each with coefficient 1 or 2. Use exactly the four marginal entropy equalities H(6,S)=H(1,S) for S subset of {2,3}, including the empty set, and I(6;1,4,5|2,3)=0. Determine which sums eliminate all coordinates involving X6 after adding rational combinations of those five equality rows; retain exact certificates and canonical projected inequalities.

**Origin:** Curator proposal. **Curator-designed scope:** Yes.

**Current status:** Unverified. **Last checked:** 2026-10-14.

**Status basis:** The copy-lemma encoding is supported by Csirmaz's Definition 24 and Lemma 27. The finite three-row, coefficient-{1,2} search is curator-proposed; neither its novelty nor its ability to yield a non-Shannon consequence has been established. The two-variable conditioning avoids the singleton obstruction only.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Recorded source years: SRC-FORMAL-004: 2025, SRC-FORMAL-016: 2026. The last-checked date records the scope described in the status basis; it is not a comprehensive literature-search date.

**Scope limits:** Curator-proposed finite protocol, not a literature-established open conjecture. Preserve four marginal equalities and full conditional-independence equality.

**Information still needed**

- No proof or certificate establishes whether the three-row coefficient restriction can yield any non-Shannon inequality.
- No novelty comparison of hypothetical output against known five-variable inequalities has been performed.

**Primary branch:** [Entropy inequalities and information geometry](../domains/info.md#info-entropy). **Related branches:** [Optimization and operations research](../domains/math.md#math-opt).

**Sources:** [Exploring the entropic region](../sources.md#src-formal-004); [Information Inequalities for Five Random Variables](../sources.md#src-formal-016).

**Exact locator:** SRC-FORMAL-004, Section 6, Definition 24 and Lemma 27 (full copy and restriction), Section 6.3 Claims 31-32, and Problem 6; bounded protocol is curator-proposed

**Potential difficulty:** Medium. The finite specification supports exact checking and automated generation. Usefulness within the stated support and coefficient limits remains unverified; an information theorist should assess these limits and existing coverage before execution.

**Possible AI role:** No named model evaluated; assumes tool-using AI can generate rational linear-algebra code and independently check derivation certificates under expert supervision.

**Verification burden:** Medium. Certificate arithmetic is mechanical; statement alignment and novelty are harder.

**Resource expectations:** Experiment: none Data: Mathematical constraints and the cited publications. Public code from the 2026 article is a possible later comparison resource, not an ingested dataset. Computation: Six variables produce 63 nonempty entropy coordinates. There are 6 + choose(6,2)*2^4 = 246 elemental Shannon rows; candidate sums grow combinatorially with support. Stream and deduplicate, record exact arithmetic bit growth, and impose a later measured resource cap. No CPU/GPU time or monetary budget is estimated.

**Assessment:** 2026-10-13; untested forecast. **Uncertainty:** High uncertainty about usefulness, output count, runtime and novelty. No theorem or computation establishing a non-Shannon output within support at most three and coefficients in {1,2} has been checked. Claim 31 covers degenerate conditioning subclasses; recent five-variable work also narrows what can count as progress.

[Read the full card](../cards/Q-FORMAL-003.md). **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-10-14

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Unverified.

The copy-lemma encoding is supported by Csirmaz's Definition 24 and Lemma 27. The finite three-row, coefficient-{1,2} search is curator-proposed; neither its novelty nor its ability to yield a non-Shannon consequence has been established. The two-variable conditioning avoids the singleton obstruction only.

**Search scope:** Re-read the copy definition, existence lemma and obstruction, then the 2026 paper's no-new-inequality section. No enumeration or proof search was run.

**Inspected evidence**

- [Exploring the entropic region](../sources.md#src-formal-004) — SRC-FORMAL-004, Section 6, Definition 24 and Lemma 27 (full copy and restriction), Section 6.3 Claims 31-32, and Problem 6; bounded protocol is curator-proposed. The source identifies the indexed question or research direction; its original date and any recorded partial results limit what it establishes about present status.
- [Exploring the entropic region](../sources.md#src-formal-004) — Definition 24; Lemma 27; Section 6.3, Claims 31–32. The copying constraints are valid, while singleton conditioning is insufficient for new inequalities.
- [Information Inequalities for Five Random Variables](../sources.md#src-formal-016) — Section 4.3, Claim 6; Section 4.4. A modular conditioning restriction also obstructs new inequalities; this does not establish utility of the indexed finite search.

**Limits and remaining work**

- No proof or certificate establishes whether the three-row coefficient restriction can yield any non-Shannon inequality.
- No novelty comparison of hypothetical output against known five-variable inequalities has been performed.

<details>
<summary>Search queries</summary>

- "Information Inequalities for Five Random Variables" "copy"


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
