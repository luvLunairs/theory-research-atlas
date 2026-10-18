# Structure-agnostic minimax risk in the partial linear model

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-FORMAL-435 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-FORMAL-435%3A+Structure-agnostic+minimax+risk+in+the+partial+linear+model&target=Q-FORMAL-435) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-FORMAL-435%3A+Structure-agnostic+minimax+risk+in+the+partial+linear+model&target=Q-FORMAL-435)

Determine the minimax risk for estimating the linear coefficient in the partial linear model when nuisance estimators are supplied as black boxes, without structural smoothness assumptions. Is double machine learning optimal once variance is included in the benchmark?

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Unverified. **Last checked:** 2026-10-15.

**Status basis:** Hu and Simchi-Levi claim matching two-learner bounds. Gu's preceding upper-bound paper is now linked and its assumptions were inspected. The exact comparison with the original problem and independent proof review remain incomplete; the claim does not establish an accepted resolution in this index.

**Statement check:** Needs clarification. **Status check:** Later literature checked.

**Source date and freshness:** Original COLT question: 2025. Gu's upper-bound paper: 23 July 2026. Hu–Simchi-Levi claim: 7 September 2026. Selected statements compared on 15 October 2026.

**Scope limits:** The recent claim distinguishes separate approximation and stochastic budgets for two learners. Its sharp asymptotic statement assumes their sum tends to zero; it must not be described as a bound for arbitrary fixed budgets.

**Information still needed**

- Read the full original COLT note to compare the intended statistical experiment and allowed black-box access.
- Align Gu's Corollary 3.2 with Hu–Simchi-Levi's Theorems 4.1–4.2 and Corollary 4.3, including the vanishing-budget regime and loss conversion.
- Review the lower-bound construction and check for corrections or publication.

**Primary branch:** [Causal inference and identifiability](../domains/stat.md#stat-causal). **Related branches:** None recorded.

**Sources:** [Open Problem: Structure-Agnostic Minimax Risk for Partial Linear Model](../sources.md#src-formal-434); [Sharp Structure-Agnostic Minimax Risk for Partial Linear Models](../sources.md#src-formal-609); [Optimal use of a black-box learner in semiparametric estimation](../sources.md#src-review-703).

**Exact locator:** Abstract

**Potential difficulty:** Unknown. A September 2026 preprint claims the original minimax question is resolved; matching its boundedness, design and nuisance-class assumptions to the original problem remains necessary.

**Possible AI role:** First align the original statistical experiment with the claimed upper and lower bounds, then assist with a line-by-line proof and assumption audit. Simulations or a related minimax result cannot establish that the original question has been resolved.

**Verification burden:** High. Upper and lower bounds must use identical distribution classes, loss, privacy or oracle conditions and quantifiers; statistical counterexamples need exact arguments.

**Resource expectations:** The formal target needs no new physical experiment. Simulations may use synthetic samples; necessary sample counts and computational costs have not been estimated.

**Assessment:** 2026-10-14; untested forecast. **Uncertainty:** Full alignment with the original problem note and independent review of the 2026 lower-bound claim remain incomplete. No model or statistical experiment has been run.

**Further work:** resolve the statement and status questions above before planning an attempt. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-10-15

**Coverage:** Statement and later literature. **Statement:** Needs clarification.

**Recorded status:** Unverified → Unverified.

Gu's upper bound provides a documented dependency for the claimed matching risk. The original formulation, lower-bound proof and acceptance still need verification.

**Search scope:** Opened the COLT abstract, Gu's July preprint, and the September claim. Compared the cited upper-bound statement and the conditions on the claimed matching risk; the original COLT PDF remained unavailable.

**Inspected evidence**

- [Open Problem: Structure-Agnostic Minimax Risk for Partial Linear Model](../sources.md#src-formal-434) — Abstract. The original question concerns the role of variance in structure-agnostic optimality.
- [Optimal use of a black-box learner in semiparametric estimation](../sources.md#src-review-703) — Section 3.3, Condition 3.2 and Corollary 3.2. The two-learner bound separates approximation and stochastic errors and assumes consistent nuisance estimation.
- [Sharp Structure-Agnostic Minimax Risk for Partial Linear Models](../sources.md#src-formal-609) — Section 3; Corollary 4.3. The sharp characterization is stated for vanishing total budget under boundedness, uniform design and nondegeneracy conditions.

**Limits and remaining work**

- The complete original problem formulation has not been compared.
- Neither the full lower-bound proof nor independent acceptance has been established.

<details>
<summary>Search queries</summary>

- "Structure-Agnostic Minimax Risk" "Partial Linear"
- Yihong Gu "Structure-Agnostic" minimax 2026


</details>

### 2026-10-14

**Coverage:** Statement and later literature. **Statement:** Needs clarification.

**Recorded status:** Unverified → Unverified.

A September 2026 preprint by Hu and Simchi-Levi explicitly claims to resolve Gu's question with matching upper and lower bounds. The statement and model qualifications were inspected, but full alignment with Gu's original black-box model and the proof have not been verified. Retain as unverified, with a resolution claim requiring review.

**Search scope:** Compared the original PMLR abstract with the new preprint's introduction and Sections 3–4; the original linked PDF was not accessible through the available reader.

**Inspected evidence**

- [Open Problem: Structure-Agnostic Minimax Risk for Partial Linear Model](../sources.md#src-formal-434) — Abstract. The source identifies the indexed question or research direction; its original date and any recorded partial results limit what it establishes about present status.
- [Sharp Structure-Agnostic Minimax Risk for Partial Linear Models](../sources.md#src-formal-609) — Introduction, equations (1.1)–(1.2), and Sections 3–4. The authors claim a sharp risk characterization under explicit learner-budget and distributional assumptions.

**Limits and remaining work**

- Check Gu's full original model against the new boundedness, uniform-design, and nondegeneracy assumptions.
- Independently review the lower-bound argument and subsequent corrections.

<details>
<summary>Search queries</summary>

- "Structure-Agnostic Minimax Risk for Partial Linear Model"


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
