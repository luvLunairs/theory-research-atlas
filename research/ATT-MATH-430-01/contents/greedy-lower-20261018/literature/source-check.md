> Publication copy of a dated working document. Original source identifiers and
> line numbers below refer to the preserved source digest in [source-map.json](../../../source-map.json).
> Historical workflow/model-status notes are superseded by the current
> [assistance and submission record](../../../assistance-and-checks.md).

# Source comparison for the lower-parameter region

18 October 2026. Local supporting draft for Q-MATH-430. Here `f>=1`,
`j>=1`, `g=2f+j`, and summands must be distinct. Write `p` for the least
eventual period of successive differences; the characteristic period `m`
is a different quantity. This note records source predictions and their
algebraic specialization, not a proof of those predictions.

## Source prediction and specialization

Daan van Berkel and Wieb Bosma,
[*Periodicity conjectures for all 2-sumfree sequences*, arXiv:2609.18522v1](https://arxiv.org/html/2609.18522v1),
Definition 3 and Conjecture 5, predict the following for `f>=5`:

| Range | Predicted `p` | Source branch |
| --- | --- | --- |
| `1<=j<=floor(f/2)` | `f+j+1` | 3(2), `k=1` |
| odd `f`, `j=(f+1)/2` | `(f+1)/2` | 3(3), `k=1` |
| `ceil(f/2)+1<=j<=f+2` | `2f+2` | 3(4), `k=1` |
| `f+3<=j<=2f-1` | `2f+2` | 3(5), `k=1`, including its correction |
| `j=2f` | `2f+2` | 3(2), `k=2` |
| `j=2f+1` | `2f+4` | 3(2), `k=2` |

These predictions supply neither `m` nor an infinite membership description.
Theorems 12 and 14 prove `g<2f` and `g=2f`; Theorems 16 and 17 cover finite
rectangles `f,d<=250` and `f,d<=500`, respectively, where `d=g-f`.
They do not prove this unbounded lower-parameter region.

Here is the explicit algebra behind the plateau. To avoid confusing the
source's within-branch variable with our `j`, call that variable `a`.
In branch 3(4), use `d=f+j`, `k=1`, and
`a=j-ceil(f/2)-1`. The dependence on `a` is multiplied by `k-1=0`, and
`floor(f/2)+ceil(f/2)=f`, yielding `2f+2`. The source's extra correction
at `d=2kf-1` does not intervene for `f>=5,k=1`. In branch 3(5),
`2(f-1)+3+1=2f+2`. At the next block's first point, branch 3(2) gives
`2(f+1+0)=2f+2`. Thus the three adjacent ranges combine exactly into
`ceil(f/2)+1<=j<=2f`.

For the proposed deficit `r=2j-f`, this combined range is equivalent to

```
f>=5, r congruent to f modulo 2, 2<=r<=3f.
```

Odd deficits therefore start at `r=3`; the exceptional odd midpoint
`r=1` is separate. For every fixed integer `r>=2`, sufficiently large
admissible `f` falls within this predicted plateau. No claim is made
that the plateau extends to all deficits: `r=3f+2` already has a different
source prediction.

| Target | Conditions avoiding small-f exceptions | Predicted gap period |
| --- | --- | --- |
| `f=2j-2`, `g=5j-4` | `j>=4` | `4j-2` |
| `f=2j-3`, `g=5j-6` | `j>=4` | `4j-4` |

These last two substitutions and the deficit reparameterization are our
algebraic deductions from the source conjecture. They are not separately
stated analytic theorems in it. For the first target, Theorems 16 and 17
include only `j<=84` and `j<=167`; for the second, only `j<=84` and
`j<=167`. These bounds follow from `d=3j-2` or `d=3j-3`, respectively,
together with the rectangles' upper bounds.

## Other inspected sources and limitations

The same authors' [*On t-sumfree sequences*, arXiv:2609.16843v1](https://arxiv.org/html/2609.16843v1),
Theorems 9 and 10, treat fixed `f=1`; Theorem 13 requires `d<f`.
Lemma 6 is a sufficient finite-block criterion, not an unconditional
lower-region classification. None of these supplies the sought proof.
Both arXiv submission histories still displayed only v1 when checked.

Ben Green's [*100 Open Problems*](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf),
December 2025 update, Problem 7 comments on printed p. 5, explicitly
distinguishes repeated from distinct summands and lists the general
eventual-periodicity question as open. This older status report gives no
proof for the present families. It is context, not a current novelty test.

Historical full-text limits in the
[earlier search (historical reference; not a proof premise)](../../../lineage.md#omitted-historical-material)
remain: Queneau and Finch originals have not been inspected in full;
no relevant original Lambert theorem was identified. A newly indexed
excerpt led to one renewed opening of Guy's
[1994 notes](https://oeis.org/A007300/a007300.pdf), but the PDF tool again
returned no readable text. No theorem is attributed from that excerpt.

The previous [preperiod comparison (historical reference; not a proof premise)](../../../lineage.md#omitted-historical-material)
records unresolved inconsistencies in Definition 8. No repair is presumed
here; any preperiod formula in the new work must be derived and checked
directly. Small `f<=4` corrections likewise require separate checking,
rather than extending the above source comparison outside its hypotheses.

## Query log and checks

Queries issued on 18 October 2026:

```text
"2-sumfree" "2f+2"
"sumfree" "2j-2"
"Periodicity conjectures for all" proof
"strict" "sumfree" periodicity 2026 proof
"0-additive" sequences "Lambert"
"strict 2-sumfree" proof family
"Berkel" "Bosma" "sumfree" proof
"0-additive sequences" periodicity proof
"2-sumfree" "family"
"sum-free" "Queneau" proof
```

No later analytic proof of the targeted lower regions was found in the
returned results inspected. Search-result summaries were used to locate
sources, not as proof. The search is bounded and does not establish novelty.

The source branches, parity conditions and endpoint substitutions were
reread and recalculated. These are contributor checks, not independent
verification. This worker's service identity/settings were unavailable
at the time of this audit. The consolidated
[assistance and check record](../../../assistance-and-checks.md) records
contributor roles, provenance and checks.
