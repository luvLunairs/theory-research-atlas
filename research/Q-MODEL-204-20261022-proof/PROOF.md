# Integer compensation and conditional EFX and Pareto optimality for personalized bivalued goods

**Q-MODEL-204 — complete proofs of partial results, 22 October 2026.** Prepared for Theory Research Atlas at the request of its connected maintainer account, @luvLunairs. Scientific review and novelty assessment remain pending. This manuscript does not settle unrestricted EFX and Pareto-optimal existence.

**Abstract.** We study complete allocations of indivisible goods with additive values in an agent-dependent positive pair. After normalizing low values to one, we characterize exactly when a fixed assignment of the other goods can be Pareto improved by redistributing a finite pool of universally unit-valued goods. We characterize the assignments that remain Pareto optimal for every such pool and derive a balanced EFX completion, a sharp normalized welfare-deficit bound, and an exact finite obstruction description. A modular residual-capacity theorem gives a sufficient condition for these assignments with arbitrary real ratios and unbounded high-good degrees. Separately, we construct a three-agent, twelve-good family in which every Nash-product maximizer among EFX allocations is Pareto dominated, while an explicit EFX and globally Pareto-optimal allocation exists; both constrained product optima are determined exactly. All analytic claims are proved below without using the finite computations as premises.

**Relation to the literature.** Jin and Tao [1, Section 5] explicitly ask whether complete EFX and integral Pareto-optimal allocations always coexist for personalized bivalued goods. Their separate failures of unrestricted Nash maximization and fractional Pareto optimality do not resolve this question. Lin, Wu and Zhou [2, Theorem 3.5 and Example 3.6] give a tight two-thirds EFX guarantee for unrestricted Nash maximizers, which does not establish exact joint existence. Section 8 below concerns the different rule of maximizing Nash product *within* the EFX set. Further inspected literature and its precise scope are recorded in [SOURCES.md](SOURCES.md).

**Reading the claims.** Sections 2–4 and 6–7 concern an arbitrary fixed additive core with values at least one and additional universal unit goods. Section 5 specializes to personalized bivalued values. Section 8 gives an explicit personalized bivalued construction. Section 9 separates finite exact evidence from the analytic results. The provenance and execution records for the entire submitted version are in [ASSISTANCE_AND_CHECKS.md](ASSISTANCE_AND_CHECKS.md).


## 1. Model and notation

There are $n\geq1$ agents and finitely many indivisible goods. Utilities are additive. In the personalized bivalued model, agent $i$'s values lie in $\{b_i,a_i\}$, where $0<b_i<a_i$. Dividing that agent's utility by $b_i$ preserves every EFX inequality and every Pareto comparison. We therefore use normalized values $\{1,r_i\}$, where $r_i=a_i/b_i>1$.

An allocation is **complete** if every good is assigned to exactly one agent. It is **EFX** if, for every pair of agents $i,j$ and every $g\in X_j$,
$$
v_i(X_i)\geq v_i(X_j\setminus\{g\}).
$$
It is **Pareto optimal (PO)** if no complete integral allocation weakly increases all agents' utilities and strictly increases at least one.

For several intermediate results, allow arbitrary additive values at least $1$ on a fixed finite set $E$ of **core goods**. Additional **universal goods** have value exactly $1$ to every agent. A core allocation $C=(C_1,\ldots,C_n)$ partitions $E$. Write $V_i=v_i(C_i)$. For $l\in\mathbb Z_{\geq0}^n$, the notation $C+l$ denotes the complete allocation obtained by adding $l_i$ universal goods to agent $i$. The identities of the universal goods are immaterial, but their number is preserved in every comparison.

Call $C$ **robust** if $C+l$ is globally PO for every $l\in\mathbb Z_{\geq0}^n$. This definition quantifies over all finite universal pools and all distributions of each pool. Write $x^+=\max(x,0)$ and $\{x\}=x-\lfloor x\rfloor$.

## 2. Exact integral compensation

**Lemma 2.1 (finite-pool compensation).** Fix $C,l$, and let $Y$ be any complete allocation of the same core goods. Put
$$
W_i=v_i(Y_i),\qquad d_i=\lceil V_i-W_i\rceil,
\qquad P=\sum_i d_i^+,\qquad t_i=(-d_i)^+.
$$
There is a redistribution of the same universal pool which, together with $Y$, strictly Pareto improves $C+l$ if and only if
$$
\sum_iW_i>\sum_iV_i
\quad\text{and}\quad
\sum_i\min(l_i,t_i)\geq P. \tag{2.1}
$$

*Proof.* A new nonnegative integer low count $l'_i$ preserves agent $i$'s utility exactly when
$$
l'_i\geq l_i+V_i-W_i,
\quad\text{equivalently}\quad
l'_i\geq \max(0,l_i+d_i).
$$
Consequently a complete weak improvement with core $Y$ exists exactly when
$$
\sum_i\max(0,l_i+d_i)\leq\sum_i l_i.
$$
If this inequality holds, assign the displayed minimum counts and distribute the remaining universal goods arbitrarily. For $d_i\geq0$, the contribution to the difference of these two sums is $d_i$. For $d_i<0$, it is $-\min(l_i,-d_i)$. Hence the inequality is equivalent to the second condition in (2.1). Since the pool is unchanged, the sum of all normalized utilities changes by exactly $\sum_i(W_i-V_i)$. A feasible weak improvement is strict exactly when this sum is positive. This proves both directions. $\square$

The ceiling in this lemma is applied after aggregating an agent's entire utility change. Rounding individual goods or exchange paths separately would give a different condition and is not justified. Equally, $Y$ must be an actual complete allocation: arbitrary count vectors cannot replace feasible assignments.

**Corollary 2.2 (all-pool criterion).** For a complete alternative core $Y$, put $d_i=\lceil V_i-W_i\rceil$ and $D=\sum_i d_i$. Then $C$ is robust if and only if every such $Y$ satisfies either
$$
D>0,
\quad\text{or}\quad
D=0\ \text{and}\ W_i+d_i=V_i\ \text{for every }i. \tag{2.2}
$$

*Proof.* Every weak improvement has $l'_i-l_i\geq d_i$; summing and using equal pool sizes gives $D\leq0$. If $D=0$, equality must hold in every count inequality, and strict improvement occurs exactly when some rounding slack $W_i+d_i-V_i$ is positive.

Conversely, suppose (2.2) fails. Choose $l_i\geq\max(0,-d_i)$ for each $i$. If $D<0$, assign $l_i+d_i$ universal goods to agent $i$, then distribute the $-D>0$ remaining goods. Every agent weakly improves and a recipient of a remaining good strictly improves. If $D=0$ and some rounding slack is positive, the counts $l_i+d_i$ already give a strict improvement. Thus failure of (2.2) contradicts robustness, completing the proof. $\square$

## 3. An exact characterization of robust cores

**Theorem 3.1 (rounded-phase characterization).** A core $C$ is robust if and only if there exists $\theta\in\mathbb R^n$ such that $C$ lexicographically maximizes
$$
\left(\sum_i\lceil v_i(Y_i)-\theta_i\rceil,
      \sum_i v_i(Y_i)\right) \tag{3.1}
$$
over all complete core allocations $Y$.

*Proof.* Suppose first that $C$ maximizes (3.1). For any $Y$, the elementary ceiling inequality gives
$$
\lceil V_i-W_i\rceil
\geq\lceil V_i-\theta_i\rceil-\lceil W_i-\theta_i\rceil.
$$
After summing, primary optimality gives $D\geq0$. If $D=0$, the primary scores must tie. Each $W_i+d_i-V_i$ is nonnegative. If one were positive, then
$$
\sum_iW_i-\sum_iV_i
=\sum_i(W_i+d_i-V_i)-D>0,
$$
contradicting secondary optimality. Corollary 2.2 proves robustness.

Conversely, suppose $C$ is robust. There are finitely many core allocations and hence finitely many possible values of each difference $W_i-V_i$. Choose $0<\varepsilon_i<1$ sufficiently small that, for every such difference,
$$
\lceil W_i-V_i+\varepsilon_i\rceil
=\lfloor W_i-V_i\rfloor+1.
$$
Such a choice is possible because only finitely many positive distances to the next integer occur. Set $\theta_i=V_i-\varepsilon_i$. The primary score of $C$ is $n$, while the primary score of $Y$ is
$$
n+\sum_i\lfloor W_i-V_i\rfloor=n-D.
$$
By robustness and Corollary 2.2, $D\geq0$. If $D=0$, all rounding slacks vanish and $\sum_iW_i=\sum_iV_i$. Therefore no $Y$ has a larger lexicographic score, proving the converse. $\square$

Adding an integer to any coordinate of $\theta$ subtracts a constant from every primary score. Thus phases can be considered modulo $1$. The theorem is an exact finite characterization, not a polynomial-time algorithm.

**Corollary 3.2 (a finite phase grid).** In the normalized bivalued model, suppose $r_i=P_i/Q_i>1$ is rational in lowest terms, and let $d_i^{\rm high}$ be agent $i$'s total number of high-valued core goods. The robust cores are precisely the union of the maximizers of (3.1) over the product of phase sets
$$
\Theta_i=\left\{\frac{P_i h\bmod Q_i}{Q_i}-\frac1{2Q_i}:
0\leq h\leq d_i^{\rm high}\right\}. \tag{3.2}
$$
After removing duplicates, $\Theta_i$ has at most $\min(d_i^{\rm high}+1,Q_i)$ elements.

*Proof.* Every core utility of agent $i$ is an integer plus $hP_i/Q_i$. All utility differences therefore lie in $Q_i^{-1}\mathbb Z$, so $\varepsilon_i=1/(2Q_i)$ is valid in the necessity proof of Theorem 3.1. The resulting $V_i-\varepsilon_i$, modulo integers, lies in (3.2). This proves that every robust core is selected somewhere on the grid. The sufficiency direction of Theorem 3.1 applies to every maximizer at every grid point. The cardinality bound follows from the $d_i^{\rm high}+1$ possible values of $h$ and the $Q_i$ possible residues. $\square$

**Corollary 3.3 (high-heldness).** In the bivalued model, if every core good is high-valued by at least one agent, every robust core assigns every good to a high-valuing agent.

*Proof.* By Theorem 3.1, a robust core maximizes (3.1) for some phase vector. Suppose a good is held at value $1$, and move it to an agent who values it at $r>1$. The old owner's primary score falls by exactly $1$. The recipient's primary score rises by at least $1$, because $\lceil x+r\rceil\geq\lceil x\rceil+1$. Total actual utility rises by $r-1>0$. Thus either the primary score rises, or it ties and the secondary score rises, contradicting lexicographic optimality. $\square$

## 4. Complete EFX allocations from robust cores

**Lemma 4.1 (cross-bundle bound).** If $C$ is robust and $i\ne j$, then
$$
v_i(C_j)\leq V_j\quad\text{when }V_j\in\mathbb Z,
\qquad
v_i(C_j)<\lceil V_j\rceil\quad\text{otherwise}.
\tag{4.1}
$$
In particular, $v_i(C_j)<\lfloor V_j\rfloor+1$.

*Proof.* Give agent $i$ exactly $c=\lceil V_j\rceil$ universal goods, and give the other agents no universal goods. Transfer the whole bundle $C_j$ to $i$, and transfer those $c$ goods from $i$ to $j$. The seller's change is $c-V_j\geq0$. The buyer's change is $v_i(C_j)-c$. If $V_j$ is integral and $v_i(C_j)>V_j$, this is a strict Pareto improvement. If $V_j$ is nonintegral and $v_i(C_j)\geq c$, it is again a strict improvement, this time already strict for $j$. Robustness excludes both cases. Empty bundles cause no exception because their value is zero. $\square$

**Theorem 4.2 (balanced EFX completion).** Let $C$ be robust. Set
$$
M=\max_i\lfloor V_i\rfloor,
\qquad K_0=nM-\sum_i\lfloor V_i\rfloor.
$$
For every integer $K\geq K_0$, the same core $C$ has a complete EFX and globally PO completion using exactly $K$ universal goods.

*Proof.* Initially give agent $i$ exactly $l_i=M-\lfloor V_i\rfloor\geq0$ universal goods. The resulting own utility is $M+\{V_i\}\geq M$. For a distinct observer $i$, Lemma 4.1 gives
$$
v_i(C_j)+l_j<\lfloor V_j\rfloor+1+M-\lfloor V_j\rfloor=M+1.
$$
Every good is worth at least $1$, so removing any good from a nonempty foreign bundle leaves value strictly below $M$. This proves EFX; self-comparisons are automatic, and an empty target bundle has no deletion constraint. Robustness proves PO. This allocation uses $K_0$ universal goods.

Suppose an EFX+PO completion retaining $C$ has already been constructed. Its strict-envy digraph is acyclic: a directed cycle would allow a rotation of the whole bundles that strictly improves every agent on the cycle and leaves all others unchanged, contradicting global PO. A finite acyclic digraph has a vertex with no incoming edge. Give one further universal good to such an unenvied agent $j$. For every other observer, deleting the new good leaves $j$'s old bundle; deleting any old good removes value at least $1$, and therefore also leaves value no greater than that old bundle. Since $j$ was unenvied, all EFX inequalities toward $j$ hold. All other observers' constraints are unchanged, and $j$'s own utility only increases. Robustness preserves PO. Iterating constructs every larger pool size. $\square$

This theorem gives a sufficient pool size, not an exact threshold. It does not imply that every EFX+PO allocation has a robust core.

**Remark 4.3 (eventual existence).** Robust cores always exist: choose a complete core maximizing $\sum_i v_i(C_i)$. For every fixed pool, all complete allocations have that same pool's contribution to total normalized utility, so no completion of the maximizing core admits a strict Pareto improvement. It is therefore robust. Theorem 4.2 implies that, for every fixed finite core instance, all sufficiently large universal pools admit EFX+PO allocations. This elementary observation is not claimed as a novel existence result; the finite-pool threshold and the unrestricted instances with smaller pools are the substantive issues.

## 5. Residual-capacity quotas for arbitrary ratios and degrees

Return to normalized personalized bivalued valuations. Let $E$ consist of all goods high-valued by at least one agent; put $G=|E|$. The other $K$ goods are universal. Let $d_i^{\rm high}=|\{g\in E:v_i(g)=r_i\}|$.

**Theorem 5.1 (modular residual-capacity theorem).** Fix $\alpha=A/k\geq1$, where $A,k$ are coprime positive integers, and suppose $r_i\geq\alpha$ and $r_i>1$ for every agent. Define
$$
s_i=\max\{s\in\{0,\ldots,d_i^{\rm high}\}:
\lfloor ur_i\rfloor=\lfloor u\alpha\rfloor
\text{ for every integer }1\leq u\leq s\}. \tag{5.1}
$$
Assume there is a complete high-held core whose counts $c_i=|C_i|$ satisfy
$$
c_i\equiv0\pmod k,
\qquad c_i\geq d_i^{\rm high}-s_i. \tag{5.2}
$$
Choose, among all such cores, one maximizing
$$
\sum_{i:r_i>\alpha}c_i. \tag{5.3}
$$
Then the chosen core is robust. Consequently it has a complete EFX+PO completion for every integer
$$
K\geq n\max_i\lfloor r_i c_i\rfloor-\sum_i\lfloor r_i c_i\rfloor. \tag{5.4}
$$
There is no upper bound on the $r_i$ or the $d_i^{\rm high}$ in this statement.

*Proof.* The selection is well-defined because the assumed feasible set is finite and nonempty. Fix an arbitrary nonnegative integer low vector $l$, with total $K$, and suppose a complete allocation $X$ weakly improves $C+l$. Let $h_i$ be the number of goods assigned to $i$ that it values at $r_i$, and let $z_i$ count all its other goods. Thus $z_i$ includes exceptional goods assigned to $i$ at value $1$. Put $H=\sum_i h_i\leq G$. Completeness and weak improvement imply
$$
\sum_i z_i=G+K-H,
\qquad z_i-l_i\geq\lceil r_i(c_i-h_i)\rceil.
$$
Therefore
$$
Q:=\sum_i[h_i+\lceil r_i(c_i-h_i)\rceil]\leq G. \tag{5.5}
$$

If $h_i\leq c_i$, then $r_i\geq\alpha$ gives
$$
\lceil r_i(c_i-h_i)\rceil\geq\lceil\alpha(c_i-h_i)\rceil.
$$
If $h_i>c_i$, put $u=h_i-c_i$. By (5.2),
$$
1\leq u\leq d_i^{\rm high}-c_i\leq s_i,
$$
so (5.1) gives
$$
\lceil r_i(c_i-h_i)\rceil
=-\lfloor ur_i\rfloor
=-\lfloor u\alpha\rfloor
=\lceil\alpha(c_i-h_i)\rceil.
$$
Since $k\mid c_i$, the number $\alpha c_i$ is integral. It follows that
$$
\begin{aligned}
Q&\geq\sum_i[h_i+\alpha c_i-\lfloor\alpha h_i\rfloor]\\
 &=G+(\alpha-1)(G-H)+\sum_i\{\alpha h_i\}\\
 &\geq G.
\end{aligned} \tag{5.6}
$$

First suppose $\alpha>1$. Equations (5.5)–(5.6) force $H=G$, $\{\alpha h_i\}=0$ for every $i$, and equality in each comparison of compensation terms. Coprimality gives $k\mid h_i$. If an agent with $r_i>\alpha$ lost high goods, then $c_i-h_i$ would be a positive multiple of $k$. Consequently $\alpha(c_i-h_i)$ would be an integer and
$$
\lceil r_i(c_i-h_i)\rceil
\geq\alpha(c_i-h_i)+1,
$$
contradicting equality. Thus $h_i\geq c_i$ for every $i$ with $r_i>\alpha$.

The equality $H=G$ means that every exceptional good is high-held in $X$. Its core therefore has modular counts and retains the lower quota for every agent above the reference ratio. An agent with $r_i=\alpha$ has $s_i=d_i^{\rm high}$, so its quota is zero. Hence the new core lies in exactly the same feasible set (5.2). Maximality in (5.3), together with $h_i\geq c_i$ above the reference ratio, implies $h_i=c_i$ for each such agent. The other agents all have ratio $\alpha$, and their aggregate high count is unchanged. Thus total normalized high utility is unchanged. Since $H=G$, all remaining goods are the $K$ universal goods, whose aggregate utility is also unchanged. A weak improvement with unchanged total utility cannot be strict.

Now suppose $\alpha=1$. Reduced form gives $A=k=1$, and every actual ratio satisfies $r_i>1$. Any positive loss $c_i-h_i$ costs
$$
\lceil r_i(c_i-h_i)\rceil>c_i-h_i.
$$
Every high-count gain, by (5.1), has compensation exactly $c_i-h_i$. A high-count loss by any agent would therefore make $Q>\sum_i[h_i+c_i-h_i]=G$, contradicting (5.5). No agent loses, while $\sum_i h_i\leq\sum_i c_i$, so $h_i=c_i$ for every agent. Again total utility is unchanged. This proves robustness for all allowed $\alpha$. Theorem 4.2 proves (5.4). $\square$

The closure of the feasible domain under the proposed improvement is essential. Without a degree restriction, replacing (5.2) by an artificial requirement that counts be only $0$ or $k$ would invalidate that closure step.

**Corollary 5.2 (a smaller pool under bounded degrees).** Under the hypotheses of Theorem 5.1, suppose also that $d_i^{\rm high}\leq2k-1$ for every agent. Put $p=G/k$ and $B=\lceil\alpha(k-1)\rceil$. Then complete EFX+PO allocations exist for every integer
$$
K\geq B(n-p). \tag{5.7}
$$

*Proof.* A feasible count is $0$ or $k$, so exactly $p$ agents are occupied. If $k=1$, every occupied core is a singleton; at pool zero every foreign one-good-deletion residual is zero. Robustness and the extension argument of Theorem 4.2 establish the assertion.

Suppose $k\geq2$. Give $B$ universal goods to every empty agent and none to occupied agents. An empty agent $i$ has $c_i=0$, so its quota forces $s_i=d_i^{\rm high}$. Consider its value for any occupied bundle after one deletion. That bundle has $k-1$ remaining goods. If $u$ of them are high to $i$, its residual value $R$ satisfies
$$
\lfloor R\rfloor
=\lfloor ur_i\rfloor+k-1-u
=\lfloor u\alpha\rfloor+k-1-u
\leq\lfloor\alpha(k-1)\rfloor.
$$
This also holds for $u=0$. Coprimality and $k\geq2$ imply $\alpha(k-1)\notin\mathbb Z$, so $R<B$. Hence the empty agent's own $B$ lows cover the residual. It also satisfies EFX toward other empty agents, whose residual value is $B-1$.

An occupied agent $i$ owns $k$ highs and has utility $kr_i$. Every occupied foreign bundle has deletion residual at most $(k-1)r_i<kr_i$. An empty agent's residual is $B-1$; moreover $kr_i\geq A$ and $B=\lceil A-\alpha\rceil\leq A-1$. Thus these comparisons hold as well. The allocation is EFX and, by robustness, PO. It uses $B(n-p)$ universal goods. The extension argument gives every larger pool. $\square$

**Corollary 5.3 (two useful specializations).**

1. Any high-held core satisfying
   $$
   (r_i-1)(d_i^{\rm high}-c_i)<1\quad\text{for every }i \tag{5.8}
   $$
   is robust. It admits the EFX completions of Theorem 4.2, without a modular condition or an optimization step.
2. If $r_i=\alpha+\varepsilon_i$, with $\varepsilon_i\geq0$, and $\varepsilon_i d_i^{\rm high}<1/k$ whenever $\varepsilon_i>0$, then $s_i=d_i^{\rm high}$. Thus any feasible modular high-held domain has a robust maximizer as in Theorem 5.1. If every $\varepsilon_i>0$, every modular high-held core is robust.

*Proof.* For the first assertion take $\alpha=1$. For a nonnegative integer $q=d_i^{\rm high}-c_i$, the inequalities $\lfloor ur_i\rfloor=u$ for $1\leq u\leq q$ hold exactly when $q(r_i-1)<1$; the case $q=0$ is vacuous. Hence (5.8) gives the quota condition. With $k=1$, modularity imposes no restriction, and the selected objective is always $G$.

For the second assertion, for every $1\leq u\leq d_i^{\rm high}$, the positive distance from $u\alpha$ to the next integer is at least $1/k$. The increase $u\varepsilon_i<1/k$ cannot cross that integer. Therefore all required floors agree. If every ratio is strictly above $\alpha$, the objective (5.3) is the constant $G$, so every feasible core is a maximizer. $\square$

These results allow arbitrary high degrees and arbitrary ratios through the residual-capacity conditions. They do not assert that the modular quota domain is nonempty for every instance, nor that the actual pool satisfies (5.4) or (5.7).

## 6. Sharp welfare control for robust cores

**Theorem 6.1.** If $n\geq2$, every robust core has normalized total utility less than $n-1$ below the maximum over complete core allocations. The constant $n-1$ is sharp even for personalized bivalued valuations. For $n=1$, the unique complete core allocation is a maximizer.

*Proof.* Let a competing core $Y$ have larger total utility by $\delta>0$. In Corollary 2.2 its compensation sum $D$ cannot be negative or zero, because at $D=0$ the sum of the rounding slacks would be $\delta>0$. Thus $D\geq1$. Since $\lceil x\rceil<x+1$ for every real $x$,
$$
1\leq D<\sum_i(V_i-W_i)+n=n-\delta.
$$
Therefore $\delta<n-1$.

To prove sharpness, take $n-1$ goods and one source agent that values all of them at $1+\varepsilon$. For each good there is one distinct sink, which values that good at $2-\varepsilon$ and all other goods at $1$. The source owns all goods in $C$. Choose
$$
0<\varepsilon<\min\{1/(n-1),1/2\}.
$$
Every different complete core allocation moves $t\geq1$ goods away from the source, costing it
$$
\lceil t(1+\varepsilon)\rceil=t+1
$$
units of integer compensation. A sink receiving $q$ goods has utility either $q$ or $q+1-\varepsilon$, according as it does not or does receive its own high good. Its integer release is consequently $q$ in both cases. The sinks receive a total of $t$ goods, so their total release is $t$. Thus $D=1>0$ for every changed assignment, and Corollary 2.2 proves robustness, including against low-held alternatives. Assigning each good to its own sink instead increases total utility by
$$
(n-1)(1-2\varepsilon).
$$
As $\varepsilon\downarrow0$, this approaches $n-1$. The $n=1$ assertion follows because there is only one complete core assignment. $\square$

## 7. Coupled finite-pool obstructions

**Theorem 7.1 (minimal funding vectors).** For a fixed core $C$, and each complete core $Y$ with $\sum_iW_i>\sum_iV_i$, define $P(Y),t_i(Y)$ as in Lemma 2.1 and form all integer vectors
$$
0\leq b_i\leq t_i(Y),\qquad \sum_i b_i=P(Y). \tag{7.1}
$$
Let $\mathcal A(C)$ be the set of componentwise-minimal elements of the union of these finite sets. Then
$$
C+l\text{ is PO}
\quad\Longleftrightarrow\quad
\text{there is no }b\in\mathcal A(C)\text{ with }b\leq l. \tag{7.2}
$$
Thus $\mathcal A(C)$ is exactly the finite antichain of minimal non-PO low vectors.

*Proof.* For any $Y$, the funding inequality in Lemma 2.1 holds exactly when there is an integer vector with $b_i\leq\min(l_i,t_i(Y))$ and total $P(Y)$. The forward direction follows by filling coordinates one at a time until that integer total is reached; the reverse follows by summing. Hence the non-PO set is the union of the componentwise upper closures of all vectors (7.1). Deleting duplicate vectors and vectors above another does not change that union. In a finite generating set, the retained minimal elements are exactly the minimal elements of the union of upper closures. This proves (7.2). $\square$

**Corollary 7.2 (one finite test for robustness).** Define
$$
T_i=\lfloor v_i(E)-V_i\rfloor\geq0.
$$
Then $C$ is robust if and only if $C+T$ is PO.

*Proof.* Every complete core has $W_i\leq v_i(E)$. Thus $t_i(Y)\leq T_i$, and every obstruction $b$ in (7.1) satisfies $b\leq T$. If any obstruction exists, Theorem 7.1 makes $C+T$ non-PO. If none exists, the same theorem makes every completion PO. $\square$

In particular, the PO low vectors form a componentwise downward-closed set. The antichain describes the coupling of all funding requirements exactly.

**Theorem 7.3 (an EFX pool bound for a nonrobust core).** For $i\ne j$, put
$$
\Delta_{ij}=\lceil v_i(C_j)-V_i-1\rceil.
$$
For a nonzero obstruction vector $b\in\mathcal A(C)$, define
$$
Q(b)=\max_{i:b_i>0}\left[b_i-1+
\sum_{j\ne i}\max\{0,b_i-1-\Delta_{ij}\}\right]. \tag{7.3}
$$
If $\mathcal A(C)\ne\varnothing$ and $0\notin\mathcal A(C)$, every complete EFX+PO completion of $C$ has pool size
$$
K\leq\min_{b\in\mathcal A(C)}Q(b). \tag{7.4}
$$
If $0\in\mathcal A(C)$, there is no PO completion.

*Proof.* Suppose $C+l$ is EFX and PO. Fix $b\in\mathcal A(C)$. By (7.2), some coordinate $i$ has $l_i<b_i$. Since the coordinates are nonnegative integers, $b_i>0$ and $l_i\leq b_i-1$. For $j\ne i$ with $l_j>0$, deleting a universal good from $j$'s bundle gives the EFX inequality
$$
V_i+l_i\geq v_i(C_j)+l_j-1,
\quad\text{hence}\quad
l_i\geq l_j+\Delta_{ij}.
$$
Consequently $l_j\leq b_i-1-\Delta_{ij}$ whenever $l_j>0$, and in all cases
$$
l_j\leq\max\{0,b_i-1-\Delta_{ij}\}.
$$
Summing, and then allowing any possible deficient coordinate $i$, yields $K\leq Q(b)$. This holds for every obstruction $b$, proving (7.4). If $0$ is an obstruction, (7.2) excludes every nonnegative low vector. $\square$

The bound (7.4) is not asserted to be an exact threshold. It bounds completions of one fixed core and does not establish that a different core becomes feasible before that bound is reached.

**Example 7.4 (why finite funding matters).** Take two agents of ratios $2,3$, and three goods high to both. Give one core good to agent 1 and two to agent 2, so $V=(2,6)$. A core is determined by how many of the three goods agent 1 receives. The only count vector with larger total normalized utility than $V$ is $(0,3)$, with $W=(0,9)$. It has $P=2$, $t=(0,3)$, so $\mathcal A(C)=\{(0,2)\}$. Thus $C+(x,y)$ is PO exactly when $y\leq1$.

If $y=0$, agent 1's EFX comparison toward agent 2 is automatic; if $y>0$, deleting one of agent 2's lows gives $x\geq y+1$, which is the strongest deletion constraint. Similarly, if $x=0$, agent 2's comparison is automatic; if $x>0$, its strongest constraint is $x\leq y+4$. With $y=0$, exactly $x=0,1,2,3,4$ work. With $y=1$, exactly $x=2,3,4,5$ work. The EFX+PO pool sizes are therefore exactly $0,1,\ldots,6$. Formula (7.3) also gives $Q((0,2))=6$.

All core utilities in this instance are integral, so Corollary 2.2 says a robust core must maximize normalized total utility. The unique robust count vector gives all three goods to agent 2. Its minimum EFX pool is four: if agent 2 has no lows, agent 1 needs four lows; if agent 2 has $y>0$ lows, agent 1 needs at least $y+5$. Four lows suffice, and Theorem 4.2's extension argument gives every larger pool. Thus a robust core cannot furnish the pool-zero allocation, even though a complete EFX+PO allocation exists there. This is a limitation of robust-core selection, not a nonexistence example.



## 8. An exact obstruction to maximizing Nash welfare within EFX

The result in this section concerns a selection rule, not the existence of an allocation satisfying EFX and Pareto optimality simultaneously. In fact, the family below has an explicitly identified EFX and globally Pareto-optimal allocation.

**Theorem N (EFX-constrained Nash maximizers can all be dominated).** For every real number
$$
\frac{26}{9}<t<3,
$$
there is a positive personalized bivalued instance with three agents and twelve goods such that:

1. The largest Nash product among complete EFX allocations is $128(t+1)$, and every allocation attaining it has utility vector $(8,8,2t+2)$.
2. Every such maximizer is globally Pareto dominated by the same complete integral allocation, with utility vector $(8,8,t+5)$.
3. The largest Nash product among complete allocations that are both EFX and globally Pareto optimal is $56(t+6)$. An allocation with utility vector $(7,8,t+6)$ attains this value.

Consequently the ratio of the two constrained optimal Nash products is
$$
\frac{16(t+1)}{7(t+6)},
$$
which tends to $64/63$ as $t$ tends to $3$ from below. If Nash welfare is defined as the geometric mean, the corresponding ratio is the cube root of this expression. This family supplies a lower-bound example for the cost of imposing Pareto optimality within EFX; it does not supply a universal upper bound.

**Construction and notation.** Let the agents be $A,B,C$, with respective high values $3,4,t$ and common low value $1$. There are exceptional goods $u,v,w,b,c$ and seven additional goods, each worth $1$ to all three agents. The valuations of the exceptional goods are

| Agent | $u$ | $v$ | $w$ | $b$ | $c$ |
|---|---:|---:|---:|---:|---:|
| $A$ | $3$ | $3$ | $1$ | $1$ | $1$ |
| $B$ | $4$ | $4$ | $4$ | $4$ | $1$ |
| $C$ | $t$ | $t$ | $t$ | $1$ | $t$ |

All allocations in the proof assign every good exactly once. Write $U_i$ for the utility of agent $i$, and write $\Pi=U_AU_BU_C$ for the Nash product. Call an allocation *proper* if every exceptional good is held by an agent who values it high. This is an auxiliary definition; prospective Pareto improvements will not be restricted to proper allocations.

We shall use the elementary function
$$
F_S(x)=\frac{x(S-x)^2}{4}\qquad(0\le x\le S).
$$
If three nonnegative utilities sum to at most $S$ and one is $x$, the arithmetic–geometric mean inequality bounds their product by $F_S(x)$. Its derivative is
$$
F'_S(x)=\frac{(S-x)(S-3x)}4.
$$
Thus $F_S$ increases on $[0,S/3]$ and decreases on $[S/3,S]$. This observation justifies the one-coordinate bounds used below.

**Proof of the EFX optimum.** Begin with the complete allocation
$$
X_A=\{u\}+5\text{ lows},\qquad
X_B=\{w,b\},\qquad
X_C=\{v,c\}+2\text{ lows}.
$$
Its utility vector is $(8,8,2t+2)$. The following table gives, in each row, the largest value that the row agent assigns to the column agent's bundle after deleting one of its goods:

| Observer | Target $A$ | Target $B$ | Target $C$ |
|---|---:|---:|---:|
| $A$ | — | $1$ | $5$ |
| $B$ | $8$ | — | $6$ |
| $C$ | $t+4$ | $t$ | — |

Each entry is at most the observer's own utility: in the only parameter-dependent comparison, $t+4\le2t+2$ follows from $t>2$. Therefore $X$ is EFX and attains
$$
N(t):=128(t+1).
\tag{N1}
$$

We next bound every other allocation, including ones in which exceptional goods are held at low value. Let $h_i$ be agent $i$'s actual number of high-valued goods and put $H=h_A+h_B+h_C$. Since there are only five exceptional goods, $H\le5$, and completeness gives
$$
U_A+U_B+U_C=12+2h_A+3h_B+(t-1)h_C.
\tag{N2}
$$
If an exceptional good is held at low value, then $H\le4$. Since $t-1<2$, if also $h_B\le2$, the sum in (N2) is at most $12+2H+h_B\le22$. Hence
$$
\Pi\le(22/3)^3.
$$
If instead $h_B\ge3$, (N2) is at most $24$, while $U_B\ge12$. The monotonicity of $F_{24}$ on $[12,24]$ gives
$$
\Pi\le F_{24}(12)=432.
$$
Both bounds are less than $4480/9$, whereas $N(t)>4480/9$ throughout the stipulated interval. Thus no nonproper allocation can maximize the Nash product over EFX allocations.

In a proper allocation, $b$ belongs to $B$ and $c$ belongs to $C$. Agent $A$ can hold zero, one or two goods from $\{u,v\}$. If it holds two, the remaining shared good $w$ goes to $B$ or $C$. If it holds one, the remaining two shared goods go independently to $B$ or $C$. If it holds none, all three shared goods go to $B$ or $C$. The possible high-count vectors are consequently exactly
$$
(2,1,2),(2,2,1),(1,1,3),(1,2,2),(1,3,1),
(0,1,4),(0,2,3),(0,3,2),(0,4,1).
\tag{N3}
$$
Each listed vector is realizable. In a proper allocation the only low-valued goods held by their owners are the seven universal lows.

The following table records upper bounds on $\Pi$ for all nine patterns. The EFX hypothesis is used only in the row explicitly marked.

| High-count vector | Upper bound on $\Pi$ |
|---|---:|
| $(2,1,2)$, $(1,1,3)$ | $(23/3)^3$ |
| $(0,1,4)$ | $121t$ |
| $(0,2,3)$ | $(t+5)^3$ |
| $(0,3,2)$ | $3(7+2t)^2$ |
| $(0,4,1)$ | $400$ |
| $(1,3,1)$ | $72(t+4)$ |
| $(2,2,1)$ | $56(t+6)$, for EFX allocations |
| $(1,2,2)$ | $128(t+1)$ |

Here are complete derivations, including the strict comparisons needed to characterize all maximizers.

For $(2,1,2)$ and $(1,1,3)$, the total utilities are $17+2t$ and $14+3t$, respectively, both less than $23$. Their products are therefore less than $(23/3)^3<4480/9<N(t)$.

For $(0,1,4)$, total utility is $11+4t$ and $U_C\ge4t>(11+4t)/3$. Thus
$$
\Pi\le F_{11+4t}(4t)=121t<363<N(t).
$$
For $(0,2,3)$, total utility is $15+3t$, giving $\Pi\le(t+5)^3$, and
$$
N(t)-(t+5)^3=(3-t)(t^2+18t+1)>0.
\tag{N4}
$$
For $(0,3,2)$, total utility is $19+2t$ and $U_B\ge12>(19+2t)/3$, giving $\Pi\le3(7+2t)^2$. Its difference from $N(t)$ is
$$
-12t^2+44t-19.
$$
This is a concave quadratic, so its minimum on the closed interval $[26/9,3]$ is attained at an endpoint. The endpoint values are $215/27$ and $5$, both positive. Hence this row also has product strictly less than $N(t)$. For $(0,4,1)$, total utility is $23+t<26$ and $U_B\ge16$, yielding $\Pi< F_{26}(16)=400<N(t)$.

For $(1,3,1)$, first suppose $B$ receives no universal low. If $A$ receives $x\in\{0,\ldots,7\}$ lows, then
$$
\Pi=12(3+x)(t+7-x).
$$
The last two factors form a strictly concave quadratic in $x$. Its continuous maximizer is $(t+4)/2\in(31/9,7/2)$, and its unique integer maximizer is $x=3$: the difference of its values at $4$ and $3$ is $t-3<0$, and strict concavity excludes every more distant integer. The resulting product is $72(t+4)$. If $B$ receives a low, then $U_B\ge13$, while total utility is $22+t<25$. Hence $\Pi<F_{25}(13)=468<72(t+4)$. Finally,
$$
N(t)-72(t+4)=56t-160>0,
\tag{N5}
$$
since $t>26/9>20/7$.

For $(2,2,1)$, the core allocation is necessarily $A:\{u,v\}$, $B:\{w,b\}$, $C:\{c\}$. Denote the low counts by $(x,y,7-x-y)$. If $x\ge1$, EFX for $B$ toward $A$, deleting a low from $A$'s bundle, requires
$$
8+y\ge8+x-1,
\quad\text{so}\quad y\ge x-1.
\tag{N6}
$$
For $x=0$ this inequality is automatic. Combining $y\ge\max(0,x-1)$ with $x+y\le7$ yields $x\le4$. For fixed $x$, the product is
$$
(6+x)(8+y)(t+7-x-y).
$$
The quadratic in $y$ has its continuous maximum at $(t-1-x)/2$. When $x=0$, its unique integer maximum occurs at $y=1$: the successive differences from $y=0$ to $1$ and from $1$ to $2$ are $t-2>0$ and $t-4<0$. When $x=1$, its unique integer maximum occurs at $y=0$, since the difference at $1$ minus that at $0$ is $t-3<0$ and the quadratic thereafter decreases. When $x\ge2$, the continuous maximizer is negative and the allowed minimum $y=x-1$ is optimal. The resulting five bounds, for $x=0,1,2,3,4$, are respectively
$$
54(t+6),\quad56(t+6),\quad72(t+4),\quad90(t+2),\quad110t.
\tag{N7}
$$
The second is strictly greater than each of the other four on the interval: their differences from it are $2(t+6)$, $48-16t$, $156-34t$, and $336-54t$, all positive. Therefore every EFX allocation in this pattern has product at most $56(t+6)$, and
$$
N(t)-56(t+6)=72t-208>0.
\tag{N8}
$$

It remains to consider $(1,2,2)$. If $B$ receives no low, writing $x$ for $A$'s low count gives
$$
\Pi=8(3+x)(2t+7-x).
$$
The quadratic has continuous maximizer $t+2\in(44/9,5)$ and unique integer maximizer $x=5$. Indeed, its successive differences from $x=4$ to $5$ and from $5$ to $6$ are $2t-5>0$ and $2t-7<0$. Thus equality with $N(t)$ requires the low vector $(5,0,2)$, and then the utilities are $(8,8,2t+2)$. If $B$ receives a low, $U_B\ge9$, while total utility is $18+2t<24$; hence
$$
\Pi\le F_{18+2t}(9)=\frac94(9+2t)^2.
$$
The difference of $N(t)$ and this bound is the concave quadratic
$$
-9t^2+47t-\frac{217}{4}.
$$
Its endpoint values at $26/9$ and $3$ are $77/12$ and $23/4$, both positive. This last case is therefore strictly below $N(t)$.

We have exhausted all complete allocations. Since $X$ attains (N1), the EFX-constrained optimum is exactly $N(t)$, and every maximizer has the stated high counts, low counts and utility vector.

**Proof of global domination of every maximizer.** The single complete allocation
$$
Y_A=\{u,v\}+2\text{ lows},\qquad
Y_B=\{w,b\},\qquad
Y_C=\{c\}+5\text{ lows}
$$
has utility vector $(8,8,t+5)$. It preserves the utilities of $A$ and $B$ at every EFX Nash maximizer, and changes $C$'s utility by $3-t>0$. It therefore strictly Pareto dominates every such maximizer, regardless of the particular assignment that produced its utility vector. The allocation $Y$ is not EFX: after deleting a low from $Y_A$, agent $B$ values the remaining goods at $9>8=U_B(Y)$. This causes no problem for the dominance argument because global Pareto comparisons include all complete integral allocations.

**Proof of the explicit EFX and Pareto-optimal alternative.** Consider
$$
Z_A=\{u,v\}+1\text{ low},\qquad
Z_B=\{w,b\},\qquad
Z_C=\{c\}+6\text{ lows}.
\tag{N9}
$$
Its utility vector is $(7,8,t+6)$. The maximal one-good deletion values are

| Observer | Target $A$ | Target $B$ | Target $C$ |
|---|---:|---:|---:|
| $A$ | — | $1$ | $6$ |
| $B$ | $8$ | — | $6$ |
| $C$ | $2t$ | $t$ | — |

Every entry is bounded by the observer's own utility, using $2t<t+6$. Thus $Z$ is EFX.

To prove global integral Pareto optimality, consider any complete allocation weakly improving every agent over $Z$. If agent $i$ receives $h$ actual high goods, its total number of goods is at least
$$
f_i(h)=h+\max\{0,\lceil U_i(Z)-r_i h\rceil\}.
\tag{N10}
$$
This follows because each other good is worth exactly $1$ to that agent. Such other goods may include exceptional goods assigned at low value. Throughout $26/9<t<3$, the functions in (N10) are

| $h$ | $0$ | $1$ | $2$ | $3$ | $4$ |
|---|---:|---:|---:|---:|---:|
| $f_A(h)$ | $7$ | $5$ | $3$ | infeasible | infeasible |
| $f_B(h)$ | $8$ | $5$ | $2$ | $3$ | $4$ |
| $f_C(h)$ | $9$ | $7$ | $6$ | $4$ | $4$ |

For example, $\lceil t+6\rceil=9$, $\lceil6-t\rceil=4$, $\lceil6-2t\rceil=1$, and $6-3t<0$, proving the parameter-dependent row. The actual high counts necessarily satisfy
$$
0\le h_A\le2,\quad0\le h_B,h_C\le4,\quad h_A+h_B+h_C\le5.
\tag{N11}
$$
We minimize the total goods requirement on this relaxed domain, which contains every feasible assignment of high goods. The complete finite calculation is

| Fixed $h_B$ | Minimum of $f_A(h_A)+f_C(h_C)$ under $h_A+h_C\le5-h_B$ | Minimizing $(h_A,h_C)$ | Minimum total including $f_B(h_B)$ |
|---:|---:|---|---:|
| $0$ | $7$ | $(2,3)$ | $15$ |
| $1$ | $9$ | $(1,3),(2,2)$ | $14$ |
| $2$ | $10$ | $(2,1)$ | $12$ |
| $3$ | $12$ | $(1,1),(2,0)$ | $15$ |
| $4$ | $14$ | $(0,1),(1,0)$ | $18$ |

Since the instance has exactly twelve goods, a weak improvement must attain the unique total of twelve. Hence its high-count vector is $(2,2,1)$, and equality in (N10) forces its low-count vector to be $(1,0,6)$. Its utility vector is exactly that of $Z$. No weak improvement can therefore be strict for any agent, proving that $Z$ is globally integral Pareto optimal. Neither EFX nor properness was assumed of its prospective dominator.

**Proof of the exact EFX-plus-PO optimum.** It remains to show that no EFX and globally PO allocation has product greater than $56(t+6)$. Nonproper allocations have already been bounded by $(22/3)^3$ or $432$, both smaller than
$$
56(t+6)>56\left(\frac{26}{9}+6\right)=\frac{4480}{9}.
\tag{N12}
$$

For the three proper patterns
$$
(1,2,2),\qquad(0,2,3),\qquad(0,3,2),
\tag{N13}
$$
global Pareto optimality forces $A$'s low count to be at most two. To see this, suppose it is at least three. Replace the proper high-count vector $(h_A,h_B,h_C)$ by $(h_A+1,h_B,h_C-1)$ and move three universal lows from $A$ to $C$. The resulting high-count vectors are respectively $(2,2,1)$, $(1,2,2)$, and $(1,3,1)$, all realizable by (N3). This is a complete feasible allocation, obtained by freely reassigning the exceptional goods to realize the indicated vector and retaining the specified low counts. Agent $A$ gains utility $3$ and loses utility $3$; agent $B$'s utility is unchanged; agent $C$ gains $3-t>0$. This is a strict Pareto improvement, proving the restriction.

In pattern $(1,2,2)$, the restriction gives $U_A\le5$, while total utility is less than $24$. Since $F_{24}$ is increasing on $[0,5]$, the Nash product is less than
$$
F_{24}(5)=\frac{1805}{4}<\frac{4480}{9}.
$$
For $(0,2,3)$, it gives $U_A\le2$ and total utility less than $24$, hence product less than $F_{24}(2)=242$. For $(0,3,2)$, it gives $U_A\le2$ and total utility less than $25$, hence product less than $F_{25}(2)=529/2$. All are below (N12).

The six remaining proper patterns are covered by the earlier bounds. For $(2,1,2)$ and $(1,1,3)$, the bound $(23/3)^3$ is less than $4480/9$. For $(0,1,4)$ and $(0,4,1)$, the respective bounds are less than $363$ and at most $400$. For $(1,3,1)$,
$$
56(t+6)-72(t+4)=48-16t>0.
$$
Finally, the EFX bound for $(2,2,1)$ is exactly $56(t+6)$. Allocation $Z$ attains this value and has already been proved EFX and globally PO. This proves the exact joint optimum. Dividing (N1) by this optimum gives the ratio claimed in Theorem N, and its limit follows by direct substitution. $\square$



## 9. Exact finite evidence and its coverage

The following computations supplement the proofs; they are not premises of the analytic theorems. At $t=29/10$, a direct labelled enumeration examines all $3^{12}=531441$ complete allocations of the Section 8 instance. It finds 14358 EFX allocations, 84 EFX-constrained Nash maximizers (all dominated), and 12 EFX+PO utility vectors. A separate implementation enumerates all 5832 classes obtained by identifying universally identical goods and reaches the same utility-level conclusions. A third implementation checks five other rational parameters. The open real interval in Theorem N is established by its analytic proof, not extrapolated from these samples.

**Proposition 9.1 (comparison cells).** Fix the high/low incidence pattern. Let $H_i$ and $L_i$ denote the numbers of goods high and low to agent $i$. Cut the half-line $r_i>1$ at every rational $p/q>1$ with integers $1\le p\le L_i$ and $1\le q\le H_i$. Include each cut as a singleton, every intervening open interval and the final unbounded interval. For any fixed complete allocation, both EFX and global integral PO are constant throughout each product of these row cells.

*Proof.* The difference between the values of any two bundles to agent $i$ is $qr_i-p$, with integer coefficients satisfying $|q|\le H_i$ and $|p|\le L_i$. If $q=0$ the sign is constant. Otherwise every zero greater than one is among the displayed cuts (reverse both signs if necessary). Thus all bundle comparisons, including ties, are constant within each row cell. EFX consists of such comparisons between an own bundle and a one-good-deleted foreign bundle. Pareto domination by any other complete allocation also consists of such comparisons, with at least one strict. There are finitely many complete allocations, so the existence or absence of any dominator is constant in each product cell. If $H_i=0$ or $L_i=0$, no cut is needed. This proves the proposition. $\square$

The retained certificates establish precisely these additional positive facts:

| Family | Exhaustive or sampled coverage | Outcome |
|---|---|---|
| The twelve-good incidence pattern of Section 8, with all three ratios arbitrary in $(1,\infty)$ | 29403 product cells, including all boundaries; 55 ownership witnesses | An EFX+PO allocation in every cell |
| Add one agent and one exceptional good; retain old ratios $(3,4,29/10)$; the new agent may value any subset of the old five exceptional goods high, and the new good is high to it and any subset of the old agents | All $32\cdot8=256$ labelled incidences and every new ratio greater than one; 9344 cells | An EFX+PO allocation throughout |
| Add two agents and two exceptional goods | 500 retained sampled five-agent, fourteen-good profiles | An EFX+PO witness in each sample |

The comparison-cell verifier reconstructs all cuts and uses distinct interior representatives from the generator. It checks EFX literally and compares witnesses with all $3^5$ exceptional-owner maps and all 36 distributions of seven identical lows, including low-held exceptional goods. The one- and two-guard verifiers enumerate all $4^6$ or $5^7$ exceptional-owner maps. For a fixed map, they compute each agent's minimum nonnegative integer low requirement to weakly attain the witness utility. A strict dominator exists exactly when these requirements sum to less than the seven available lows, or sum to seven with an already strict utility increase. This is the finite-pool completeness argument of Lemma 2.1 applied to every actual core assignment.

Nash-product rankings need not be constant inside comparison cells. For example, the products $128(t+1)$ and $56(t+6)$ cross at $t=26/9$ within the same cell $(8/3,3)$. Proposition 9.1 therefore does not certify a Nash maximizer throughout a cell.

The source programs, certificates, retained exact outputs and earlier proof inputs are stored byte-for-byte in [evidence.zip](evidence.zip). The [reproduction driver](reproduce.py) extracts them into a fresh project-local working directory and runs nine checks without changing the archive. Exact output comparisons ignore only execution-time fields. The [final check record](ASSISTANCE_AND_CHECKS.md) identifies the tested version and limitations.

## 10. What remains unresolved

Theorem 5.1 extends the previous local maximal-sink argument by allowing a rational reference ratio and quotas on unheld high goods. For $\alpha=R-1/k$ with integer $R\ge2$, agents with ratio $\alpha$ have zero quota, and agents of degree at most $k$ with ratio in $(\alpha,R)$ have every possible gain safe. Modular counts at those latter agents are zero or $k$, so maximizing their total high count is equivalent to maximizing the number of occupied sinks. The earlier theorem is recovered when its feasibility construction supplies a modular core.

The present results leave two substantive issues: the quota domain may be empty, and the actual finite pool may be smaller than the sufficient EFX completion bound. A finite-pool PO allocation can use a nonrobust core because a beneficial exchange is unaffordable, as Example 7.4 proves. Neither the fixed-core obstruction cutoff nor the existence of robust cores shows that some EFX+PO core is available at every intermediate pool size. Global monotonicity under addition of a universal good is also not proved here.

Accordingly the unrestricted claim remains open within this work: for every finite incidence pattern, every positive personalized ratio profile and every finite number of universal goods, does a complete EFX and globally integral PO allocation exist? Theorem N excludes one selection rule, not every EFX allocation of an instance. No claim of established novelty, formal machine certification, or independent human verification is made.

## References and attribution

[1] Jiarong Jin and Biaoshuai Tao. *On Pareto-Optimal and Fair Allocations with Personalized Bi-Valued Utilities*. arXiv:2507.18251v2, 17 October 2025. Relevant passage: Section 5; model and Pareto characterization: Sections 2–3. [Versioned text](https://arxiv.org/html/2507.18251v2).

[2] Zehan Lin, Xiaowei Wu and Shengwei Zhou. *When Maximum Nash Welfare Becomes Strongly Fair: Bi-valued Goods*. arXiv:2610.00122v1. Relevant passages: Theorem 3.5, Example 3.6 and Section 6. [Versioned text](https://arxiv.org/html/2610.00122v1). The HTML header reports 9 September 2026 while the manuscript title page says December 2025; that date discrepancy is retained rather than resolved by inference.

The proofs in Sections 2–8 consolidate the dated local v8 mathematical arguments, themselves extending the earlier v4–v7 integer-compensation and maximal-sink work. The original theory, structure, search and parent-agent roles, exact source digests, current drafting and adversarial-review roles, and the newly recovered model configuration evidence are recorded once in [ASSISTANCE_AND_CHECKS.md](ASSISTANCE_AND_CHECKS.md). The earlier proof texts and independent checkers are preserved in the evidence archive. These arguments are not attributed to [1] or [2]; those papers supply the problem and relevant background. The analytic statements remain candidate partial results pending scientific review.

Original manuscript text and data follow the project's CC BY 4.0 terms; contributed code follows MIT. References retain their own terms. See the repository [license](../../LICENSE.md).
