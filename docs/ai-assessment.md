# AI trial assessment

Assess AI suitability for a defined task and a stated model or capability profile. A useful assessment explains what the system could contribute, what human expertise is needed, and how the result could be checked. Suitability can change as tools, models and the literature change.

The [AI contribution policy](ai-contributions.md) separately identifies recommended model configurations and submission requirements for scientific contributions. Inclusion in that list is a project preference; it is not task-specific evidence, a benchmark ranking or a measured success rate. Apply the assessment below to the actual problem, model, configuration and evidence.

## Evaluate dimensions separately

Each dimension has a `low`, `medium`, `high` or `unknown` rating and a reason. These are ordinal judgments, not probabilities. No weighted aggregate score is used.

| Dimension | Evidence to seek | Meaning of a high rating |
| --- | --- | --- |
| Clarity | Definitions, quantifiers, fixed target and success criteria | The statement is explicit |
| Decomposability | Independent sublemmas, finite cases and reusable artifacts | Useful bounded milestones exist |
| Methods and literature | Applicable results, worked analogues and accessible references | Relevant support is substantial |
| Search or symbolic suitability | Finite encodings, symbolic invariants, certificates or falsifiers | Tool use has a concrete role |
| Checkability | An independent, affordable verification method | Results can be checked reliably |
| Expertise / human intervention | Prerequisites, delicate assumptions and specialist decisions | Human expertise requirements are substantial |
| Significance | Connection to established questions and value of a bounded result | Potential scholarly value is substantial |
| Verification difficulty | Completeness, numerical error and statement alignment | Validation is difficult |

Assess computing, data and experiments independently. A feasible checker does not imply feasible search. A short statement, apparent proximity to known results or a model's confidence is insufficient evidence of tractability.

## Priority labels

Difficulty and priority answer different questions. Every candidate has a brief research profile; only a full card supplies the complete eight-dimension assessment and an approach-specific priority. A frontier question may contain a useful first milestone, while a simple-looking finite question may resist substantial computation.

| Potential difficulty | Interpretation |
| --- | --- |
| `low` | Routine or tightly bounded under stated prerequisites; not a promise of model success |
| `medium` | Structured work with substantial reasoning, implementation or domain preparation |
| `high` | Specialist research with significant unresolved obstacles |
| `frontier` | A major longstanding target or a comparably deep general problem |
| `unknown` | Insufficient task-specific evidence to defend a rating |

Brief profiles record a reason, a conditional AI role, verification burden, resource expectations, uncertainty and assessment date. Unless an explicitly narrower scope is stated, difficulty refers to the full question. These labels are not comparable numerical scores across disciplines. All current profiles are untested forecasts; capabilities mentioned in the AI-role field are requirements, not measured performance.

Use [difficulty browsing](difficulty.md) to explore ambitious targets and [full research cards](research-candidates.md) to find more developed starting points.

| Label | Basis |
| --- | --- |
| `priority_trial` | A bounded target, accessible methods and credible independent verification are specified; the task has a stated value and no unresolved prerequisite prevents a trial |
| `preparation_required` | Worth considering, but data, theory, environment, resource estimates or expert review still need attention |
| `exploratory` | Potential value exists, but the approach, resource needs or verification burden remain highly uncertain |
| `unassessed` | Evidence is insufficient for a useful judgment |

Priority indicates a reason to consider a task, not a predicted success rate. Calibration and new research have different purposes. A famous conjecture does not deserve priority solely because of its prominence.

## What would count as quick progress?

Quick progress is one possible research objective, not a condition for inclusion or a property of the indexed questions. Before testing it, define the target, model and tools, starting information, human assistance, resource limit and stopping rule. Measure discovery time and verification time separately. Record total human work, including preparation and correction, rather than counting model runtime alone.

A useful early target might be one exact certificate, a counterexample in a specified finite class, a rigorously checked special case or a sharper bound. State why that target matters and what larger claim it would leave untouched. A short proof found after extensive unrecorded guidance is different evidence from an independently reproducible result under a fixed budget.

Known-result tasks test the workflow and may reveal statement or verification errors. They cannot establish novelty, and prior exposure to their published solutions limits what they reveal about discovery. Compare outcomes only under sufficiently described conditions; neither a small set of successes nor unreported failures supports a general success-rate claim.

## Evidence levels

- `untested_forecast`: judgment based on problem structure and literature.
- `public_attempt_evidence`: an identified public attempt supports a specific claim, with its documented model, environment, human assistance and validation limits.
- `project_measured`: an actual attempt has reproducible records and measured outcomes.

Evidence from a public paper must remain attributable to that paper. It does not become a project measurement, and results for one problem do not establish general capability.

## Resources and revisions

Distinguish estimates, spending limits and actual consumption. Record units, currency and the basis of an estimate. Checking may be inexpensive while discovery costs remain unknown. Qualitative resource estimates should explain the relevant problem size, arithmetic, storage or verification burden.

Date each assessment and identify the model/version or required capability profile. Record evidence, uncertainty and the basis of any revision. Name a reviewer only when a review has actually taken place. Retain material changes in the record, and do not transfer conclusions between models, proof systems, problem families or levels of human assistance without evidence.
