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


\newpage

# A. Rank-two geometry and the single-unfolding comparison

## 1. Model and statement: PROVED

Fix $0<\alpha <1/2$ and tensor order $K\ge 3$ and dimensions $d_j\ge 3$. Let $e_0,e_1,e_2$ denote the first three coordinate vectors in each mode, and let

\[
 \begin{gathered}
 \Theta_2=\{B:\operatorname{rank}(B^{[k]})\le2,
                   \ k=1,\ldots,K-1\},\\
 B_b=a e_0^{\otimes K}+b e_1^{\otimes K},\quad0\le b\le a,
 \quad A=e_2^{\otimes K}.
\end{gathered}
\]

Use the unbounded, closed rank-capped class. For b>0 every bond rank is exactly two, and its two nonzero singular values are a and b. There are no cap-one cuts. At $b=0$ the rank drops to one. Define

\[
 \omega(t;b)=\sup_{B\in\Theta_2:\|B-B_b\|_F\le t}
                  |\langle A,B-B_b\rangle|.
\]

For b>0 and every t>0,

\[
 \omega(t;b)\asymp_K
       t\min\{1,(t/b)^{K-1}\}. \tag{T1}
\]

At $b=0$, $\omega (t;0)=t$. More precisely, for 0<t<b,

\[
 b\left\{(1+t^2/b^2)^{1/K}-1\right\}^{K/2}
 \le\omega(t;b)\le
 \min\left\{t,\frac{t^K}{K^{K/2}(b-t)^{K-1}}\right\}. \tag{T2}
\]

Consequently the leading local constant is sharp:

\[
 \lim_{t/b\to0}\frac{b^{K-1}\omega(t;b)}{t^K}
       =K^{-K/2}. \tag{T3}
\]

The limit allows a and b to vary with t, subject to $a\ge b>0$. All geometric bounds are independent of the ambient dimensions. For $K=4$, the leading term is $t^{4}/(16b^{3})$.

## 2. Cross interpolation and the upper bound

For $k=1,...,K-1$ take prefix indices $P_k=\{0^k,1^k\}$ and suffix indices $Q_k=\{0^{K-k},1^{K-k}\}$. Let $S_k(B)=B(P_k,Q_k)$, a $2\times 2$ pivot. At $B_b$ each pivot is diag(a,b). If $\|B-B_b\|\le t<b$, then $\|S_k(B)-\operatorname{diag}(a,b)\|_{op}\le t$ and thus

\[
 \sigma_{\min}\{S_k(B)\}\ge b-t>0.
\]

Let $C_1(B)=B(2,Q_1)$, $C_K(B)=B(P_{K-1},2)$, and for $2\le k\le K-1$ let $C_k(B)=B(P_{k-1},2,Q_k)$. The endpoint slices are a row and column vector; the others are $2\times 2$ matrices. Exact TT cross interpolation gives

\[
 \langle A,B\rangle=C_1(B)S_1(B)^{-1}C_2(B)
             \cdots S_{K-1}(B)^{-1}C_K(B). \tag{T4}
\]

For completeness, a rank-at-most-two matrix with an invertible selected $2\times 2$ submatrix S satisfies $M=M(:,Q)S^{-1}M(P,:)$: the selected columns form a column-space basis, and their coefficients are identified by restriction to the selected rows. Apply this identity first to the first prefix unfolding. Apply it again to the remaining factor using the next prefix unfolding, and continue. This gives (T4), equivalently the familiar exact TT cross formula. Invertibility also implies that each nearby unfolding has rank exactly two.

All entries in $C_k(B_b)$ are zero. More strongly, the entry sets of $C_1,...,C_K$ are pairwise disjoint: entries in $C_k$ have their only coordinate equal to 2 at site k and all other coordinates in {0,1}. Hence

\[
 \sum_{k=1}^K\|C_k(B)\|_F^2\le\|B-B_b\|_F^2\le t^2.
\]

Use (T4), operator norm bounded by Frobenius norm, and arithmetic–geometric mean:

\[
 |\langle A,B\rangle|
 \le\frac{\prod_k\|C_k(B)\|_F}{(b-t)^{K-1}}
 \le\frac{(t^2/K)^{K/2}}{(b-t)^{K-1}}.
\]

Cauchy–Schwarz separately gives $|\langle A,B-B_b\rangle |\le t$. This proves the upper bound in (T2).

## 3. Attainability, the weak-bond transition and sharpness

Use the TT-feasible path

\[
 B(s)=a e_0^{\otimes K}+b(e_1+s e_2)^{\otimes K}.
\]

It is a sum of two product tensors, so all prefix ranks are at most two. Orthogonality of the coordinate products gives

\[
 \|B(s)-B_b\|_F^2=b^2\{(1+s^2)^K-1\},\qquad
 \langle A,B(s)\rangle=bs^K.
\]

Choose $s^{2}=(1+t^{2}/b^{2})^{1/K}-1$. This proves the lower bound in (T2), and in fact this lower bound holds for every t>0.

Here is an explicit verification of the uniform equivalence (T1). Put $u=t/b$. If $0<u\le 1$, the mean value theorem gives

\[
 (1+u^2)^{1/K}-1\ge u^2/(2K),
\]

so the lower bound is at least $(2K)^{-K/2}t$ $u^{K-1}$. If $u\ge 1$, divide the expression in braces by $u^{2/K}$. The resulting function is $f(v)=(1+v)^{1/K}-v^{1/K}$, with $v=u^{-2}\in (0,1]$. Its derivative is negative, so $f(v)\ge f(1)=2^{1/K}-1$. This gives a lower bound $(2^{1/K}-1)^{K/2}t$. For the upper bound, if $t\le b/2$ apply (T2) and $b-t\ge b/2$. If b/2<t<b, use $\omega \le t\le 2^{K-1}t(t/b)^{K-1}$; if $t\ge b$, use $\omega \le t$. These bounds prove (T1).

As $t/b\to 0$, the lower bound is $K^{-K/2}t^K/b^{K-1}\{1+o(1)\}$ and the upper bound has the same coefficient. This proves (T3). At $b=0$ the feasible path a $e_0^{\otimes K}+t$ $e_2^{\otimes K}$ attains the ambient upper bound t exactly.

## 4. Comparison with every single prefix unfolding: PROVED

Fix a cut k and impose only $\operatorname{rank}(B^{[k]})\le 2$, retaining the same center and target. Denote that matrix-model modulus by $\omega _k^mat(t;b)$. In the orthonormal row and column bases containing $0^k,1^k,2^k$ and $0^{K-k},1^{K-k},2^{K-k}$, the center has pivot diag(a,b). Matrix skeleton interpolation gives the target entry as a row times the inverse pivot times a column. These two off-pivot slices occupy disjoint entries of the perturbation. The same energy argument gives

\[
 \omega_k^{\mathrm{mat}}(t;b)\le t^2/\{2(b-t)\},\quad0<t<b.
\]

The rank-two matrix path rotating the weak component's row and column toward the corresponding all-2 vectors has target $bs^{2}$ and distance $b\sqrt (2s^{2}+s^{4})$. Therefore

\[
 \omega_k^{\mathrm{mat}}(t;b)\sim t^2/(2b)
 \quad\text{as }t/b\to0,
\]

and the same two-regime argument gives $\omega _k^mat(t;b)\asymp t$ min(1,t/b). In particular,

\[
 \frac{\omega(t;b)}{\min_k\omega_k^{\mathrm{mat}}(t;b)}
 \sim\frac2{K^{K/2}}(t/b)^{K-2}\longrightarrow0.
\]

This compares the full TT class with each single-unfolding relaxation. It does not claim that no matrix representation with additional nonlinear constraints could encode the tensor problem. The intersection of compatible rank constraints is the substantive distinction.


\newpage

# B. General normal-loading geometry

Status: **PROVED**, with complete internal derivations below. This is a generalization of the rank-two calculation, not a claim that TT parametrizations or higher-order tangent spaces are new. Tensor order and rank caps are fixed unless explicitly stated otherwise.

## G1. General sharp modulus theorem

Let $H=\otimes _{j=1}^K$ $R^{d_j}$, $K\ge 2$, and let $\Theta _r$ consist of tensors whose prefix unfolding ranks are at most $r=(r_1,...,r_{K-1})$, with $r_0=r_K=1$. Let $B_*$ have exact ranks r. Put $\beta _j=\sigma _{r_j}(B_*^{[j]})>0$ and $\beta =min_j$ $\beta _j$. Take unit $w_j$ and $A=\otimes _j$ $w_j$. Assume

\[
 B_*\times_j w_j^T=0\quad\text{for every }j.
\]

Here $\times _j$ is contraction in physical mode j. This says that the loading direction is absent from the signal in each mode. It is stronger than merely $\langle A,B_*\rangle =0$ or first-order tangent orthogonality. It admits arbitrary TT cores and arbitrary admissible ranks within the complementary physical spaces.

For $\omega _A(t;B_*)=sup_{B\in \Theta _r, \|B-B_*\|\le t}|\langle A,B-B_*\rangle |$,

\[
 \lim_{t/\beta\to0}
 \frac{\omega_A(t;B_*)\prod_{j=1}^{K-1}\beta_j}{t^K}
       =K^{-K/2}. \tag{G1}
\]

The limit is uniform over dimensions, ranks and reference tensors for fixed K, subject to the stated exact ranks and $t/\beta \to 0$. In particular the normalizing factor is the product of the weakest singular values at all bonds, not necessarily $\beta ^{K-1}$.

An explicit upper bound for $0<t<\beta$ is

\[
 \omega_A(t;B_*)\le
 \frac{K^{-K/2}\{t^2+t^4\sum_{i<j}(\beta_i-t)^{-2}\}^{K/2}}
      {\prod_{j=1}^{K-1}(\beta_j-t)}, \tag{G2}
\]

where i<j ranges over $1\le i<j\le K$, so $\beta _i$ is only needed for i<K. Also $\omega _A\le t$. For $0<t\le \beta /2$, a lower bound is

\[
 \omega_A(t;B_*)\ge
 2^{-K/2}K^{-K/2}\frac{t^K}{\prod_j\beta_j}. \tag{G3}
\]

No uniform weak-bond formula for arbitrary patterns of unequal vanishing $\beta _j$ is claimed by this theorem.

## Proof of the upper bound

Rotate coordinates independently in each mode so $w_j$ is the last basis vector. Orthogonal changes preserve tensor norm, prefix singular values and TT ranks. Write a nearby B in left-orthonormal TT form with cores $G_j$. This form exists by successively applying thin QR factorizations, or thin singular-value decompositions, to the prefix unfoldings. Because $t<\beta$, Weyl's inequality gives exact ranks r for B.

Let $L_j$ be its left interface with orthonormal columns and $R_j$ its right interface, so $B^{[j]}=L_jR_j$. The nonzero singular values of $R_j$ are those of $B^{[j]}$. Define $Q_j=(R_jR_j^T)^{1/2}$, j<K; $Q_K=1$. Define $H_j=G_j(w_j)$, the core slice in the target physical direction, $Z_j=H_jQ_j$, and $d_j=\|Z_j\|_F$. The isometry of $L_{j-1}$ and the identity $\|H_jR_j\|_F=\|H_jQ_j\|_F$ imply

\[
 d_j=\|B\times_jw_j^T\|_F\le t,
 \quad\|H_j\|_{\mathrm{op}}\le t/(\beta_j-t)\quad(j<K).
\]

The target entry factors exactly as

\[
 \langle A,B\rangle
 =Z_1Q_1^{-1}Z_2Q_2^{-1}\cdots Q_{K-1}^{-1}Z_K.
\]

Therefore $|\langle A,B\rangle |\le \prod d_j/\prod (\beta _j-t)$. To retain the sharp energy constant, it remains to control $\sum d_j^{2}$ more carefully than the bound $Kt^{2}$.

For i<j, restrict the left interface $L_{j-1}$ to the target direction at site i. Its operator norm is at most $\|H_i\|_{op}$: before site i the left interface is an isometry; after site i the recursion $L_l=(L_{l-1}\otimes I)G_l^left$ multiplies by matrices of operator norm one. Consequently

\[
 \|B\times_iw_i^T\times_jw_j^T\|_F
 \le\|H_i\|_{\mathrm{op}}\|H_jR_j\|_F
 \le t^2/(\beta_i-t).
\]

Decompose B into mutually orthogonal components $B_S$ according to which modes lie along $w_j$ and which lie in $w_j^\perp$. Since $B_*$ has only its $S=\varnothing$ component,

\[
 \sum_{S\ne\varnothing}\|B_S\|^2\le t^2,
 \quad \sum_jd_j^2=\sum_{S\ne\varnothing}|S|\|B_S\|^2.
\]

For $s\ge 2$, $s-1\le \operatorname{binom}(s,2)$. The pairwise contractions count each $B_S$ exactly binom(|S|,2) times. It follows that

\[
 \sum_jd_j^2\le t^2+
 \sum_{i<j}\|B\times_iw_i^T\times_jw_j^T\|^2
 \le t^2+t^4\sum_{i<j}(\beta_i-t)^{-2}.
\]

Arithmetic–geometric mean, $\prod d_j\le (\sum d_j^{2}/K)^{K/2}$, proves (G2). This argument covers all nearby feasible tensors and does not assume a particular differentiable path.

## Proof of attainability and the sharp constant

Take a left-orthonormal TT representation of $B_*$ and define its $Q_j$ as above. Each target core slice is zero: the full physical slice is $L_{j-1}G_j(w_j)R_j=0$, and both interfaces have full respective column and row rank. Let $v_j$ be a unit eigenvector of $Q_j$ with eigenvalue $\beta _j$. Set

\[
 \begin{gathered}
 Z_1=v_1^T/\sqrt K,\quad
 Z_j=v_{j-1}v_j^T/\sqrt K\ (1<j<K),\quad
 Z_K=v_{K-1}/\sqrt K,\\
 H_j=Z_jQ_j^{-1}\ (j<K),\qquad H_K=Z_K.
 \end{gathered}
\]

Replace the zero target slice of each core by $uH_j$ and leave every other slice unchanged. The resulting B(u) belongs to $\Theta _r$ for every real u. Expand $B(u)-B_*$ by the nonempty set S of replaced cores. The terms $u^{|S|}V_S$ are mutually orthogonal because they have different physical target patterns. For $|S|=1$, $\|V_S\|=\|Z_j\|=1/\sqrt{K}$, so the first-order squared norm is $u^{2}$. The target is exactly

\[
 \langle A,B(u)\rangle
 =\frac{u^K}{K^{K/2}\prod_j\beta_j}.
\]

We bound the remainder uniformly. If $S=\{i_1<...<i_s\}$, then contractions before its last site have operator norm at most $\prod _{l<s}\|H_{i_l}\|_{op}$; intervening left-orthonormal cores have operator norm one. At the last site, $\|H_{i_s}R_{i_s}\|=1/\sqrt{K}$. Hence

\[
 \|V_S\|_F\le K^{-s/2}\beta^{-(s-1)}.
\]

Thus

\[
 u^2\le\|B(u)-B_*\|^2
 \le\beta^2\{(1+u^2/(K\beta^2))^K-1\}
 \le u^2\exp(u^2/\beta^2).
\]

For $t\le \beta /2$, $u=t/\sqrt 2$ makes the final bound strictly smaller than $t^{2}$ and proves (G3). For the sharp limit use $u=t$ $\operatorname{exp}\{-t^{2}/(2\beta ^{2})\}$. Then $u\le t$ and $u^{2}$ $\operatorname{exp}(u^{2}/\beta ^{2})\le t^{2}$, while $u/t\to 1$ uniformly as $t/\beta \to 0$. This proves the matching lower limit. In (G2), the relative energy correction is at most $\operatorname{binom}(K,2)(t/\beta )^{2}/(1-t/\beta )^{2}$, and the denominator correction at most $(1-t/\beta )^{-(K-1)}$. This proves the claimed uniform sharp limit. $\blacksquare$

## G2. A weak component added to a general TT background

For each mode take orthogonal subspaces $E_j$, $\operatorname{span}(v_j)$, $\operatorname{span}(w_j)$, where $v_j,w_j$ are unit. Let $C\in \otimes E_j$ have exact positive TT ranks $s_j$ and smallest nonzero singular values at least $a_0>0$. Set $r_j=s_j+1$ and

\[
 B_b=C+b\bigotimes_jv_j,\quad A=\bigotimes_jw_j,
 \qquad0\le b\le a_0.
\]

Orthogonality of both prefix and suffix factors makes the nonzero singular values at each cut the union of those of C and {b}; thus, for b>0, $B_b$ has ranks $r_j$ and $\beta _j=b$. Then, uniformly for every t>0 and $0<b\le a_0$,

\[
 \omega_A(t;B_b)\asymp_K t\min\{1,(t/b)^{K-1}\}.
\]

The strong-bond leading coefficient is $K^{-K/2}$, and $\omega _A(t;B_0)=t$. The background need not be diagonal, a product tensor, or a sum of two products. Rank profiles may vary across the chain.

**Proof.** For $t\le b/2$, (G2) supplies the upper bound $C_Kt^K/b^{K-1}$; otherwise the ambient upper bound t differs from the claimed rate by at most $2^{K-1}$. For a lower bound use $C+b\otimes (v_j+u$ $w_j)$. Its difference from $B_b$ has squared norm $b^{2}\{(1+u^{2})^K-1\}$; its target equals $bu^K$. It is feasible because a sum of a tensor of ranks s and a product has ranks at most s+1. Choose $u^{2}=(1+t^{2}/b^{2})^{1/K}-1$. Put $x=t/b$. For $x\le 1$, the mean value theorem gives $(1+x^{2})^{1/K}-1\ge x^{2}/(2K)$, yielding the lower constant $(2K)^{-K/2}$. For $x\ge 1$, the ratio of the expression in braces to $x^{2/K}$ is $(1+v)^{1/K}-v^{1/K}$, $v=x^{-2}\le 1$. This function decreases in v, so it is at least $2^{1/K}-1$, giving a positive constant times t. At $b=0$, C+tA is feasible and attains the ambient bound. The sharp coefficient for $t/b\to 0$ follows from G1. $\blacksquare$

## What these statements do and do not establish

The diagonal rank-two result is a special case with $C=a$ $e_0^{\otimes K}$. The new theorems extend both its geometry and its vanishing-component family. At a general fixed reference, the coefficient depends on every bond; for the weak-component family, all weakest bond singular values coincide, so a complete uniform transition is available.

Physical normality in every mode is essential. First-order tangent orthogonality alone does not imply order K. For example, a loading with only two active normal modes in a rank-one tensor model generally has order two. Likewise, losing rank at only one cut does not imply that adding an arbitrary product tensor respects every other cap. The all-bond weak-component construction supplies the needed feasible path.

The exact modulus constant is not an optimal confidence-interval constant. General dense loadings, partially normal loadings, simultaneous unequal rank losses and efficiently attainable sharp confidence constants remain open.


\newpage

# C. Selected-cross inference and calibration

Status: **PROVED** for the statements below. Exact finite-sample coverage means a mathematical probability guarantee under the stated Gaussian experiment, not equality of coverage to the nominal level at every parameter. Numerical code uses floating-point arithmetic and is separately checked; it is not a formal machine-arithmetic proof.

## C1. A regression with only the required coordinates

Consider independent $x_i\sim N_p(0,I_p)$, $Y_i=\langle x_i,B\rangle +\epsilon _i$, $\epsilon _i\sim N(0,\sigma ^{2})$, $\sigma >0$ unknown. Let $\Theta _2$ be the all-rank-at-most-two TT class from Appendix A. Fix its cross pivots $S_k$, target slices $C_j$ and target $A=e_2^{\otimes K}$ before looking at inference data.

Let F be the set of distinct tensor coordinates used by all $S_k$, all $C_j$ and A. There are exactly

\[
 m=|F|=2K+(4K-4)+1=6K-3
\]

coordinates: the two diagonal pivot entries are shared by all cuts, each cut adds two distinct off-diagonal pivot entries, the target slices are disjoint, and the target entry is new. Let $\theta =B_F$ and $W=(x_{i,F})_{i=1}^n$. Then

\[
 Y=W\theta+\xi,\qquad
 \xi\mid W\sim N_n(0,\tau_B^2I_n),\qquad
 \tau_B^2=\sigma^2+\|B_{F^c}\|^2.
\]

**Proof.** The Gaussian coordinate blocks $x_{i,F}$ and $x_{i,F^c}$ are independent. The omitted linear predictor is independent Gaussian noise with the displayed variance. Independence holds across observations. This is conditional on W, not on the full original design. $\blacksquare$

The vector $\theta$ is not falsely asserted to be a TT tensor. It is a vector of coordinates satisfying the cross relation inherited from the original B. This relation is all the procedure requires. The variance $\tau _B$, rather than $\sigma$, must be estimated in this regression.

## C2. Exact calibration with unknown effective variance

For n>m define

\[
 \begin{gathered}
 S=W^TW,\quad z=S^{-1}W^TY,\quad
 \widehat\tau^2=\|Y-Wz\|^2/(n-m),\\
 e=\widehat\tau\sqrt{mF_{m,n-m;1-\alpha}/\lambda_{\min}(S)}.
 \end{gathered}
\]

Then $P_{B,\sigma }(\|z-\theta \|\le e$ | $W)\ge 1-\alpha$, uniformly over every B and $\sigma >0$. Indeed, conditional on W, $S^{1/2}(z-\theta )/\tau _B$ is standard normal, $RSS/\tau _B^{2}$ is $\chi ^{2}_{n-m}$, and these are independent orthogonal projections of Gaussian noise. Their ratio gives

\[
 \frac{(z-\theta)^TS(z-\theta)}{m\widehat\tau^2}
       \sim F_{m,n-m}.
\]

The ellipsoid event implies the ball event by $\lambda _{min}(S)\|z-\theta \|^{2}\le (z-\theta )^TS(z-\theta )$. Thus the finite-sample critical value is calibrated without a rank-selected reference distribution or a nuisance-parameter grid.

Extract all cross slices from z using their coordinate maps. If $d_k=\sigma _{min}(S_k(z))-e>0$ for every k, define the old numerator $P_{old}=\prod _j(c_j+e)$, $c_j=\|C_j(z)\|_F$, and denominator $D=\prod _k$ $d_k$. Intersect $[-P_{old}/D,P_{old}/D]$ with $[z_A-e,z_A+e]$, using the singleton $\{z_A\}$ if empty. If any $d_k\le 0$ use $[z_A-e,z_A+e]$. The cross identity proves coverage on the common ball event for every $B\in \Theta _2$.

## C3. An optimized numerator certificate

The disjoint target slices share the same error budget. On the ball event, $\delta _j=\|C_j(\theta )-C_j(z)\|$ satisfies $\sum \delta _j^{2}\le e^{2}$. Replace $P_{old}$ by

\[
 P_*(c,e)=\max_{\delta_j\ge0,\ \sum_j\delta_j^2\le e^2}
                   \prod_{j=1}^K(c_j+\delta_j). \tag{C1}
\]

This replacement preserves coverage and cannot increase interval length on any dataset. It optimizes the numerator relaxation, not the entire confidence-region image: errors in the pivots also consume budget, which this relaxation does not exploit.

For $e=0$, $P_*=\prod c_j$. For e>0 the unique optimizing $\delta$ has

\[
 \delta_j(\mu)=\frac{\sqrt{c_j^2+4\mu}-c_j}{2},\qquad
 \sum_j\delta_j(\mu)^2=e^2,\quad\mu>0. \tag{C2}
\]

**Proof.** A positive feasible product exists. Its log is strictly concave on positive factors and increases in every $\delta _j$, so the constraint is active. At an optimum every $\delta _j>0$: with $c_j>0$, the derivative at $\delta _j=0$ is positive while the ball's derivative in that coordinate is zero; with $c_j=0$ a positive product requires $\delta _j>0$. The Lagrange equations are $1/(c_j+\delta _j)=2\lambda \delta _j$, $\lambda >0$. Set $\mu =(2\lambda )^{-1}$ to obtain (C2). Its left side is continuous, strictly increasing from zero to infinity, proving existence and uniqueness. Concavity makes this stationary point the global optimum. $\blacksquare$

Bisection provides an explicit certificate. Start with $\mu _l=0$ and $\mu _u=e^{2}+e$ $max_j$ $c_j$; the latter gives $\delta _j(\mu _u)\ge e$, hence $\sum \delta _j^{2}\ge e^{2}$. Maintain the bracket and stop when

\[
 \frac{\prod_j(c_j+\delta_j(\mu_u))}
      {\prod_j(c_j+\delta_j(\mu_l))}\le1+\varepsilon.
\]

The two products bracket $P_*$; use the upper product. To retain dataset-wise dominance over the old numerator even with a deliberately loose stopping tolerance, take its minimum with $P_{old}$. Both quantities are valid upper bounds. The stable formula $\delta _j=2\mu /(sqrt(c_j^{2}+4\mu )+c_j)$ avoids cancellation. Exact-arithmetic certification and the numerical stopping tolerance are different statements; the code records the achieved bracket ratio.

If $c_j=0$ for every j, $P_*=e^K/K^{K/2}$, whereas $P_{old}=e^K$. This is a deterministic bound on a particular input, not an asserted average efficiency factor.

## C4. A complete growing-dimension weak-bond theorem

Let $B_b=a$ $e_0^{\otimes K}+b$ $e_1^{\otimes K}$, $0\le b\le a$, in arbitrary dimensions $d_j\ge 3$. Fix $0<\alpha <1/2$ and $K\ge 3$. With $n\ge m+max(K,2)$ and $t_n=\sigma /\sqrt{n}$, the procedure above, including its optimized-numerator version, is globally honest over $\Theta _2$ and all $\sigma >0$ and satisfies

\[
 E_{B_b,\sigma}|I_n|\le C_{K,\alpha}
 t_n\min\{1,(t_n/b)^{K-1}\}. \tag{C3}
\]

The constant is independent of p, the $d_j$, a and b. At $b=0$ interpret the right side as C $t_n$. The corresponding pointwise optimal expected length under global honesty has the same order, with dimension-free lower constants. This combines the weak-bond theorem with growing ambient dimensions and requires neither a global tensor optimizer nor n>p.

**Proof of moments.** At $B_b$, all nonzero coefficients are in F, so $\tau _{B_b}=\sigma$. The compressed experiment has fixed dimension m. Conditional Gaussianity and the residual independence above reduce moments of $\|z-\theta \|$ and e to inverse moments of $\lambda _{min}(S)$, with $S\sim Wishart_m(n,I)$. For each diagonal entry of $S^{-1}$, the reciprocal has $\chi ^{2}_{n-m+1}$ law by residualizing one design column against the others. Its order k/2 inverse moment equals $2^{-k/2}Γ((n-m+1-k)/2)/Γ((n-m+1)/2)$, finite when n−m+1>k. Since $\lambda _{min}(S)^{-1}\le tr(S^{-1})$, sum-power inequalities give E $\lambda _{min}(S)^{-k/2}\le C_{m,k}n^{-k/2}$ for $2\le k\le K$; Jensen and the second moment give $k=1$. Positive moments of RSS/(n−m) are bounded, and F quantiles remain bounded for fixed $m,\alpha$ and $n-m\ge max(K,2)$. Hence $E(\|z-\theta \|+e)^k\le C_{K,\alpha }t_n^k$ for $k\le K$. The gamma-ratio bound follows from its finite limit after multiplication by $n^{k/2}$ and boundedness over the remaining finitely many admissible integer n; this is sufficient because m,K are fixed.

**Proof of length.** Put $T=\|z-\theta \|+e$. At $B_b$, $C_j(\theta )=0$ and each pivot's smallest singular value is b. On $T\le b/2$ the old interval length is at most $2^K$ $T^K/b^{K-1}$. On T>b/2, it is at most $2e\le 2T\le 2^K$ $T^K/b^{K-1}$. It is always at most 2e. Take expectations and the smaller of these two bounds. The optimized interval is no longer on every outcome. At $b=0$ the ambient bound suffices.

**Proof of lower bound.** Conditional on a design row, the two response means differ by $\langle x,B-B'\rangle$. The conditional normal KL is its square divided by $2\sigma ^{2}$; expectation over x gives $\|B-B'\|^{2}/(2\sigma ^{2})$, and independence multiplies this by n. Thus the full-data KL is $n\|B-B'\|^{2}/(2\sigma ^{2})$, regardless of ambient dimension. The feasible weak-component path in the rank-two proof gives target displacement $\Delta \psi$ at least a constant times t $min\{1,(t/b)^{K-1}\}$ at distance t. For a globally honest interval, under B the probability it contains both $\psi (B)$ and $\psi (B')$ is at least $1-2\alpha -TV(P_B,P_B')$: transport coverage of $\psi (B')$ from $P_B'$ to $P_B$, then use a union bound. Hence $E_B|I|\ge |\Delta \psi |[1-2\alpha -TV]$. Choose $t=(1-2\alpha )\sigma /\sqrt{n}$. Pinsker gives $TV\le (1-2\alpha )/2$, and the bracket is positive. Finally $f(ct,b)\ge c^K$ f(t,b) for $0<c\le 1$ and $f(t,b)=t$ $min\{1,(t/b)^{K-1}\}$. This proves the matching lower bound for every globally honest procedure, including procedures that use all covariates. $\blacksquare$

This is a prespecified-coordinate result. It does not prove that one procedure adapts at the same cost to every unknown rotation of $B_b$. The selected features are fixed parts of the procedure, not true directions supplied after observing the parameter. Global honesty nevertheless holds at rotated tensors; only the short-length assertion is restricted to the stated family.

## C5. Extension to other fixed cross patterns

For caps r, use fixed nonsingular crosses with target-slice coordinates disjoint from pivots and one another. The number of selected coordinates is at most

\[
 1+\sum_{k=1}^{K-1}r_k^2+\sum_{j=1}^K r_{j-1}r_j.
\]

The same coverage and optimized-numerator proofs apply. If all target slices vanish at a reference, the effective noise is $\tau _*^{2}=\sigma ^{2}+\|B_{*,F^c}\|^{2}$ and pivot strengths, rather than full unfolding singular values, control the interval's length. When these strengths are between $\gamma$ and $\kappa \gamma$ for fixed $\kappa$, the same proof gives an upper bound $C_{K,r,\alpha ,\kappa }(\tau _*/\sqrt{n})min\{1,(\tau _*/(\gamma \sqrt{n}))^{K-1}\}$. This is an upper bound; no general weak-pivot lower bound is asserted. A pivot can become small because a particular cross is poor even when the full unfolding remains well conditioned.

## Calibration status

Finite-sample F calibration, the numerator maximization and dataset-wise length dominance are proved. Exact optimal expected-length constants remain unknown. A sharper likelihood-ratio calibration is a separate problem; the existing cubic benchmark and generic minimum-distance literature do not establish a universal $\chi ^{2}_1$ reference distribution for all nonzero product targets.


\newpage

# D. Learned mode compression

Status: **PROVED** for the conditional and existence results stated here. A computationally efficient pilot at the displayed sample threshold and uniform adaptation through unidentified weak directions remain **PARTIAL**. These distinctions are necessary for publication-level claims.

## D1. Coverage after data-dependent mode compression

Use iid isotropic Gaussian regression and a deterministic unit product loading $A=\otimes w_j$. The parameter class is $\Theta _r(M)=\{B: TT ranks\le r, \|B\|\le M\}$. Split $n=n_1+n_2$ observations independently. From training data choose mode subspaces $V_j$ that contain $w_j$ and have dimensions at most $m_j$, with orthonormal bases $U_j$. Extend smaller subspaces by a measurable deterministic completion if needed. Write $U=\otimes U_j$ and $P=UU^T$.

Conditional on training, the inference regression in the $m=\prod dim(V_j)$ coordinates $U^Tx$ has coefficient $C=U^TB$ and unknown residual variance $\tau _B^{2}=\sigma ^{2}+\|(I-P)B\|^{2}$. Modewise linear maps do not increase any prefix rank, so C lies in the compressed TT class. The target is unchanged because $PA=A$. Use the unknown-variance F confidence ball in this regression and invert it over the compressed TT class intersected with $\|C\|\le M$. Take the smallest interval containing the resulting target values; if the feasible set is empty return {0}.

This interval is honest over every $B\in \Theta _r(M)$ and every $\sigma >0$ whenever $n_2>m$ and $0<\alpha <1$. The proof is conditional Gaussian independence plus inclusion of the true C on the confidence event. The feasible set is compact, because the rank constraints and ball are closed and bounded; extrema exist. Measurability follows by real algebraic elimination: unfolding-rank constraints are vanishing minors, norm constraints are polynomial inequalities, and the existence of a feasible C whose linear target exceeds a real number is a projection of a semialgebraic set. The Tarski–Seidenberg projection theorem makes this set semialgebraic and therefore Borel in its finite-dimensional inputs. This gives measurable extrema and, by semialgebraic selection, a measurable choice of the compact least-squares argmin in D3. Measurable orthogonal completions follow by Gram–Schmidt applied to the chosen vectors and then the coordinate basis, discarding zero residuals in a fixed order. The procedure has length at most 2M. It is a statistical existence construction: exact nonconvex confidence-region inversion has not been certified as polynomial-time.

## D2. Expected length with an explicit training event

Assume the reference $B_*$ has exact ranks r, satisfies $B_*\times _jw_j^T=0$ for all j, and its smallest nonzero bond singular values obey

\[
 b\le\beta_j\le\kappa b\quad\text{for all }j,
 \qquad b>0,\quad\kappa\ge1.
\]

The bounded ratio is an extra assumption. The geometric coefficient theorem does not require it, but it prevents a rare small-denominator fallback from being concealed inside a claimed uniform expected-length constant.

Suppose a training event G has probability at least $1-\delta$ and on G

\[
 \|(I-P)B_*\|\le r_0\le\min(b/2,\sigma).
\]

Then, for $n_2\ge m+max(K,2)$, the interval from D1 satisfies

\[
 E_{B_*,\sigma}|I_n|
 \le C_{K,m,\alpha,\kappa}
 \min\left\{\frac\sigma{\sqrt{n_2}},
 \frac{\sigma^K}{n_2^{K/2}\prod_j\beta_j}\right\}
       +2M\delta. \tag{D1}
\]

**Proof.** On G, $\tau _*\le \sqrt 2\sigma$. Since $P_j$ contains $w_j$, it commutes with $w_jw_j^T$, so $PB_*$ is still annihilated by contraction along $w_j$ in each mode. Weyl's inequality gives $|\beta _j(PB_*)-\beta _j(B_*)|\le r_0$. Thus the compressed tensor has the same exact ranks, $\beta _j(PB_*)\ge \beta _j/2$, and its weakest-bond ratio is at most $2\kappa +1$.

Condition on training in G. Let z,e be the compressed center and radius and $T=\|z-C_*\|+e$. If the inverted confidence region is nonempty, all its coefficients lie within T of $C_*$, so its target diameter is at most $2\omega _A(T;C_*)$. On $T\le \beta _{min}(C_*)/2$, the explicit general modulus bound gives at most $C_KT^K/\prod \beta _j(C_*)$. On the complementary event, $diameter\le 2T$, and

\[
 2T\le2^K T^K/\beta_{\min}(C_*)^{K-1}
 \le2^K(2\kappa+1)^{K-1}T^K/\prod_j\beta_j(C_*).
\]

It is also at most 2T on every outcome. The compressed Gaussian regression moments established in C4 give $ET^k\le C(\tau _*/\sqrt{n_2})^k$ up to $k=K$, proving the minimum of the two bounds on G. Integrate, and use $length\le 2M$ on $G^c$. $\blacksquare$

When $0<\alpha <1/2$ and $\sigma /\sqrt{n}\le c_Kb$, the general feasible-path theorem and the full-data Gaussian KL give a matching lower bound of order $\sigma ^K/(n^{K/2}\prod \beta _j)$, provided the reference is inside the norm cap with enough margin for the chosen local path. For example, assume $\|B_*\|\le M-\rho$ for a fixed $\rho >0$ and $t_n\le c\rho$. This lower bound does not require the bounded bond ratio. No general matching lower bound is asserted when $\sigma /\sqrt{n}$ is comparable to b outside the weak-component family.

## D3. A pilot supplying the training event

Let B̃ minimize training squared loss globally over $\Theta _r(M)$. This is a compact class, so a measurable minimizer exists. Put $s_j=min(d_j,r_{j-1}r_j)$. A TT tensor has mode-j matrix rank at most $s_j$, since separating its jth core from its left and right interfaces factors that matrix through a space of dimension $r_{j-1}r_j$.

Choose $V_j$ to contain both $w_j$ and the mode-j column space of B̃; then $dim(V_j)\le min(d_j,s_j+1)$, $P\widetilde B=\widetilde B$, and

\[
 \|(I-P)B_*\|\le\|B_*-\widetilde B\|.
\]

Set $q_j=min(d_j,2s_j)$, $e_K=\{16(K+1)\}^{-1}$, and

\[
 W=\log2+\left(\prod_jq_j\right)\log(1+2/e_K)
       +\sum_jd_jq_j\log(1+2\sqrt{q_j}/e_K).
\]

For x>0 and $n_1\ge 128(W+x)$,

\[
 P\{\|\widetilde B-B_*\|>18\sigma\sqrt{(W+x)/n_1}\}
       \le2e^{-x}. \tag{D2}
\]

Here are the steps of the tail proof, included to specify the rank and dimension factors. A difference of two feasible tensors has mode ranks at most $q_j$. Every unit tensor in this Tucker envelope has a unit core of dimension $\prod q_j$ and orthonormal $d_j\times q_j$ factors. Euclidean/Frobenius $e_K-nets$ on the core sphere and Stiefel factors have total cardinality N with $\operatorname{log}(2N)\le W$ by volume packing. Replacing factors and core successively creates K+1 error terms, each in the same Tucker envelope and with norm at most $e_K$. Any linear-map supremum is therefore bounded by its net maximum plus 1/16 of the same supremum.

For each net point, $\|XH\|^{2}$ is $\chi ^{2}_{n_1}$. The bound $P\{| \|XH\|^{2}/n_1-1 |>1/4\}\le 2exp(-n_1/128)$ and a union bound give net norms between 3/4 and 5/4 after division by $\sqrt{n_1}$, outside probability $e^{-x}$. The 1/16 extension gives restricted norms between 2/3 and 4/3 for the full envelope. Conditional on this event, Gaussian noise and a second union bound give a scalar net maximum $|\epsilon ^TXH|/(\sigma \sqrt{n_1})\le (4/3)\sqrt {2(W+x)}$ outside probability $e^{-x}$; extension bounds the full maximum by $4\sqrt (W+x)$. The least-squares inequality $\|X\Delta \|^{2}\le 2\epsilon ^TX\Delta$ then gives $(4/9)n_1\|\Delta \|^{2}\le 8\sigma \sqrt {n_1(W+x)}\|\Delta \|$. Division yields (D2). This proof does not assume an algorithm reaches the global minimizer.

It is sufficient for the event in D2 to imply G that

\[
 n_1\ge\max\{128,324,1296\sigma^2/b^2\}(W+x).
\]

Combine with D1 and $\delta =2e^{-x}$. For fixed K,r, W is at most a constant times $1+\sum d_j$, even though $p=\prod d_j$ can grow much faster. The inference dimension is at most $\prod min(d_j,s_j+1)$, also bounded for fixed K,r. Choose x of logarithmic order to make $4Me^{-x}$ smaller than the desired expected-length scale. If b or $\sigma$ varies with n, state that choice explicitly rather than silently absorbing it into a constant.

## D4. Interpretation of the combined result

There are now two distinct complete growing-dimension results. The selected-cross theorem is computationally explicit and valid through $b≈\sigma /\sqrt{n}$ for a prespecified-coordinate weak-component family. The learned-subspace theorem handles unknown orientations and general physically normal TT references, but its rate guarantee requires accurate learning of the weak directions. Its sufficient condition includes $n_1b^{2}/\sigma ^{2}$ of order W+x.

For growing W, that condition does not reach $b≈\sigma /\sqrt{n}$ with a proportional split. The intermediate regime $\sigma /\sqrt{n}\ll b\lesssim \sigma \sqrt {W/n}$ remains a real statistical question. The current proof neither establishes a necessary dimension penalty nor proves adaptation impossible there. A lower bound must compare one globally honest procedure across many orientations; a two-point argument at one known orientation does not suffice.

Practical alternatives such as TT-SVD initialization followed by IHT or Riemannian descent need their own assumptions and tail bounds. Existing estimation papers are candidates, not a license to call a local numerical optimizer a global minimizer. Prespecified-support results and learned-support results should remain separate in the manuscript until that issue is resolved.


\newpage

# E. Minimum-distance calibration: established and partial results

The finite-sample F calibration and optimized cross numerator are implemented in the revision. This note records additional exact facts for minimum-distance testing and a rigorous route to numerical certification. It does not claim that sharp product-mean confidence intervals have been solved.

## M1. Exact worst-case calibration for the zero-product null

Observe $Z\sim N_K(h,I)$, test $H_0:\prod h_j=0$, and use $T_0(Z)=inf_{u:\prod u_j=0}\|Z-u\|^{2}$. The null is a union of coordinate hyperplanes, so

\[
 T_0(Z)=\min_j Z_j^2.
\]

At least one coordinate $h_j$ is zero under the null. Therefore $P_h(T_0>c)\le P(G^{2}>c)$. Let that coordinate remain zero and all other $|h_i|\to \infty$. Independence gives convergence of the rejection probability to $P(G^{2}>c)$. The exact worst-case $level-\alpha$ critical value is $\chi ^{2}_{1,1-\alpha }$. At $h=0$ the rejection probability is $\alpha ^K$, not $\alpha$. This proves that high boundary coverage can coexist with optimal worst-case calibration of this particular statistic. It does not justify $\chi ^{2}_1$ for nonzero product targets or for $h_1h_2h_3+\kappa h_1$ when $\kappa ≠0$.

## M2. A finite computation certificate for a general target null

Let $g:R^K\to R$ be continuous with nonempty closed level set $H_\theta =\{h:g(h)=\theta \}$, and $T_\theta (z)=\operatorname{dist}(z,H_\theta )^{2}$. Fix $\beta ,\eta >0$ with $\beta +\eta <\alpha$ before examining the data. Let $C_\beta (Z)$ be a confidence set for the full mean with coverage at least $1-\beta$; for example the Gaussian ball of radius $sqrt(\chi ^{2}_{K,1-\beta })$.

Suppose a finite collection of centers $h_1,...,h_N$ covers $C_\beta (Z)∩H_\theta$ within Euclidean distance $\rho$. Centers need not be on the null. Suppose the following two computational bounds are available:

1. A certified lower bound $L\le T_\theta (Z)$.
2. For each fresh simulation $Z_{jl}\sim N(h_j,I)$, a certified upper bound $U_{jl}\ge T_\theta (Z_{jl})$.

The simulations must be independent of observed Z conditional on their data-dependent centers. Fix their sample count $N_{MC}$ and the bounding algorithm conditional on the observed data and centers, so each center supplies identically distributed Bernoulli trials. Adaptive stopping requires a separate anytime-valid bound. Let $q_j$ be an upper Clopper–Pearson bound with error probability $\eta /N$ for the Bernoulli success count $\sum _l$ $1\{U_{jl}\ge L\}$. Define

\[
 p_{\mathrm{cert}}=
 \min\left\{1,\max_jq_j+
             2\Phi(\rho/2)-1+\beta+\eta\right\}. \tag{M1}
\]

If the intersection is empty, use $p_{cert}=\beta +\eta$, provided emptiness itself is certified; otherwise retain a conservative value such as one. Then rejection when $p_{cert}\le \alpha$ has type-I error at most $\alpha$ for every $h\in H_\theta$, jointly over data and calibration randomness.

**Proof.** With probability at least $1-\beta$ the true h lies in $C_\beta (Z)∩H_\theta$. Conditional on observed Z, simultaneous Clopper–Pearson coverage fails with probability at most $\eta$ by the union bound. On their intersection, choose a center $h_j$ with $\|h-h_j\|\le \rho$. Gaussian laws with identity covariance have total variation distance $2\Phi (\|h-h_j\|/2)-1$: the likelihood-ratio comparison depends only on the projection along their mean difference, and the two one-dimensional Gaussian half-space probabilities give this formula. Thus

\[
 \begin{aligned}
 P_h\{T_\theta(Z')\ge T_\theta(Z)\}
 &\le P_h\{T_\theta(Z')\ge L\}\\
 &\le P_{h_j}\{T_\theta(Z')\ge L\}+2\Phi(\rho/2)-1\\
 &\le q_j+2\Phi(\rho/2)-1.
 \end{aligned}
\]

The first quantity is a super-uniform tail p-value under h, including atoms if present. Rejection on the two successful events implies that this p-value is at most $\alpha -\beta -\eta$. Add their failure probabilities $\beta$ and $\eta$. $\blacksquare$

This is a specialization of the confidence-set maximization principle associated with Berger–Boos, with explicit discretization, simulation and optimization errors. It is not a novel general p-value construction. For the cubic target, certified constrained-distance bounds and an efficient covering of the null intersection still need implementation. A local optimizer provides a feasible-point upper bound on distance, which is the wrong direction for L. Using it as an observed-distance lower bound can invalidate the test.

The theorem is per tested $\theta$. To make a jointly computed confidence interval, one must also certify its inversion over the continuum of $\theta$; a finite grid followed by unqualified endpoint interpolation is insufficient. Pointwise valid tests give coverage at the true $\theta$, but numerical interpolation has to preserve their acceptance set.

## Current status

- **PROVED and implemented elsewhere:** finite-sample F calibration of selected-coordinate regression, optimized numerator with a one-dimensional root bracket, and no-longer-than-baseline intervals.
- **PROVED:** zero-product worst-case $\chi ^{2}_1$ calibration and the conditional numerical certificate M2.
- **PARTIAL:** efficient nonzero-target minimum-distance calibration and its interval inversion. The certificate specifies what must be bounded, but does not supply an efficient cubic optimizer.
- **OPEN:** exact optimal expected length, or a small certified ratio to that optimum. The previous analytic brackets 3.61839 and 34.94889 remain brackets in a separate Gaussian experiment.
