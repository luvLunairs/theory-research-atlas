> Publication copy of a dated working document. Original source identifiers and
> line numbers below refer to the preserved source digest in [source-map.json](../../../source-map.json).
> Historical workflow/model-status notes are superseded by the current
> [assistance and submission record](../../../assistance-and-checks.md).

# Scoped adversarial audit: first seed four

18 October 2026. Local scientific draft for full-text human review and
manual submission. This is a same-team contributor audit, including an
audit of some work previously written by this worker. It is not independent
verification, formal verification, human screening, acceptance or approval.
The parent's shared assistance record covers this version; actual service
model identity, version and configuration are unknown.

**Outcome.** No unresolved mathematical gap was found in the inspected
membership and eventual-periodicity claims for first seed four. Two
tempting domain extensions have explicit counterexamples to their unchanged
formulas. One inherited wording correction and one new editorial count
correction are recorded below. A new analytic anchor lemma reduces the
zero-offset coverage obligation from 103 gap rows to 51, while preserving
the exact candidate and the separate exclusion obligation.

This outcome does not assert least periods, optimal transient lengths,
historical novelty, independent review or the soundness of unlisted
families. All old files remain unchanged. No old evidence writer was run.

## Exact examined material

Paths in this table are relative to `work/`. Line spans identify the
membership arguments actually inspected; the hashes identify the complete
files, including material outside that verdict.

| File | Inspected scope / lines | SHA-256 |
| --- | --- | --- |
| `greedy-analytic-20261018/small/f4-zero-exclusion.md` | Full text, 1--306; all collision classes, transient targets and source lifetimes | `4237E9A50D8E498C8C678C1754BA2B417D9FB8B934CA8ED98155EFB6B6B60CE1` |
| `greedy-analytic-20261018/even-multiples/f4-zero-coverage.md` | Full text; candidate, masks, carry and global identification | `82B8777B1B66DF1A27ED6836B900CA23388907B669E0269D9907DA95CB87CD82` |
| `greedy-analytic-20261018/even-multiples/f4-coverage-tables.md` | Full text, 1--149; all 103 rows / 172 sum identities | `3FDFA6BCB2586FC8AC621889EAB0FB1DE562F6354A1FCAA9E89DFAE09E37CF33` |
| `greedy-analytic-20261018/upper/f4-fixed.md` | Full text, 1--223; three fixed cases, strict lifetimes, seeds and periodic conclusions | `8ED17855451E3C9F828111F4DC4CBEF439730F50A4D873F64494A3D49DAF1C30` |
| `greedy-analytic-20261018/upper/f4-fixed-tables.md` | Full text, 1--413; all selected lifetimes, exhaustive supported-target pair lists and gap witnesses | `CB663DCE7DAE696006E4188D3222530D1D5863397C256D72FBA9DA40D4A32B55` |
| `greedy-analytic-20261018/even-multiples/a1-first-seed-four.md` | Full text, 1--243; quotient regimes k>=3, k=2, k=1 | `72782A2D09740CDC32A98B6691F0FB899C239CB95B50B9F4240C89FC0C256123` |
| `greedy-comprehensive-20261018/a1/proof.md` | 1--308: candidate and complete membership proof; minimality/transient assertions not adopted | `665A56F1E317C03F5A353E16A4F21BBCC6A4B3C750790E99F6B4A9CFC869E50B` |
| `greedy-families-20261018/j12/proof.md` | 1--151: membership proof, specialized to f=4,j=1 | `1FB4A11D23F6B3C54B7B7212482534D3537193F95F605EDA9FA945DD0F0840BB` |
| `greedy-analytic-20261018/small-domain-extensions.md` | Full text, 1--183; verdict restricted here to f=4 | `608905FABEA235A8559649952184D6EFB655D8639178A449702F70CD95AD6183` |
| `greedy-unified-20261018/odd-multiple-proof.md` | 1--172: membership argument, evaluated at f=4 for all k>=1 | `F5C508D9D7562015BB998F3F6FFFBB97EBDDCD086E570421D49F30065B1B6627` |
| `greedy-upper-20261018/upper2/proof.md` | 1--256: collisions, chronological induction and coverage, specialized to f=4,b=3,k>=3 | `21BECD61D994FE36CDE9A0FD8FBF82FC98C1E13F970CAF7AEE6359CF042E3FFB` |
| `greedy-analytic-20261018/plateau-corner.md` | Full text, 1--202; all 28 ordinary pairs, exceptions and every gap, including f=4 | `E708F0AD9B5ABEDBFC97AF5E99925C677E1CEED65E2E09B02E4753AB837B31F1` |
| `greedy-lower-20261018/lower/proof.md` | 1--138 and 160--256: band f=4,4<=j<=7 and transition f=4 | `37869C5D0F046630877277526F7B6ABDDE369A672811EEC017702CB2DBD82487` |
| `greedy-lower-20261018/endpoint-proof.md` | 1--135: endpoint membership proof at f=4 | `F0F6595541BED37F958D3042A0F1A43B29B2567F695E18F7B00FE1AEE48D66C3` |

The older quotient-two boundary file's digest was also confirmed as
`DC4FFF7236EFD13CFB1EC1FBFC647157188C7B1E8F150BC3DCF02E8D1F693902`.
Its complete general-f proof was not newly audited here: the first-seed-
four appendix supplies the explicit k=2 specialization, whose 21 regular
pair classes, 18 exception/regular classes, three exceptional cross pairs
and seven gap rows were checked directly.

## Zero-offset exclusion: attempted collisions and actual lifetimes

The envelope has thirteen disjoint AP components. The retained proof's
lines 64--79 list sixteen possible ordinary H-pair intersections with R.
The carry changes the AP class by minus one, because m=32k+1. This rule
was rederived before checking the intersections. For example, `e+y` has
carried class zero and rows `[-4,2k-3]`; `e+w` has carried class seven
and rows `[-2,2k-2]`. The `e+v` lower intersection really is
`max(k+2,2k-5)`, so replacing that maximum by just its second argument
would be wrong at k=6.

The phrase H+R avoids R is stronger than a strict self-sum statement.
It was checked with ordinary, not strict, sums: the relevant portions
of both inputs in every one of the sixteen collision classes are
outside R. In particular, `a+a` can hit A only by using row k twice;
row k lies below the recurring A exactly when k>=6. The `a+x` hit
requires a row at most 2k-6, below recurring A's lower row 2k-5.
In `b+e`, a hit needs b>=2k-3, above recurring B's upper row 2k-4.
The analogous thresholds for `c+e`, `d+e`, `e+w`, `e+y` and
`e+z` are respectively k-1, k-4, 4k-2, 4k-5 and 3k-3;
each is just outside the corresponding recurring interval.

The lifetime bullets at lines 95--142 then remove every possible
core collision. The following adversarial cases were checked explicitly:

* Row k in a occurs initially and in block one. Those two **different**
  actual entries do have a valid sum, but it lands at row 2k in block
  one, where the candidate omits it. The two same-block copies are
  not available. Removing every equal-residue sum would have been an
  invalid shortcut; the proof does not do that.
* The formal `v+v` and `x+x` sums hit recurring C and D. They are
  unavailable solely because each exceptional component has one actual
  occurrence. Two late copies of the same residue would be different
  and could not be discarded, which is why ordinary H+R exclusion is
  needed for the tail.
* At k=6, block-one `a+x` can hit class-six row 3k+1=19. The actual
  P_1 column is `[16,17] union [20,21]`, so 19 is a hole. For example,
  249+102=351=193+8*19+6 is a representation of an omitted candidate,
  not a contradiction. This checks the conservative y_H target list
  against the actual split column rather than its convex hull.
* The `t+x` collision targets A row 2k in block two, which contains
  only rows 2k-2 and 2k-1. The `e+y` and `e+z` collisions expire
  before their target endpoints enter the candidate. Their carry and
  block increments were checked, not merely their modular positions.

Every transient-target paragraph, lines 189--292, was read against
the actual block table. The conservative list at 174--183 includes
the boundary-only `(y+y)*` and `b+y` possibilities. Initial protection
and protection of later selected extras are separate: modular avoidance
of R alone would not establish either. No circular claim about a future
greedy block is used; the proof concerns a completely defined candidate,
and positive-summand induction identifies it only after both obligations.

**Normative wording correction for an integrated proof.** At old line
191, replace the phrase “the double of the least seed 8k” and its
ambiguous preceding “nonseed terms” with:

> Two terms other than the first seed 4 cannot hit these low
> progressions, except through the double of the second seed 8k;
> that pair repeats an actual summand and is forbidden.

The old file is preserved. The smallest seed is 4, so “least seed 8k”
is literally incorrect terminology. The numerical bound and conclusion
of the argument are unchanged by this correction.

## Coverage and its shorter analytic replacement

Every one of the original 172 displayed sum intervals was rechecked,
including its source block, class, endpoint interval and carry. Subtracting
the exact candidate from the canonical masks gives precisely the 103
listed gaps. The residue-zero mask includes row 4k, namely offset m-1.
All three strict self-pairs occur in the early sections; ordinary sums
elsewhere use different actual blocks or disjoint actual progressions.
The block-five class-two witness uses blocks one and three with a carry.
The old block-six class-three repair has exactly adjacent intervals,
`[k-4,3k-6]` and `[3k-5,4k-1]`.

[The replacement anchor lemma](anchor-compression.md) is stronger than
grouping four evaluated cases. It holds on the independent parameter box

    k>=6, 2<=a<=5, 2<=b<=3, 2<=d<=5.

It gives all thirteen current-block gaps and twenty-two explicit sum
identities. Its preceding-block interface specifies only four needed
components. The literal candidate satisfies that interface from block
three onward, including the singleton E in block two. Since every
witness pairs an initial component with block n or n-1>=2, no strict
self-sum exception is hidden by the compression. The seven displayed
sufficient inequalities establish all endpoint joins throughout the box.

Thus the main proof may retain original table lines 7--58 only (the
38 early gap rows), followed by the new thirteen-row lemma: 51 rows
in total. The parent read every new identity, mask, inequality and
interface and reported no unresolved mathematical gap. This is another
same-team reading, not independent review.

An initial draft incorrectly counted the new table as 24 identities.
The parent caught this arithmetic count: the thirteen row counts are
`1,2,1,2,3,3,2,2,1,2,1,1,1`, whose sum is 22. Both prose occurrences
were corrected; no formula or table entry changed. The final literal
table check also confirms 13 rows and 22 identities.

## Fixed g=24,32,40: complete lifetime identities

The three fixed proofs define their candidates by literal selected
lifetimes in moduli 67, 91 and 115. They do not use retained prefixes
as premises. For every supported residue, the audit reconstructed all
unordered supported-residue pairs, including diagonals, and compared
their exact strict lifetime union with the printed one. This checks
exhaustiveness as well as individual arithmetic. All 353 listed pairs
matched. All 208 printed gap witnesses also matched their exact
interval/ray identities and covered the required omitted lifetimes.

| g | Supported residues | Exhaustive pairs at supported targets | Gap witnesses |
| --- | --- | --- | --- |
| 24 | 23 | 42 | 50 |
| 32 | 33 | 106 | 71 |
| 40 | 43 | 205 | 87 |

Special tests included the empty strict self-sum of lifetime `{0}`,
different-block copies at an equal residue, and the disconnected
`L_40={0} union [9,infinity)` for g=40. Its strict self-sum is the
ray `[9,infinity)`, because the cross-component sums start at 9 while
within-ray strict sums start at 19. Treating it as a single interval
from zero would be false. At g=40,r=80, the union from `17:63`,
`40:40` and `86:109` starts at block 8 and is disjoint from `[0,7]`.
At r=40, the sole pair `75:80` supplies exactly blocks 1--8, so the
initial occurrence and later return are both protected.

The guards were checked literally: positivity, exactly 4,g at or below
g, and the correct scanned lifetime starting at zero for r>g and one
otherwise. Consequently every represented candidate has earlier positive
summands. The last finite-lifetime ends and ray starts justify the
sufficient starts 603, 637 and 1035. For g=40 the recurring residues
are exactly `union_(j=0)^4(23j+{2,3,10,17,18})`, so the asserted
sufficient period 23 follows directly from the modulus-115 description.
No least-period or optimal-start claim is needed or audited.

The larger modulus in the last fixed case already makes the lifetime
description materially shorter. No further replacement for these full
fixed-case exclusion tables is offered: deleting unexamined pair lists
would obscure, rather than remove, their arithmetic obligation.

## Offset one and the other f=4 relaxations

For the offset-one proof, the inherited general-k argument was read
through identification, with the following boundary tests.

* At f=4, an A+A offset -4 can reach a preceding A-cell only at
  coordinate zero. Both input indices must be at least two, so the
  target index is at least four and excludes zero.
* The new unwrapped A+C equality would need the upper coordinate of
  C_0. Its index equation forces both indices to zero, where the
  actual sum offset is nonnegative, not -2. This index argument is
  essential; a blanket claim of a strict one-cell separation is false.
* The other four regular categories, all mixed exceptional categories,
  exceptional cross sums and the block-one exceptional targets retain
  their stated endpoint separations. The index-zero or index-at-most-one
  exclusions in the mixed pairs were checked, not replaced by parity
  alone.
* All coverage bridges remain nonempty. The repaired gamma_i point
  for n>=2 is represented by lower C endpoints in different blocks.
  For n=1,i=2, the two endpoints of initial C_1 are different actual
  integers. At k=2 the explicit f=4 table handles all seven gaps;
  the point 45+28 is 33+40, and the other fifth-gap points use
  `F_1+{49}`. At k=1 the previously proved j=1 membership domain
  already includes f=4; sufficient period 21 is not claimed least.

The other first-seed-four specializations were checked as membership
statements, not as transfers of their old minimality arguments:

* **Odd multiples, every k>=1.** Reflection, all unwrapped/wrapped
  ordinary sums and exceptional sums still exclude the recurring row.
  The carry at the last short early run has coordinate zero where
  `f-2=2>0`; the other critical upper bounds are 0<2 and 2<3.
  All initial and positive-block coverage rows, including k=1, retain
  their distinct actual factors and overlap.
* **Upper plateau b=3,k>=3.** B_2 is a singleton and its left
  component is empty. It is never used as the full last anchor.
  B_k has its two surviving endpoint singletons separated by two
  missing points. A length-four F interval added to those endpoints
  produces two intervals sharing an endpoint, hence the full asserted
  convolution. The only ordinary H+H core collision remains u+u;
  the chronological proof excludes later u before permitting that
  collision. Core protection therefore does not assume u's uniqueness
  without proving it. The high/high coordinate discrepancy is at most
  2, still strictly less than f=4.
* **Corner g=23.** All 28 ordinary-pair bounds and exceptional
  target arguments were recomputed. The first uncarried B+D interval
  is empty at f=4; it must not be interpreted as a reversed nonempty
  range. D={42} is a singleton. The three x_j+D intervals are adjacent
  singletons 16,17,18 after the carry, which still cover the required
  part of G2. The strict initial B self-sum is [47,49] and bridges
  the neighboring ranges at 46 and [49,51].
* **First-quotient band, j=4,...,7.** All eighteen regular/mixed
  rows and all gap identities survive. The initial middle-gap join
  is tight at j=7. All initial restricted intervals have length four.
  The low-gap crossing starts below the block boundary at f=4.
* **Transition g=11.** The tail is A=[3,5], B=[11,13], C=[20,21],
  D=[28,29], modulus 33. A+A=[6,10] fills its permitted gap
  exactly; all other 21 regular/mixed rows avoid the tail. The
  exceptional sum 14+22=33+3 hits the missing block-one A endpoint,
  and every initial/positive-block coverage interval remains valid.
* **Endpoint g=16.** The tail in modulus 43 is A=[3,4], B=[17,18],
  C=[24,26], D={32}, E=[38,39]. All fifteen regular and fifteen
  mixed pair bounds avoid it; carried E+E=[33,35] begins exactly
  at the permitted gap. The block-one G1 endpoint 43+5=48 is
  supplied by 16+32, not an inadmissible diagonal.

## Failed attempts to refute or extend the formulas

No counterexample was found **inside** the audited domains. The following
attempts establish useful limits rather than extra positive examples.

1. **The same zero-offset candidate at k=5 is false.** Its modulus
   would be 161 and its recurring class-zero row contains offsets
   40 and 80. The distinct proposed selected terms 1006 and 1167
   sum to another proposed selected term 2173. All three lie in
   recurring blocks. This is a mathematical counterexample to that
   unchanged formula, not to periodicity of S(4,40).
2. **The same offset-one candidate at f=3 is false.** For k=3,
   m=52 and the proposed recurring row contains A_2=13, the lower
   C_1 point 42 and the upper A_0 point 3. Then
   `169=3m+13`, `198=3m+42` and `367=7m+3` are proposed selected,
   but 169+198=367. For k>=4, the same A_2+C_1 sum reaches the
   upper C_3 point. This explains why the repaired f=4 equalities
   cannot be replaced by an unrestricted f>=3 assertion.
3. **Discarding all equal residues would hide real obstructions.**
   The k=5 example uses equal offsets in different blocks. Conversely,
   permitting every ordinary equal-actual pair would wrongly remove
   the selected initial double endpoints protected by strictness.
4. **A singleton previous column does not invalidate a cross-block
   interval sum.** The new anchor lemma's E^- at n=3 is a singleton,
   but it pairs with an initial AP in another block. The failed
   objection confuses an ordinary sum with a strict self-sum.
5. **The block-one k=6 split class-six column cannot be convexified.**
   Doing so creates the apparent a+x counterexample discussed above;
   keeping its two actual omitted rows resolves it.

## Reproducible new checks and resource use

The new [check_printed.py](check_printed.py) reads the literal Markdown
tables and imports no prior checker or generator. It parses every selected
lifetime, reconstructs supported-residue pair lists, applies exact strict
interval/ray addition, and checks the printed unions and coverage. For
the uniform candidate it verifies the 103 gaps and all 172 printed affine
sum identities using coefficient inequalities for every k>=6. It also
checks selected-target exclusion by a second organization: ordinary
H+R for any pair involving a recurring block, and exact strict pairs
from the six transient blocks for all other possibilities. Each collision
condition is a conjunction of affine inequalities solved over the whole
integer ray k>=6; no sampled k establishes emptiness.

The resulting counts are 208 H+R target intersections and 2,942 transient-
input target intersections, with no possible selected collision. This
supports the written exclusion audit; it is not substituted for its
sixteen core types and transient-target argument. The new compressed
table is also parsed literally: all 22 sum identities and thirteen masks
match, and joins hold throughout the independent parameter box by exact
linear lower bounds. Its previous-block interface remains an explicitly
checked part of the written proof, not a software-inferred sequence.

The [retained report](printed-results.json) binds the examined tables,
new compressed proof and helper. The final run used Python 3.12.14 and
recorded 0.015625 process CPU seconds and 0.013689500003238209 wall
seconds. Two earlier stages each recorded 0.015625 CPU seconds, for a
total of 0.046875 process CPU seconds across the three runs. The stages
added exact exclusion and then the compressed-table checks; no failed
mathematical assertion was suppressed. No new greedy scan or numerical
parameter census was performed. Peak memory was not measured; only finite
interval objects were constructed, and no memory measurement is claimed.

Current output digests:

| File | SHA-256 |
| --- | --- |
| `anchor-compression.md` | `87C375C2A856C6819750417EB3EC0D15800E82F5E825014663618792FC181341` |
| `check_printed.py` | `FA1760CDAA7074EAB830567DDFF21C48C81589FE5F7C0DEF9DD9AE3A15BC7A48` |
| `printed-results.json` | `E8BA742BDA6F2CF87C8F073800E700D351FFDA85B17F16DC8A8FD55F8EA38072` |

These checks are a different implementation path inside the same AI-assisted
team, not independent verification. The original conjecture and predictions
remain credited to van Berkel and Bosma. This audit adds no literature
search or priority assessment; those are explicitly part of the parent's
source review. Original prose/data use CC BY 4.0 and code MIT.

The audit retains the specified normative wording correction and the
shorter analytic coverage lemma. Its mathematical scope and stated
review limitations remain unchanged.
