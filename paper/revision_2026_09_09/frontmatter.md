---
title: "Sharp Normal Moduli and Honest Inference Near Tensor-Train Rank Boundaries"
subtitle: "Research revision with complete proof supplement"
date: "9 September 2026"
fontsize: 11pt
geometry: margin=1in
mainfont: DejaVu Serif
sansfont: DejaVu Sans
monofont: DejaVu Sans Mono
colorlinks: true
linkcolor: blue
urlcolor: blue
toc: true
toc-depth: 2
---

# Abstract {-}

Confidence intervals for linear tensor functionals can have vanishing first-order variance even at a full-rank tensor-train reference. We study the local variation of a product loading that is absent from the signal in every physical mode. For arbitrary admissible TT ranks, we establish a sharp Frobenius local modulus whose leading coefficient is the reciprocal product of the weakest bond singular values, multiplied by $K^{-K/2}$. Adding a weak product component to an orthogonal TT background gives a uniform transition from order $t^K/b^{K-1}$ to order $t$ as its strength $b$ approaches the localization scale $t$. In Gaussian regression, an explicit rank-two procedure attains the corresponding honest expected-length rate using only $6K-3$ prespecified coordinates, irrespective of the ambient dimension. An optimized shared error budget preserves finite-sample coverage and shortens the conservative baseline on every dataset. We also give an existence result after learned mode compression, with an explicit dimension-dependent training condition. In 95,000 independent simulated datasets, the optimized interval substantially reduces strong-pivot lengths but remains conservative. Sharp confidence constants and adaptation to unknown weak orientations remain unresolved.

# Introduction

Low-rank tensor constraints can make a linear functional locally much easier to infer than its ambient dimension suggests. The relevant difficulty is not determined solely by the number of free parameters. It also depends on how rapidly the functional changes along feasible local perturbations. At a point where all first-order changes vanish, a regular tangent-based variance formula is insufficient to describe the inferential scale.

Tensor trains impose compatible matrix-rank constraints at every prefix cut. A single unfolding can miss their combined effect. Consider a four-way coefficient with two orthogonal product components and a loading in a third, unused coordinate direction. In each separate rank-two matrix relaxation the loading changes at quadratic order. Under all TT constraints it changes only at quartic order. As the weaker component disappears, the same loading becomes first-order estimable. An interval required to cover all tensors in the capped class must accommodate this transition without selecting a rank and then treating that choice as certain.

The ingredients behind this example have substantial precedents. TT cross interpolation gives exact coordinate identities, and matrix-product-state theory studies higher-order core variations. Statistical work on tensor functionals gives regular tangent-based inference, while the broader degeneracy literature studies failures of first-order approximations. Our question is narrower: what is the exact local modulus of a physically normal product loading, and can a globally honest interval attain its scale uniformly as bond strength vanishes?

The central geometric argument has two parts. A canonical TT representation factors the target through all inverse bond metrics. Full physical contractions overlap, so their energies require a second-order overlap bound before an arithmetic–geometric mean argument gives a sharp constant. A feasible perturbation aligns adjacent cores with weakest bond directions and attains that constant. This extends the diagonal rank-two example to non-diagonal references and arbitrary admissible rank profiles.

For inference we distinguish prespecified and learned structure. A fixed collection of cross entries leads to a small Gaussian regression in which omitted coefficients enter the residual variance. This yields an explicit procedure valid for every tensor in the capped class, with short expected length at the aligned weak-component family even when the ambient dimension exceeds the sample size. Learning supporting mode subspaces gives a separate theorem whose training requirement depends on dimension. That theorem does not reach unidentified weak directions at the parametric boundary.

The contributions are:

1. A sharp, uniform normal-loading modulus involving every weakest bond singular value, and a complete weak-component transition over a general orthogonal TT background.
2. A globally honest, computable rank-two interval attaining the transition with $6K-3$ selected features, together with a strict comparison to each single-unfolding relaxation.
3. A certified optimization of the numerator error budget, and a separate learned-compression existence theorem with explicit assumptions and a training-failure term.

All theorem statements below have complete internal derivations in the appendices. Mathematical checking is distinct from independent peer review and confirmation of publication-level novelty.

# Related work

## Tensor geometry and interpolation

Fixed-rank TT representations and rank-capped tangent cones are established [@kutschan2018]. Higher-order MPS variations, including metric factors associated with right-interface densities, appear in @wouters2013. Exact TT cross reconstruction under invertible pivots is stated in @dolgov2019. We do not propose a new TT parametrization or cross identity. The candidate addition is the optimized Frobenius-neighborhood modulus, its uniform sharp constant and its statistical consequence. Whether that consequence is sufficiently distinct from the earlier geometry requires specialist scrutiny.

## Regular and degenerate inference

Regular low-rank tensor inference includes @xia2022 and @xu2025. The covariance-weighted framework of @ke2026 is especially close: its projected-variance theory and local lower bounds address a nondegenerate regime. Our fully normal loading has zero first-order tangent variance. We therefore study a different regime, without asserting an improvement over their valid regular guarantees. General first-order degeneracy and singular testing already have an extensive theory [@chenfang2019; @dufour2025; @bei2026]. The tensor constraint intersection and its explicit sharp coefficient are the proposed distinction.

## Sketching and conservative calibration

Importance sketching for tensor regression is established by @islet2020, and TT estimation and optimization guarantees are studied by @qin2025. Gaussian omitted-signal variance is an established part of projected regression. Our selected-coordinate reduction is useful because the target cross identity depends on few entries; it is not a new general sketching principle. Likewise, nuisance maximization over confidence sets [@bergerboos1994] and conservative Monte Carlo test inversion [@glazer2026] are established. Appendix E specifies sufficient numerical certificates, but it supplies no new generic p-value principle or completed optimal calibration algorithm.

# Statistical problem

Fix tensor order $K\ge3$ and dimensions $d_1,\ldots,d_K\ge3$. Set

\[
\mathcal H=\bigotimes_{j=1}^K\mathbb R^{d_j},\qquad
p=\prod_{j=1}^K d_j.
\]

The $k$th prefix unfolding $B^{[k]}$ has its first $k$ physical indices as rows and its remaining indices as columns. For deterministic admissible caps $r=(r_1,\ldots,r_{K-1})$, with $r_0=r_K=1$, define

\[
\Theta_r=\{B\in\mathcal H:\operatorname{rank}(B^{[k]})\le r_k
\text{ for }1\le k<K\}.
\]

We observe independent pairs $(X_i,Y_i)$, where

\[
\operatorname{vec}(X_i)\sim N_p(0,I_p),\qquad
Y_i=\langle X_i,B\rangle+\epsilon_i,\qquad
\epsilon_i\sim N(0,\sigma^2).
\]

Errors are independent of the designs and of one another. The coefficient $B$ and scale $\sigma>0$ are unknown. There are no latent random factors, dependent observations or contamination in this experiment. The squared-error loss is $\ell(B;X,Y)=(Y-\langle X,B\rangle)^2/2$, the empirical risk is its sample average, and the excess population risk under truth $B_*$ is $\|B-B_*\|_F^2/2$.

Fix unit vectors $w_j$ before observing inference data and let $A=\bigotimes_jw_j$. The estimand is $\psi_A(B)=\langle A,B\rangle$. For $0<\alpha<1/2$, a random interval $I_n$ is globally honest if

\[
\inf_{B\in\Theta_r,\,\sigma>0}
P_{B,\sigma}\{\psi_A(B)\in I_n\}\ge1-\alpha.
\]

The pointwise optimal expected length under this restriction is

\[
L_{\alpha,n}(B_*;\sigma)
=\inf_{I_n\text{ globally honest}}E_{B_*,\sigma}|I_n|.
\]

Our geometric object is

\[
\omega_A(t;B_*)=
\sup_{B\in\Theta_r:\|B-B_*\|_F\le t}
|\langle A,B-B_*\rangle|.
\]

Dimensions may vary with $n$. Statistical growth results keep $K$ and the rank caps fixed. The geometric uniformity statement is stronger and does not require bounded ranks. Rank uncertainty means that actual ranks may vary within a prespecified capped class; the cap itself is not selected from inference data.

# Main geometric results

**Theorem 1 (sharp physically normal modulus; G1).** Suppose $B_*$ has exact TT ranks $r$, and put $\beta_j=\sigma_{r_j}(B_*^{[j]})$, $\beta=\min_j\beta_j>0$. Assume

\[
B_*\times_jw_j^T=0\quad\text{for every }j.
\]

For fixed $K$, uniformly over dimensions, ranks and references as $t/\beta\to0$,

\[
\omega_A(t;B_*)=
\frac{t^K}{K^{K/2}\prod_{j=1}^{K-1}\beta_j}\{1+o(1)\}.
\]

Appendix B supplies explicit finite-radius upper and lower bounds and a feasible path attaining the leading coefficient. The assumption annihilates the signal in each loading mode. Merely requiring $\psi_A(B_*)=0$, or orthogonality to a first-order tangent space, is insufficient.

**Corollary 1 (general weak-component transition; G2).** Let $C\in\bigotimes_jE_j$ have exact positive ranks $s_j$ and smallest nonzero bond singular values at least $a_0$. In each mode take mutually orthogonal $E_j$, $\operatorname{span}(v_j)$ and $\operatorname{span}(w_j)$, with unit $v_j,w_j$. For caps $r_j=s_j+1$, set $B_b=C+b\bigotimes_jv_j$, where $0\le b\le a_0$. Then

\[
\omega_A(t;B_b)\asymp_K
t\min\{1,(t/b)^{K-1}\},
\]

with value $t$ at $b=0$ and sharp strong-bond coefficient $K^{-K/2}$. The background can be non-diagonal and have different ranks across bonds. This result does not classify all patterns of unequal vanishing singular values.

**Comparison with a matrix relaxation.** At $B_b=a e_0^{\otimes K}+b e_1^{\otimes K}$ and $A=e_2^{\otimes K}$, impose only the rank-two constraint at one prefix cut. Its modulus is asymptotic to $t^2/(2b)$, whereas the TT modulus is asymptotic to $t^K/(K^{K/2}b^{K-1})$. For $K>2$, their ratio tends to zero as $t/b\to0$. This comparison concerns each separate unfolding relaxation; it makes no claim against a matrix encoding augmented with all equivalent nonlinear constraints. Appendix A proves both statements.

# A computable honest interval

For the rank-two family, use prefix indices $P_k=\{0^k,1^k\}$ and suffix indices $Q_k=\{0^{K-k},1^{K-k}\}$. The pivots are $S_k(B)=B(P_k,Q_k)$; the target slices are $C_1(B)=B(2,Q_1)$, $C_K(B)=B(P_{K-1},2)$ and $C_j(B)=B(P_{j-1},2,Q_j)$ otherwise. Invertible pivots imply

\[
\psi_A(B)=C_1(B)S_1(B)^{-1}C_2(B)\cdots
S_{K-1}(B)^{-1}C_K(B).
\]

The union $F$ of all required coordinates, including the target, has cardinality $m=6K-3$. Regress $Y$ on the corresponding design coordinates $W=X_F$. The coefficient is $\theta=B_F$, and the effective noise variance is

\[
\tau_B^2=\sigma^2+\|B_{F^c}\|_F^2.
\]

Conditional on $W$, this is an ordinary Gaussian regression. Let $z$ be OLS, $\widehat\tau^2$ its residual variance estimate, and

\[
e=\widehat\tau
\sqrt{\frac{m F_{m,n-m;1-\alpha}}{\lambda_{\min}(W^TW)}}.
\]

The ball $\|z-\theta\|\le e$ has coverage at least $1-\alpha$. If every $d_k=\sigma_{\min}(S_k(z))-e$ is positive, form

\[
H=\frac{P_*(c,e)}{\prod_kd_k},\qquad
c_j=\|C_j(z)\|_F,\qquad
P_*(c,e)=\max_{\delta\ge0:\sum_j\delta_j^2\le e^2}
\prod_j(c_j+\delta_j).
\]

Return $[-H,H]\cap[z_A-e,z_A+e]$, or the singleton $\{z_A\}$ if empty. If a pivot is uncertified, return $[z_A-e,z_A+e]$. The empty case cannot occur on the common coverage event.

The maximizing errors satisfy

\[
\delta_j=\frac{\sqrt{c_j^2+4\mu}-c_j}{2},\qquad
\sum_j\delta_j^2=e^2,
\]

with a unique positive $\mu$ when $e>0$. Monotone bisection gives lower and upper numerator bounds. Using the upper bound preserves coverage. Replacing $P_*$ by $\prod_j(c_j+e)$ defines the separate-bound baseline; the new interval is no longer on any dataset. This optimizes a relaxation of confidence-region inversion, leaving conservatism from pivot bounds and the F-ball conversion.

**Theorem 2 (growing-dimension weak-bond inference; C4).** Fix $K\ge3$, $0<\alpha<1/2$ and $n\ge6K-3+\max(K,2)$. In arbitrary $d_j\ge3$, the interval above is globally honest over $\Theta_2$ and all $\sigma>0$. At $B_b=a e_0^{\otimes K}+b e_1^{\otimes K}$, $0\le b\le a$, let $t_n=\sigma/\sqrt n$. There are positive constants depending only on $K,\alpha$ such that

\[
c_{K,\alpha}t_n\min\{1,(t_n/b)^{K-1}\}
\le L_{\alpha,n}(B_b;\sigma)
\le E_{B_b,\sigma}|I_n|
\le C_{K,\alpha}t_n\min\{1,(t_n/b)^{K-1}\}.
\]

At $b=0$ the scale is $t_n$. Constants do not depend on the ambient dimensions or on $a,b$. For $K=4$, only 21 selected features enter inference and the strong-bond scale is $\sigma^4/(b^3n^2)$.

The procedure never receives $a$, $b$ or a true decomposition. Its coordinate pattern is fixed in advance. Honesty holds at all other tensors in the class, but the short-length theorem is restricted to the displayed family. The full-data lower bound permits competing procedures to use every covariate. Appendix C proves calibration, moments, length and the two-point obstruction in detail.

# Learning supporting subspaces

The selected-coordinate result does not settle unknown orientations. For this question, restrict the parameter to $\Theta_r(M)=\{B\in\Theta_r:\|B\|_F\le M\}$ and split the sample into training and inference parts. From training choose mode subspaces containing the loading directions, with orthogonal product projection $P$. Inference on the compressed design preserves the target and the TT caps, while the residual variance becomes $\sigma^2+\|(I-P)B\|_F^2$. Inverting a valid confidence ball over the compressed capped class gives global honesty.

**Theorem 3 (learned-compression existence bound; D1–D3).** Suppose $B_*$ satisfies Theorem 1, $b\le\beta_j\le\kappa b$, and training produces an event $G$ with probability at least $1-\delta$ on which $\|(I-P)B_*\|_F\le\min(b/2,\sigma)$. If the compressed dimension is $m$ and $n_2\ge m+\max(K,2)$, then the interval satisfies

\[
E|I_n|\le C_{K,m,\alpha,\kappa}
\min\left\{\frac\sigma{\sqrt{n_2}},
\frac{\sigma^K}{n_2^{K/2}\prod_j\beta_j}\right\}+2M\delta.
\]

A global constrained least-squares pilot supplies such an event with $\delta=2e^{-x}$ if

\[
n_1\ge\max\{128,324,1296\sigma^2/b^2\}(W+x),
\]

where Appendix D gives an explicit Tucker-envelope entropy $W=O_{K,r}(1+\sum_jd_j)$ and a complete concentration proof. The inference dimension is bounded for fixed $K,r$. Exact global minimization and confidence-set inversion are existence constructions; no polynomial-time guarantee is asserted.

The condition on $n_1b^2/\sigma^2$ excludes $b\asymp\sigma/\sqrt n$ when $W$ grows and the split is proportional. Whether one globally honest procedure can attain the selected-direction scale throughout the intermediate regime $\sigma/\sqrt n\ll b\lesssim\sigma\sqrt{W/n}$ remains unresolved. An orientation-estimation lower bound alone would not settle a functional confidence-length problem.

# Numerical study

We generated 5,000 independent Gaussian regression sufficient-statistic realizations for each of 19 prespecified settings, giving 95,000 independent datasets and 380,000 paired interval records. The coefficient is embedded in dimensions $(40,40,40,40)$, so $p=2,560,000$, while inference uses $m=21$. Bartlett Wishart sampling, conditional normal OLS error and residual chi-square sampling reproduce the exact marginal regression law. A full ambient design is not materialized.

With $a=3$, $\sigma=0.2$, $K=4$ and nominal coverage 0.95, we vary $b/t_n$ over $\{0,2,8,32,128\}$ at $n=512,8192$. Nonzero-target alternatives follow $a e_0^4+b(e_1+s e_2)^4$ with $s=2t_n/b$ and $b/t_n\in\{2,8,32\}$; their omitted-signal variance is included. A fixed $b=0.3$ study uses $n=512,8192,131072$. Methods are the separate and joint cross bounds, common-ball projection, and a scalar Student-t interval. The latter is a valid unstructured marginal-regression baseline.

![Mean length and coverage at the aligned family, n=8192. Coverage bars are Wilson intervals over 5,000 replications. The cross intervals remain conservative; the error-budget improvement is visible after pivots are well separated.](../../simulations/figures/tt_revision_2026_09_09/weak_bond.pdf){width=100%}

At $n=8192$ and $b/t_n=32$, the ratio of mean joint to mean separate length is 0.13436, with paired Monte Carlo SE 0.00024. At the corresponding nonzero-target alternative it is 0.17723, with SE 0.00030. At small bond strengths the fallback intervals largely coincide. Thus the new bound improves strong-pivot lengths substantially without a universal efficiency improvement over scalar Student-t.

All stored intervals satisfy the proved joint-versus-separate length dominance. Every structured interval contains the target on the common confidence-ball event. Coverage is highly conservative; all aligned-family cross rows cover in all 5,000 replications. Their Wilson lower endpoint is approximately 0.99923. At true 0.95 coverage, Monte Carlo SE would be 0.00308, or 0.31 percentage points. Zero plug-in SE for an all-success row does not establish exact population coverage.

The three-point fixed-bond log-log slope is −2.2252 for the joint method, with Monte Carlo SE 0.0011, whereas the asymptotic prediction is −2. This discrepancy reflects visible finite-sample effects, not Monte Carlo uncertainty. The study supports the strong-bond decay and deterministic length improvement; it does not certify convergence of the exponent or optimal constants. It does not test learned subspaces or a nonzero-target minimum-distance algorithm. Full raw summaries, Wilson intervals, paired errors and reproducible seeds accompany the project.

# Discussion

The combined TT constraints can impose higher-order contact that no separate unfolding relaxation captures. For physically normal product loadings, the sharp local coefficient depends on every weakest bond singular value. The associated statistical length transition can be attained in a focused growing-dimension experiment with exact finite-sample coverage and unknown variance.

The limitations identify the next mathematical questions. Physical normality is stronger than tangent orthogonality. Unequal rank losses can interact in ways not covered by a single weak component. Learned subspaces currently require the weak directions to be estimable, and their inversion procedure is not computationally certified. The finite-sample cross interval remains conservative even after optimizing its numerator. Exact geometric constants do not supply exact optimal confidence constants.

For a zero-product Gaussian mean target, Appendix E proves the exact worst-case chi-square calibration of the distance-to-null statistic. For nonzero targets it gives a conditional certification framework, while the necessary global distance solver and continuum inversion remain unfinished. These are explicitly partial computational directions.

The model is a general structured regression problem. A TT adapter can motivate a linearized coefficient, but actual neural features need not be independent isotropic Gaussians and training does not supply the required experiment automatically. No LLM experiment or theorem is claimed. The strongest next result would resolve the cost of unknown weak orientations through matching functional lower and upper bounds, or extend the sharp modulus beyond fully normal product loadings.

# References {-}

::: {#refs}
:::

\newpage

# Complete proof supplement {-}

The appendices reproduce the full derivations using development identifiers G1–G2, C1–C5, D1–D3 and M1–M2. Theorem 1 corresponds to G1, Theorem 2 to C4, and Theorem 3 to D1–D3. PROVED means a complete internally checked derivation. PARTIAL and CONJECTURED items are not used as theorem premises.
