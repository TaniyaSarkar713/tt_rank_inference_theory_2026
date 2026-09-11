---
title: "Unequal Bond Strengths and Partial Rank Loss in Honest Tensor-Train Inference"
subtitle: "Proof addendum to the 9 September 2026 manuscript"
date: "11 September 2026"
fontsize: 11pt
geometry: margin=1in
mainfont: DejaVu Serif
sansfont: DejaVu Sans
monofont: DejaVu Sans Mono
colorlinks: true
toc: true
toc-depth: 2
---

# Purpose and scope

This addendum proves an all-radius modulus for fully normal product loadings
with unequal TT bond strengths. It derives matching fixed-dimensional honest
length, removes the balanced-gap premise from the learned-compression bound,
and gives a computable 23-feature interval for an explicit single-cut rank loss.
The existing September 9 manuscript supplies the finite-radius normal-modulus
bound, Gaussian OLS moments, and training-pilot result used here.

Proof status is internal. Unknown weak orientations, general loadings, optimal
confidence constants, and an efficient general pilot remain unresolved. The new
checks are algebraic falsification checks, not a Monte Carlo coverage study.


\newpage

# Unequal-bond moduli and partial rank loss

Development date: 11 September 2026. **PROVED** below means a complete internal derivation, not independent review. This note extends the September 9 general-normal theorem without altering its archived statement. Statistical consequences are in [unequal-bond inference](../../theory/unequal_bond_inference.md).

## U1. A uniform modulus at every localization radius

Fix order $K\ge2$ and positive caps $r=(r_1,\ldots,r_{K-1})$. Let $B^{[j]}$ group the first $j$ modes as rows and the others as columns, and define $\Theta_r=\{B:\operatorname{rank}(B^{[j]})\le r_j\ \forall j\}$. For a unit product loading $A=\bigotimes_{j=1}^K w_j$, set $\omega_A(t;B_*)=\sup\{|\langle A,B-B_*\rangle|:B\in\Theta_r,\ \|B-B_*\|_F\le t\}$. Suppose $B_*\in\Theta_r$ satisfies

$$B_*\times_j w_j^T=0\quad(j=1,\ldots,K).$$

First suppose the reference has exact ranks $r$. Write $\beta_j=\sigma_{r_j}(B_*^{[j]})>0$ and define

$$F(t;\beta)=t\prod_{j=1}^{K-1}\min\{1,t/\beta_j\},\qquad t>0.$$

There are explicit positive constants depending only on $K$ such that, for **every** $t>0$,

$$c_K F(t;\beta)\le\omega_A(t;B_*)\le C_K F(t;\beta),\tag{U1}$$

where one valid choice is

$$c_K=(2^{1/K}-1)^{K/2},\qquad
C_K=2^{K-1}\max_{1\le J\le K}
\left(\frac{1+\binom J2}{J}\right)^{J/2}.$$

The constants are independent of dimensions, ranks, reference norm, and ratios between the bond singular values. No claim is made that these two constants are optimal. When $t/\min_j\beta_j\to0$, the existing sharp result remains

$$\omega_A(t;B_*)\sim K^{-K/2}F(t;\beta).$$

For a rank-deficient reference, define $\beta_j=\sigma_{r_j}(B_*^{[j]})\ge0$ and interpret the corresponding factor in $F$ as one when $\beta_j=0$. The same conclusion holds provided that the exact-rank-$r$ stratum is nonempty inside $\bigotimes_j w_j^\perp$. This complementary-space admissibility condition is automatic at an exact-rank reference; it is an explicit additional premise for the boundary extension.

### Upper bound: retain the cuts that are strong at radius $t$

Let $S=\{j:\beta_j\ge2t\}$ and $J=|S|+1$. Group consecutive physical modes into $J$ blocks, cutting only at indices in $S$. Frobenius distance is unchanged by this reshaping. Every original feasible tensor belongs to the relaxed grouped TT class, whose caps are $(r_j:j\in S)$. The grouped reference has exact ranks at these retained cuts, even if some discarded cuts are rank deficient. Its retained singular values are exactly $(\beta_j:j\in S)$.

The loading on a block is the product of its original loading vectors. Contracting the reference with that block loading gives zero: it includes contraction with at least one of the original $w_j$. Thus the grouped loading satisfies the same physical-normality condition.

If $J=1$, use $\omega_A(t;B_*)\le t$. If $J\ge2$, apply the finite-radius upper bound G2 in [the September 9 general-normal note](../../theory/general_normal_modulus.md) to the grouped tensor. Every retained gap is at least $2t$, so its overlap term is at most $t^2\binom J2$ and each denominator is at least half its reference singular value. Therefore

$$\omega_A(t;B_*)\le
2^{J-1}\left(\frac{1+\binom J2}{J}\right)^{J/2}
\frac{t^J}{\prod_{j\in S}\beta_j}.$$

For a discarded cut, $\min\{1,t/\beta_j\}\ge1/2$, including the convention at zero. Consequently

$$F(t;\beta)\ge 2^{-(K-J)}\frac{t^J}{\prod_{j\in S}\beta_j}.$$

Combining the last two inequalities gives the asserted $C_K$. The same comparison with $J=1$ covers the case of no retained cuts. Importantly, grouping is used only to obtain an upper bound; it does not assert that all grouped feasible perturbations satisfy the original caps.

### Lower bound: a perturbation satisfying every original cap

For now all $\beta_j$ are positive. Rotate physical coordinates so that $w_j$ is the last coordinate vector. Take a left-orthonormal TT representation $G_1,\ldots,G_K$ of $B_*$. For $j<K$, let $R_j$ be its right interface,

$$Q_j=(R_jR_j^T)^{1/2},\qquad Q_jv_j=\beta_jv_j,\qquad\|v_j\|=1.$$

The left interface is an isometry, so the eigenvalues of $Q_j$ are the nonzero singular values of $B_*^{[j]}$. Define rank-one matrices of Frobenius norm one by

$$Z_1=v_1^T,\qquad Z_j=v_{j-1}v_j^T\ (1<j<K),\qquad Z_K=v_{K-1},$$

and $H_j=Z_jQ_j^{-1}$ for $j<K$, $H_K=Z_K$. These have

$$\|H_j\|_{\mathrm{op}}=\beta_j^{-1},\qquad
\|H_jR_j\|_F=1\quad(j<K).$$

The reference target slice of every core is zero: full physical contraction equals $L_{j-1}G_j(w_j)R_j$, and both interfaces have full relevant rank. Put $h_K=\sqrt{2^{1/K}-1}$ and choose the **different** perturbation sizes

$$x_j=h_K\min\{t,\beta_j\}\quad(j<K),\qquad x_K=h_Kt.$$

Replace only the zero target slice of core $j$ by $x_jH_j$. Denote the resulting tensor by $B_x$. Its TT core sizes have not changed, so $B_x\in\Theta_r$ at every $t$.

Expand $B_x-B_*$ by nonempty subsets $T$ of replaced cores. The terms $V_T$ are orthogonal, since they use $w_j$ at exactly the sites in $T$ and $w_j^\perp$ elsewhere. If $\ell=\max T$, left isometry of intervening unchanged cores and the right-interface identity at the last changed core give

$$\|V_T\|_F\le x_\ell\prod_{i\in T,\ i<\ell}\frac{x_i}{\beta_i}
\le h_K^{|T|}t.$$

This estimate applies also when $\ell=K$, using $\|H_K\|_F=1$. Hence

$$\|B_x-B_*\|_F^2
=\sum_{T\ne\varnothing}\|V_T\|_F^2
\le t^2\{(1+h_K^2)^K-1\}=t^2.$$

The target contraction uses every new slice. The adjacent vectors $v_j$ align exactly, so

$$\langle A,B_x-B_*\rangle
=\frac{\prod_{j=1}^Kx_j}{\prod_{j=1}^{K-1}\beta_j}
=h_K^K F(t;\beta)=c_K F(t;\beta).$$

This proves the uniform lower bound in the **original** TT class. It does not require the gaps to be comparable or $t$ to be smaller than the weakest one.

### Boundary extension and its premise

Assume the exact-rank stratum is nonempty in the complementary physical space. Represent $B_*$ there with padded core sizes $r$, and choose another such core tuple representing an exact-rank tensor. Interpolate the two core tuples linearly in a scalar $u$. For each cut, choose a rank-$r_j$ minor that is nonzero at $u=1$. Each chosen minor is a nonzero polynomial in $u$. Avoiding their finitely many roots gives exact-rank tensors $B_u\to B_*$, all still physically normal.

Write $\delta_u=\|B_u-B_*\|_F$. For $\delta_u<t$, apply the proved lower construction at $B_u$ with radius $t-\delta_u$. Its witness lies within distance $t$ of $B_*$. All reference target values are zero. Singular-value continuity and

$$\min\{1,(t-\delta_u)/\beta_j(B_u)\}\longrightarrow
\begin{cases}\min\{1,t/\beta_j(B_*)\},&\beta_j(B_*)>0,\\1,&\beta_j(B_*)=0\end{cases}$$

give the same lower bound at $B_*$. The upper bound already covers this case. No assertion is made here for boundary caps that cannot be attained in the complementary physical space.

## U2. Interpretation and scaling inequalities

Each gap much larger than $t$ contributes a factor $t/\beta_j$. A gap below the localization scale contributes only a constant-order factor. In particular, one vanishing cut need not restore the ambient linear modulus: the remaining strong cuts can still force higher-order contact.

For $s>0$,

$$F(st;\beta)\le\max\{s,s^K\}F(t;\beta),$$

and for $0<c\le1$,

$$F(ct;\beta)\ge c^K F(t;\beta).\tag{U2}$$

These follow factor by factor from the clipped product and hold when some gaps are zero. Also, if $\beta'_j\ge\beta_j/2$ for every $j$, then $F(t;\beta')\le2^{K-1}F(t;\beta)$. These elementary inequalities are the reason the statistical argument no longer needs a bound on $\max\beta_j/\min\beta_j$.

For fixed noise scale and an actual feasible reference sequence with $\beta_{j,n}\asymp n^{-\gamma_j}$, substitution of $t_n\asymp n^{-1/2}$ yields

$$F(t_n;\beta_n)\asymp
n^{-\{1/2+\sum_j(1/2-\gamma_j)_+\}}.$$

This statement evaluates feasible tensors; it does not claim arbitrary prescribed TT singular spectra can be realized. Such feasibility has its own constraints; see [Krämer, arXiv:1701.08437](https://arxiv.org/abs/1701.08437).

## U3. An explicit four-mode example with only one weak cut

In dimensions at least three and caps $(2,2,2)$, put

$$B_\varepsilon=e_0^{\otimes4}
+e_0\otimes e_1^{\otimes3}
+\varepsilon e_1\otimes e_0^{\otimes3},\qquad
A=e_2^{\otimes4},\quad 0\le\varepsilon\le1.$$

At the first cut, the nonzero matrix in orthonormal bases is
$\left(\begin{smallmatrix}1&1\\\varepsilon&0\end{smallmatrix}\right)$, so

$$b_\varepsilon=\beta_1
=\varepsilon\sqrt{\frac{2}{2+\varepsilon^2+\sqrt{4+\varepsilon^4}}}
\sim\varepsilon/\sqrt2.$$

At the other two cuts, the two nonzero singular values are $\sqrt{1+\varepsilon^2}$ and $1$. Thus $\beta_2=\beta_3=1$, and U1 gives

$$\omega_A(t;B_\varepsilon)\asymp
t\min\{1,t/b_\varepsilon\}\min\{1,t\}^2.\tag{U3}$$

For small $t$ this changes from order $t^4/b_\varepsilon$ to order $t^3$, rather than to order $t$. The four-mode exact-rank sharp coefficient is still $1/16$ when $t/b_\varepsilon\to0$.

At $\varepsilon=0$ there is also an exact **cubic leading coefficient**:

$$\omega_A(t;B_0)\sim\frac{t^3}{3^{3/2}}\qquad(t\to0).\tag{U4}$$

For the upper bound group modes $(1,2),3,4$. The three grouped signal and loading directions are orthogonal, and the retained gaps equal one, so the three-mode sharp theorem gives this upper coefficient. For attainability in the original class use

$$B_0(u)=e_0^{\otimes4}
+(e_0\otimes e_1+u e_2\otimes e_2)
\otimes(e_1+u e_2)\otimes(e_1+u e_2).$$

Its first-mode space lies in $\operatorname{span}(e_0,e_2)$; the other two prefix unfoldings are sums of two rank-one matrices. Thus every original rank is at most two. Direct orthogonality gives

$$\|B_0(u)-B_0\|_F^2=(1+u^2)^3-1,\qquad
\langle A,B_0(u)\rangle=u^3.$$

Taking $u^2=(1+t^2)^{1/3}-1$ proves the sharp lower coefficient. This concrete witness also shows why simply adding an arbitrary product perturbation at one slack cut would not be a valid proof.

## Dependencies and remaining limits

The upper proof uses the established finite-radius G2 bound after grouping. The lower proof changes its equal-size core perturbation into independently capped sizes; the boundary argument uses polynomial minors. TT core parametrizations and cross identities are established tools, as documented in the [reference guide](../../references/README.md). No independent novelty review has certified this extension.

This resolves unequal-bond **rate geometry for fully normal product loadings**, with the stated premise at exact boundaries. It does not resolve arbitrary loadings, exact confidence constants, or adaptation to unknown weak orientations.


\newpage

# Honest inference with unequal weak bonds

Development date: 11 September 2026. **PROVED** denotes complete internal derivations. The geometric input is [U1–U4](../../theory/unequal_bond_modulus.md). This note proves general fixed-dimensional attainment, removes the balanced-bond premise from the learned-compression bound, and gives a computable 23-feature interval for a single-cut rank loss. It does not solve unknown-orientation adaptation near the noise scale.

## V1. General fixed-dimensional honest length

Observe independent isotropic Gaussian regressions

$$Y_i=\langle X_i,B\rangle+\epsilon_i,
\qquad \operatorname{vec}(X_i)\sim N_p(0,I_p),\qquad
\epsilon_i\sim N(0,\sigma^2),$$

with unknown $\sigma>0$. The errors and designs are independent. Fix a unit product loading $A$ and caps $r$ before observing data. An interval $I_n$ is honest if $P_{B,\sigma}\{\langle A,B\rangle\in I_n\}\ge1-\alpha$ for every $B\in\Theta_r$ and $\sigma>0$. Write $L_{\alpha,n}(B_*;\sigma)$ for the infimum of $E_{B_*,\sigma}|I_n|$ over all such measurable intervals; the class $\Theta_r$ is unbounded.

Let $B_*$ satisfy U1, including its complementary-space admissibility premise if it is rank deficient. For $0<\alpha<1/2$, $n\ge p+\max(K,2)$, and $t_n=\sigma/\sqrt n$,

$$L_{\alpha,n}(B_*;\sigma)\asymp_{K,p,\alpha}
F(t_n;\beta),\qquad
F(t;\beta)=t\prod_{j=1}^{K-1}\min\{1,t/\beta_j\}.\tag{V1}$$

Zero gaps contribute a factor one. There is no gap-ratio restriction, no reference norm cap, and no requirement that $t_n$ be below every gap. The upper construction is confidence-set inversion and is not claimed to run in polynomial time.

### Upper proof

Let $z$ be full OLS, $\widehat\sigma^2$ its residual variance, and $S=X^TX$. Use the existing unknown-variance confidence radius

$$e=\widehat\sigma
\sqrt{\frac{p F_{p,n-p;1-\alpha}}{\lambda_{\min}(S)}}.$$

Conditionally on the design, the usual $F$ ellipsoid contains $B$ with probability $1-\alpha$ and implies $\|z-B\|_F\le e$. Intersect this Euclidean ball with $\Theta_r$ and report the smallest interval containing all its target values, using $\{0\}$ if the intersection is empty. The intersection is compact even though $\Theta_r$ is unbounded: it is closed and contained in the finite-radius ball. Its extrema are measurable by the same semialgebraic argument used in the September 9 compression proof. True-parameter inclusion proves global honesty.

Put $T=\|z-B_*\|_F+e$. The target diameter is at most $2\omega_A(T;B_*)$. U1 and U2 give

$$|I_n|\le2C_KF(T;\beta)
\le2C_KF(t_n;\beta)
\left\{T/t_n+(T/t_n)^K\right\}.$$

The OLS/inverse-Wishart moment proof in [C4](../../theory/certified_cross_inference.md) gives $E T^k\le C_{K,p,\alpha}t_n^k$ for $k=1,K$ under the displayed sample threshold. Taking expectations proves the upper bound at every radius, including samples that cross some rank boundaries. There is no separate fallback estimate involving only the smallest gap.

### Lower proof

Put $c=1-2\alpha>0$. U1 provides an alternative $B'\in\Theta_r$ with distance at most $ct_n$ and target separation at least $c_KF(ct_n;\beta)$. If a supremum is not attained, use arbitrarily close witnesses and take a limit. The full-data Gaussian KL divergence is at most $c^2/2$, so total variation is at most $c/2$. For any globally honest interval, transport its coverage at $B'$ to $B_*$ and apply a union bound. The interval contains both target values with probability at least $1-2\alpha-c/2=c/2$. Thus

$$E_{B_*,\sigma}|I_n|
\ge\frac{c}{2}c_KF(ct_n;\beta)
\ge\frac{c_Kc^{K+1}}2F(t_n;\beta).$$

This bound allows a competitor to use all covariates. Fixing $\sigma$ for the comparison is legitimate because honesty was required over every $\sigma$.

## V2. Learned compression without balanced gaps

Use the bounded class $\Theta_r(M)$ and independent training/inference split from [D1](../../theory/growing_dimension_general_tt.md). The training procedure chooses a product projection $P$ containing every loading direction; let its compressed dimension be a deterministic $m$, using measurable completion as in D1. Suppose the reference has exact ranks $r$, is fully physically normal, and a training event $G$ satisfies

$$P(G)\ge1-\delta,\qquad
\|(I-P)B_*\|_F\le\min\{\beta_{\min}/2,\sigma\}\quad\text{on }G.$$

For $n_2\ge m+\max(K,2)$ the same inverted compressed confidence ball is globally honest and now obeys

$$E|I_n|\le C_{K,m,\alpha}
F(\sigma/\sqrt{n_2};\beta)+2M\delta.\tag{V2}$$

Unlike the earlier D2 statement, the constant contains no balance parameter $\kappa$ and the rate retains every individual gap.

**Proof.** Conditional on training, the effective variance is
$\tau_*^2=\sigma^2+\|(I-P)B_*\|_F^2$. On $G$, $\tau_*\le\sqrt2\sigma$. Loading inclusion preserves physical normality, and Weyl's inequality gives the same exact ranks and compressed gaps $\beta'_j\ge\beta_j/2$. Apply the V1 upper proof conditionally to the compressed reference and use the factorwise inequality $F(t;\beta')\le2^{K-1}F(t;\beta)$. The moment constants depend only on $K,m,\alpha$; the variance inflation contributes at most a factor $2^{K/2}$. On $G^c$, the norm cap bounds length by $2M$. Integration proves V2. Coverage still holds conditional on every training outcome and does not require $G$.

The previous global least-squares pilot can supply this event under its existing condition

$$n_1\ge\max\{128,324,1296\sigma^2/\beta_{\min}^2\}(W+x),
\qquad\delta=2e^{-x}.$$

For a reference with $\|B_*\|\le M-\rho$ and $ct_n\le\rho$, the V1 lower witness lies in the norm cap. Hence proportional splits and a negligible $2M\delta$ term give matching orders wherever the learning condition holds. The condition on $n_1\beta_{\min}^2/\sigma^2$ remains dimension dependent; removing $\kappa$ does **not** establish adaptation to unidentifiable weak orientations.

## V3. An explicit interval with 23 selected features

Take the four-mode family U3, $0\le\varepsilon\le1$, $A=e_2^{\otimes4}$, arbitrary physical dimensions at least three, and global class $\Theta_{(2,2,2)}$. Directions and the following coordinate pattern are fixed before sampling. The procedure does not receive $\varepsilon$.

Write multi-indices as strings. Choose prefix and suffix sets

$$\begin{array}{c|c|c}
k&P_k&Q_k\\\hline
1&\{0,1\}&\{000,111\}\\
2&\{00,01\}&\{00,11\}\\
3&\{000,011\}&\{0,1\}.
\end{array}$$

The pivot matrices $S_k(B)=B(P_k,Q_k)$ satisfy

$$S_1(B_\varepsilon)=
\begin{pmatrix}1&1\\\varepsilon&0\end{pmatrix},\qquad
S_2(B_\varepsilon)=S_3(B_\varepsilon)=I_2.$$

There are two valid cross identities for the target:

1. The full four-mode identity, with slices
$C_1=B(2,Q_1)$, $C_2=B(P_1,2,Q_2)$, $C_3=B(P_2,2,Q_3)$, $C_4=B(P_3,2)$ and all three pivots.
2. The three-block identity for grouped modes $(1,2),3,4$, with slices $D_1=B(22,Q_2)$, $D_2=C_3$, $D_3=C_4$ and pivots $S_2,S_3$.

Each identity follows from the standard exact TT-cross formula when its pivots are invertible. The grouped class contains the original class. All these target slices vanish at $B_\varepsilon$.

Let $\mathcal F$ be the union of pivot coordinates, slice coordinates, and the target $2222$. There are **23 distinct coordinates**: eight pivot entries, twelve full-pattern slice entries, two additional entries in $D_1$, and one target. All three nonzero reference coefficients belong to $\mathcal F$.

Regressing $Y$ on these selected Gaussian features gives

$$Y=W\theta+\xi,\quad \theta=B_{\mathcal F},\quad
\xi\mid W\sim N_n(0,\tau_B^2I_n),\quad
\tau_B^2=\sigma^2+\|B_{\mathcal F^c}\|_F^2.$$

For $n>23$ compute selected OLS $z$, residual standard deviation $\widehat\tau$, and the common $F$ radius $e$ with dimension 23. Set $I_a=[z_A-e,z_A+e]$ and $d_k=\sigma_{\min}(S_k(z))-e$.

For each pattern whose required $d_k$ are all positive, form

$$H_4=\frac{\prod_{j=1}^4(\|C_j(z)\|_F+e)}{d_1d_2d_3},\qquad
H_3=\frac{\prod_{j=1}^3(\|D_j(z)\|_F+e)}{d_2d_3}.$$

For an uncertified pattern take its $H$ to be $+\infty$. Return

$$I=I_a\cap[-H_4,H_4]\cap[-H_3,H_3],$$

using $\{z_A\}$ if the intersection is empty. The optimized shared-budget numerator C3 may replace either product without weakening the guarantee, but the new implementation uses the displayed simple products to keep the proof-to-code correspondence direct.

### Coverage and rate

On the common event $\|z-\theta\|\le e$, every certified pivot is truly invertible and each certified cross bound contains the target. The ambient interval also contains it. Intersecting the two bounds therefore needs no extra error-probability split. Global finite-sample coverage is at least $1-\alpha$ for every original-class tensor and every unknown variance.

At $B_\varepsilon$, put $T=\|z-\theta\|+e$ and $b=b_\varepsilon\le1$. Each estimated slice norm plus $e$ is at most $T$. If $T\le1/2$, the grouped denominators are at least $1/2$, so length is at most $8T^3$. If $T>1/2$, the ambient bound $2e\le2T\le8T^3$ gives the same conclusion. Thus the grouped interval gives a cubic bound on **every** outcome.

For $b>0$, on $T\le b/2$ the full-pattern bound is at most $16T^4/b$. On $T>b/2$, the already established cubic bound implies $8T^3\le16T^4/b$. Consequently, on every outcome,

$$|I|\le\min\{2T,8T^3,16T^4/b\}.\tag{V3a}$$

At $b=0$ omit the last expression. Because the selected coordinates contain all reference signal, $\tau_{B_\varepsilon}=\sigma$. The selected OLS moment bounds through degree four hold for $n\ge23+4=27$. Taking expectations of each bound gives

$$E_{B_\varepsilon,\sigma}|I|
\le C_\alpha\,t_n\min\{1,t_n/b_\varepsilon\}\min\{1,t_n\}^2.\tag{V3b}$$

The V1 lower argument applied to U3 proves a matching lower bound for every globally honest competitor, including competitors using the full ambient design. Constants are independent of $\varepsilon$ and the physical dimensions. For $t_n\ll1$, the transition is

$$\frac{\sigma^4}{b_\varepsilon n^2}
\quad\text{when }b_\varepsilon\gg t_n,
\qquad
\frac{\sigma^3}{n^{3/2}}
\quad\text{when }b_\varepsilon\lesssim t_n.$$

The latter includes the exact rank loss $\varepsilon=0$. This is a quartic-to-cubic example with only the first cut losing rank. It does not demonstrate orientation-free adaptation or optimal confidence constants.

## Computational statement and validation scope

The 23-feature procedure is implemented in [methods.py](../../simulations/code/unequal_bonds/methods.py). Forming the fixed-dimensional regression Gram matrix costs $O(n\,23^2)$ arithmetic operations, solving it costs $O(23^3)$, and each cross certificate uses fixed-size $2\times2$ singular values. These counts exclude acquisition of the original observations; the algorithm only requests the selected features. V1 inversion and the global pilot in V2 remain existence constructions.

The accompanying [check script](../../simulations/code/unequal_bonds/check_theory.py) checks algebraic witnesses, singular values, grouping bounds, both cross identities, deterministic target inclusion on constructed confidence-ball events, and the outcome-wise length bound. These are numerical falsification checks, not empirical coverage estimates or a formal floating-point proof. No new Monte Carlo coverage study is asserted.
