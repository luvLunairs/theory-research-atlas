# Largest neutral death–birth diversity time on undirected graphs

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

**Q-MODEL-304 · Candidate outline.**

[Suggest a correction](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=correction.yml&title=%5BCorrection%5D+Q-MODEL-304%3A+Largest+neutral+death%E2%80%93birth+diversity+time+on+undirected+graphs&target=Q-MODEL-304) · [Share progress](https://github.com/luvLunairs/theory-research-atlas/issues/new?template=research-progress.yml&title=%5BResearch%5D+Q-MODEL-304%3A+Largest+neutral+death%E2%80%93birth+diversity+time+on+undirected+graphs&target=Q-MODEL-304)

Determine the asymptotic order of max_G E[T] over connected simple undirected N-vertex graphs, initially N distinct types, for neutral death–birth updating without mutation: select a vertex uniformly for replacement, then a neighbor uniformly to supply its type. T counts all updates until consensus.

**Origin:** Literature-origin question. **Curator-designed scope:** No.

**Current status:** Unverified. **Last checked:** 2026-11-26.

**Status basis:** Brewster et al. report a gap from Omega(N^4) to O(N^5 log N). Oliveira bounds continuous-time voter consensus by the maximum hitting time, and Feige bounds the walk's cover time by O(N^3) steps. Together these point to a matching upper bound after conversion to single-update time. That comparison awaits review.

**Statement check:** Source located. **Status check:** Later literature checked.

**Source date and freshness:** Feige, 1995; Oliveira manuscript, September 2010; Brewster et al., 2025.

**Scope limits:** Oliveira uses independent rate-one receiver clocks and uniform neighbours, with arbitrary initial opinions. The atlas counts individual updates, including those that preserve a label.

**Information still needed**

- Reconcile the per-vertex clock and the all-event count with the worst-case hitting-time bound, then compare with the published barbell lower bound.

**Primary branch:** [Evolution, population genetics and phylogenetics](../domains/bio.md#bio-evol). **Related branches:** [Dynamics on networks and collective behavior](../domains/net.md#net-dynamics), [Discrete probability and random structures](../domains/prob.md#prob-discrete).

**Sources:** [Maintaining diversity in structured populations](../sources.md#src-model-301); [Maintaining diversity in structured populations](../sources.md#src-model-800); [On the coalescence time of reversible random walks](../sources.md#src-model-902); [A tight upper bound on the cover time for random walks on graphs](../sources.md#src-model-907).

**Exact locator:** Brewster et al., Table 1, Discussion and Supplementary Section 8.1; Oliveira, Section 1.1, Corollary 1.1. Feige, cover-time bound.

**Potential difficulty:** High. The finite Markov chain is explicit, but a statement for every population size needs structure beyond finite enumeration.

**Possible AI role:** Check the time normalization and the hitting-time hypotheses before treating this as a new extremal problem.

**Verification burden:** High. Check the update order, null updates, initial partition and the recurrence proof; simulations do not establish an asymptotic theorem.

**Resource expectations:** Experiment: none for the stated mathematical model. Data: public definitions and any generated certificates. Computation: small examples may fit ordinary hardware; the general proof has no defensible runtime or cost estimate. Mathematical validity would not establish empirical adequacy.

**Assessment:** 2026-11-26; untested forecast. **Uncertainty:** No independent theorem transfer or exact finite-size extremizer has been certified.

**Further work:** resolve the statement and status questions above before planning an attempt. **Human review:** Pending.

## Literature checks

These are editorial evidence checks, not signed expert reviews or independent proof verification.

### 2026-11-26

**Coverage:** Statement and later literature. **Statement:** Matched.

**Recorded status:** Source reports open → Unverified.

Brewster et al. report a gap from Omega(N^4) to O(N^5 log N). Oliveira bounds continuous-time voter consensus by the maximum hitting time, and Feige bounds the walk's cover time by O(N^3) steps. Together these point to a matching upper bound after conversion to single-update time. That comparison awaits review.

**Search scope:** Compared the historical gap with a voter-model theorem whose update rule matches the receiver-first model; distinguished synchronous and per-vertex clocks.

**Inspected evidence**

- [Maintaining diversity in structured populations](../sources.md#src-model-800) — Table 1, Barbells and Discussion. Reports the published extremal gap for receiver-first updating.
- [On the coalescence time of reversible random walks](../sources.md#src-model-902) — Section 1.1 and Corollary 1.1. The receiving vertex chooses a uniform neighbour at rate one; the theorem bounds expected consensus time in that clock.
- [A tight upper bound on the cover time for random walks on graphs](../sources.md#src-model-907) — Abstract, main result. Bounds the expected time to visit every vertex by order N^3 in single-walker steps.

**Limits and remaining work**

- No independent theorem transfer or exact finite-size extremizer has been certified.

<details>
<summary>Search queries</summary>

- consensus time voter model coalescence time maximum graph tight O(n^3) worst-case barbell simple graph continuous time random walks Oliveira hitting time
- Aldous Fill random walk every connected graph 4/27 n^3 hitting time commute time bound graph unweighted explicit cubic Hitting time simple graph O(n^3) Feige 1995


</details>

<details>
<summary>Structured records</summary>

[Candidate data](../../data/candidates.json) · [Check records](../../data/candidate-checks.json)

</details>

[Back to the index](../candidates.md)
