# Sample complexity of approximately private PAC learning

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-439 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-439%3A+Sample+complexity+of+approximately+private+PAC+learning&target=Q-FORMAL-439) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-439%3A+Sample+complexity+of+approximately+private+PAC+learning&target=Q-FORMAL-439)

Characterize the optimal sample complexity of approximate-differentially-private PAC learning for finite concept classes, quantifying its possible separation from nonprivate complexity measured by VC dimension.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Source reports open. **Last checked:** 2026-11-28.

**Status basis:** At fixed accuracy, confidence and privacy parameters, Moran and Yan obtain an upper bound of order d log d for Littlestone dimension d. They explicitly leave open whether a polynomial in the VC dimension and log-star d suffices. This is the regime in which a finite class can have a large gap between its two dimensions.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Nissim, Stemmer and Tsfadia, COLT 2026 problem statement. Moran and Yan, October 2026, introduction and the discussion after the general sample bound.

**Scope limits:** At fixed accuracy, confidence and privacy parameters, Moran and Yan obtain an upper bound of order d log d for Littlestone dimension d. They explicitly leave open whether a polynomial in the VC dimension and log-star d suffices. This is the regime in which a finite class can have a large gap between its two dimensions.

**Information still needed**

- A worst-case dependence on Littlestone dimension does not settle the sharper joint dependence. The published open-problem statement and October preprint concern approximate privacy.

**Primary branch:** [Statistical learning and high-dimensional theory](../domains/stat.md#stat-learn). **Related branches:** None recorded.

**Sources:** [Invited Open Problem: Does Differential Privacy Make PAC Learning Much Harder?](../sources.md#src-formal-437); [Nearly Linear Private Learning of Littlestone Classes](../sources.md#src-model-926).

**Exact locator:** Nissim, Stemmer and Tsfadia, COLT 2026 problem statement. Moran and Yan, October 2026, introduction and the discussion after the general sample bound.

**Potential difficulty:** Unknown. The source identifies an unresolved research target; its present difficulty has not been independently assessed.

**Possible AI role:** Compare known upper and lower bounds on classes where the VC and Littlestone dimensions grow at different rates.

**Verification burden:** High. Upper and lower bounds must use identical distribution classes, loss, privacy or oracle conditions and quantifiers; statistical counterexamples need exact arguments.

**Resource expectations:** The formal target needs no new physical experiment. Simulations may use synthetic samples; necessary sample counts and computational costs have not been estimated.

**Assessment:** 2026-11-28; untested forecast. **Uncertainty:** A worst-case dependence on Littlestone dimension does not settle the sharper joint dependence. The published open-problem statement and October preprint concern approximate privacy.

**Further work:** define a scoped target, resource requirements and a verification plan before developing a full card. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-28

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Source reports open.

At fixed accuracy, confidence and privacy parameters, Moran and Yan obtain an upper bound of order d log d for Littlestone dimension d. They explicitly leave open whether a polynomial in the VC dimension and log-star d suffices. This is the regime in which a finite class can have a large gap between its two dimensions.

**Search scope:** Compared the indexed question with the passages and later records listed below.

**Inspected evidence**

- [Invited Open Problem: Does Differential Privacy Make PAC Learning Much Harder?](../sources.md#src-formal-437) — Abstract, finite-class comparison. Distinguishes finite-class private complexity from the nonprivate VC benchmark.
- [Nearly Linear Private Learning of Littlestone Classes](../sources.md#src-model-926) — Introduction, theorem for general Littlestone classes and the following paragraph on the log-star question. The authors obtain O(d log d) sample complexity at fixed learning and privacy parameters for Littlestone dimension d. They explicitly retain the question about a polynomial in the VC dimension and log-star d.

**Limits and remaining work**

- A worst-case dependence on Littlestone dimension does not settle the sharper joint dependence. The published open-problem statement and October preprint concern approximate privacy.

<details>
<summary>Search queries</summary>

- Nissim Stemmer Tsfadia finite concept classes private PAC log-star Littlestone dimension Moran Yan 2026


</details>

### 2026-10-14

**Coverage:** Access limited. **Statement:** Needs clarification.

**Recorded status:** Unverified → Unverified.

The source supports identifying this question, but does not establish its present unresolved status.

**Search scope:** Read the publisher's abstract and bibliographic record. The full formal problem note was not successfully inspected; targeted discovery did not establish a later resolution.

**Inspected evidence**

- [Invited Open Problem: Does Differential Privacy Make PAC Learning Much Harder?](../sources.md#src-formal-437) — Abstract. The source identifies the indexed question or research direction; its original date and any recorded partial results limit what it establishes about present status.

**Limits and remaining work**

- The precise conjectured dependence on class size and privacy parameters needs extraction; current status beyond this 2026 problem note is unchecked.
- No exhaustive search for subsequent resolutions was completed.
- Full-text model assumptions and quantitative targets remain unverified; an abstract alone is insufficient for a complete statement check.

<details>
<summary>Search queries</summary>

- "Does Differential Privacy Make PAC Learning Much Harder"


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
