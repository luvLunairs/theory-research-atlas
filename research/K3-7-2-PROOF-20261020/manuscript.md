# An exact computational lower bound for the ternary covering number K₃(7,2)

English proof draft for Theory Research Atlas, 20 October 2026.

## Abstract

We give a computer-assisted proof that every radius-two covering code in
the ternary Hamming space of length seven has at least 30 words. The proof
applies to arbitrary codes. It uses isometry-averaged indicator moments,
fixed-cardinality identities, Boolean and covering inequalities, integer
count inequalities, and explicitly positive semidefinite Gram matrices.
A supplied rational certificate combines these necessary conditions into
a linear expression whose maximum over exact orbit bounds is strictly
negative. The accompanying checker reconstructs the coefficients and
orbit sizes and performs the final calculation in exact arithmetic,
without an optimization solver or saved coefficient matrices. We also
give the previously published 34-word construction and a separate
exhaustive coverage check. Thus the supported interval is
$30\le K_3(7,2)\le34$; its exact value remains undetermined.

The proof is computational: the explicitly specified finite certificate
calculation is part of it. External scientific review and a determination
of priority remain pending.

## 1. Statement and context

Let $\Omega=\{0,1,2\}^7$, let $N=|\Omega|=2187$, and write
$d(x,y)=|\{i:x_i\ne y_i\}|$. Put

$$
B_r(a)=\{x\in\Omega:d(x,a)\le r\},\qquad
S_r(a)=\{x\in\Omega:d(x,a)=r\}.
$$

A radius-two covering code is a set $C\subseteq\Omega$ such that
$C\cap B_2(a)\ne\varnothing$ for every $a\in\Omega$. Its minimum possible
cardinality is $K_3(7,2)$. Every ball $B_2(a)$ has
$1+7\cdot2+\binom72 2^2=99$ elements.

**Theorem 1 (computer-assisted).**
Every radius-two covering code in $\Omega$ has at least 30 words.
Consequently,

$$
30\le K_3(7,2)\le34.
$$

No linearity, additivity, or invariance condition on $C$ is assumed.
The upper bound is the construction of Östergård and Hämäläinen [OH93],
reproduced in Section 8.

The starting comparison is Gijswijt and Polak [GP26, Table 2], which
reports $27\le K_3(7,2)\le34$. Their matrix-cut and symmetry-reduction
approach, building on [G05], supplies the methodological background.
The use of moments, nonnegative localizing polynomials, finite-group
averaging, and positive semidefinite matrices is established machinery;
these general principles are not claimed as new here. The contribution
presented for review is the particular strengthening and exact
certificate for this parameter.

Exact rational SDP certificates with standalone checking are also
used in the later covering-code computations of Marosi [M26].
That work reports cells over alphabets of size at least five;
it does not provide a bound for the ternary cell studied here.
The use of exact certification itself is therefore not a novelty claim.

The proof has three components. Sections 2–4 show that an arbitrary
hypothetical 29-word cover supplies moments satisfying the necessary
conditions. Sections 5–7 specify the finite data and exact contradiction.
Section 8 proves the upper bound by the supplied word list. Section 9
records two elementary consequences usable beyond this parameter.

## 2. Moments of an arbitrary covering code

Let $G=S_3^7\rtimes S_7$ act on $\Omega$ by independent symbol
permutations in each coordinate and by coordinate permutations.
Every element of $G$ preserves Hamming distance, and $G$ is transitive
on $\Omega$.

Suppose that a covering code $C$ has exactly $M$ words. Choose $h$
uniformly from $G$ and define the random indicators

$$
X_v=\mathbf1_{\{v\in hC\}}\quad(v\in\Omega).
$$

For each finite set $S\subseteq\Omega$, define

$$
z_S=\frac NM\,\mathbb E\!\left[\prod_{v\in S}X_v\right],
\qquad z_\varnothing=\frac NM.
\tag{1}
$$

Repeated factors are removed using $X_v^2=X_v$. Write $\mathcal L$
for the linear functional on such Boolean polynomials given by
$\mathcal L(\prod_{v\in S}X_v)=z_S$. Thus
$\mathcal L(p)=(N/M)\mathbb E[p(X)]$. This definition also applies to
complex polynomials, with conjugation commuting with $\mathcal L$.

**Lemma 2 (invariance and normalization).**
The value $z_S$ depends only on the $G$-orbit of $S$, and
$z_{\{v\}}=1$ for every $v\in\Omega$.

*Proof.*
For any $g\in G$, the random element $g^{-1}h$ is uniform in $G$.
The products indexed by $S$ and $gS$ therefore have the same
expectation. Transitivity makes $\mathbb E[X_v]$ independent of $v$,
whereas $\sum_v X_v=M$ for every $h$. Consequently
$\mathbb E[X_v]=M/N$. ∎

This averaging makes the *distribution* invariant. It does not replace
the assumed code by an invariant code and imposes no restriction on it.

**Lemma 3 (orbit bounds).**
Let $\mathcal O$ be the orbit of a nonempty $k$-element set. Then

$$
0\le z_{\mathcal O}\le
U_{\mathcal O}:=
\min\left\{1,\frac{N\binom Mk}{M|\mathcal O|}\right\}.
\tag{2}
$$

*Proof.*
Let $n_{\mathcal O}(C)$ count the $k$-subsets of $C$ in $\mathcal O$.
For fixed $S\in\mathcal O$, the set $h^{-1}S$ is uniform on
$\mathcal O$, so
$\mathbb E[\prod_{v\in S}X_v]=n_{\mathcal O}(C)/|\mathcal O|$.
Use $0\le n_{\mathcal O}(C)\le\binom Mk$. Also, for any $u\in S$,
$0\le\prod_{v\in S}X_v\le X_u$; Lemma 2 gives the bound 1. ∎

**Lemma 4 (fixed-cardinality identities).**
For every finite $S\subseteq\Omega$,

$$
\sum_{v\in\Omega}z_{S\cup\{v\}}-M z_S=0.
\tag{3}
$$

*Proof.*
Multiply the pointwise identity $\sum_vX_v=M$ by
$\prod_{u\in S}X_u$ and apply $\mathcal L$. ∎

The certificate uses (3) only when all its moments occur in the
selected finite list. Other necessary identities may be omitted:
any contradiction from a subset of necessary conditions still excludes
the assumed code.

## 3. Nonnegative scalar expressions

For an anchor $a\in\Omega$, define its coverage count and excess by

$$
A(a)=\sum_{v\in B_2(a)}X_v,\qquad g_a=A(a)-1.
$$

Every $hC$ is a covering code, so $A(a)\in\{1,\ldots,M\}$ and
$g_a\ge0$.

**Lemma 5 (Boolean and covering products).**
For any finite lists of anchors $a_1,\ldots,a_r$, selected points
$p_1,\ldots,p_s$, and excluded points $q_1,\ldots,q_t$,

$$
\mathcal L\!\left[
\prod_{\nu=1}^r g_{a_\nu}
\prod_{\nu=1}^s X_{p_\nu}
\prod_{\nu=1}^t(1-X_{q_\nu})
\right]\ge0.
\tag{4}
$$

Lists may contain repetitions, including the same point in the selected
and excluded lists.

*Proof.*
Every factor is nonnegative for each possible indicator vector $X$.
Their product and its expectation are nonnegative, and $N/M>0$. ∎

The finite certificate uses Boolean atoms of degrees four and five,
one covering factor with up to three Boolean factors, and products
with up to four covering and Boolean factors in total.

For clarity, if $p_1,\ldots,p_k$ is an ordered list and
$I\subseteq\{1,\ldots,k\}$, the Boolean-atom expansion is

$$
\mathcal L\!\left[
\prod_{i\in I}X_{p_i}\prod_{j\notin I}(1-X_{p_j})
\right]
=\sum_{J\subseteq I^c}(-1)^{|J|}z_{\{p_i:i\in I\cup J\}}.
\tag{5}
$$

The empty set on the right is interpreted by (1).

**Lemma 6 (integer cubic).**
For any $u\in\Omega$,

$$
\mathcal L\!\left[
X_u(A(0)-1)(A(0)-3)(A(0)-4)
\right]\ge0.
\tag{6}
$$

*Proof.*
For an integer $a\ge1$, the polynomial
$(a-1)(a-3)(a-4)$ is zero at $1,3,4$, equals 2 at $2$, and
is positive at every $a\ge5$. Multiply by $X_u\ge0$ and apply
$\mathcal L$. ∎

Its explicit expansion is
$\mathcal L[X_u(A(0)^3-8A(0)^2+19A(0)-12)]$.
The certificate uses distances $d(0,u)=3,7$.

The remaining scalar family consists of conditional squares. Fix
$u=(1^d,0^{7-d})$, where $1\le d\le7$. For
$0\le b\le7-d$, $r_0,r_1\ge0$, and $r_0+r_1\le d$, put

$$
T_{b,r_0,r_1}(X)=
\sum_{\substack{v:\ |\{i>d:v_i\ne0\}|=b\\
|\{i\le d:v_i=0\}|=r_0,\quad
|\{i\le d:v_i=1\}|=r_1}}X_v.
\tag{7}
$$

For every real vector $v_\alpha$ indexed by these triples,

$$
\mathcal L\!\left[
X_0X_u\left(\sum_\alpha v_\alpha T_\alpha(X)\right)^2
\right]\ge0.
\tag{8}
$$

This follows pointwise from a nonnegative indicator times a square.
All retained vectors have integer entries. The implementation divides
each expanded row by the positive greatest common divisor of its
nonzero integer coefficients; this positive rescaling preserves (8).

## 4. Positive semidefinite matrices

**Lemma 7 (Gram positivity).**
If a real random variable $w(X)$ is nonnegative for every permitted
indicator vector and $p(X)$ is a finite complex vector, then

$$
\mathcal L[w(X)p(X)p(X)^*]\succeq0.
\tag{9}
$$

*Proof.*
For every constant complex vector $a$, its quadratic form equals
$\mathcal L[w\,|a^*p|^2]\ge0$. ∎

We now specify every matrix family with a nonzero multiplier in the
certificate. There are no additional positive semidefiniteness
assumptions.

### 4.1 Shell matrices with a covering factor

Write $H_i(X)=\sum_{v\in S_i(0)}X_v$ for $0\le i\le7$.
For $u=(1^d,0^{7-d})$, define the $8$ by $8$ matrix

$$
B^{\mathrm{sh},d}_{ij}(z)
=\mathcal L[X_u\,g_0\,H_iH_j].
\tag{10}
$$

It is positive semidefinite by Lemma 7 with weight $X_u g_0$.
The certificate uses $d=3,4,5,6,7$. Each entry has degree at most four
after Boolean reduction.

### 4.2 Integer shell-count matrices

For integers $\eta_0,\ldots,\eta_7$ and $j$, put
$T=\sum_i\eta_iH_i$. Since $T$ is integer-valued,
$(T-j)(T-j-1)\ge0$, whether $T$ is positive, zero, or negative.
Consequently

$$
B^{\mathrm{int},\eta,j}_{ab}(z)
=\mathcal L[(T-j)(T-j-1)H_aH_b]\succeq0.
\tag{11}
$$

The two retained choices are

$$
(\eta,j)=((0,0,1,1,1,1,1,1),28),
\qquad
((0,1,0,0,0,0,0,0),0).
$$

Expanding $T^2-(2j+1)T+j(j+1)$ specifies every coefficient of
(11) using radial moments of degrees two, three, and four.

### 4.3 A matrix of ordered center-pair counts

For $0\le i\le7$, define

$$
P_i(X)=\sum_{a\in\Omega}\sum_{v\in S_i(a)}X_aX_v.
$$

The matrix used by the certificate is

$$
B^{\mathrm{pair}}_{ij}(z)=\frac1N\mathcal L[P_iP_j].
\tag{12}
$$

It is positive semidefinite by Lemma 7 and the positive factor $1/N$.
For reconstruction, fix the first anchor to $0$, use invariance, and
group the second anchor by distance $d$. If
$s_d=|S_d(0)|=\binom7d2^d$ and $u_d=(1^d,0^{7-d})$, then

$$
B^{\mathrm{pair}}_{ij}(z)
=\sum_{d=0}^7 s_d
\sum_{\substack{v\in S_i(0)\\w\in S_j(u_d)}}
z_{\{0,u_d,v,w\}}.
\tag{13}
$$

The code names this matrix `fourier_pair`, with frequency index 0.
No nonzero multiplier uses the other frequency indices.

### 4.4 Fourier quadratic matrices

Identify $\Omega$ with $\mathbb F_3^7$, put
$\omega=\exp(2\pi i/3)$, and define the unnormalized transform

$$
\widehat X_\ell=\sum_{a\in\Omega}X_a\omega^{\ell\cdot a}.
$$

For $k\in\{0,\ldots,7\}$ fix $t_k=(1^k,0^{7-k})$. Partition
frequencies $\ell\in\Omega$ into classes $I=(b,a,c)$ as follows:
$b$ is their number of nonzero entries outside the support of $t_k$,
and $a,c$ are the smaller and larger, respectively, of the numbers
of entries 0 and 1 on that support. Thus

$$
0\le b\le7-k,\qquad 0\le a\le c,\qquad a+c\le k.
$$

Write $\Lambda_I$ for such a class and set

$$
Q_I(X)=\sum_{\ell\in\Lambda_I}
\widehat X_\ell\widehat X_{t_k-\ell},\qquad
B^{\mathrm{fq},k}_{IJ}(z)
=\frac1N\mathcal L[Q_I\overline{Q_J}].
\tag{14}
$$

Each matrix in (14) is Hermitian positive semidefinite by Lemma 7.
The dimensions, in order $k=0,\ldots,7$, are
$8,14,24,30,36,36,32,20$.

All their coefficients in the orbit moments are real integers. To see
this and obtain an exact reconstruction, expand the four transforms.
Their frequency tuple is
$(\ell,t_k-\ell,-m,m-t_k)$, whose sum is zero. Translation
invariance permits fixing the first spatial word to $0$; the $N$
choices for its original value cancel $1/N$ in (14). In one coordinate,
let $f=(f_1,f_2,f_3,f_4)$ be the frequency tuple and let $p$ specify
the equality partition of the four spatial symbols. Summing over
symbols with first symbol 0 gives the integer

$$
D(f,p)=
\begin{cases}
1,&p\text{ has one block},\\
2,&p\text{ has two or three blocks and }f\cdot p=0\pmod3,\\
-1,&p\text{ has two or three blocks and }f\cdot p\ne0\pmod3.
\end{cases}
\tag{15}
$$

Here the blocks are labeled by their order of first occurrence.
For two or three blocks there are exactly two compatible assignments
with first symbol 0; they are negatives of one another. Their phases
sum to 2 or to $\omega+\omega^2=-1$. For one block the phase is 1.
Multiplying (15) across the seven coordinates, summing over
$\ell\in\Lambda_I,m\in\Lambda_J$, and collecting the resulting
set-orbit keys reconstructs (14) without floating-point complex
arithmetic. The coefficient arrays are therefore real symmetric.

## 5. The finite moment list and its exact encoding

Set $M=29$ for the rest of the lower-bound proof. The finite list has
4,294 nonempty set-orbit moments: all 4,085 orbits of sets of sizes at
most four, together with 209 selected orbits of five-element sets.
The constant coordinate is separate and is not a further unknown moment.

### 5.1 Complete orbits through degree four

For an ordered list of $r$ words, each coordinate specifies an equality
partition of $\{1,\ldots,r\}$ into at most three blocks. Represent a
partition by its restricted-growth string, beginning with 0 and assigning
new labels in order of first occurrence. Two ordered lists are
equivalent under $G$ precisely when their multisets of coordinate
partitions agree. For unordered sets, minimize also over permutations
of the rows.

For four rows there are 14 possible coordinate patterns. Enumerating
all weak compositions of seven into these 14 types gives
$\binom{20}{13}=77,520$ ordered-list types. This enumeration is
complete because any four words yield one such composition, and each
composition is realized by concatenating the indicated columns.
Permuting the four rows and collapsing repeated words produces exactly
4,085 distinct nonempty set types.

The implementation orders the 14 patterns lexicographically. If $n_p$
is a pattern multiplicity, the four-element key is

$$
2^{50}+\min_{\pi\in S_4}\sum_{p=0}^{13}n_p\,8^{\pi(p)}.
\tag{16}
$$

Here $\pi(p)$ means the pattern induced by the row permutation.
Every multiplicity is at most seven, so the base-eight representation
has no carries. For at most three distinct words, repeat the first word
if necessary to obtain a triple, let $d_1\le d_2\le d_3$ be its pair
distances, and let $e$ be the number of coordinates with three distinct
symbols. Its key is

$$
((8d_1+d_2)8+d_3)8+e.
\tag{17}
$$

The three distances and $e$ determine the five triple-pattern
multiplicities, up to row permutation, so (17) distinguishes these
orbits. A singleton has key 0. Sort the 4,085 keys increasingly; this
is the order of columns 0 through 4,084. The first 95 are precisely
the orbits of sets of size at most three.

The same construction with the first row fixed and only the last
three rows permuted produces 14,176 rooted types. These are used to
index the one-covering-factor inequalities, whose root is 0.

### 5.2 Selected fifth moments

Enumerate the four-element subsets of the 15-word ball $B_1(0)$
in lexicographic word order. Under the preceding set equivalence they
have five types. Take the first encountered representative of each
type, preserving first-encounter order. For each representative $S$,
enumerate $S\cup\{v\}$ for all $v\in\Omega\setminus S$. These sets
have 209 distinct five-element orbit types.

Five rows have 41 possible restricted-growth patterns. For each row
permutation $\pi$, sort the seven coordinate-pattern indices as
$p^\pi_0\le\cdots\le p^\pi_6$. The five-element key is
$2^{60}+\min_{\pi\in S_5}\sum_{j=0}^6p^\pi_j64^j$.
The indices are less than 64 and the packed sum is less than
$2^{42}$, so the encoding, including its digit order, is unambiguous.
Append the 209 increasing keys after the degree-four keys.

This selection makes all five identities (3) for the chosen
four-element sets meaningful in the finite moment list. The other
95 identities (3) use the first 95 orbit representatives. Together
with $z_{\{0\}}=1$, there are 101 retained identities.

### 5.3 Orbit sizes

**Lemma 8 (set stabilizer).**
Let $S$ have $k$ distinct words, written as rows. For each equality
pattern $p$, let $n_p$ count its columns. Let $a(S)$ be the number
of permutations of the $k$ rows that preserve this multiset of
patterns, and let $n_{\mathrm{eq}}$ count columns whose entries
are all equal. Then

$$
|\operatorname{Stab}_G(S)|
=a(S)\,2^{n_{\mathrm{eq}}}\prod_p n_p!,
\qquad
|\mathcal O(S)|=
\frac{7!\,6^7}{a(S)\,2^{n_{\mathrm{eq}}}\prod_p n_p!}.
\tag{18}
$$

*Proof.*
An isometry stabilizing a set of distinct rows induces a unique
permutation of those rows. Such a permutation is possible exactly
when it preserves the multiset of equality patterns. For any such
row permutation, equal-pattern columns can be matched in
$\prod_pn_p!$ ways. In a matched column with $b$ distinct symbols,
the prescribed bijection of its used symbols extends to a symbol
permutation in $(3-b)!$ ways. This number is 2 for a constant column
and 1 otherwise. Multiplication gives the stabilizer formula;
orbit-stabilizer gives the second identity. ∎

For singletons and pairs, the implementation equivalently uses
$|\mathcal O|=2187$ and
$|\mathcal O|=2187\binom7d2^d/2$, respectively. It recomputes every
bound (2) from these cardinalities and (18). As a completeness
control, for each $k=1,2,3,4$ the sum of the orbit sizes is checked
to be $\binom{2187}{k}$.

## 6. The exact certificate

All finite data accompany the [exact checker](proof/verify.py).
The main files are:

| File | Mathematical content |
| --- | --- |
| [certificate.json](proof/certificate.json) | Nonnegative scalar multipliers, integer Gram factors, signed equality multipliers, and the resulting coefficient vector |
| [orbit-box.json](proof/orbit-box.json) | The 4,294 rational bounds (2) and the exact final upper estimate |
| [scalar-selection.json](proof/data/scalar-selection.json) | Selected Boolean-atom indices and the vectors in (8) |
| [scalar-product-witnesses.json](proof/data/scalar-product-witnesses.json) | Literal anchor and Boolean-factor lists for products (4) |

The two primary input SHA-256 digests are:

```text
certificate.json
7aff789b16f702aac7dc3cac37642760878bc6fc0ff25f52214f0c8e1922a4c4

orbit-box.json
355eb1930b175fe7192ad6172c3e23a41f51876905be5d0550a06fd660963f40
```

Digests identify the data; they do not establish the validity of
their mathematical contents. That validity follows from the
reconstruction and exact calculation below.

### 6.1 The scalar support

The certificate contains nine named scalar groups, of which two
have no nonzero weights. Their total nonzero support is 4,753 rows.

| Group key, or its distinguishing prefix | Rows with nonzero weight | Interpretation |
| --- | ---: | --- |
| `boolean_cover_all` | 2,758 | $g_0$ times a three-factor Boolean atom, (4) |
| `atoms4` | 15 | Four-factor Boolean atoms, (5) |
| `two_cover` | 578 | Covering/Boolean products, (4) |
| `quartic-cuts29-r1.npz` | 28 | 24 products (4) and four instances of (6) |
| `selected-psd-cuts-29-…` | 124 | Conditional squares, (8), with positive gcd normalization |
| `atoms5` | 696 | Five-factor Boolean atoms, (5) |
| `accumulated_full_r0` | 554 | Covering/Boolean products, (4) |
| `old`, `pair_integer` | 0 | Unused; no rows from these groups enter the proof |

Names containing `.npz` are historical group labels. No NPZ file is
an input to the verification.

For `boolean_cover_all`, a row index is $m\cdot14176+t$, where
$0\le m<8$ selects the positive Boolean factors on the last three
points of rooted representative $t$; its complement selects the
negative factors. For `atoms4`, the metadata maps the retained row
index to $m\cdot4085+t$, with $0\le m<16$. For `atoms5`, the index
is $32t+m$, with $0\le t<209$ and $0\le m<32$, in the fifth-orbit
order of Section 5.2.

The literal product witnesses specify all other products in (4).
Indices 30, 31, 32, 33 of the quartic group mean (6) with
$d(0,u)=7,3,3,7$, respectively. Repeated inequalities with
different nonnegative weights cause no difficulty.

For (8), a metadata block `["pair",b]` has $b$ divisible by three
and specifies $d=b/3+1$. Its vector is in increasing order of
$(b',r_0,r_1)$ in (7). These indexing conventions determine every
nonzero scalar polynomial from the supplied finite lists.

### 6.2 The Gram support

There are 16 matrices with nonzero factors, comprising 33 nonzero
integer factor columns.

| Matrix | Dimensions | Nonzero factor columns |
| --- | --- | --- |
| $B^{\mathrm{sh},d}$, $d=3,\ldots,7$ | $8$ each | $1$ each |
| First choice in (11) | $8$ | $5$ |
| Second choice in (11) | $8$ | $1$ |
| $B^{\mathrm{pair}}$ | $8$ | $1$ |
| $B^{\mathrm{fq},k}$, $k=0,\ldots,7$ | $8,14,24,30,36,36,32,20$ | $1,2,1,3,3,3,3,5$ |

For each block $b$, the data give an integer matrix $L_b$.
The multiplier $L_bL_b^{\mathsf T}$ is positive semidefinite
by construction. Its contraction with the raw matrix $B_b(z)$ is

$$
\langle L_bL_b^{\mathsf T},B_b(z)\rangle
=\sum_{\text{columns }\ell\text{ of }L_b}
\ell^{\mathsf T}B_b(z)\ell\ge0.
\tag{19}
$$

In the stored labels, `["shell",2d]` means (10);
`radial_selected_integer` means (11); `["fourier_pair",0]`
means (12); and `["fourier_quadratic",k]` means (14).
All other stored Gram factors are zero and contribute nothing.

### 6.3 Aggregation and normalization

Let $R_i(z)$ be the raw scalar expressions in Section 6.1, and let
$E_j(z)$ be the 100 left sides of (3) selected in Section 5.
The certificate supplies nonnegative integers $w_i$, the integer
matrices $L_b$, signed integers $\lambda_j$, and a signed integer
$\lambda_*$ for the singleton identity. Define

$$
F(z)=2^{-120}\left[
M\sum_iw_iR_i(z)
+M\sum_b\langle L_bL_b^{\mathsf T},B_b(z)\rangle
+\sum_j\lambda_jE_j(z)
+\lambda_*(z_{\{0\}}-1)
\right].
\tag{20}
$$

The displayed factors $M=29$ are intentional. Every raw scalar or
Gram row represents $\mathcal L$ applied to its polynomial; its
empty-moment entry is $N/M$. Multiplication by $M$ therefore
multiplies nonempty-moment coefficients by 29 and the empty entry
by 2187. The fixed-cardinality and singleton identities are already
expressed in $z$ and are not multiplied by this extra factor.
This matches exactly the aggregation in `verify.py`.

Equivalently, scalar and equality multipliers have denominator
$2^{120}$, and Gram factors have denominator $2^{60}$; their
products also have denominator $2^{120}$.

By Lemmas 4–7 and (19), every hypothetical 29-word cover gives

$$
F(z)\ge0.
\tag{21}
$$

After Boolean expansion and orbit collection, write

$$
F(z)=2^{-120}\left(c_\varnothing+
\sum_{\mathcal O}c_{\mathcal O}z_{\mathcal O}\right).
\tag{22}
$$

All $c_{\mathcal O}$ are integers. Their complete ordered list,
followed by $c_\varnothing$, is the field
`combined_integer_coefficients` of `certificate.json`.
The checker reconstructs all 4,295 entries from (20) and compares
the entire vector to that field. In particular,

$$
c_\varnothing=-534530428526633002442351867126464512.
$$

**Lemma 9 (exact finite certificate calculation).**
For the coefficients reconstructed from the supplied data,

$$
2^{-120}\left(c_\varnothing+
\sum_{c_{\mathcal O}>0}c_{\mathcal O}U_{\mathcal O}\right)
=-\frac{5058649380435826018685689638659}
{1276058875953519237987654777869130792960}<0.
\tag{23}
$$

*Verification.*
Expand the scalar and Gram expressions by the finite procedures
in Sections 3–5 and Appendix A, form (20) with integer arithmetic,
and recompute each $U_{\mathcal O}$ using (2) and (18).
Sum only the positive-coefficient terms in (23), using rational
arithmetic. The supplied program
[verify.py](proof/verify.py) performs these steps, checks every
coefficient and bound against the supplied lists, and checks
exactly the numerator, denominator, and negative sign in (23).
The reproduced output is [verification.json](proof/verification.json).
Appendix A describes the finite coefficient algorithms, and
[reproduction.md](reproduction.md) gives the commands and dependencies.
Neither a stored success report nor a numerical solver result is an
input to this calculation. ∎

The stronger upper bounds in (2) are material. If every
$U_{\mathcal O}$ is replaced by 1, the numerator before division
by $2^{120}$ is the positive integer
$151152861867856550173546616200$.

## 7. Proof of the lower bound

*Proof of Theorem 1, lower-bound part.*
Suppose first that $|C|=29$. Lemmas 2–4 give the normalized
orbit moments, bounds, and identities. Sections 3 and 4 establish
the nonnegativity and positive semidefiniteness of every expression
used with a nonzero multiplier. Hence (21) holds.

On the other hand, (2) and (22) imply

$$
F(z)\le2^{-120}\left(c_\varnothing+
\sum_{c_{\mathcal O}>0}c_{\mathcal O}U_{\mathcal O}\right)<0
$$

by Lemma 9: positive coefficients use their upper bounds, and
negative coefficients use $z_{\mathcal O}\ge0$.
This is a contradiction.

If a cover had fewer than 29 words, add distinct ambient words
until its size is 29. There are 2,187 available words, and adding
words cannot destroy coverage. The resulting cover has just been
excluded. Thus every cover has size at least 30. ∎

## 8. The published upper bound

The following 34 words reproduce the construction in [OH93,
Table III, printed p. 22], decoded using the skip-vector convention
on printed p. 16:

```text
0012200 0020020 0020101 0020212 0101002 0101110 0101221
0120101 0212011 0212122 0220200 1002020 1002101 1002212
1021200 1102212 1110002 1110110 1110221 1202200 1221011
1221122 2000200 2011011 2011122 2111020 2122002 2122110
2122221 2200011 2200122 2211020 2211101 2211212
```

**Proposition 10.**
The displayed set has covering radius two.

*Verification.*
For each $x\in\{0,1,2\}^7$, compute
$r(x)=\min_{c\in C}|\{i:x_i\ne c_i\}|$ by direct coordinate
comparison. The exact frequency table is

| $r(x)$ | 0 | 1 | 2 | At least 3 |
| --- | ---: | ---: | ---: | ---: |
| Number of words | 34 | 467 | 1,686 | 0 |

The entries sum to 2,187. The separate checker
[check_cover.py](proof/check_cover.py) enumerates all ambient
words and computes precisely these distances; it also validates
the alphabet, word length, and distinctness of the 34 centers.
The input is [known34.txt](proof/known34.txt).
This is a finite exhaustive check of the displayed object, so it
proves the proposition and completes the upper-bound part of
Theorem 1. ∎

No improvement of this published construction is claimed.

## 9. Two structural observations

These lemmas are independent of the certificate calculation.
They give reusable constraints and a construction criterion.
Neither is used to infer nonexistence from a restricted search.

### 9.1 Counting in coordinate slices

**Lemma 11.**
Let $n\ge5$, and let $C\subseteq\{0,1,2\}^n$ be a radius-two
cover of size $M$. Fix two coordinate positions. Let $a_{ij}$
count centers with symbols $i,j$ in those positions, and let
$r_i=\sum_j a_{ij}$, $c_j=\sum_i a_{ij}$. Then

$$
M+2(n-2)\bigl((n-4)a_{ij}+r_i+c_j\bigr)\ge3^{n-2}.
\tag{24}
$$

*Proof.*
Consider the $3^{n-2}$ words with these two fixed symbols.
A center agreeing with both can cover at most
$1+2(n-2)+4\binom{n-2}{2}=1+2(n-2)^2$ of them.
A center agreeing with just one covers $1+2(n-2)$, and a
center agreeing with neither covers one. The three numbers
of centers are $a_{ij}$, $r_i+c_j-2a_{ij}$, and
$M-r_i-c_j+a_{ij}$. Their total covering capacity must be at
least $3^{n-2}$. Expansion gives (24). Overlaps can only
decrease the number covered, so the counting is valid. ∎

Put $d=n-4>0$ and
$R=\left\lceil(3^{n-2}-M)/(2(n-2))\right\rceil$.
Integrality in (24) gives
$d a_{ij}+r_i+c_j\ge R$. Summing a row yields
$(n-1)r_i+M\ge3R$.

If a row has margin $r$ and equality
$(n-1)r+M=3R$, then every column margin satisfies

$$
c_j\le R-r,\qquad c_j\equiv R-r\pmod{n-4},
\qquad a_{ij}=\frac{R-r-c_j}{n-4}.
\tag{25}
$$

Indeed, let $b_j=\max(0,\lceil(R-r-c_j)/d\rceil)$.
Then $a_{ij}\ge b_j$ and
$e_j=d b_j-(R-r-c_j)\ge0$. Since $\sum_jc_j=M$,

$$
\sum_j e_j=d\sum_j b_j-3R+3r+M
\le(n-1)r+M-3R=0.
$$

All $e_j$ vanish, and equality forces $\sum_jb_j=r$.
Thus $a_{ij}=b_j$ in every cell, giving (25).
At $n=5$ the congruence modulo 1 is vacuous, while the other
conclusions still hold.

### 9.2 Lifting by assigning one coordinate

**Lemma 12.**
Let $q\ge2$, $n\ge2$, and $R\ge1$ be integers. Let
$T\subseteq\{0,\ldots,q-1\}^{n-1}$ and
$f:T\longrightarrow\{0,\ldots,q-1\}$. Then

$$
C_f=\{(t,f(t)):t\in T\}
$$

is a radius-$R$ cover if and only if, for each prefix
$x$ with $d(x,T)\ge R$, the values
$\{f(t):t\in T,\ d(x,t)=R\}$ contain all $q$ symbols.
For $T=\varnothing$ use $d(x,T)=+\infty$.

*Proof.*
If $d(x,t)\le R-1$ for some $t$, each extension $(x,a)$ is
within distance $R$ of $(t,f(t))$. Otherwise every distance
$d(x,t)$ is at least $R$. In that case
$d((x,a),(t,f(t)))\le R$ holds precisely when
$d(x,t)=R$ and $a=f(t)$. Hence all extensions of $x$ are
covered exactly under the stated condition. ∎

For $q=3,R=2$, a critical prefix with exactly three
distance-two neighbors requires three different colors on them.
This supplies exact local obstructions for a construction search.
The lemma concerns codes with injective projection onto the first
$n-1$ coordinates; it does not assert that every covering code
has such a projection.

## Appendix A. Finite coefficient reconstruction

This appendix explains how the verifier implements the mathematical
expressions above. Its input data consist of multipliers, integer
vectors, literal words, and orbit bounds, rather than precomputed
constraint matrices.

### A.1 Boolean reduction and direct products

In every monomial, remove duplicate word variables and replace the
remaining set by its key in Section 5. The empty monomial maps to
the separate constant slot. For a covering factor, use
$g_a=\sum_{v\in B_2(a)}X_v-1$ and enumerate the 99 literal ball
words. Boolean complements are expanded by (5).
This directly gives every atom and each product with at most
three covering factors, using at most $99^3$ ordered ball choices
for a highest-degree term.

The conditional cubic is expanded as in (6), with one, two, and
three literal ball variables. Its ordered enumeration counts
$99,99^2,99^3$ terms before collecting coincident variables.

### A.2 Four covering factors

The implementation computes the four-ball products using an exact
finite adjacency recurrence. Let $A_1,A_2$ be the distance-one
and distance-two matrices of $\Omega$. Counting two-step walks
gives

$$
A_1^2=14I+A_1+2A_2,
\qquad
I+A_1+A_2=\frac{A_1^2+A_1-12I}{2}.
\tag{26}
$$

There are 14 two-step returns, one two-step walk between
distance-one words (through the third symbol), and two between
distance-two words (the two coordinate orders).

For each of the four slots of an ordered tuple, move that word
to each of its 14 neighbors and count transitions among the
77,520 coordinate-pattern types of Section 5.1. This is a valid
quotient operation because each Hamming isometry preserves
neighbor counts into every type. Apply the second identity of
(26) in each selected slot. It enumerates its entire radius-two
ball, with total mass multiplied by 99. The four slot operations
commute because they act on distinct components.

Expand the excess products by inclusion-exclusion, and finally
project each resulting tuple to its set-orbit moment. This is
exactly the direct four-ball polynomial expansion, computed through
a finite quotient. Division by two in (26) is checked to be
integral at every application. A three-ball instance is also
cross-checked against literal enumeration.

### A.3 Conditional pair and shell counts

For a fixed pair $(0,u_d)$, an ordered pair $(v,w)$ is described
by the equality-pattern counts $n_p$ of $(0,u_d,v,w)$.
If $t$ is the number of coordinates where the anchors agree
but the four symbols are not all equal, the multiplicity is

$$
\gamma=\frac{(7-d)!\,d!\,2^t}{\prod_p n_p!}.
\tag{27}
$$

Indeed, allocate the coordinate patterns within the agreeing
and differing anchor positions by multinomial coefficients.
An agreeing position with a nonconstant pattern has two choices
for the other symbol labeling; all other positions have one.
This proves (27). Summing it over all conditional types gives
$N^2$, the number of ordered choices $(v,w)$.

Formula (27), multiplied by the specified vector entries,
reconstructs (8). Summing a further ball variable reconstructs
(10), with the negative constant of $g_0$ subtracted. Equation
(13) can alternatively be reconstructed by multiplying the
one-coordinate pattern-count polynomials for $(0,u_d,v,w)$.
The supplied checker uses this alternative for the pair matrix.

### A.4 Radial products

Write
$R_{i_1,\ldots,i_r}(z)=\mathcal L[H_{i_1}\cdots H_{i_r}]$.
It is the sum of $z_{\{v_1,\ldots,v_r\}}$ over ordered choices
$v_\nu\in S_{i_\nu}(0)$, with repeats allowed. This definition
already gives a finite independent reconstruction.

The implementation groups choices by equality-pattern types
of $r$ rows, for $r=2,3,4$. If $a$ row permutations preserve
the pattern histogram and $c$ columns are constant, the
multinomial orbit weight, divided by the number $N$ of possible
origins, is

$$
\frac{7!\,2^{7-c}\,r!}{a\prod_p n_p!}.
\tag{28}
$$

This follows by applying orbit-stabilizer to the combined
isometry and row-permutation action on ordered tuples, then
dividing by $N$. For each representative tuple, enumerate all
$N$ possible origins and count its sorted distances from that
origin. If the required distance multiset has multiplicities
$m_i$, divide by $r!/\prod_i m_i!$ to obtain one fixed ordering
of the shell indices. Symmetry in the tuple positions makes
these contributions equal. All divisions are exact. The sum
of each resulting row is checked to be
$\prod_{\nu=1}^r\binom7{i_\nu}2^{i_\nu}$.

The expansion stated after (11) then gives the two integer
shell-count matrices.

### A.5 Fourier products

Equation (15) is the one-coordinate transform. Products of its
14-pattern coefficient vectors across seven coordinates are
collected by histogram and then by the set-orbit key. Coordinate
permutations, row permutations, and simultaneous negation of the
frequency tuple reduce the repeated work; each preserves the
collected expression. All frequencies $\ell,m$ in the classes
of (14) are counted, using seven nine-choice coordinate
polynomials. The resulting class-pair counts sum to the product
of their class cardinalities,

$$
|\Lambda_{(b,a,c)}|
=\binom{7-k}{b}2^b\cdot
\frac{k!}{a!\,c!\,(k-a-c)!}\cdot
\begin{cases}1,&a=c,\\2,&a<c.\end{cases}
\tag{29}
$$

The reconstruction uses only integer coefficients: no numerical Fourier transform or
eigenvalue test enters the proof.

### A.6 Exact arithmetic and acceptance

Raw finite counts are held in signed 64-bit integer arrays where
their magnitudes are bounded. For example, a seven-coordinate
transform row in A.5 has sum of absolute coefficients at most
$3^{21}$, and a compressed class-pair count is at most $2187^2$;
their product is less than $2^{63}$. The conditional-square and
integer-localizer computations check corresponding explicit
absolute-sum bounds. The final weighted Gram contractions,
coefficient aggregation, orbit fractions, and (23) use arbitrary
precision Python integers and fractions.

The acceptance procedure is:

1. Validate the target $M=29$, dimensions, data grammar, signs of
   scalar weights, integer Gram factors, and dyadic denominators.
2. Reconstruct every nonzero scalar and Gram row from the definitions
   above; reject an unsupported or unaccounted-for nonzero row.
3. Reconstruct all retained cardinality identities and the singleton
   identity, and compare all 4,295 coefficients of (20).
4. Recompute all orbit sizes and bounds and the exact negative
   quantity (23).
5. Independently check the 34-word construction over all 2,187 words.

The checker rejects optimized Python execution, because assertions
are part of its acceptance procedure. Corruption controls test
invalid word witnesses and a changed Gram-factor entry; for the
latter, the initial certificate hash check is deliberately bypassed
in memory so that coefficient reconstruction must detect the
inconsistency. No input file is changed by these controls.

Ordinary correctness of the interpreter, integer-array libraries,
and hardware is part of the computational trust basis. The package
is not a formalization in a proof assistant. Its separately
implemented checker is distinct from the numerical discovery
programs; all present checking remains contributor checking,
not an independent human review or the repository's approved
“Machine checked” designation.

## References and attribution

[GP26] Dion Gijswijt and Sven Polak,
*Semidefinite lower bounds for covering codes*,
[arXiv:2504.01932v2](https://arxiv.org/html/2504.01932v2),
19 June 2026, especially the moment/matrix-cut formulation,
Table 2, and Appendix B. Journal metadata:
*IEEE Transactions on Information Theory* 72(9), 6599–6614
(2026), [DOI 10.1109/TIT.2026.3706793](https://doi.org/10.1109/TIT.2026.3706793).
The inspected full text is the arXiv version; the final journal
text remains uninspected.

[G05] Dion C. Gijswijt,
*Matrix Algebras and Semidefinite Programming Techniques for Codes*,
Ph.D. thesis, University of Amsterdam, 2005,
[author's institutional copy](https://pure.uva.nl/ws/files/3915123/37219_Gijswijt.pdf),
Sections 5.3.1–5.3.2, printed pp. 53–59.

[OH93] Patric R. J. Östergård and Heikki O. Hämäläinen,
*New Upper Bounds for Binary/Ternary Mixed Covering Codes*,
Research Report A22, Digital Systems Laboratory, Helsinki University
of Technology, March 1993, 33 pp.,
[primary report](https://www.tcs.hut.fi/Publications/bibdb/HUT-TCS-A22.ps),
especially printed pp. 16 and 22. This is the source of the
construction in Section 8.

[Keri] Gerzson Kéri,
*Tables for bounds on covering codes*,
[table index](https://old.sztaki.hu/~keri/codes/index.htm),
[ternary table](https://old.sztaki.hu/~keri/codes/3_tables.pdf),
and [bibliography](https://old.sztaki.hu/~keri/codes/biblio.pdf),
inspected 19 October 2026. The construction source key led to
[OH93]; the served lower-bound table predates [GP26].

[LPS16] Bart Litjens, Sven Polak, and Alexander Schrijver,
*Semidefinite bounds for nonbinary codes based on quadruples*,
[arXiv:1602.02531v1](https://arxiv.org/pdf/1602.02531),
8 February 2016, Section 2.1, equations (7)–(8).
Its representation-theoretic framework informed numerical
discovery; the raw Gram identities in Section 4, rather than a
numerical block decomposition, justify the delivered certificate.

[M26] Márk Marosi,
*New upper and lower bounds on covering codes $K_q(n,R)$ for
alphabets of size $5\le q\le21$*,
[arXiv:2608.19872v3](https://arxiv.org/html/2608.19872v3),
2 September 2026. Its search and exact-certificate procedures
provide related computational precedent. Its stated alphabet range
does not include the present parameter.

The [GP26 companion implementation](https://github.com/CoveringCodes/Julia/tree/32b46d8dbdeb49e1743c6ea83760a896bd6ca5eb)
was inspected and credited as prior work. It is not required to
run this proof package. The exact checker and certificate have
their retained lineage in [source-map.json](proof/source-map.json).
The local derivations of the particular constraints and of
Lemmas 11–12 do not establish their novelty in the literature.

Substantive AI assistance, model provenance, contributor roles,
and the absence of external scientific review are recorded once
in [ASSISTANCE.md](ASSISTANCE.md). The checks for this exact
version are recorded in [CHECK_REPORT.md](CHECK_REPORT.md).
The finite certificate establishes only the stated lower bound;
it does not determine the exact covering number or certify
priority or significance.


