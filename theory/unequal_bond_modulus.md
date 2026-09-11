# Unequal-bond moduli and partial rank loss

Development date: 11 September 2026. **PROVED** below means a complete internal derivation, not independent review. This note extends the September 9 general-normal theorem without altering its archived statement. Statistical consequences are in [unequal-bond inference](unequal_bond_inference.md).

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

If $J=1$, use $\omega_A(t;B_*)\le t$. If $J\ge2$, apply the finite-radius upper bound G2 in [the September 9 general-normal note](general_normal_modulus.md) to the grouped tensor. Every retained gap is at least $2t$, so its overlap term is at most $t^2\binom J2$ and each denominator is at least half its reference singular value. Therefore

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

The upper proof uses the established finite-radius G2 bound after grouping. The lower proof changes its equal-size core perturbation into independently capped sizes; the boundary argument uses polynomial minors. TT core parametrizations and cross identities are established tools, as documented in the [reference guide](../references/README.md). No independent novelty review has certified this extension.

This resolves unequal-bond **rate geometry for fully normal product loadings**, with the stated premise at exact boundaries. It does not resolve arbitrary loadings, exact confidence constants, or adaptation to unknown weak orientations.
