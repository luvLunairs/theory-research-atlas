> Publication copy of a dated working document. Original source identifiers and
> line numbers below refer to the preserved source digest in [source-map.json](../../source-map.json).
> Historical workflow/model-status notes are superseded by the current
> [assistance and submission record](../../assistance-and-checks.md).

# One midpoint theorem with two finite supersolutions

18 October 2026. Mathematical appendix consolidated from the retained
[odd-midpoint proof (historical reference; not a proof premise)](../../lineage.md#omitted-historical-material) and
[Boolean midpoint proof (historical reference; not a proof premise)](../../lineage.md#omitted-historical-material).
The exact inherited versions are identified in the [audit (historical reference; not a proof premise)](../../lineage.md#omitted-historical-material).
This is same-team AI assistance, not independent verification or approval.
Full-text human review and manual submission remain required.

## Theorem

For every pair of integers `h>=2`, `k>=1`, put

    f=2h-1,       q=4h-2,       H=h-1,       g=kq+h.

The strict greedy sequence `S(f,g)` is eventually periodic. More
explicitly, every `q`-block with index `n>C` contains exactly
`nq+[h,f]`, where the sufficient bound is

    C=max(3k^2+7k,6k^2-2k-1)                   if h>=3,
    C=max(4k,3k^2+2k-1,6k^2-3k-4)             if h=2.

These are sufficient bounds, not exact transient formulas. The gap
period prediction is credited to van Berkel and Bosma,
[Definition 3(3), Conjecture 5](https://arxiv.org/html/2609.18522v1).
The proof below does not assume the conjecture or equality with either
supersolution.

## 1. Exact causal recurrence for every h>=2

For `n>=k`, define

    U_n=min({H} union {L_i+L_j+[i=j]: i,j>=k, i+j=n}),
    L_n=max({0} union {U_i+U_j-H-[i=j]: i,j>=k, i+j=n-1}).       (1)

Every right-hand index is smaller than `n`, and `0<=L_n,U_n<=H`.
The actual greedy sequence is

    {f} union union_{n>=k}(nq+[h+L_n,f+U_n]).                  (2)

Here are the details establishing (2), including strictness. The
initial blocks `k,...,2k-1` are the full corridor `[h,3h-2]`:
before `2g` two nonseed terms cannot exclude a candidate, while
adding the seed `f` to a corridor interval fills the following
high and low gaps. Equation (1) gives `L=0,U=H` in these blocks.

The sum of two corridor residues lies in `[2h,6h-4]`, which
contains neither `f=2h-1` nor `f+q=6h-3`. Thus the central
residue `f` is protected as long as earlier entries lie in the
corridor. To maintain that condition, exclude every outside residue
by the following already selected terms. In block `2k`, residues
`0<=r<=h-1` are the seed plus residue `f+r` in initial block
`2k-1`. For `n>=2k+1`, residue zero is the seed plus the central
entry of block `n-1`, and for `1<=r<=h-1` use

    (kq+f+r)+((n-k-1)q+f)=nq+r.

For `n>=2k` and `3h-1<=r<=q-1`, use

    (kq+r-f)+((n-k)q+f)=nq+r.

Here the first term is in initial block `k`, and the second is an
earlier central entry. In the last two formulas the residues differ
when the block indices coincide, so the terms are still distinct.
These representations and the protected center prove confinement by
ascending induction.

Write the selected interval in an earlier block as `[l_i,u_i]`
in residue coordinates. For different blocks the sum interval is
`[l_i+l_j,u_i+u_j]`; for the same block its strict sum interval is
`[2l_i+1,2u_i-1]`, provided it is not a singleton. An uncarried
pair has `i+j=n` and removes only a terminal interval from the
right half `[f+1,3h-2]`: its upper sum endpoint is at least
`2f-1>=3h-2`. A carried pair has `i+j=n-1` and removes only
an initial interval from the left half `[h,f-1]`: its lower
endpoint after subtracting `q` is at most `1`. Taking the first
and last forbidden endpoints gives exactly (1).

The only possible singleton is `{f}`. Its formal same-block lower
endpoint `2f+1` is above the right half, and its formal carried
upper endpoint `-1` is below the left half. Thus these inactive
bounds do not introduce a fictitious obstruction. Seed sums miss
the corridor, current-block nonseed pairs cannot hit that block,
and `0<r+s<2q` rules out other carries. This proves (1)--(2)
with the distinct-pair condition intact.

For any candidate sequence `V`, let `W` be the max operator in
(1) applied to `V`, and let `F(V)` be the min operator applied to
`W`. Both operators are coordinatewise nondecreasing and causal.
By [the causal supersolution principle, Lemma 5](core-lemmas.md),

    F(V)<=V  implies  U<=V and L<=W.                       (3)

It suffices to give `V,W` with finite support. Bounded endpoint
values alone are not a finite-memory argument.

## 2. Supersolution when h>=3

Now `H>=2`. Write `d=3k+1`. Initially set `V=H` on
`[k,2k-1]` and `V_(2k)=1`. For `1<=t<=k+1`, let

    P_t=dt+[k-1,2k-t]=[a_t,b_t].

On this interval assign value `1` to either endpoint, value `H-1`
to any nonendpoint at distance one from an endpoint, and value `H`
to every other interior point. Endpoint assignments take precedence
on intervals of length one or two. Set `V=0` elsewhere. The
intervals are disjoint and end by `B=3k^2+5k`.

Let `P={V>0}`, `R_H={V=H}`, and let `Q` consist of the initial
`H` interval and the nonendpoint interiors of the later intervals.
Their descriptions are

| Set | Initial interval | Later intervals |
| --- | --- | --- |
| `P` | `[k,2k]` | `dt+[k-1,2k-t]`, `1<=t<=k+1` |
| `Q` | `[k,2k-1]` | `dt+[k,2k-t-1]`, `1<=t<=k-1` |
| `R_H` | `[k,2k-1]` | `dt+[k+1,2k-t-2]`, `1<=t<=k-3` |

An empty index range contributes nothing. The support of `W` is
exactly `1+(R_H+P)`, with an ordinary index sum. Indeed a pair
with values `H` and a positive value contributes positively; on a
diagonal both values are `H` and the correction leaves `H-1>=1`.
If neither value is `H`, a value `1` cannot contribute positively.
Both indices must therefore be in `Q`. For `H=2` such pairs
do not contribute; for `H>=3` their sums lie in `R_H+P`:
initial `Q` sums already do, and two later intervals of index sum
`v` give

    dv+[2k,4k-v-2],                  2<=v<=2k-2.           (4)

For `k>=4`, write every such `v=s+t` with
`1<=s<=k-3`, `1<=t<=k+1`; the corresponding `R_H` and `P`
intervals give exactly (4). For `k<=3`, the possible `v` satisfy
`v<=k+1`, and (4) is contained in initial `R_H` plus `P_v`.

Adding these intervals gives disjoint, separated support intervals

    D_0=[2k+1,4k],
    D_s=ds+[2k,4k-s],                  1<=s<=k+1,
    D_s=ds+[2k+1,4k-s-1],              k+2<=s<=2k-2.        (5)

The initial sum before adding one is `[2k,4k-1]`; mixed
initial/later sums are `ds+[2k-1,4k-s-1]`; later/later sums are
(4). The latter are contained in the mixed row when `s<=k+1`,
and otherwise give the last row of (5). Thus no support is
missing. In particular `W=0` on `J=[k,2k]` and for `n>C`.

We also need small boundary values, not merely the support:

    W_(2k+1)=H-1,    W_(4k)=1,    W_(4k-1)=H-1.           (6)

The first and third are diagonal pairs at `k` and `2k-1`.
At `4k` the only positive extreme pair has indices `2k-1,2k`
and values `H,1`. Any alternative at `4k-1` contributes at
most `1<=H-1`. These statements include `k=1`.

For a primary interval `D_s=[l_s,r_s]`, `1<=s<=k+1`,

    W_(l_s)=W_(r_s)=1.                                   (7)

At its neighbors needed below, where `s<=k-2`,

    W_(l_s+1)<=H-1,       W_(r_s-1)<=H-1.                 (8)

To check (7), a mixed initial/wave extreme has values `H,1`
and contributes one. Two later intervals of index sum `s` have
sum range `ds+[2k-2,4k-s]`; a target endpoint minus one is
one step inward from its extreme. The values then total at most
`1+(H-1)=H` and contribute nothing positive. Other index sums
cannot reach the target: the previous one's maximum is `ds+k-s`,
the next one's minimum is `ds+5k-1`. For (8), two inward
steps give total at most `max(H+1,2H-2)` and contribution at
most `max(1,H-2)<=H-1`. Mixed initial/wave contributions are
also at most `H-1`, and diagonal corrections only decrease them.

We now prove `F(V)<=V`. Away from the support of `V`, a
distinct zero pair from `J` suffices. For `2k<n<4k`, such
pairs fill all these sums. For `n>=4k+1`, consider

    I_n=[n-2k,n-k].

If `j in I_n` lies outside (5), pair it with `i=n-j in J`.
Both `W` values vanish and `i!=j` because `n>4k`. Otherwise
this contiguous interval of `k+1` entries must fit into one
support interval. It fits into `D_0` only for
`4k+1<=n<=5k`, part of the first wave. It fits into a primary
`D_s` only for

    ds+4k<=n<=ds+5k-s.

For `s<=k` this is exactly `P_(s+1)`; for `s=k+1` it is
empty. Last-row intervals in (5) have fewer than `k+1` entries.
Thus every off-wave index has the required zero pair.

On a site with `V=H`, the cap in the min operator suffices.
At `n=2k` and `a_1=4k`, the diagonal zero pairs `k,k` and
`2k,2k` give `F(V)<=1`. At a later left endpoint `a_t`,
use `i=2k`, `j=a_t-2k=l_(t-1)`; at any right endpoint
`b_t`, use `i=k`, `j=b_t-k=r_(t-1)`. Equations (6)--(7)
give value at most one, with distinct indices in these last pairs.
At nonendpoint neighbors, use the same fixed `i` and move `j`
one step inward. Equation (6) handles the first wave and (8)
handles the others, giving at most `H-1`. The neighbor condition
only arises for `t<=k-1`, so the required `s=t-1<=k-2`
lies within (8). This covers every assigned value and proves (3).

The last possible support endpoints in (5) are bounded by
`max(3k^2+7k,6k^2-2k-1)=C`, and `C>=B`. Thus `U=L=0`
for `n>C` by the causal comparison, giving the claimed tail.

## 3. Boolean supersolution when h=2

Here `H=1`. The exact recurrence (1) becomes

    U_n=1 iff no distinct i,j>=k have i+j=n and L_i=L_j=0,
    L_n=1 iff some distinct i,j>=k have i+j=n-1 and U_i=U_j=1.

An equal-index min term is at least one, and an equal-index max
term is nonpositive; this is why the support geometry changes.
Put `d=3k+2` and let `V` indicate the union `I` of

    I_0=[k,2k],
    I_t=dt+[k,2k-t-1],                    1<=t<=k-1.       (9)

The intervals are disjoint, of lengths `k+1,k-1,k-2,...,1`.
They end by `B=max(2k,3k^2-2)`. Now `W` indicates the
restricted index sumset `1+(I dotplus I)`, whose exact support is

    D_0=[2k+2,4k],
    D_s=ds+[2k+1,4k-s],                    1<=s<=k-1,
    D_s=ds+[2k+1,4k-s-1],                  k<=s<=2k-3.     (10)

The first row is the strict self-sum of `I_0`, shifted by one.
The second is `1+I_0+I_s`, using disjoint intervals. For two
later intervals of index sum `s`, ordinary sums plus one give
the last-row expression. When `s<=k-1` this lies within the
second row. For `k<=s<=2k-3`, choose interval indices `k-1`
and `s-k+1 in [1,k-2]`; they differ and attain the full
interval. At `s=2k-2` the only possibility doubles the last
singleton, yielding no strict sum. This also treats `k=1,2`,
where the corresponding ranges are empty.

The support intervals are separated and `W=0` on
`J=[k,2k+1]`. The last endpoint of (10) is at most the stated
`C=max(4k,3k^2+2k-1,6k^2-3k-4)`, with empty rows harmless.

On `I`, the Boolean cap gives `F(V)<=V`. Off `I`, indices
`2k+1<=n<=4k+1` are represented by distinct indices from
`J`, because `J dotplus J=[2k+1,4k+1]`. For `n>=4k+2`,
consider

    T_n=[n-(2k+1),n-k],

which has `k+2` entries. A zero-`W` index `j` in it gives
`i=n-j in J`. They are distinct for `n>4k+2`. At the boundary
`n=4k+2`, the target belongs to `I_1` if `k>=2`, and so is
not an off-`I` target; if `k=1,n=6`, use `i=1,j=5`, both
zero-`W` indices.

If `T_n` had no zero-`W` entry, it would fit in one interval
of (10). Fitting in `D_0` forces `4k+3<=n<=5k`, within
`I_1` (or empty if that interval is absent). Fitting in a
second-row `D_s` forces

    ds+4k+2<=n<=ds+5k-s.

For `s<=k-2` this is exactly `I_(s+1)`; for `s=k-1` it is
empty. A last-row interval has length `2k-s-1<=k-1`, too
short for `T_n`. Consequently every off-`I` index has the
required distinct zero pair, and `F(V)<=V` everywhere.

Since `C>=B`, (3) again implies `U=L=0` for every `n>C`.
Equation (2) proves the theorem, including the smallest odd seed
`f=3` and every quotient `k>=1`.

## Limits and retained failed extrapolation

No equality `U=V`, exact preperiod or finite-memory assertion is
used. The earlier `H>=2` wave formula must not be extended as an
exact formula to `H=1`: at `h=2,k=1`, recurrence (1) gives
`U_4=0`, whereas that old wave assigns `V_4=1`. This retained
counterexample concerns exact wave equality, not eventual periodicity
and not the causal recurrence. The separate Boolean construction
above has its own exact support and strict-diagonal argument.

This consolidation uses no new diagnostic enumeration. The original
contributor proofs and their evidence remain unchanged. Actual
service-supplied model identity, version and configuration are unknown;
the parent assistance note records the common scientific provenance.
Prose and mathematical data use the repository's CC BY 4.0 terms.
