# Sources, intellectual credit and tool attribution

Source passages were rechecked on 18 October 2026. These references
separate the problem and known results from the submitted candidate
arguments. No historical priority or comprehensive novelty claim is made.

| Source | Exact role and inspected locator |
| --- | --- |
| Daan van Berkel and Wieb Bosma, [Periodicity conjectures for all 2-sumfree sequences](https://arxiv.org/html/2609.18522v1), arXiv:2609.18522v1, 16 September 2026 | Conjecture 1 is the precise two-seed target. Definition 3 and the period predictions informed the parameter split. Theorems 12 and 14 and Example 13 supply attributed known cases. Theorem 15 is finite-continuation background, not a premise of this analytic proof. |
| Daan van Berkel and Wieb Bosma, [On t-sumfree sequences](https://arxiv.org/html/2609.16843v1), arXiv:2609.16843v1, 15 September 2026 | Section 1 fixes strict distinct-summand conventions. Section 5, Theorems 9/10 and Remarks 12 cover first seed one. Section 2 credits Queneau's earlier non-additive formulation; Section 3 credits the Calkin–Finch criterion underlying its strict continuation result. |
| Ben Green, [100 Open Problems](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf), December 2025 revision | Printed page 5, Problem 7 comments: catalogue entry point for Queneau's distinct-pair variant with arbitrary finite seeds. This is broader than the submitted two-seed result. |

The original papers remain third-party works. Both September preprints
display CC BY-NC-ND 4.0; this package distributes its own argument,
mathematical descriptions and citations, not their PDF/HTML or a relicensed
copy of their prose. The project's CC BY 4.0/MIT terms do not override
source licenses. The source names, exact versions and theorem numbers
are retained alongside every imported known result.

Raymond Queneau's *Sur les suites s-additives* (1972) is historical
background identified through the inspected companion paper. Its original
full text was not inspected, so no unexamined theorem is silently relied
on. The companion identifies its s=0 case with the strict two-sumfree
construction. Neil J. Calkin and Steven R. Finch's *Conditions on
Periodicity for Sum-Free Sets*, Experimental Mathematics 5(2) (1996),
131–137, is credited for the earlier continuation criterion as described
in the companion's Section 3. That continuation method is not used to
establish the present analytic theorem. Historical full-text gaps recorded
for Queneau, Finch's 1992 work and relevant Guy passages remain limits.

The source histories and the bounded later-result searches are preserved
in the included [source record](contents/greedy-analytic-audit-20261018/literature.md)
and its selected predecessors. No later primary proof was identified in
those searches; that is not evidence that no such proof exists. The
recent period predictions are credited as motivation, not treated as
proved facts. Explicit elementary proofs of known small cases are
identified as attributed reproductions within the larger argument.

## Tools and original supporting code

OpenAI Codex, using the recorded model/configuration in
[model-provenance.json](model-provenance.json), assisted with research
ideas, algebra, proof prose, code, source inspection and same-team checks.
Models are tools, not human authors or independent reviewers. The human
contribution and preliminary review are described without expansion in
[the assistance note](assistance-and-checks.md).

The exact arithmetic helpers and publication runner are original project
code under MIT. They use Python 3.12.14 and its standard library; the
portable runner supports Python 3.10 or later with assertions enabled.
Git, PowerShell, the connected GitHub tools and the repository's own
validation/rendering scripts are used for packaging and submission.
Web retrieval is used for inspecting sources. No third-party research
checker is silently incorporated, and no paid computation is claimed.

The cited papers' use of Magma, Rust or Walnut is not a claim that these
tools were used for this contribution. The published replay is the
contributor team's own arithmetic check, not an independent execution,
an approved certificate checker or formal proof verification.
