# Machine verification

**An exact certificate can establish correctness without a new line-by-line human proof review for every submission.** This route applies when a human has already approved the precise claim and checking procedure, and an independent run of that procedure accepts the submitted evidence.

**Machine checked** means that the retained certificate passed that approved procedure for the stated claim and version. It does not mean human reviewed, novel, significant or empirically confirmed. It does not automatically merge a contribution or change a problem to `resolved` or `disproved`.

## Start here

1. Identify the problem, exact claim and an approved specification in the [verification index](verifications.md). If none exists, propose one for human review; you can still share an ordinary research update.
2. Supply the complete certificate or proof, required inputs, versions and attribution using the [machine verification template](../templates/machine-verification.md). Link the associated research attempt and state any difference from the approved target.
3. Perform your own recheck, then request an independent run under the approved specification. Retain its result and evidence. A successful contributor run alone cannot grant the label.

Scientific submissions still follow the [AI contribution policy](ai-contributions.md). Machine verification does not waive full-text human review and **manual submission** when non-recommended or unidentified models contribute scientific content, including through mixed workflows. Maintenance of these documents or tools follows the [work-type requirements](../CONTRIBUTING.md#requirements-by-work-type); changes to an approved target, checker or trust assumptions remain subject to specification approval below.

## Eligible evidence

| Evidence | Required check | Claim it can establish |
| --- | --- | --- |
| Exact counterexample | The object satisfies every premise and falsifies the stated conclusion, with exact arithmetic or another approved rigorous certificate | Failure of the precise claim addressed by the witness |
| Lean proof | The approved formal target passes the strict procedure below | The fixed theorem under its declared logical foundations |
| Finite construction | Every required constraint is checked against the complete object | Existence, feasibility or a specified bound; optimality needs separate evidence |
| Bounded exhaustive certificate | The finite domain, enumeration completeness, reductions and every case are covered by the approved check | Only the stated finite range or class |

A decimal approximation, plot, screenshot, solver success message or sample of tested cases is insufficient. Rigorous interval certificates may qualify when the approved procedure checks their error bounds and boundary conditions. A failed search establishes nonexistence only if its completeness has been justified. For statements with alternating quantifiers, a single failed instance may not be a counterexample to the whole claim.

## Approve the specification

A named human reviewer checks the statement and procedure; the maintainer authorizes their use for this route. Approval must identify the exact specification version and retain:

- the source problem, claim, definitions, assumptions, quantifiers and exclusions, including how the certificate establishes that claim;
- the verifier, dependency versions, input format, exact acceptance criteria and resource limits;
- the trusted components, arithmetic or logical foundations, and checks for malformed inputs, boundary cases and invalid certificates;
- the reviewer, date, examined artifacts, approval scope, limitations and supporting review record.

Approval of a general tool does not approve every statement submitted to it. A contributor must not alter the target, checker or acceptance rule in the same unchecked submission and inherit the old approval. Changes to the claim, definitions, verifier, dependencies or trust assumptions require renewed approval. Approval can be withdrawn when a defect or unresolved objection affects its validity; earlier runs remain in the history.

## Strict Lean procedure

Use a clean, isolated environment with locked Lean and dependency versions. Bind the theorem to a separately maintained target, including its definitions and hypotheses. Check transitive axioms against an explicit allowlist: normally `propext`, `Classical.choice` and `Quot.sound`. Reject `sorryAx`, undeclared assumptions and added custom axioms. Compilation or editor indicators alone do not satisfy this route.

Independently recheck the proof and compare it with the trusted target. The approved protocol must specify the checker and target-comparison procedure. `lean4checker --fresh` replays stored proofs; `comparator` with external checking additionally supports checking against a trusted challenge in an isolated workflow. These tools still have stated trust assumptions. See the [official Lean validation guide](https://lean-lang.org/doc/reference/latest/ValidatingProofs/), inspected 16 October 2026.

The strict route excludes `native_decide`, `decide +native` and equivalent native-evaluation trust extensions. Their trusted computation differs from ordinary proof reduction; see the [Lean tactic reference](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/). Such work may be retained for a separately described review, without the strict label.

## Run and retain the evidence

The project or a designated independent verifier reruns the approved procedure against the exact submitted artifacts. Independence here means a separate verification run under the approved procedure, not a claim that a second checker implementation is always available. The submitter's logs remain useful evidence but cannot substitute for this run.

Retain the specification version, claim and attempt versions, certificate checksums, verifier and environment versions, run identity and date, command or procedure, outputs, result and limitations. Keep enough evidence to reproduce the result. A result applies only to the artifacts it checked: changed statements, proof files, inputs or dependencies invalidate its use for the changed submission.

Failed, incomplete, unavailable or out-of-scope checks leave the claim unverified by this route. Do not convert a missing check into a pass. Retain failures and superseded runs rather than overwriting them. A known verifier defect or conflicting evidence prevents reliance on an earlier pass until resolved.

Specifications belong in `data/verification-specs/VSPEC-*.json`; runs belong in `data/verifications/VER-*.json`. A run binds the specification and attempt by digest and retains certificate and log checksums. The displayed label is derived from current, approved, matching records and independent evidence; a contributor-only success remains **Reported pass**. The [data model](data-model.md) defines the fields.

Repository validation checks record consistency and local hashes. It does **not** execute Lean or other certificate checkers, authenticate reviewers or establish who ran a command. Maintainer intake must check the claimed approval and independent-run provenance before accepting those records. Passing repository checks alone cannot grant scientific acceptance.

## What acceptance leaves open

Within an approved specification, a valid independent pass is sufficient to accept the **certified claim's correctness** without repeating the same human mathematical review. Broader conclusions still need their own evidence. In particular, an exact feasible object does not establish optimality, and a formal model theorem does not confirm its physical assumptions.

Novelty, significance, attribution, reuse rights, model disclosure and editorial inclusion remain separate assessments. Changing a problem's literature status requires the [status review](evidence-policy.md#check-a-status-claim), even when machine evidence supports the proposed change. `human_review_status` records actual human review and must never be populated from a machine pass.

[Contributing](../CONTRIBUTING.md) · [Record maintenance](maintaining.md) · [Review guide](review-guide.md)
