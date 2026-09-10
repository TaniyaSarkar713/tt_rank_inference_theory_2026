# Learning supporting subspaces for general TT inference

Status: **PROVED** for the conditional and existence results stated here. A computationally efficient pilot at the displayed sample threshold and uniform adaptation through unidentified weak directions remain **PARTIAL**. These distinctions are necessary for publication-level claims.

## D1. Coverage after data-dependent mode compression

Use iid isotropic Gaussian regression and a deterministic unit product loading A=⊗w_j. The parameter class is Θ_r(M)={B: TT ranks≤r, ||B||≤M}. Split n=n_1+n_2 observations independently. From training data choose mode subspaces V_j that contain w_j and have dimensions at most m_j, with orthonormal bases U_j. Extend smaller subspaces by a measurable deterministic completion if needed. Write U=⊗U_j and P=UU^T.

Conditional on training, the inference regression in the m=∏dim(V_j) coordinates U^Tx has coefficient C=U^TB and unknown residual variance τ_B²=σ²+||(I−P)B||². Modewise linear maps do not increase any prefix rank, so C lies in the compressed TT class. The target is unchanged because PA=A. Use the unknown-variance F confidence ball in this regression and invert it over the compressed TT class intersected with ||C||≤M. Take the smallest interval containing the resulting target values; if the feasible set is empty return {0}.

This interval is honest over every B∈Θ_r(M) and every σ>0 whenever n_2>m and 0<α<1. The proof is conditional Gaussian independence plus inclusion of the true C on the confidence event. The feasible set is compact, because the rank constraints and ball are closed and bounded; extrema exist. Measurability follows by real algebraic elimination: unfolding-rank constraints are vanishing minors, norm constraints are polynomial inequalities, and the existence of a feasible C whose linear target exceeds a real number is a projection of a semialgebraic set. The Tarski–Seidenberg projection theorem makes this set semialgebraic and therefore Borel in its finite-dimensional inputs. This gives measurable extrema and, by semialgebraic selection, a measurable choice of the compact least-squares argmin in D3. Measurable orthogonal completions follow by Gram–Schmidt applied to the chosen vectors and then the coordinate basis, discarding zero residuals in a fixed order. The procedure has length at most 2M. It is a statistical existence construction: exact nonconvex confidence-region inversion has not been certified as polynomial-time.

## D2. Expected length with an explicit training event

Assume the reference B_* has exact ranks r, satisfies B_*×_jw_j^T=0 for all j, and its smallest nonzero bond singular values obey

\[
 b\le\beta_j\le\kappa b\quad\text{for all }j,
 \qquad b>0,\quad\kappa\ge1.
\]

The bounded ratio is an extra assumption. The geometric coefficient theorem does not require it, but it prevents a rare small-denominator fallback from being concealed inside a claimed uniform expected-length constant.

Suppose a training event G has probability at least 1−δ and on G

\[
 \|(I-P)B_*\|\le r_0\le\min(b/2,\sigma).
\]

Then, for n_2≥m+max(K,2), the interval from D1 satisfies

\[
 E_{B_*,\sigma}|I_n|
 \le C_{K,m,\alpha,\kappa}
 \min\left\{\frac\sigma{\sqrt{n_2}},
 \frac{\sigma^K}{n_2^{K/2}\prod_j\beta_j}\right\}
       +2M\delta. \tag{D1}
\]

**Proof.** On G, τ_*≤√2σ. Since P_j contains w_j, it commutes with w_jw_j^T, so PB_* is still annihilated by contraction along w_j in each mode. Weyl's inequality gives |β_j(PB_*)−β_j(B_*)|≤r_0. Thus the compressed tensor has the same exact ranks, β_j(PB_*)≥β_j/2, and its weakest-bond ratio is at most 2κ+1.

Condition on training in G. Let z,e be the compressed center and radius and T=||z−C_*||+e. If the inverted confidence region is nonempty, all its coefficients lie within T of C_*, so its target diameter is at most 2ω_A(T;C_*). On T≤β_min(C_*)/2, the explicit general modulus bound gives at most C_KT^K/∏β_j(C_*). On the complementary event, diameter≤2T, and

\[
 2T\le2^K T^K/\beta_{\min}(C_*)^{K-1}
 \le2^K(2\kappa+1)^{K-1}T^K/\prod_j\beta_j(C_*).
\]

It is also at most 2T on every outcome. The compressed Gaussian regression moments established in C4 give ET^k≤C(τ_*/√n_2)^k up to k=K, proving the minimum of the two bounds on G. Integrate, and use length≤2M on G^c. ∎

When 0<α<1/2 and σ/√n≤c_Kb, the general feasible-path theorem and the full-data Gaussian KL give a matching lower bound of order σ^K/(n^{K/2}∏β_j), provided the reference is inside the norm cap with enough margin for the chosen local path. For example, assume ||B_*||≤M−ρ for a fixed ρ>0 and t_n≤cρ. This lower bound does not require the bounded bond ratio. No general matching lower bound is asserted when σ/√n is comparable to b outside the weak-component family.

## D3. A pilot supplying the training event

Let B̃ minimize training squared loss globally over Θ_r(M). This is a compact class, so a measurable minimizer exists. Put s_j=min(d_j,r_{j−1}r_j). A TT tensor has mode-j matrix rank at most s_j, since separating its jth core from its left and right interfaces factors that matrix through a space of dimension r_{j−1}r_j.

Choose V_j to contain both w_j and the mode-j column space of B̃; then dim(V_j)≤min(d_j,s_j+1), PB̃=B̃, and

\[
 \|(I-P)B_*\|\le\|B_*-\widetilde B\|.
\]

Set q_j=min(d_j,2s_j), e_K={16(K+1)}^{-1}, and

\[
 W=\log2+\left(\prod_jq_j\right)\log(1+2/e_K)
       +\sum_jd_jq_j\log(1+2\sqrt{q_j}/e_K).
\]

For x>0 and n_1≥128(W+x),

\[
 P\{\|\widetilde B-B_*\|>18\sigma\sqrt{(W+x)/n_1}\}
       \le2e^{-x}. \tag{D2}
\]

Here are the steps of the tail proof, included to specify the rank and dimension factors. A difference of two feasible tensors has mode ranks at most q_j. Every unit tensor in this Tucker envelope has a unit core of dimension ∏q_j and orthonormal d_j×q_j factors. Euclidean/Frobenius e_K-nets on the core sphere and Stiefel factors have total cardinality N with log(2N)≤W by volume packing. Replacing factors and core successively creates K+1 error terms, each in the same Tucker envelope and with norm at most e_K. Any linear-map supremum is therefore bounded by its net maximum plus 1/16 of the same supremum.

For each net point, ||XH||² is χ²_{n_1}. The bound P{| ||XH||²/n_1−1 |>1/4}≤2exp(−n_1/128) and a union bound give net norms between 3/4 and 5/4 after division by √n_1, outside probability e^{-x}. The 1/16 extension gives restricted norms between 2/3 and 4/3 for the full envelope. Conditional on this event, Gaussian noise and a second union bound give a scalar net maximum |ε^TXH|/(σ√n_1)≤(4/3)√{2(W+x)} outside probability e^{-x}; extension bounds the full maximum by 4√(W+x). The least-squares inequality ||XΔ||²≤2ε^TXΔ then gives (4/9)n_1||Δ||²≤8σ√{n_1(W+x)}||Δ||. Division yields (D2). This proof does not assume an algorithm reaches the global minimizer.

It is sufficient for the event in D2 to imply G that

\[
 n_1\ge\max\{128,324,1296\sigma^2/b^2\}(W+x).
\]

Combine with D1 and δ=2e^{-x}. For fixed K,r, W is at most a constant times 1+Σd_j, even though p=∏d_j can grow much faster. The inference dimension is at most ∏min(d_j,s_j+1), also bounded for fixed K,r. Choose x of logarithmic order to make 4Me^{-x} smaller than the desired expected-length scale. If b or σ varies with n, state that choice explicitly rather than silently absorbing it into a constant.

## D4. Interpretation of the combined result

There are now two distinct complete growing-dimension results. The selected-cross theorem is computationally explicit and valid through b≈σ/√n for a prespecified-coordinate weak-component family. The learned-subspace theorem handles unknown orientations and general physically normal TT references, but its rate guarantee requires accurate learning of the weak directions. Its sufficient condition includes n_1b²/σ² of order W+x.

For growing W, that condition does not reach b≈σ/√n with a proportional split. The intermediate regime σ/√n≪b≲σ√{W/n} remains a real statistical question. The current proof neither establishes a necessary dimension penalty nor proves adaptation impossible there. A lower bound must compare one globally honest procedure across many orientations; a two-point argument at one known orientation does not suffice.

Practical alternatives such as TT-SVD initialization followed by IHT or Riemannian descent need their own assumptions and tail bounds. Existing estimation papers are candidates, not a license to call a local numerical optimizer a global minimizer. Prespecified-support results and learned-support results should remain separate in the manuscript until that issue is resolved.
