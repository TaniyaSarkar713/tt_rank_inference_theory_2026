# Honest inference with unequal weak bonds

Development date: 11 September 2026. **PROVED** denotes complete internal derivations. The geometric input is [U1–U4](unequal_bond_modulus.md). This note proves general fixed-dimensional attainment, removes the balanced-bond premise from the learned-compression bound, and gives a computable 23-feature interval for a single-cut rank loss. It does not solve unknown-orientation adaptation near the noise scale.

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

The OLS/inverse-Wishart moment proof in [C4](certified_cross_inference.md) gives $E T^k\le C_{K,p,\alpha}t_n^k$ for $k=1,K$ under the displayed sample threshold. Taking expectations proves the upper bound at every radius, including samples that cross some rank boundaries. There is no separate fallback estimate involving only the smallest gap.

### Lower proof

Put $c=1-2\alpha>0$. U1 provides an alternative $B'\in\Theta_r$ with distance at most $ct_n$ and target separation at least $c_KF(ct_n;\beta)$. If a supremum is not attained, use arbitrarily close witnesses and take a limit. The full-data Gaussian KL divergence is at most $c^2/2$, so total variation is at most $c/2$. For any globally honest interval, transport its coverage at $B'$ to $B_*$ and apply a union bound. The interval contains both target values with probability at least $1-2\alpha-c/2=c/2$. Thus

$$E_{B_*,\sigma}|I_n|
\ge\frac{c}{2}c_KF(ct_n;\beta)
\ge\frac{c_Kc^{K+1}}2F(t_n;\beta).$$

This bound allows a competitor to use all covariates. Fixing $\sigma$ for the comparison is legitimate because honesty was required over every $\sigma$.

## V2. Learned compression without balanced gaps

Use the bounded class $\Theta_r(M)$ and independent training/inference split from [D1](growing_dimension_general_tt.md). The training procedure chooses a product projection $P$ containing every loading direction; let its compressed dimension be a deterministic $m$, using measurable completion as in D1. Suppose the reference has exact ranks $r$, is fully physically normal, and a training event $G$ satisfies

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

The 23-feature procedure is implemented in [methods.py](../simulations/code/unequal_bonds/methods.py). Forming the fixed-dimensional regression Gram matrix costs $O(n\,23^2)$ arithmetic operations, solving it costs $O(23^3)$, and each cross certificate uses fixed-size $2\times2$ singular values. These counts exclude acquisition of the original observations; the algorithm only requests the selected features. V1 inversion and the global pilot in V2 remain existence constructions.

The accompanying [check script](../simulations/code/unequal_bonds/check_theory.py) checks algebraic witnesses, singular values, grouping bounds, both cross identities, deterministic target inclusion on constructed confidence-ball events, and the outcome-wise length bound. These are numerical falsification checks, not empirical coverage estimates or a formal floating-point proof. No new Monte Carlo coverage study is asserted.
