> Publication copy of a dated working document. Original source identifiers and
> line numbers below refer to the preserved source digest in [source-map.json](../../source-map.json).
> Historical workflow/model-status notes are superseded by the current
> [assistance and submission record](../../assistance-and-checks.md).

# Research update: strict audit and consolidation of the analytic candidate

## Question and outcome

Work date: 18 October 2026. This revises the
[preceding analytic candidate (historical reference; not a proof premise)](../../lineage.md#omitted-historical-material)
addressing Conjecture 1 of Daan van Berkel and Wieb Bosma,
[Periodicity conjectures for all 2-sumfree sequences, v1](https://arxiv.org/html/2609.18522v1),
read again on that date. The exact target is: for every positive pair
f<g, the greedy sequence that excludes sums of two different actual
earlier entries has an eventually periodic characteristic function.
The [target record](target.md) fixes scope and success criteria.

The [revised manuscript](manuscript.md) and its mathematical appendices
give a continuous candidate proof with an exhaustive parameter partition.
The strict audit found three inherited wording issues, a missing
empty-input guard in a new consolidation lemma, and concrete failures
of proposed formula extensions outside their stated domains. The
corrections and failed attempts are preserved in [findings.md](findings.md).
No unresolved membership or eventual-periodicity gap was identified
within the recorded readings. This is a contributor assessment, not
independent verification or an accepted resolution of the conjecture.

Six common lemmas separate actual distinctness, exact carry arithmetic,
all-block lifetimes, chronological coverage, acyclic exception extinction
and causal supersolutions. A reflection lemma removes duplicated
wrapped-sum analysis. The first-seed-three stable coverage now uses
eighteen cross-block identities. The first-seed-four zero-offset coverage
uses one rectangular-domain anchor lemma; with the early blocks it
requires 51 gap rows instead of 103. The special midpoint mechanism
and necessary small boundary cases are retained with their hypotheses.
No expanded seed enumeration was substituted for these arguments.

## Evidence and checks

The reading scopes are recorded in the [parent](root-audit.md),
[large-family](large/audit.md), [small-seed](small/audit.md) and
[first-seed-four](four/audit.md) audit notes. New same-team parsers
recompute the actual printed interval/ray tables and affine identities;
they import no earlier discovery generator. Targeted finite checks
probe the general strict-sum formulas at empty and singleton inputs.
Written arguments, finite corroboration and exact table arithmetic
are distinguished in the [shared check report](../../assistance-and-checks.md).

The [source recheck](literature.md) credits known results and reports
the bounded later-result search and historical full-text gaps.
Correctness, novelty, significance and publication are separate issues.
No independent review or formal verification is available.

The runtime is Python 3.12.14 with standard library only. Retained
diagnostic timings are actual per-run measurements; total model compute
and peak memory are unknown.
The [manifest (historical reference; not a proof premise)](../../lineage.md#omitted-historical-material) seals this version and eleven unchanged
prior snapshots. [reproduce.ps1 (historical reference; not a proof premise)](../../lineage.md#omitted-historical-material) replays the local
consistency and arithmetic checks without rewriting retained results.

## Credit and AI assistance

Daan van Berkel and Wieb Bosma are credited for the conjecture,
period predictions and cited known theorems. Earlier local contributions
retain their formulas, sources, failed attempts and AI-assistance notes.
The user supplied the research direction; no human mathematical review
or substantive correction is asserted without a record.

The parent and three delegated OpenAI Codex workers contributed
substantive mathematical ideas, proof text, code and same-team checks.
Actual service-supplied model identifiers, versions and reasoning/compute
configurations are unknown. The single [assistance note](../../assistance-and-checks.md)
lists their roles and exact-version checks. Under the repository
policy, full-text human review followed by manual submission is required;
automated submission remains prohibited after review. No scientific
status, human approval or machine-verification
approval is assigned. Original prose/data use CC BY 4.0 and original
code uses MIT under the repository terms; cited sources retain their rights.
