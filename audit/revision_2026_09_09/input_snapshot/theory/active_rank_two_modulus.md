# A rank-two TT example with a sharp boundary-dependent modulus

This development note supplies complete internal proofs of a stronger special case. **PROVED** is an internal proof status; publication novelty remains provisional. The result uses established TT cross interpolation. It is separate from the completed manuscript audit and has not yet been incorporated into its numbered theorems.

## 1. Model and statement: PROVED

Fix tensor order K≥3 and dimensions d_j≥3. Let e_0,e_1,e_2 denote the first three coordinate vectors in each mode, and let

\[
 \Theta_2=\{B:\operatorname{rank}(B^{[k]})\le2,
                   \ k=1,\ldots,K-1\},\qquad
 B_b=a e_0^{\otimes K}+b e_1^{\otimes K},\quad0\le b\le a,
 \quad A=e_2^{\otimes K}.
\]

Use the unbounded, closed rank-capped class. For b>0 every bond rank is exactly two, and its two nonzero singular values are a and b. There are no cap-one cuts. At b=0 the rank drops to one. Define

\[
 \omega(t;b)=\sup_{B\in\Theta_2:\|B-B_b\|_F\le t}
                  |\langle A,B-B_b\rangle|.
\]

For b>0 and every t>0,

\[
 \omega(t;b)\asymp_K
       t\min\{1,(t/b)^{K-1}\}. \tag{T1}
\]

At b=0, ω(t;0)=t. More precisely, for 0<t<b,

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

The limit allows a and b to vary with t, subject to a≥b>0. All geometric bounds are independent of the ambient dimensions. For K=4, the leading term is t⁴/(16b³).

## 2. Cross interpolation and the upper bound

For k=1,...,K−1 take prefix indices P_k={0^k,1^k} and suffix indices Q_k={0^{K−k},1^{K−k}}. Let S_k(B)=B(P_k,Q_k), a 2×2 pivot. At B_b each pivot is diag(a,b). If ||B−B_b||≤t<b, then ||S_k(B)−diag(a,b)||_op≤t and thus

\[
 \sigma_{\min}\{S_k(B)\}\ge b-t>0.
\]

Let C_1(B)=B(2,Q_1), C_K(B)=B(P_{K−1},2), and for 2≤k≤K−1 let C_k(B)=B(P_{k−1},2,Q_k). The endpoint slices are a row and column vector; the others are 2×2 matrices. Exact TT cross interpolation gives

\[
 \langle A,B\rangle=C_1(B)S_1(B)^{-1}C_2(B)
             \cdots S_{K-1}(B)^{-1}C_K(B). \tag{T4}
\]

For completeness, a rank-at-most-two matrix with an invertible selected 2×2 submatrix S satisfies M=M(:,Q)S^{-1}M(P,:): the selected columns form a column-space basis, and their coefficients are identified by restriction to the selected rows. Apply this identity first to the first prefix unfolding. Apply it again to the remaining factor using the next prefix unfolding, and continue. This gives (T4), equivalently the familiar exact TT cross formula. Invertibility also implies that each nearby unfolding has rank exactly two.

All entries in C_k(B_b) are zero. More strongly, the entry sets of C_1,...,C_K are pairwise disjoint: entries in C_k have their only coordinate equal to 2 at site k and all other coordinates in {0,1}. Hence

\[
 \sum_{k=1}^K\|C_k(B)\|_F^2\le\|B-B_b\|_F^2\le t^2.
\]

Use (T4), operator norm bounded by Frobenius norm, and arithmetic–geometric mean:

\[
 |\langle A,B\rangle|
 \le\frac{\prod_k\|C_k(B)\|_F}{(b-t)^{K-1}}
 \le\frac{(t^2/K)^{K/2}}{(b-t)^{K-1}}.
\]

Cauchy–Schwarz separately gives |〈A,B−B_b〉|≤t. This proves the upper bound in (T2).

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

Choose s²=(1+t²/b²)^{1/K}−1. This proves the lower bound in (T2), and in fact this lower bound holds for every t>0.

Here is an explicit verification of the uniform equivalence (T1). Put u=t/b. If 0<u≤1, the mean value theorem gives

\[
 (1+u^2)^{1/K}-1\ge u^2/(2K),
\]

so the lower bound is at least (2K)^{−K/2}t u^{K−1}. If u≥1, divide the expression in braces by u^{2/K}. The resulting function is f(v)=(1+v)^{1/K}−v^{1/K}, with v=u^{−2}∈(0,1]. Its derivative is negative, so f(v)≥f(1)=2^{1/K}−1. This gives a lower bound (2^{1/K}−1)^{K/2}t. For the upper bound, if t≤b/2 apply (T2) and b−t≥b/2. If b/2<t<b, use ω≤t≤2^{K−1}t(t/b)^{K−1}; if t≥b, use ω≤t. These bounds prove (T1).

As t/b→0, the lower bound is K^{−K/2}t^K/b^{K−1}{1+o(1)} and the upper bound has the same coefficient. This proves (T3). At b=0 the feasible path a e_0^{⊗K}+t e_2^{⊗K} attains the ambient upper bound t exactly.

## 4. Comparison with every single prefix unfolding: PROVED

Fix a cut k and impose only rank(B^[k])≤2, retaining the same center and target. Denote that matrix-model modulus by ω_k^mat(t;b). In the orthonormal row and column bases containing 0^k,1^k,2^k and 0^{K−k},1^{K−k},2^{K−k}, the center has pivot diag(a,b). Matrix skeleton interpolation gives the target entry as a row times the inverse pivot times a column. These two off-pivot slices occupy disjoint entries of the perturbation. The same energy argument gives

\[
 \omega_k^{\mathrm{mat}}(t;b)\le t^2/\{2(b-t)\},\quad0<t<b.
\]

The rank-two matrix path rotating the weak component's row and column toward the corresponding all-2 vectors has target bs² and distance b√(2s²+s⁴). Therefore

\[
 \omega_k^{\mathrm{mat}}(t;b)\sim t^2/(2b)
 \quad\text{as }t/b\to0,
\]

and the same two-regime argument gives ω_k^mat(t;b)≍t min(1,t/b). In particular,

\[
 \frac{\omega(t;b)}{\min_k\omega_k^{\mathrm{mat}}(t;b)}
 \sim\frac2{K^{K/2}}(t/b)^{K-2}\longrightarrow0.
\]

This compares the full TT class with each single-unfolding relaxation. It does not claim that no matrix representation with additional nonlinear constraints could encode the tensor problem. The intersection of compatible rank constraints is the substantive distinction.

## 5. Honest inference and a computable interval: PROVED for fixed ambient dimension

Return to iid Gaussian tensor regression with unknown σ. Let p=∏d_j be fixed and n≥p+max(K,2). Write z for ambient OLS and let e be the audited unknown-variance F-based Euclidean confidence radius. It has P{||z−B||≤e}≥1−α and moments up to order K at rate t_n=σ/√n. The interval below does not use a, b or B_b.

Extract the same slices and pivots from z. Set d_k=σ_min{S_k(z)}−e. If all d_k>0, let

\[
 H(z,e)=\frac{\prod_{j=1}^K\{\|C_j(z)\|_F+e\}}
                      {\prod_{k=1}^{K-1}d_k},\qquad
 I_s=[-H(z,e),H(z,e)].
\]

Intersect I_s with I_a=[〈A,z〉−e,〈A,z〉+e]. If the intersection is empty return {〈A,z〉}. If any d_k≤0, return I_a.

On the confidence-ball event, positive d_k certify invertibility of every true pivot, and (T4) implies |ψ(B)|≤H(z,e). The ambient interval also contains ψ(B). If pivots are not certified the ambient interval alone still covers. Thus this procedure is honest over **all** Θ_2, not just over the diagonal family B_b, and uses no rank pretest or TT optimization solver.

For length, put T=||z−B_b||+e. At B_b all C_j vanish and σ_min(S_k)=b. On T≤b/2, each numerator factor is at most T and each denominator at least b−T, so length is at most 2^K T^K/b^{K−1}. On T>b/2, length is at most 2e≤2T≤2^K T^K/b^{K−1}. On every outcome it is also at most 2e. Taking expectations and using the audited OLS moments proves

\[
 E_{B_b,\sigma}|I|\le C_{K,p,\alpha}
 t_n\min\{1,(t_n/b)^{K-1}\}. \tag{T5}
\]

At b=0 use the ambient bound. Constants are uniform in a≥b and b≥0; dimensions remain fixed in this statistical upper bound.

For the lower bound, take a feasible path from Section 3 with distance t=c_αt_n, where c_α=1−2α. Gaussian-regression KL is nt²/(2σ²), hence total variation is at most c_α/2. The two-point confidence-interval inequality and the uniform modulus lower bound yield

\[
 \inf_{I\ \mathrm{globally\ honest}}
 E_{B_b,\sigma}|I|
 \ge c_{K,\alpha}t_n\min\{1,(t_n/b)^{K-1}\}. \tag{T6}
\]

To compare scales, f(ct,b)≥c^K f(t,b) for 0<c≤1 and f(t,b)=t min{1,(t/b)^{K−1}}. Thus replacing t_n by c_αt_n only changes the constant. At b=0 use the exact rank-two path from Section 3. The lower bound remains valid when honesty also ranges over unknown σ, since it already holds in the fixed-σ subexperiment.

Combining (T5) and (T6) gives a matching boundary-dependent honest-length scale, including sequences b=b_n approaching zero:

\[
 L_{\alpha,n}(B_b;\sigma)\asymp_{K,p,\alpha}
 \frac{\sigma}{\sqrt n}
 \min\left\{1,\left(\frac{\sigma}{b\sqrt n}\right)^{K-1}\right\}. \tag{T7}
\]

For K=4, b≫σ/√n gives order σ⁴/(b³n²); b≲σ/√n gives order σ/√n. The corresponding single-unfolding model has strong-bond order σ²/(bn). The sharp modulus constant in (T3) is **not** an exact optimal confidence-length constant.

## 6. What this resolves, and what it does not

This example moves beyond an original-mode rank-one center and beyond cap-one factorization. It supplies both a uniform weak-bond transition and a direct statistical procedure. At b>0 the TT point is on the full-rank smooth stratum: the estimand is degenerate there. At b=0 the parameter becomes rank deficient and the inferential rate changes. These two sources of nonregularity should not be conflated.

The diagonal center and loading aligned with an unused coordinate are special. Higher-order MPS expansions and TT cross formulas already exist, so the geometry should be presented as a sharp modulus calculation and its inferential consequence, not as a new parametrization. The immediate open problem is a classification using the first nonzero products of the cross slices, followed by a growing-dimension inference theorem valid through weak bonds. The separate compression theorem currently covers a different block-product branch; the two results have not been combined into one general TT theorem.

## Sources

1. Dolgov and Savostyanov, [Parallel cross interpolation for high-precision calculation of high-dimensional integrals](https://cris.brighton.ac.uk/ws/files/6746392/1_s2.0_S0010465519302565_main.pdf), accepted 2019, DOI 10.1016/j.cpc.2019.106869, Theorem 2 and equation (5): exact TT reconstruction from invertible crosses. The identity is also proved directly above.
2. Kutschan (2018), [Tangent cones to tensor train varieties](https://arxiv.org/pdf/1705.10152), Theorem 14: pre-existing first-order geometry of rank-capped TT varieties.
3. Wouters, Nakatani, Van Neck and Chan (2013), [The Thouless theorem for matrix product states and subsequent post-density matrix renormalization group methods](https://arxiv.org/pdf/1305.1761), Sections VI–VII: parametrizations and higher-order tangent/excitation constructions. These are relevant geometry competitors, not statistical confidence-interval theorems.
4. Audited project [appendix.tex](../paper/appendix.tex), Gaussian-regression KL, two-point interval inequality and OLS moment lemmas; [appendix_strengthening.tex](../paper/appendix_strengthening.tex), scope of the unbounded-class extension.
