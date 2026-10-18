> Publication copy of a dated working document. Original source identifiers and
> line numbers below refer to the preserved source digest in [source-map.json](../../../source-map.json).
> Historical workflow/model-status notes are superseded by the current
> [assistance and submission record](../../../assistance-and-checks.md).

# Extending the offset-one analytic proof to first seed four

18 October 2026. Local domain-relaxation proof for full-text human review
and manual submission. Same-team AI assistance, not independent review or
a novelty finding. No sealed file is changed.

## Statement

For every integer `k>=1`, `S(4,8k+1)` is eventually periodic with
characteristic period `m=24k-3`. This is a valid period, without an
assertion that it is least. The cases have the following direct proofs.

For `k>=3`, the complete membership formula in the retained
[direct offset-one proof](../../greedy-comprehensive-20261018/a1/proof.md)
is valid also for `f=4`. More generally that proof's membership
statement has domain `f>=4,k>=3`. The separate quotient-boundary
argument below handles `k=2`, and the already proved `k=1` formula
is stated explicitly at the end.

The inherited proof's SHA-256 is
`665A56F1E317C03F5A353E16A4F21BBCC6A4B3C750790E99F6B4A9CFC869E50B`.
The following checks address every place where reducing the seed bound
could change an exclusion, an overlap or a distinctness argument. The
proof uses the existing explicit membership formula and argument, not
its optional certificate or a finite diagnostic pass. This note concerns
membership and eventual periodicity; it does not need new least-period
or exact-preperiod assertions.

## New regular-pair boundary alignments for k>=3

Keep the inherited notation

    A_i=(2i+1)f+a_i,
    B_i=(2k+2i)f+b_i,
    C_i=(4k+2i)f+c_i,

where `a_0 in [-1,0]`, `a_1=-1`, later `a_i in [-2,-1]`;
`b_0 in [2,f-1]`, `b_1 in [1,f-1]`, later `b_i in [1,f-2]`;
`c_0 in [1,2]`, and later `c_i in [0,1]`.

An `A_i+A_j` sum has even coefficient `2(i+j+1)f` and offset
`e in [-4,0]`. At `f=4` a sum can newly reach the preceding
odd cell when `e=-4`. Its coordinate there is zero, namely the
zero offset of the putative run `A_(i+j)`. But `e=-4` requires
`a_i=a_j=-2`, hence `i,j>=2` and `i+j>=4`. Every such `A`
run excludes zero; if the index is outside the run range there is
no target at all. The other offsets cannot reach an odd `A` run.
The even `B` offsets are positive and all `C` cells are farther
away, just as in the inherited argument. Thus `A+A` is safe.

Here are the remaining five regular-pair bounds at `f=4`:

* `A+B` in the preceding even cell has coordinate at least
  `f-1=3>2`, so the old exclusion of a neighboring `C` remains
  strict. Its sole possible `B` endpoint collision still forces
  target index at least three, where that endpoint is absent.
* Unwrapped `A+C` has odd-cell offset `[-2,2]`. A preceding
  `C` would require offset at most `2-f=-2`; equality can only
  target a `C_0` upper endpoint. But at an odd cell adjacent to
  `C_0`, the sum would require `i+j=0`, hence `i=j=0`, whose
  actual offset is nonnegative. The next `C` starts at offset
  at least `f=4`, outside the range. After wrapping the offset
  is `[-3,1]` at an early even cell: the preceding `A` ends
  at most at `-f=-4`, and the next starts at least at
  `f-2=2`. Both remain out of reach.
* Wrapped `B+B` has positive odd-cell offset at most `2f-3=5`,
  whereas the next `A` starts no earlier than `2f-2=6`.
  The unwrapped possible coordinate two still forces a later
  `C` index whose upper coordinate is one.
* The original `B+C` alignment conditions are unchanged: its
  zero-offset `A` possibility requires indices whose sum is at
  least two and hence excludes that endpoint; its next-even-cell
  `C` possibility requires the `C_0` endpoint and a `B` index
  at most one, leaving it before all `C` cells.
* Wrapped `C+C` has odd-cell offset `[-1,3]`. A preceding
  `C` ends at most at `2-f=-2`, and the next begins at least
  at `f=4`; neither can be hit. Its sole `B` endpoint
  possibility still forces the later index where that endpoint
  is absent.

The extra detail for unwrapped `A+C` above closes an equality
which the original broad phrase about a one-cell distance need not
separate when `f>=5`. At `f=4` the equality is ruled out by
its actual indices, not by a false strict bound.

## Exceptional residues and early targets

The inherited exceptions are the seed `g`, the initial
`beta_i=(2k+2i+1)f`, and initial/block-one copies of
`gamma_i=beta_i-1` for `i>=2`. Their six pair types with
regular runs remain excluded as follows.

The three `g+R` calculations are unchanged. For
`D_i=beta_i+epsilon`, with `epsilon=0` or the permitted `-1`,
`D_i+A_j` has even-cell offset in `[-3,0]`; the preceding
odd `A` coordinate is at most `-4`, and the next is at least
two. Thus the inherited parity argument still has a strict separation.
Its possible `C` coordinate zero again forces `j=0` and a
nonexistent `C` index, or `C_0`, which excludes zero.

Wrapped `D_i+B_j` has offset in `[-1,2]`. Reaching a next
`A` requires offset two, which forces `epsilon=0,b_j=3`;
then `j<=1` and the target `A` index is at most one, where
offset `-2` does not occur. Wrapped `D_i+C_j` has offset in
`[-2,1]`, strictly between neighboring odd `A` ranges. Its
possible `B` offset one still forces the `C_0` upper endpoint
and a target at most `B_0`, whose lower offset is two.

For exceptional-exceptional sums, the old offsets `0,-1,-2`
before wrapping and `-1,-2,-3` in the relevant odd cells after
wrapping do not reach any additional neighboring cell when `f=4`.
The selected exceptional targets themselves remain safe: initial ones
precede all nonseed pair sums; a block-one target `(8k+2i)f`
cannot be reached by an initial `F+C` sum because its offset is
strictly between zero and `2f=8`. An initial `C+C` sum with
zero offset would still repeat the lower endpoint of `C_1`.
The remaining block-one cases use exactly the same size inequalities
and missing endpoints as in the inherited proof.

## Coverage and identification

Every displayed coverage interval in the inherited proof remains
nonempty at `f=4`: `F_i` has four terms, `B_0` and each
later `B_i` have two, `B_1` has three, and the full `C_i`
have two. The self-sum identities therefore remain applicable.

For the early gaps in blocks `n>=2`, the overlapping bridge
`F_(i-1)+C_1[n-1]` ends at `(2i+2)f`, after the other
interval begins at `(2i+1)f+1`; the overlap margin is
`f-1=3`. The two intervals after the last `A` similarly
overlap. In block one, the junctions between the `F+F` ranges
are supplied by the same `F+C_1` bridges. The only lost strict
self-sum endpoint is still included in its bridge, since that
bridge extends a further `f` integers. These comparisons need
no inequality stronger than `f>=4`.

The B-gap singleton repair for `n>=2,i>=2` still uses the two
lower endpoints of `C_1[0]` and `C_(i-1)[n-1]`, which lie
in different blocks. At `n=1,i=2`, the repair still uses the
two different endpoints of initial `C_1`. The gaps following
all `C` runs are the same exact sums; shrinking `f` to four
does not change their adjacency or their distinct actual factors.

Consequently both exclusion and coverage from the inherited direct
proof hold at `f=4`. Its proposed set has exactly the forced
seeds at or below `g`; positivity of all summands makes induction
on the scanned integer valid. The full membership formula is therefore
the true greedy sequence, and its recurring row from block three
proves eventual periodicity. No computer certificate is required.

## The quotient boundary k=2

The retained [quotient-boundary proof](../../greedy-comprehensive-20261018/a1/boundary.md)
also extends from `f>=5` to `f>=4` for its membership assertion.
Its source SHA-256 is
`DC4FFF7236EFD13CFB1EC1FBFC647157188C7B1E8F150BC3DCF02E8D1F693902`.
Only `f=4` needs checking here. Put `g=17,m=45` and

    A_0=[3,4], A_1={11}, B_0=[18,19], B_1=[25,27],
    C_0=[33,34], C_1=[40,41], F_0=[17,20], F_1=[25,28].

Let `R` be the union of the six `A,B,C` runs. Then

    P_0={4} union F_0 union F_1 union C_0 union C_1,
    P_1=R minus {3},
    T=P_0 union (45+P_1) union union_(n>=2)(45n+R).       (1)

The regular and mixed exceptional exclusions just checked specialize
to `k=2`: every run indexed at least two is empty. In particular the
new `A+A` boundary alignment cannot occur, and the new unwrapped
`A+C` equality is impossible by the same index-zero argument. The
three exceptions are `17,20,28`, all initial. Their distinct pair
sums are `37`, `45`, and `48=45+3`; the first two are gaps, and the
last is the omitted point of `45+P_1`. Each exceptional double is
forbidden because that actual integer occurs only once. All initial
exceptions are safe targets: seed-plus-`F` sums are in the gaps,
and two `F` entries sum to at least `34>28`.

For clarity, every complement interval of a full positive `R` block
has the following available sums, with offsets relative to `45n`:

| Gap | Covering sums and offset intervals, n>=2 |
| --- | --- |
| `[0,2]` | `F_0+B_1[n-1]=[-3,2]` |
| `[5,10]` | `F_1+B_1[n-1]=[5,10]` |
| `[12,17]` | `F_0+C_1[n-1]=[12,16]`, `F_1+C_0[n-1]=[13,17]` |
| `[20,24]` | `F_0+A_0[n]=[20,24]` |
| `[28,32]` | `F_1+A_0[n]=[28,32]` |
| `[35,39]` | `F_0+B_0[n]=[35,39]` |
| `[42,44]` | `F_0+B_1[n]=[42,47]` |

All these pairs use different blocks. In block one, the low gap
`[0,3]` is covered by `F_0+F_1=45+[-3,3]`. The next gap is
covered by `F_0+C_0=45+[5,9]` together with the restricted
self-sum `F_1 dotplus F_1=45+[6,10]`. Thus no negative-index
run is needed. The third row is unchanged with initial `C`
copies. The fourth gap is `F_1+C_1=45+[20,24]`. For the fifth,
`F_1+{49}=45+[29,32]` covers everything except its first point,
which is `33+40=45+28`, using distinct initial `C` entries.
The last two rows are unchanged.

Initially, `4+F_0` and `4+F_1` cover the gaps after the `F`
runs. The restricted self-sum `F_0 dotplus F_0=[35,39]`
covers the gap between `C_0` and `C_1`; `F_0+F_1=[42,48]`
covers the final gap below `45`. All intervals used have the
listed nonempty lengths; in particular `B_0` has two terms,
`B_1` three, and each `F` four. These exclusions and coverings
prove (1) for every block by the positive-summand greedy induction.
They are an infinite argument, not a computed-prefix assertion.
Consequently period `45` is valid from `90` onward.

## The existing quotient boundary k=1

The retained [two-family direct proof](../../greedy-families-20261018/j12/proof.md)
already assumes `f>=j+2`, which includes `f=4,j=1`. Its SHA-256 is
`1FB4A11D23F6B3C54B7B7212482534D3537193F95F605EDA9FA945DD0F0840BB`.
It gives, with `m=21`,

    P={4} union [9,12] union [17,18],
    R=[3,4] union [10,11] union [17,18],
    S(4,9)=P union union_(n>=1)(21n+R).

This is a direct sum-and-complement proof on the stated domain, so it
already supplies the remaining `k=1` case. The valid period `21`
is not primitive here: the earlier proof records least characteristic
period `7`. Nothing in this appendix asserts otherwise.

Together, the three quotient regimes establish eventual periodicity
for `S(4,8k+1)` for every `k>=1`, using analytic proofs throughout.

## Limits and provenance

The parent contributor proposed this relaxation and identified its new
`A+A` alignment. This worker checked all regular and exceptional
types and the coverage bridges, adding the explicit `A+C` equality
analysis above, then checked all quotient-two boundary intervals and
reopened the already proved quotient-one membership statement. The earlier
formula, argument, source conjecture and
same-team contributions retain their original credit. Actual
service-supplied model identity, version and configuration are unknown.
No new enumeration was used for this domain proof; human review and
manual submission remain required. Prose/data use CC BY 4.0 under the
repository terms.
