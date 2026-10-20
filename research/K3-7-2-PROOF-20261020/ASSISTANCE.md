# Assistance and provenance for the proof draft

This note covers the complete `K3-7-2-PROOF-20261020` contribution:
the English manuscript, explanatory files, claim-specific verification
code, certificates, witness data, and retained reports. The final
[CHECK_REPORT.md](CHECK_REPORT.md) identifies its exact checked version.

## Human and AI roles

The maintainer, `luvLunairs`, selected the unrestricted covering-number
problem, directed the research, requested the proof revision, and
recognized the model configuration described below. These roles do not
assert a human derivation of the proof or completed specialist scientific
review. The reported preliminary human review is recorded below with
its actual limits.

OpenAI Codex assistance contributed mathematical derivations, numerical
and combinatorial exploration, certificate extraction, checker
implementation, source inspection, English drafting, and contributor
review. The root agent coordinated the work; the three delegated agents
handled checking, literature, and structural analysis. Their checks
provide separate implementations or separate readings within the same
AI-assisted investigation. They are not independent human peer review.

The revision of 20 October 2026 expanded the proof into definitions,
lemmas, exact constraint formulas, coefficient-reconstruction arguments,
and a complete contradiction. It retained the accepted certificate and
checker bytes and reran the delivered verification package. No new
cover or stronger numerical bound is claimed by this revision.

## Configuration evidence

[MODEL_CONFIGURATION.json](MODEL_CONFIGURATION.json) records the
application-supplied configuration fields for the root and all three
contributing agents. The recorded provider is `openai`, model identifier
`gpt-6-astra`, and effort `ultra`; the recorded Codex Desktop client is
`0.163.0-alpha.10.2`. Read-only inspection was refreshed on 20 October
2026 and includes the continuation used for this proof revision.

The metadata extract contains configuration fields and their digest,
not conversation text, private reasoning, account identifiers, or
credentials. The underlying backend/model build and hardware allocation
are not supplied by those records. Client version is not a model version.

On 20 October 2026, the maintainer explicitly described this configuration
as “GPT-6 Astra Ultra (Max plus subagents)” and recognized it as meeting
the project's recommended-model requirement. That recognition and the
application records are disclosed together under the project's
18 October 2026 AI policy. Model eligibility is separate from scientific
correctness, novelty, and acceptance.

## Maintainer recognition, review report, and authorization

The following relevant statements by the maintainer, `luvLunairs`, are
retained from the instructions in this task on 20 October 2026. English
translations are supplied here; these are attributed user statements,
not independently authenticated provider attestations.

- Configuration recognition: "The current model is GPT-6 Astra Ultra
  (Max plus subagents, therefore it meets the recommended-model
  requirement)."
- Submission instruction and review report: "Please help me submit in
  accordance with the requirements. It was generated using a recommended
  model, and preliminary human review has passed."

The first statement documents the maintainer's recognition of the
recorded `gpt-6-astra` / `ultra` configuration as corresponding to the
recommended GPT-6 Astra configuration. The service-supplied fields
are retained in [MODEL_CONFIGURATION.json](MODEL_CONFIGURATION.json).
The configuration relationship is the maintainer's stated recognition;
an independent provider specification equating the labels is unavailable.

The second statement authorizes automated submission of this proof
package to `luvLunairs/theory-research-atlas`. The intended action is
publication on a topic branch followed by a draft pull request for
assessment. It authorizes neither merging nor a scientific acceptance
decision. The final files are bound by the manifest identified in
[CHECK_REPORT.md](CHECK_REPORT.md).

The preliminary-review pass is reported by `luvLunairs` on 20 October
2026 and concerns the preceding delivered proof draft. The identities
of the human reader or readers, their independence, exact coverage,
review date, and detailed findings were not supplied. No human
mathematical corrections were reported. In particular, this report
does not establish full-text coverage of all supporting code and
evidence, independent peer review, novelty, or the project's approved
"Machine checked" status.

Preparation for submission changed only the assistance, action and
version disclosures. The manuscript and every file under `proof/`
remain byte-identical to the delivered version at local commit
`1f10bf359d838e62ec2c6c3daa428a4bc06bc5bb`. The contributor recheck
covers the final submission version; no renewed human review of the
administrative wording is claimed.

## Retained material and credit

The package retains the actual mathematical inputs and executable checker.
The source map identifies their original retained versions and adaptations.
The earlier draft and full exploratory archive remain local. They are
not hidden dependencies of the new package.

Prior mathematical work and the published 34-word construction are credited
in the manuscript. General symmetrization, moment, localizing-polynomial,
and semidefinite principles are not presented as original inventions.
The first-person scientific statements in the manuscript describe the
contribution prepared for assessment, not a claim that an AI is a human
author or reviewer.

The actual contributor checks and their limits are listed in the single
version-specific check report. This revision is prepared for the
authorized public draft submission. Catalogue acceptance, merge, and
external scientific endorsement remain pending.
