# Honest boundary inference after target-preserving compression

This development note supplements the audited manuscript. It does not change the manuscript's numbered theorem inventory. **PROVED** below means that a complete internal derivation is supplied; it does not certify novelty or replace independent mathematical review. The projection identity and the preliminary estimation argument are established statistical ingredients. The proposed research contribution is their combination with honest inference for a degenerate tensor functional.

## 1. A focused model with growing dimensions

Fix the number of blocks J≥2, but allow D_1,...,D_J≥2 to grow with n. Write p=∏D_j and

\[
\mathcal S_M=\{\beta v_1\otimes\cdots\otimes v_J:
 |\beta|\le M,\ \|v_j\|=1\}.
\]

Observe independent pairs x_i∼N_p(0,I_p), Y_i=x_i^T b+ε_i, with independent ε_i∼N(0,σ²), σ>0 unknown. The target is ψ(B)=〈A,B〉 for a fixed, known unit product A=w_1⊗⋯⊗w_J. No preliminary estimate is assumed to know the true directions. The evaluation points are

\[
\mathcal N_D(\lambda)=\{B_0=\lambda v_1\otimes\cdots\otimes v_J:
 \|v_j\|=1,\ \langle v_j,w_j\rangle=0\ \forall j\},
 \qquad 0<\lambda<M/2.
\]

Honesty is over all B∈S_M and every σ>0, including points outside N_D(λ). Short expected length is claimed on N_D(λ). This separation is essential: ψ is identically zero on the evaluation set, but the interval must cover nonzero targets elsewhere in S_M.

The four-way TT cap profile (1,2,1) is contained in this model with J=3 and block dimensions (d_1,d_2d_3,d_4). Its internal constraint is retained for interpreting the original class but is unnecessary for the upper bound, which is honest over the larger block-product class. A lower bound transfers to the TT class when the selected feasible paths also respect its internal caps, as specified below.

## 2. Exact compression: PROVED (supporting ingredient)

Split the observations into independent training and inference samples of sizes n_1 and n_2. From the training sample choose any measurable unit h_j∈w_j^⊥. Use a deterministic fallback when an algorithm does not supply such a vector. Set

\[
 U_j=[h_j,w_j],\qquad U=U_1\otimes\cdots\otimes U_J,
 \qquad P=UU^T,\qquad m=2^J.
\]

The columns of U are orthonormal and A is in their span. For inference observations define z_i=U^Tx_i and C=U^TB, interpreted as an order-J binary tensor. Then, conditional on the training sample,

\[
 z_i\stackrel{\mathrm{iid}}\sim N_m(0,I_m),\qquad
 Y_i=z_i^T C+\xi_i,\qquad
 \xi_i\stackrel{\mathrm{iid}}\sim
 N\{0,\sigma^2+\|(I-P)B\|^2\},
\]

and the ξ_i are independent of the z_i. Moreover, C is a block-rank-one tensor (possibly zero), and

\[
 \langle U^TA,C\rangle=\langle A,B\rangle.
\]

**Proof.** Decompose x_i=Px_i+(I−P)x_i. Conditional on the training sample, the two terms are independent Gaussian vectors because their cross-covariance is zero. The omitted term 〈(I−P)x_i,(I−P)B〉 is Gaussian with variance ||(I−P)B||² and is independent of z_i and ε_i. Applying a product of linear maps to a product tensor preserves its product form. Finally PA=A, so 〈A,PB〉=〈A,B〉. These statements hold for every training outcome and do not require accurate h_j. ∎

**Scope of conditioning.** This is conditional on training data and, for the subsequent OLS pivot, the projected inference design. It is not a Gaussian-noise representation conditional on the full original inference design: the omitted mean is then fixed. Arbitrary correlated or non-Gaussian designs do not have this independence automatically. ISLET already uses the Gaussian omitted-signal variance calculation; it is not claimed as a new identity.

Use the audited unknown-variance confidence-ball procedure in dimension m on this compressed rank-one cone. Intersect its resulting interval with [−M,M]; if this intersection is empty, return {0}. Denote the result I_n. Since the true target lies in [−M,M], this clipping cannot reduce coverage on a successful coverage event and guarantees |I_n|≤2M. For n_2>m the interval is globally honest:

\[
 \inf_{B\in\mathcal S_M,\,\sigma>0}
 P_{B,\sigma}\{\psi(B)\in I_n\}\ge1-\alpha.
\]

The procedure must estimate the **effective** variance from the compressed regression residuals, even if the original σ were known. Substituting σ for the effective variance is generally invalid.

## 3. An anchor-quality theorem: PROVED

At B_0∈N_D(λ), write c_j=〈h_j,v_j〉 and define

\[
 \lambda_P=\lambda\prod_j|c_j|,\qquad
 \sigma_P^2=\sigma^2+\lambda^2\{1-\prod_jc_j^2\}.
\]

Because h_j⊥w_j and v_j⊥w_j, the compressed coefficient equals λ(∏c_j)e_0^{⊗J}; the target loading is e_1^{⊗J}. Thus its functional remains purely degree J. There is no tangent leakage caused by anchor estimation in this particular construction.

Suppose an event G in the training sample satisfies

\[
 P(G^c)\le\delta,\qquad
 \lambda_P\ge\lambda/\sqrt2,\quad \sigma_P\le\sqrt2\sigma
 \quad\text{on }G.
\]

If n_2≥m+max(J,2) and σ/√n_2≤c_Jλ for a sufficiently small constant depending only on J, then

\[
 E_{B_0,\sigma}|I_n|
 \le C_{J,\alpha}\frac{\sigma^J}{\lambda^{J-1}n_2^{J/2}}
       +2M\delta. \tag{H1}
\]

**Proof.** Conditional on any training outcome in G, apply the audited fixed-dimensional pure-degree expected-length bound to the compressed model in dimension m. Its bound is C σ_P^J/(λ_P^{J−1}n_2^{J/2}), which is at most a constant depending only on J and α times the first term in (H1). The theorem is uniform in the compressed unit directions; their signs do not matter. Integrate this bound over G. On G^c use the deterministic clipping bound 2M. This controls expectation, rather than just stochastic order. ∎

The normal-loading restriction is substantive. For arbitrary loadings and arbitrary evaluation points, there is no claim here that projection preserves the full loading-uniform modulus with dimension-free constants.

## 4. A preliminary estimator with an explicit tail bound: PROVED

This section supplies a statistical existence construction. It does **not** assert a polynomial-time algorithm for globally optimizing a tensor least-squares problem.

Let B̃ be a measurable global minimizer of training squared loss over S_M. Existence follows from compactness. The usual measurable-minimizer construction applies to this continuous loss over a compact finite-dimensional parameterization; a fixed measurable choice handles nonuniqueness. Factor a nonzero B̃ into a scalar and unit vectors ṽ_j; use a measurable sign convention. Define h_j by normalizing the projection of ṽ_j onto w_j^⊥, with a fixed unit fallback if this projection vanishes. If B̃=0, use the same fallback.

Here are explicit, deliberately conservative constants. Put

\[
 e_J=\{16(J+1)\}^{-1},\qquad
 W_J(D)=\log 2+2^J\log(1+2/e_J)
                +2\sum_jD_j\log(1+2\sqrt2/e_J),
 \quad L=W_J(D)+x.
\]

For x>0 and n_1≥128L,

\[
 P\left\{\|\widetilde B-B_0\|>
       18\sigma\sqrt{L/n_1}\right\}\le2e^{-x}. \tag{H2}
\]

This bound holds uniformly for B_0∈S_M, without a nonzero singular-value assumption. The constants in (H2) are proof certificates, not suggested tuning parameters.

**Proof of (H2).**

1. Every difference of two product tensors has Tucker multilinear ranks at most two. Let T_2 be the unit-Frobenius set of tensors with these ranks. Every member can be represented by a unit core of dimension 2^J and J orthonormal D_j×2 factor matrices, padding deficient ranks if necessary.

2. Cover the core sphere in Euclidean norm and each Stiefel set in Frobenius norm by e_J-nets whose centers remain in the respective sets. The elementary volume-packing bound gives a product net N with

   log(2|N|)≤W_J(D).

   For each H∈T_2, replace its core and factors successively by their net points. Multilinearity gives an exact telescoping expansion of H−H_net with J+1 summands. Each summand has Tucker ranks at most two and norm at most e_J, since all other factors have operator norm one and the core has norm one. Hence any linear map F satisfies

   sup_{H∈T_2}||FH|| ≤ max_{H∈N}||FH|| +(1/16)sup_{H∈T_2}||FH||.

   The same argument applies to the absolute value of any scalar linear functional. The net contains unit tensors because its factors are orthonormal and its cores have unit norm.

3. Write X for the training measurement map. For a fixed unit H, ||XH||² has a χ²_{n_1} law. Its moment generating function is (1−2t)^{−n_1/2}; Chernoff's inequality and log(1+u)≥u−u²/2, −log(1−u)−u≤u²/{2(1−u)} give

   P{| ||XH||²/n_1−1 |>1/4}≤2exp(−n_1/128).

   A union bound and n_1≥128L show that all net norms ||XH||/√n_1 lie in [3/4,5/4], except on an event of probability at most e^{−x}. The telescoping bound then gives an upper restricted norm at most (5/4)/(15/16)=4/3. For an arbitrary unit H, its lower norm is at least 3/4−(4/3)/16=2/3. Consequently,

   (2/3)||H|| ≤ ||XH||/√n_1 ≤ (4/3)||H||

   for all Tucker-rank-at-most-two H on this event. No ambient full-rank design assumption is used.

4. Conditional on this design event, ε^T XH/(σ√n_1) is centered Gaussian with variance at most (4/3)² for each net point. A Gaussian tail bound and the same union bound show that its maximum absolute value on N is at most (4/3)√(2L), except with probability e^{−x}. The scalar telescoping argument gives

   sup_{H∈T_2}|ε^T XH|/(σ√n_1)
   ≤(16/15)(4/3)√(2L) ≤4√L.

5. Since B_0 is feasible, the least-squares basic inequality for Δ=B̃−B_0 is ||XΔ||²≤2ε^TXΔ. If Δ≠0, then Δ/||Δ||∈T_2. The two preceding bounds imply

   (4/9)n_1||Δ||² ≤8σ√(n_1 L)||Δ||,

   giving ||Δ||≤18σ√(L/n_1). Combine the design and noise failure probabilities. ∎

**From tensor error to anchor quality.** On ||B̃−B_0||≤r<λ, B̃ is nonzero. Projection orthogonal to ṽ_j in block j annihilates B̃, so

\[
 \lambda\sqrt{1-\langle\widetilde v_j,v_j\rangle^2}\le r.
\]

As v_j⊥w_j, removing the w_j component of ṽ_j cannot decrease its absolute correlation with v_j. Therefore 1−c_j²≤r²/λ². Since 0≤c_j²≤1,

\[
 1-\prod_jc_j^2\le\sum_j(1-c_j^2)\le Jr^2/\lambda^2.
\]

The product inequality follows by induction from 1−ab=(1−a)+a(1−b)≤(1−a)+(1−b). In particular, Jr²≤min(λ²/2,σ²) supplies exactly the event G in Section 3.

## 5. Growing-dimension honest length: PROVED in this focused model

Combining the previous results, if

\[
 n_1\ge\max\{128,\ 324J,\ 648J\sigma^2/\lambda^2\}
          \{W_J(D)+x\},
\]

and n_2 meets the conditions in Section 3, then the same globally honest procedure satisfies, uniformly over B_0∈N_D(λ),

\[
 E_{B_0,\sigma}|I_n|
 \le C_{J,\alpha}\frac{\sigma^J}{\lambda^{J-1}n_2^{J/2}}
      +4M e^{-x}. \tag{H3}
\]

For n_1,n_2 proportional to n, λ and σ in fixed compact subsets of (0,∞), λ<M/2, and x=(J/2+1)log n, this gives a single procedure with expected length of order σ^J/(λ^{J−1}n^{J/2}) whenever n≥C(ΣD_j+log n). The constants can be uniform over those compact parameter sets. In particular p may greatly exceed n. J remains fixed; the construction does not solve growing tensor order.

**Matching lower bound in this regime.** Fix B_0∈N_D(λ) and consider B(s)=λ⊗_j(v_j+s w_j). Then

\[
 \|B(s)-B_0\|^2=\lambda^2\{(1+s^2)^J-1\},\qquad
 \psi\{B(s)\}-\psi(B_0)=\lambda s^J.
\]

Choose t=(1−2α)σ/√n≤λ/2 and set s²=(1+t²/λ²)^{1/J}−1. The mean value theorem gives s²≥4t²/(5Jλ²). The path belongs to S_M when λ+t<M. Joint Gaussian-regression KL equals nt²/(2σ²), so total variation is at most √n t/(2σ)=(1−2α)/2. The audited two-point interval inequality therefore gives

\[
 E_{B_0,\sigma}|I|\ge
 \frac{(1-2\alpha)^{J+1}}2
 \left(\frac4{5J}\right)^{J/2}
 \frac{\sigma^J}{\lambda^{J-1}n^{J/2}}
\]

for every globally honest I. This is dimension-free. It also bounds the infimum over globally honest procedures of the supremum of expected lengths on N_D(λ). For a TT submodel, the path is feasible if v_j and w_j are each original-mode product tensors and every within-block cap is at least two: v_j+s w_j has internal unfolding ranks at most two. Thus the (1,2,1) example admits the lower bound with these directions.

**Interpretation.** The theorem removes an ambient sample-size obstacle in a genuine growing-dimension special case. It does not improve the regular tensor estimation rate, prove sharp constants, establish optimal dimension or SNR thresholds, or give a polynomial-time preliminary estimator. The clipped bounded class is used to control rare training failures; the earlier manuscript's unbounded-class extension does not automatically remove that device here.

## 6. What remains PARTIAL or CONJECTURED

- **PARTIAL:** an efficiently computable anchor estimator with sufficiently strong tail control. Existing ISLET/TT estimation results are candidates, but their initialization, SNR and dimension requirements must be carried through exactly. A numerical ALS solution is not a certified global least-squares solution.
- **PARTIAL:** sharp sample-size/SNR necessity for one honest procedure that adapts across unknown orientations. H3 proves a sufficient regime, not a phase transition. Mixture lower bounds may differ from the present two-point lower bound.
- **PARTIAL:** uniform expected length for near-normal rather than exactly normal loadings, and for nonzero local departures from N_D(λ). Coverage is already uniform; the optimal length profile is the additional target.
- **CONJECTURED research target:** a matched characterization of the adaptive length benchmark throughout weak and strong orientation-identification regimes. No formula for the weak regime is asserted.
- **OPEN:** correlated designs, finite-variance errors, general TT points with active internal constraints, and arbitrary dense loadings for this compression construction. The exact Gaussian identity must not be silently reused in these settings.

## Sources and dependencies

1. Audited manuscript, Theorem 6 and its unknown-variance length proof; Theorem 3 and Lemma 14 for honest-length lower bounds. Local files: [main.pdf](../paper/main.pdf), [appendix.tex](../paper/appendix.tex), [appendix_strengthening.tex](../paper/appendix_strengthening.tex).
2. Zhang, Luo, Raskutti and Yuan (2020), [ISLET: Fast and Optimal Low-Rank Tensor Regression via Importance Sketching](https://arxiv.org/pdf/1911.03804), Theorem 4, Remark 5 and supplementary projection-noise calculations. Gaussian compression and tensor sketching are prior ingredients.
3. Qin and Zhu (2025 version), [Computational and Statistical Guarantees for Tensor-on-Tensor Regression with Tensor Train Decomposition](https://arxiv.org/html/2406.06002v2), Theorems 1–2 and algorithmic initialization conditions. Related restricted-isometry/estimation theory; H2 is derived directly above rather than imported with unmatched assumptions.
