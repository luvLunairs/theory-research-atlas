> Publication copy of a dated working document. Original source identifiers and
> line numbers below refer to the preserved source digest in [source-map.json](../../../source-map.json).
> Historical workflow/model-status notes are superseded by the current
> [assistance and submission record](../../../assistance-and-checks.md).

# Source and status inspection, 18 October 2026

The local record examined was Q-MATH-430 in `data/candidates.json`, at
repository revision `dbac8f582b101cbc31c1429b814c7a568d105923`. The existing
record cites Green and reports openness at that source's date. A search
of `research/` for Q-MATH-430, Queneau and sumfree returned no matching
local attempt. That says nothing about unpublished or inaccessible work.

| Source opened | Passages inspected | Relevance |
| --- | --- | --- |
| Ben Green, [100 Open Problems](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf), December 2025 revision | Problem 7 and comments, printed p. 5 | Original atlas statement; separates distinct-summand Queneau sequences from Dickson sequences and Ulam's unique-representation rule. |
| Daan van Berkel and Wieb Bosma, [Periodicity conjectures for all 2-sumfree sequences](https://arxiv.org/html/2609.18522v1), v1, 16 September 2026 | Definitions 3 and 8; Conjectures 1, 5 and 9; Theorems 12, 14, 15, 16 and 17, including the relevant proofs; Section 5 | Primary source of the exact period prediction and finite-block method used here. |
| The same authors, [On t-sumfree sequences](https://arxiv.org/html/2609.16843v1), v1, 15 September 2026 | Sections 1--3 and 5; Theorems 9, 10 and 13; Lemma 6; historical references | The companion paper's proved two-seed families are f=1 or g<2f. Neither contains the chosen parameters. Its three-sum-free results concern a different recurrence. |

The two September papers are the original primary sources for this
contribution's exact conjecture and method. Their web pages report preprints;
no peer-review acceptance has been inferred. The conjecture remains open
in them. Our selected points have f>500, d>500 and g>2f, so they are outside
the computational rectangle and analytic families inspected. This is a
scoped non-duplication argument, not proof of mathematical novelty.

Queries executed through web search:

- `Dickson Queneau sum free greedy sequence eventual periodicity`
- `"Dickson" "Queneau" periodicity 2026`
- `"2609.18522" counterexample correction`
- `"van Berkel" "Bosma" "sumfree" conjecture 2026`
- `Queneau Sur les suites s additives 1972 pdf`

The returned results identified the September primary papers and mirrors,
with no later resolution of the exact period conjecture among the results
inspected. Older related work in the returned results concerns non-strict
sum-free sequences and was not used to infer the strict case.

Historical limitation: Queneau's 1972 *Sur les suites s-additives*,
[DOI](https://doi.org/10.1016/0097-3165%2872%2990083-0), was identified from
the primary companion paper's reference 11. Opening that DOI failed in the
web tool; the 1972 full text was not inspected. No theorem from it is relied
on here. The exact modern prediction and method were inspected at their
original sources. Searches are not exhaustive, and there was no contact
with the authors or access to their unpublished computations.

Selection also considered Q-MATH-201 and Q-MATH-208. Flammenkamp's
[author-maintained no-three-in-line page](https://wwwhomes.uni-bielefeld.de/achim/no3in/readme.html)
was opened; the n=75 construction frontier was plausible but its search
space was much larger. Sudermann-Merx's
[Heilbronn paper](https://arxiv.org/html/2603.11107v1), Section 6.1, was
opened; a later search found Trela's
[September preprint](https://arxiv.org/abs/2609.25035) on critical-triangle
stress structure. That later paper was not fully inspected, so a new
critical-triangle argument was deferred. The chosen sequence task offers
small exact certificates and a specific prediction to test.

No copyrighted paper or third-party program is redistributed. All retained
code and prose are newly written; mathematical methods and source credit
are stated in the contribution. See [batch assistance note](../../../assistance-and-checks.md).
