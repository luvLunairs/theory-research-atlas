> Publication copy of a dated working document. Original source identifiers and
> line numbers below refer to the preserved source digest in [source-map.json](../../source-map.json).
> Historical workflow/model-status notes are superseded by the current
> [assistance and submission record](../../assistance-and-checks.md).

# Common lemmas for a continuous periodicity proof

18 October 2026. These are contributor proofs, with AI assistance and
source credit recorded in the shared assistance note. They consolidate
the earlier [common proof (historical reference; not a proof premise)](../../lineage.md#omitted-historical-material)
and [rectangle lemma (historical reference; not a proof premise)](../../lineage.md#omitted-historical-material).
The strict finite-continuation result is Daan van Berkel and Wieb Bosma,
[Theorem 15](https://arxiv.org/html/2609.18522v1). Their
[companion paper, Section 3](https://arxiv.org/html/2609.16843v1#S3),
credits an adaptation and generalization of Calkin and Finch's criterion.
The final analytic proof does not use finite continuation as a premise. Its displayed heading
says Theorem; the introduction and later cross-references sometimes
call it Corollary 15. We follow the displayed heading.

All intervals in this note are integer intervals. An interval with its
lower endpoint greater than its upper endpoint is empty. For sets A,B,
write A+B={a+b:a in A,b in B}, and write A dotplus A for sums of two
distinct members of A. A residue may occur twice in different periods;
equal residues do not imply equal actual summands.

## Lemma 1. Identification by exclusion and coverage

Let f<g be positive integers. Let T be either a set of positive integers
or a finite such set below a bound Q>g. Suppose its members at or below
g are exactly f,g, and, throughout the part of n>g under consideration,

    n in T  if and only if  n not in T dotplus T.          (1)

Then T agrees there with the strict greedy sequence S(f,g).

Proof. Induct on the integer n, starting at g+1. Every summand of a
representation of n by positive integers is strictly below n. Thus the
set of admissible pairs at n is already fixed by the preceding induction
steps and the forced seeds. Equation (1) is precisely the decision rule.
This also justifies computing the sumset of an entire proposed prefix:
no proposed future integer can participate in the sum of a smaller one.
Both directions in (1) are necessary. Modular sum exclusion alone does
not identify a greedy set. QED.

## Lemma 2. Finite continuation with a strict-diagonal repair

Let m,L be positive integers with L>g. Suppose the true characteristic
function c of S(f,g) satisfies c(n+m)=c(n) whenever both arguments lie
in [L,2L+3m). Then c is m-periodic for all integers n>=L.

Proof. Extend c on [L,L+m) periodically, and suppose v>=2L+3m is
the first integer where this extension disagrees with c. All comparisons
between numbers in [L,v) in the same residue class modulo m are valid.
In particular c(v-m) is the prescribed membership at v.

If c(v)=1 and c(v-m)=0, then v-m>g, so v-m=x+y for selected
x<y. The inequality y>(v-m)/2>=L+m puts y and y+m in the
already periodic region. Also y+m=v-x<v. Hence y+m is selected,
and x<y+m is a distinct pair representing v, a contradiction.

If c(v)=0 and c(v-m)=1, write v=x+y with selected x<y.
Then y>v/2>=L+3m/2, so y-m>=L and y-m is selected. If y-m
differs from x, these two positive selected integers represent v-m.
If y-m=x, then v=2x+m and x=(v-m)/2>=L+m. Therefore x-m>=L
is selected by the same earlier periodicity. The pair x-m,y is
distinct and has sum v-m. Either case contradicts c(v-m)=1. All
summands are smaller than the integer they represent by positivity.
Thus no first discrepancy exists. QED.

In particular, a table constant from m-block b needs a certified prefix
below (2b+3)m and the guard bm>g. One must check these two conditions,
not simply observe several repetitions. The bound is sufficient; no
optimality is asserted. Every table used in this manuscript has a
nonempty repeated row. The greedy sequence itself is infinite: a finite
set has only finitely many pair sums and therefore always has a larger
admissible next integer.

## Lemma 3. Exact interval and rectangle sums

If either input set is empty, its sum with any set is empty. For
nonempty integer intervals I=[a,b], J=[c,d], I+J=[a+c,b+d]. For
nonempty I, its restricted self-sum is empty if a=b, and
[2a+1,2b-1] if a<b.
For a sum n in the latter interval, use (a,n-a) when n<=a+b and
(n-b,b) when n>a+b. These are distinct and lie in I. This proves
both coverage and the exclusion of the two endpoint doubles.

Fix d>0. A normalized rectangle represents

    X={dt+r : l<=t<=u, a<=r<=b},  0<=a<=b<d.

The coordinates (t,r) of each integer are unique. For two disjoint
rectangles, the ordinary coordinatewise interval sum is therefore
exact and all cross pairs are distinct actual integers. For one
rectangle, its restricted self-sum before carrying is the image of

    [2l,2u] x [2a+1,2b-1],
    [2l+1,2u-1] x {2a},
    [2l+1,2u-1] x {2b}.                                (2)

Proof. If the residues differ, their sums are exactly the interior
residue interval in the first row, and the row sum is unrestricted.
If the residues agree, distinctness requires different row coordinates.
Their sums lie in [2l+1,2u-1]; all interior residue sums are already
covered by the first row, leaving just its two extremes. Conversely,
each row in (2) has the indicated distinct representation. Empty
intervals contribute nothing, including the case of a single integer.
Carrying a residue r through a multiple cd replaces (t,r) by
(t+c,r-cd). Splitting at all such multiples is an exact set identity.
The one-column case gives the arithmetic-progression formulas with
strict self-sum row indices [2l+1,2u-1]. QED.

## Lemma 4. Soundness of a universal interval certificate

Suppose the parameter domain is an integer interval, or a Cartesian
product of two such intervals. Suppose a finite tree partitions it by
splits [l,u]=[l,c] disjoint-union [c+1,u], with the other coordinate
unchanged. At each leaf, construct disjoint positive selected rectangles
or progressions in the prescribed blocks, with exactly f,g at or below
g. Use Lemma 3 to construct all distinct sums. If the selected set and
its distinct sumset partition [g+1,Q-1], the prefix is correct throughout
that leaf by Lemma 1. If it also has a literal repeated row on
[bm,(2b+3)m), Q>=(2b+3)m and bm>g, Lemma 2 proves the tail throughout
that leaf. A tree whose leaves exhaust the root proves the entire
declared parameter family.

There is no inference from tested parameter values here. For an affine
integer expression ax+b, nonnegativity on [l,u] is equivalent to the
two endpoint tests when u is finite, and to al+b>=0 and a>=0 when
u is infinite. An unresolved endpoint order must cause a subdivision
or a refusal. Once the normalized residue endpoints and their successors
are put in a universally valid order, each rectangle contains a whole
residue slab or misses it. Exact union and intersection of row intervals
then establish the required identity on that slab. All slabs together
establish it at every integer, including the partial first and last rows.

For variable d=2f, row endpoints depend affinely on k and residue
endpoints affinely on f. Physical endpoint guards reduce to
Akf+Bf+C>=0. On a bounded rectangle it suffices to check the corners:
fix one variable and apply the affine endpoint result, then the other.
If k is unbounded and f>0, checking A>=0 reduces to the lowest k;
if f is unbounded, the resulting slope in f must also be nonnegative.
These are sufficient exact tests used by the checker. Floor carries
are bounded by the extrema of (af+b)/(2f), which is monotone for f>0;
its infinite-end floor is a/2-1 when a is even and b<0, and floor(a/2)
otherwise. This accounts for approach to an integer limit from below.

The mathematical lemma does not assert that a particular implementation
or table satisfies its hypotheses. Those are explicit, auditable finite
obligations retained with the certificates. A passing parser, a discovery
sample, or a stored string saying "pass" is insufficient.

## Lemma 5. A causal supersolution principle

Let two endpoint sequences obey U_n=A_n(L), L_n=B_n(U), where each
operator uses only indices smaller than n and is coordinatewise
nondecreasing. Let V be a nonnegative candidate bound, put W_n=B_n(V),
and suppose A_n(W)<=V_n for every n. Then U_n<=V_n and L_n<=W_n
for every n, provided the initial seeds satisfy the same inequalities.

Proof. At step n, all inputs to B_n and A_n already satisfy their
bounds. Monotonicity gives L_n<=B_n(V)=W_n and
U_n<=A_n(W)<=V_n. This is ordinary strong induction, with no
simultaneous fixed-point assumption. In particular finite support of
V and W proves endpoint extinction. Bounded endpoint values by
themselves do not prove finite memory or eventual periodicity. QED.

## Lemma 6. Characteristic and gap periods

An infinite increasing set with a nonempty eventual characteristic word
of period m has periodic successive gaps: list the selected residues
in one m-block and take their consecutive differences, including the
wrap to the next block. Conversely, a repeating finite gap word with
positive total m translates all sufficiently late selected terms by m
and leaves no unlisted selected integers between them; membership is
therefore eventually m-periodic. This equivalence needs no minimality
claim. Least periods and exact transient lengths require separate proofs
and are excluded from the main theorem in this audit.
