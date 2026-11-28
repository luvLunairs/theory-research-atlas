# Channel reliability function

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-455 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-455%3A+Channel+reliability+function&target=Q-FORMAL-455) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-455%3A+Channel+reliability+function&target=Q-FORMAL-455)

For a discrete memoryless channel with finite alphabets and maximum-likelihood decoding, find an exact single-letter expression for the largest exponential decay rate of the average error over sequences of rate-R block codes, including the low-rate region where known exponents differ. The source also asks about mismatched decoding.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-11-28.

**Status basis:** The workshop asks for an exact single-letter expression for the optimal average-error exponent. Boche and Deppe describe the unresolved low-rate region and study limits on uniform channel-by-channel computation. For binary symmetric channels, Barg and McGregor identify a range below the critical rate where the random-coding exponent is exact. Somekh-Baruch gives a converse for general channels. Gaps remain in the matched-decoding formulation.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** The problem statement and references listed in the 28 November 2026 literature check were inspected.

**Scope limits:** The candidate tracks matched decoding. The workshop also poses the wider problem with a prescribed mismatched metric.

**Information still needed**

- For any proposed formula specify the channel, rate range and decoding metric, and show matching achievability and converse exponents.

**Primary branch:** [Classical information theory](../domains/info.md#info-shannon). **Related branches:** None recorded.

**Sources:** [New Mathematical Techniques in Information Theory](../sources.md#src-formal-445); [An Upper Bound on the Reliability Function of the DMC](../sources.md#src-math-933); [The Computability of the Channel Reliability Function and Related Bounds](../sources.md#src-math-931); [Distance distribution of binary codes and the error probability of decoding](../sources.md#src-math-932).

**Exact locator:** Somekh-Baruch, Oberwolfach report, p. 699, question 2. Boche and Deppe, introduction and discussion of Theorem 3. Barg and McGregor, abstract.

**Potential difficulty:** Unknown. The source identifies an unresolved research target; its present difficulty has not been independently assessed.

**Possible AI role:** Compare upper and achievable lower exponents on a fixed input alphabet and rate interval, retaining the optimal-code and blocklength limits.

**Verification burden:** High. Achievability and converse arguments must match channel, coding, error and asymptotic conventions; local numerical extrema are insufficient.

**Resource expectations:** No physical channel experiment is required for the formal question. Alphabet optimization and symbolic calculations may be costly; no resource bound is established.

**Assessment:** 2026-11-28; untested forecast. **Uncertainty:** For any proposed formula specify the channel, rate range and decoding metric, and show matching achievability and converse exponents. Model performance on this task has not been measured.

**Further work:** define a scoped target, resource requirements and a verification plan before developing a full card. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-28

**Coverage:** Statement and later literature. **Statement:** Corrected.

**Recorded status:** Unverified → Source reports open.

The workshop asks for an exact single-letter expression for the optimal average-error exponent. Boche and Deppe describe the unresolved low-rate region and study limits on uniform channel-by-channel computation. For binary symmetric channels, Barg and McGregor identify a range below the critical rate where the random-coding exponent is exact. Somekh-Baruch gives a converse for general channels. Gaps remain in the matched-decoding formulation.

**Search scope:** Somekh-Baruch, Oberwolfach report, p. 699, question 2. Boche and Deppe, introduction and discussion of Theorem 3. Barg and McGregor, abstract.

<details>
<summary>Previous indexed wording</summary>

Characterize the optimal error exponent of discrete memoryless channels at rates where existing reliability bounds differ.

The current statement appears at the top of this page.
</details>

**Inspected evidence**

- [New Mathematical Techniques in Information Theory](../sources.md#src-formal-445) — Printed p. 699, open question 2. Asks for an exact single-letter expression with average decoding error and explicitly includes matched and mismatched decoding.
- [An Upper Bound on the Reliability Function of the DMC](../sources.md#src-math-933) — Abstract on the genie-receiver converse. Gives a channel-coding converse that improves on the sphere-packing bound in examples.
- [The Computability of the Channel Reliability Function and Related Bounds](../sources.md#src-math-931) — Introduction and discussion after Theorem 3 on the critical rate and known reliability intervals. Describes the unresolved low-rate characterization and studies computability as a function of the channel and rate.
- [Distance distribution of binary codes and the error probability of decoding](../sources.md#src-math-932) — Version 3, abstract on binary symmetric channels and maximum-likelihood decoding. Identifies an interval immediately below the critical rate where the random-coding exponent gives the reliability function for the binary symmetric channels covered by the theorem.

**Limits and remaining work**

- For any proposed formula specify the channel, rate range and decoding metric, and show matching achievability and converse exponents.

<details>
<summary>Search queries</summary>

- reliability function DMC low rates exact single letter expression 2025 2026
- Somekh-Baruch upper bound reliability function Barg McGregor below critical rate


</details>

### 2026-10-14

**Coverage:** Statement only. **Statement:** Matched.

**Recorded status:** Unverified → Unverified.

The source supports identifying this question, but does not establish its present unresolved status.

**Search scope:** Inspected the named source statement and its recorded qualifications; no comprehensive citation-chain or specialist database review. The listed targeted searches were exploratory; no verified later source establishing current resolution status was obtained.

**Inspected evidence**

- [New Mathematical Techniques in Information Theory](../sources.md#src-formal-445) — p. 699, Anelia Somekh-Baruch. The source identifies the indexed question or research direction; its original date and any recorded partial results limit what it establishes about present status.

**Limits and remaining work**

- Specify matched or mismatched decoding, rate regime and error criterion before selecting a subproblem.
- Current resolution status was not established by a completed later-literature review.

<details>
<summary>Search queries</summary>

- "reliability function" "discrete memoryless" "2026" "open"


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
