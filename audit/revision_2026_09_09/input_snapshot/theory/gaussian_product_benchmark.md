# A calibration benchmark for the cubic boundary experiment

This is a separate decision problem for improving constants. It is not yet an optimized finite-sample tensor-regression procedure. Statements labeled **PROVED** have complete internal derivations below. Their ingredients are classical testing and Gaussian geometry; these calculations alone do not establish a new inferential principle.

## Experiment and objective

Observe Z∼N_3(h,I_3), h∈R³, and infer g_κ(h)=h_1h_2h_3+κh_1, where κ is known. This is the candidate local experiment for the current normal/tangent loading transition: if t_n=σ/√n and ε_n=κt_n²/λ², then a local product path with block angles t_n h_j/λ has target, divided by s_n=t_n³/λ², tending to g_κ(h). Establishing uniform transfer of an optimized procedure back to regression is additional work, especially with estimated anchors, scale and amplitude.

Define

\[
 \ell^*_{\alpha,\kappa}(0)=\inf_I E_0|I|,
 \quad\text{subject to}\quad
 \inf_{h\in\mathbb R^3}P_h\{g_\kappa(h)\in I(Z)\}\ge1-\alpha.
\]

Intervals are measurable and may be data dependent. The objective evaluates length at h=0 but imposes honesty over all h. Coverage at h=0 alone would make the problem trivial.

## An integrated testing lower bound: PROVED

Put d_κ(θ)=inf{||h||:g_κ(h)=θ} and z=Φ^{-1}(1−α). The level set is nonempty and closed, and a distance minimizer exists by coercivity of the norm. For any honest interval and any h on that level set, its acceptance event E_θ={θ∈I(Z)} has P_h(E_θ)≥1−α. The Neyman–Pearson lemma implies

\[
 P_0(E_\theta)\ge\Phi\{z-\|h\|\}.
\]

Indeed, the event minimizing P_0 at fixed P_h is an upper half-space in h^TZ/||h||; under P_h this variable has mean ||h|| and variance one, so its threshold is ||h||−z and its P_0 probability is Φ(z−||h||). The h=0 case follows directly from coverage. Taking the nearest h and integrating θ using Tonelli's theorem gives

\[
 \ell^*_{\alpha,\kappa}(0)\ge
 \int_{\mathbb R}\Phi\{z-d_\kappa(\theta)\}\,d\theta. \tag{C1}
\]

For κ=0, arithmetic–geometric mean gives d_0(θ)=√3|θ|^{1/3}, attained by three equal absolute coordinates with the appropriate product sign. Consequently,

\[
 \ell^*_{\alpha,0}(0)\ge
 \frac{2}{3\sqrt3}\,E[(z-G)_+^3]
 =\frac{2}{3\sqrt3}\{(z^3+3z)\Phi(z)+(z^2+2)\phi(z)\},
 \quad G\sim N(0,1). \tag{C2}
\]

To verify the integral, substitute x=√3θ^{1/3} on θ>0 and interchange integration with the probability Φ(z−x)=P(G≤z−x). Integrating x² over [0,(z−G)_+] yields the first expression. Expanding (z−G)³ and integrating the Gaussian density on (−∞,z] gives the second expression.

At α=.05, (C2) equals **3.6183903491**. This is a lower bound, not the optimum. Separate optimal acceptance events need not form a jointly optimal family of confidence intervals.

## A rigorous upper bracket: PROVED

Let r²=χ²_{3,1−α}, and project the Euclidean ball {u:||u−Z||≤r} through g_0. Its image is an interval because the ball is connected and g_0 is continuous. This is an honest interval. For any u in that ball,

\[
 |u_1u_2u_3|\le\|u\|^3/(3\sqrt3)
 \le(\|Z\|+r)^3/(3\sqrt3).
\]

Writing R=||G_3||, G_3∼N_3(0,I), gives

\[
 \ell^*_{\alpha,0}(0)\le
 \frac{2}{3\sqrt3}E(R+r)^3. \tag{C3}
\]

Since ER=2√(2/π), ER²=3 and ER³=8√(2/π), this upper bound is **34.9488882036** at α=.05. Thus

\[
 3.61839\le\ell^*_{.05,0}(0)\le34.94889.
\]

The factor 9.65868 between these analytic bounds is not an estimate of the actual efficiency gap. Neither bound is asserted sharp. These numbers also cannot be directly substituted for the current regression interval's finite-sample length constants: the experiments and procedures differ.

## The optimization problem to solve next

Use the minimum-distance statistic

\[
 T_{\theta,\kappa}(Z)=
 \inf_{h:g_\kappa(h)=\theta}\|Z-h\|^2.
\]

A valid critical value is

\[
 c_{\alpha}(\theta,\kappa)=
 \sup_{h:g_\kappa(h)=\theta}
 Q_{1-\alpha}\{T_{\theta,\kappa}(h+G_3)\}.
\]

By evaluating the infimum at the true h, T≤||G_3||² under the null, so c_α≤χ²_{3,1−α}. Inverting these tests and taking an interval hull gives honesty and a set contained in the corresponding projection interval. This is a definition of a valid calibration, not an algorithm for computing the supremum.

The hard tasks are to certify the supremum over the **unbounded** nuisance level set, solve or bound each constrained distance, handle κ near zero and large κ, and establish uniform regression transfer. A grid search or Monte Carlo maximum over finitely many h values cannot certify global size. One useful route is to prove a compact-region bound plus a regular-limit tail bound before numerical optimization. An independent Monte Carlo calibration error bound is also needed if random critical values are used.

**PARTIAL:** analytic benchmark bounds and a well-defined calibrated procedure. **OPEN:** exact optimal expected-length constants, certified efficient calibration, and uniform transfer. **Not claimed:** that minimum-distance inversion is new, that ordinary bootstrap is valid at the boundary, or that exact-boundary Wald calibration gives nearby honesty.

## Sources

1. Cai and Low (2004), [An Adaptation Theory for Nonparametric Confidence Intervals](https://arxiv.org/pdf/math/0503662), for the relationship between globally honest expected length and testing/modulus arguments. The Gaussian integration above is provided directly.
2. Andrews and Mikusheva (2016), [A Geometric Approach to Nonlinear Econometric Models](https://economics.mit.edu/sites/default/files/publications/ecta12030-%20final%20version.pdf), for curvature-based minimum-distance calibration.
3. Bei and Navjeevan (2026), [Inference under First-Order Degeneracy](https://arxiv.org/html/2602.07377v1), Sections 3–4, for degeneracy and uniformly valid minimum-distance inference. The proposed cubic/near-cubic calculation must be compared against that framework, not presented as the first treatment of degeneracy.
