# Predicting perception after neural perturbation

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-CROSS-441 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-CROSS-441%3A+Predicting+perception+after+neural+perturbation&target=Q-CROSS-441) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-CROSS-441%3A+Predicting+perception+after+neural+perturbation&target=Q-CROSS-441)

Can a model of higher visual cortex predict how perceptual judgments change when a specified neural subpopulation is activated or suppressed? Predictions should distinguish the stimulus, neural target and behavioral task.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Unverified. **Last checked:** 2026-11-28.

**Status basis:** Shahbazi and coauthors measured which image changes macaques confused with localized stimulation in inferior temporal cortex. Those changes depended on the image and stimulation conditions. This supplies a concrete behavioral comparison within the broader modeling question.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Yamins and DiCarlo, Question 3 on perturbing subpopulations. Shahbazi and coauthors, 2024 abstract and Figure 1.

**Scope limits:** Shahbazi and coauthors measured which image changes macaques confused with localized stimulation in inferior temporal cortex. Those changes depended on the image and stimulation conditions. This supplies a concrete behavioral comparison within the broader modeling question.

**Information still needed**

- The task uses behavioral reports to infer perceptual effects. Generalization to other animals, stimuli and neural populations requires new evidence.

**Primary branch:** [Theoretical neuroscience](../domains/cog.md#cog-neuro). **Related branches:** None recorded.

**Sources:** [Eight open questions in the computational modeling of higher sensory cortex](../sources.md#src-cross-404); [Neural population control via deep image synthesis](../sources.md#src-cross-612); [Perceptography unveils the causal contribution of inferior temporal cortex to visual perception](../sources.md#src-model-927).

**Exact locator:** Yamins and DiCarlo, Question 3 on perturbing subpopulations. Shahbazi and coauthors, 2024 abstract and Figure 1.

**Potential difficulty:** High. The target involves model choice, competing mechanisms or extrapolation; a narrow instance may be manageable, but the full research direction has no established cost bound.

**Possible AI role:** Assess how well a model predicts condition-specific behavioral reports in a specified dataset and keep extrapolations explicit.

**Verification burden:** High. Check formal deductions and numerical convergence separately from empirical fit, identifiability and causal interpretation. A good fit alone cannot identify the mechanism.

**Resource expectations:** Model analysis can begin without new experiments. Simulations or existing data may need substantial computing. Data access, licenses, preprocessing and representativeness remain unaudited; empirical conclusions may require additional observations or complex experiments.

**Assessment:** 2026-11-28; untested forecast. **Uncertainty:** The task uses behavioral reports to infer perceptual effects. Generalization to other animals, stimuli and neural populations requires new evidence.

**Further work:** resolve the statement and status questions above before planning an attempt. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-28

**Coverage:** Statement and later literature. **Statement:** Corrected.

**Recorded status:** Unverified → Unverified.

Shahbazi and coauthors measured which image changes macaques confused with localized stimulation in inferior temporal cortex. Those changes depended on the image and stimulation conditions. This supplies a concrete behavioral comparison within the broader modeling question.

**Search scope:** Compared the indexed question with the passages and later records listed below.

<details>
<summary>Previous indexed wording</summary>

Predict perceptual changes caused by selective neural perturbations.

The current statement appears at the top of this page.
</details>

**Inspected evidence**

- [Eight open questions in the computational modeling of higher sensory cortex](../sources.md#src-cross-404) — Question 3, p. 116. Asks whether models can predict behavioral changes after perturbing particular neural populations.
- [Perceptography unveils the causal contribution of inferior temporal cortex to visual perception](../sources.md#src-model-927) — Abstract and Figure 1, cortical perturbation detection task in macaques. The study found image changes that macaques had difficulty distinguishing from stimulation in inferior temporal cortex. The inferred change depended on the image, site and stimulation intensity.

**Limits and remaining work**

- The task uses behavioral reports to infer perceptual effects. Generalization to other animals, stimuli and neural populations requires new evidence.

<details>
<summary>Search queries</summary>

- macaque inferotemporal cortex perturbation perceptual prediction Shahbazi perceptography stimulus dependent visual perception


</details>

### 2026-10-14

**Coverage:** Statement and later literature. **Statement:** Needs clarification.

**Recorded status:** Unverified → Unverified.

The 2016 heading identifies a research program; the present record lacks a single falsifiable success criterion. Partial predictive success is not a complete mechanistic explanation. The 2019 neural-control result concerns image-induced V4 responses, not a complete neural-intervention-to-perception model.

**Search scope:** Compared the original sensory-cortex heading with the listed later empirical/model results. Coverage does not establish an exhaustive history or a complete biological explanation.

**Inspected evidence**

- [Eight open questions in the computational modeling of higher sensory cortex](../sources.md#src-cross-404) — Heading 3, p. 116; Yamins and DiCarlo (2016). Identifies the historical target.
- [Neural population control via deep image synthesis](../sources.md#src-cross-612) — Abstract and publication record; Science 364, eaav9436; DOI 10.1126/science.aav9436. Model-designed stimuli can influence V4 population activity.

**Limits and remaining work**

- Specify intervention, neural site and behavioral endpoint; stimulus-driven activation is not a direct neural perturbation.
- This check is not an independent proof audit or an exhaustive review of all later literature.

<details>
<summary>Search queries</summary>

- "neural population" "control" Bashivan Kar DiCarlo 2019 Science


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
