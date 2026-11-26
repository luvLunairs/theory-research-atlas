# Goal-driven models beyond vision

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-CROSS-445 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-CROSS-445%3A+Goal-driven+models+beyond+vision&target=Q-CROSS-445) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-CROSS-445%3A+Goal-driven+models+beyond+vision&target=Q-CROSS-445)

Determine when task-optimized models explain nonvisual sensory cortex.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Unverified. **Last checked:** 2026-11-26.

**Status basis:** Tuckute et al. compared audio-trained models on two independent human fMRI datasets using the same 165 natural sounds. Most tested models improved on the spectrotemporal baseline, with differences across models and cortical regions. The broader nonvisual question remains a research direction.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Yamins and DiCarlo, 2016; Kell et al., 2018; Tuckute et al., 2023.

**Scope limits:** The two datasets cover different participants and the same sounds. Predicting regional fMRI responses tests a defined auditory benchmark; identifying a causal cortical mechanism requires other evidence.

**Information still needed**

- Choose the auditory region, stimulus generalization target and baseline for a specific follow-up.

**Primary branch:** [Theoretical neuroscience](../domains/cog.md#cog-neuro). **Related branches:** None recorded.

**Sources:** [Eight open questions in the computational modeling of higher sensory cortex](../sources.md#src-cross-404); [A Task-Optimized Neural Network Replicates Human Auditory Behavior, Predicts Brain Responses, and Reveals a Cortical Processing Hierarchy](../sources.md#src-review-801); [kelletal2018: auditory network parameters and demonstration](../sources.md#src-review-802); [Many but not all deep neural network audio models capture brain responses and exhibit correspondence between model stages and brain regions](../sources.md#src-model-906).

**Exact locator:** Yamins and DiCarlo, Question 7; Tuckute et al., Results, Discussion and Data Availability.

**Potential difficulty:** Unknown. The direction spans several modalities and has no common completion test. Difficulty depends on the proposed comparison or theoretical claim.

**Possible AI role:** Use the archived activations and responses to compare a specified region and held-out sounds across models.

**Verification burden:** High. Separate training, model selection and held-out evaluation. Report uncertainty, noise ceilings and controls for alternative explanations; prediction quality alone does not identify causation.

**Resource expectations:** The author repository offers model parameters and an inference notebook. Data access and licensing need a separate audit. Training, inference and neural-data collection have different costs; none has been measured for a proposed task.

**Assessment:** 2026-11-26; untested forecast. **Uncertainty:** The numerical results were not rerun; this study tests auditory prediction, not every nonvisual system.

**Further work:** resolve the statement and status questions above before planning an attempt. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-26

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Unverified → Unverified.

Tuckute et al. compared audio-trained models on two independent human fMRI datasets using the same 165 natural sounds. Most tested models improved on the spectrotemporal baseline, with differences across models and cortical regions. The broader nonvisual question remains a research direction.

**Search scope:** Reopened the original review and the multisystem auditory comparison, including its stimulus design and data availability.

**Inspected evidence**

- [Eight open questions in the computational modeling of higher sensory cortex](../sources.md#src-cross-404) — Question 7. Extends the modeling question beyond vision.
- [Many but not all deep neural network audio models capture brain responses and exhibit correspondence between model stages and brain regions](../sources.md#src-model-906) — Results, Discussion and Data Availability. Provides model comparisons, two fMRI datasets and an archive with activations, data and analysis code.

**Limits and remaining work**

- The numerical results were not rerun; this study tests auditory prediction, not every nonvisual system.

<details>
<summary>Search queries</summary>

- many but not all deep neural network audio models capture brain responses and exhibit correspondence between model stages and brain regions auditory cortex 2023 primary nature reproducibility


</details>

### 2026-10-15

**Coverage:** Statement and later literature. **Statement:** Needs clarification.

**Recorded status:** Unverified → Unverified.

Kell et al. establish predictive progress for auditory models. The broader nonvisual-cortex direction still requires a chosen modality, explanatory claim and evaluation criterion.

**Search scope:** Reopened the 2016 agenda, read the 2018 auditory paper's results, limitations and availability statement, and inspected its authors' repository.

**Inspected evidence**

- [A Task-Optimized Neural Network Replicates Human Auditory Behavior, Predicts Brain Responses, and Reveals a Cortical Processing Hierarchy](../sources.md#src-review-801) — Results; Limitations and Future Directions; p. e16. Reports auditory predictive progress and describes limits on explanatory scope and data access.
- [kelletal2018: auditory network parameters and demonstration](../sources.md#src-review-802) — README and file listing. Trained parameters and an inference demonstration are available in the author repository.

**Limits and remaining work**

- This is not a comprehensive review through 2026. Repository execution, full data availability and permissions remain unchecked.

<details>
<summary>Search queries</summary>

- Kell Yamins Shook Norman Haignere McDermott 2018 task optimized auditory model hierarchical auditory cortex Neuron full text
- "Kell" "2018" "PMC" "auditory" "630"


</details>

### 2026-10-14

**Coverage:** Statement only. **Statement:** Needs clarification.

**Recorded status:** Unverified → Unverified.

The 2016 heading identifies a research program; the present record lacks a single falsifiable success criterion. Partial predictive success is not a complete mechanistic explanation.

**Search scope:** Original heading checked. Kell et al. (2018), DOI 10.1016/j.neuron.2018.03.044, was located, but accessible full-text retrieval failed; its results need direct follow-up.

**Inspected evidence**

- [Eight open questions in the computational modeling of higher sensory cortex](../sources.md#src-cross-404) — Heading 7, pp. 117–118; Yamins and DiCarlo (2016). Identifies the historical target.

**Limits and remaining work**

- Specify modality and benchmark; auditory task-optimized models already have published partial successes.
- This check is not an independent proof audit or an exhaustive review of all later literature.

<details>
<summary>Search queries</summary>

- "task-optimized" "auditory" Kell 2018 Neuron


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
