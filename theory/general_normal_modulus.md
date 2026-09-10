# Sharp contact of a fully normal product loading

Status: **PROVED**, with complete internal derivations below. This is a generalization of the rank-two calculation, not a claim that TT parametrizations or higher-order tangent spaces are new. Tensor order and rank caps are fixed unless explicitly stated otherwise.

## G1. General sharp modulus theorem

Let H=⊗_{j=1}^K R^{d_j}, K≥2, and let Θ_r consist of tensors whose prefix unfolding ranks are at most r=(r_1,...,r_{K−1}), with r_0=r_K=1. Let B_* have exact ranks r. Put β_j=σ_{r_j}(B_*^[j])>0 and β=min_j β_j. Take unit w_j and A=⊗_j w_j. Assume

\[
 B_*\times_j w_j^T=0\quad\text{for every }j.
\]

Here ×_j is contraction in physical mode j. This says that the loading direction is absent from the signal in each mode. It is stronger than merely 〈A,B_*〉=0 or first-order tangent orthogonality. It admits arbitrary TT cores and arbitrary admissible ranks within the complementary physical spaces.

For ω_A(t;B_*)=sup_{B∈Θ_r, ||B−B_*||≤t}|〈A,B−B_*〉|,

\[
 \lim_{t/\beta\to0}
 \frac{\omega_A(t;B_*)\prod_{j=1}^{K-1}\beta_j}{t^K}
       =K^{-K/2}. \tag{G1}
\]

The limit is uniform over dimensions, ranks and reference tensors for fixed K, subject to the stated exact ranks and t/β→0. In particular the normalizing factor is the product of the weakest singular values at all bonds, not necessarily β^{K−1}.

An explicit upper bound for 0<t<β is

\[
 \omega_A(t;B_*)\le
 \frac{K^{-K/2}\{t^2+t^4\sum_{i<j}(\beta_i-t)^{-2}\}^{K/2}}
      {\prod_{j=1}^{K-1}(\beta_j-t)}, \tag{G2}
\]

where i<j ranges over 1≤i<j≤K, so β_i is only needed for i<K. Also ω_A≤t. For 0<t≤β/2, a lower bound is

\[
 \omega_A(t;B_*)\ge
 2^{-K/2}K^{-K/2}\frac{t^K}{\prod_j\beta_j}. \tag{G3}
\]

No uniform weak-bond formula for arbitrary patterns of unequal vanishing β_j is claimed by this theorem.

## Proof of the upper bound

Rotate coordinates independently in each mode so w_j is the last basis vector. Orthogonal changes preserve tensor norm, prefix singular values and TT ranks. Write a nearby B in left-orthonormal TT form with cores G_j. This form exists by successively applying thin QR factorizations, or thin singular-value decompositions, to the prefix unfoldings. Because t<β, Weyl's inequality gives exact ranks r for B.

Let L_j be its left interface with orthonormal columns and R_j its right interface, so B^[j]=L_jR_j. The nonzero singular values of R_j are those of B^[j]. Define Q_j=(R_jR_j^T)^{1/2}, j<K; Q_K=1. Define H_j=G_j(w_j), the core slice in the target physical direction, Z_j=H_jQ_j, and d_j=||Z_j||_F. The isometry of L_{j−1} and the identity ||H_jR_j||_F=||H_jQ_j||_F imply

\[
 d_j=\|B\times_jw_j^T\|_F\le t,
 \quad\|H_j\|_{\mathrm{op}}\le t/(\beta_j-t)\quad(j<K).
\]

The target entry factors exactly as

\[
 \langle A,B\rangle
 =Z_1Q_1^{-1}Z_2Q_2^{-1}\cdots Q_{K-1}^{-1}Z_K.
\]

Therefore |〈A,B〉|≤∏d_j/∏(β_j−t). To retain the sharp energy constant, it remains to control Σd_j² more carefully than the bound Kt².

For i<j, restrict the left interface L_{j−1} to the target direction at site i. Its operator norm is at most ||H_i||_op: before site i the left interface is an isometry; after site i the recursion L_l=(L_{l−1}⊗I)G_l^left multiplies by matrices of operator norm one. Consequently

\[
 \|B\times_iw_i^T\times_jw_j^T\|_F
 \le\|H_i\|_{\mathrm{op}}\|H_jR_j\|_F
 \le t^2/(\beta_i-t).
\]

Decompose B into mutually orthogonal components B_S according to which modes lie along w_j and which lie in w_j^⊥. Since B_* has only its S=∅ component,

\[
 \sum_{S\ne\varnothing}\|B_S\|^2\le t^2,
 \quad \sum_jd_j^2=\sum_{S\ne\varnothing}|S|\|B_S\|^2.
\]

For s≥2, s−1≤binom(s,2). The pairwise contractions count each B_S exactly binom(|S|,2) times. It follows that

\[
 \sum_jd_j^2\le t^2+
 \sum_{i<j}\|B\times_iw_i^T\times_jw_j^T\|^2
 \le t^2+t^4\sum_{i<j}(\beta_i-t)^{-2}.
\]

Arithmetic–geometric mean, ∏d_j≤(Σd_j²/K)^{K/2}, proves (G2). This argument covers all nearby feasible tensors and does not assume a particular differentiable path.

## Proof of attainability and the sharp constant

Take a left-orthonormal TT representation of B_* and define its Q_j as above. Each target core slice is zero: the full physical slice is L_{j−1}G_j(w_j)R_j=0, and both interfaces have full respective column and row rank. Let v_j be a unit eigenvector of Q_j with eigenvalue β_j. Set

\[
 \begin{gathered}
 Z_1=v_1^T/\sqrt K,\quad
 Z_j=v_{j-1}v_j^T/\sqrt K\ (1<j<K),\quad
 Z_K=v_{K-1}/\sqrt K,\\
 H_j=Z_jQ_j^{-1}\ (j<K),\qquad H_K=Z_K.
 \end{gathered}
\]

Replace the zero target slice of each core by uH_j and leave every other slice unchanged. The resulting B(u) belongs to Θ_r for every real u. Expand B(u)−B_* by the nonempty set S of replaced cores. The terms u^{|S|}V_S are mutually orthogonal because they have different physical target patterns. For |S|=1, ||V_S||=||Z_j||=1/√K, so the first-order squared norm is u². The target is exactly

\[
 \langle A,B(u)\rangle
 =\frac{u^K}{K^{K/2}\prod_j\beta_j}.
\]

We bound the remainder uniformly. If S={i_1<...<i_s}, then contractions before its last site have operator norm at most ∏_{l<s}||H_{i_l}||_op; intervening left-orthonormal cores have operator norm one. At the last site, ||H_{i_s}R_{i_s}||=1/√K. Hence

\[
 \|V_S\|_F\le K^{-s/2}\beta^{-(s-1)}.
\]

Thus

\[
 u^2\le\|B(u)-B_*\|^2
 \le\beta^2\{(1+u^2/(K\beta^2))^K-1\}
 \le u^2\exp(u^2/\beta^2).
\]

For t≤β/2, u=t/√2 makes the final bound strictly smaller than t² and proves (G3). For the sharp limit use u=t exp{−t²/(2β²)}. Then u≤t and u² exp(u²/β²)≤t², while u/t→1 uniformly as t/β→0. This proves the matching lower limit. In (G2), the relative energy correction is at most binom(K,2)(t/β)²/(1−t/β)², and the denominator correction at most (1−t/β)^{−(K−1)}. This proves the claimed uniform sharp limit. ∎

## G2. A weak component added to a general TT background

For each mode take orthogonal subspaces E_j, span(v_j), span(w_j), where v_j,w_j are unit. Let C∈⊗E_j have exact positive TT ranks s_j and smallest nonzero singular values at least a_0>0. Set r_j=s_j+1 and

\[
 B_b=C+b\bigotimes_jv_j,\quad A=\bigotimes_jw_j,
 \qquad0\le b\le a_0.
\]

Orthogonality of both prefix and suffix factors makes the nonzero singular values at each cut the union of those of C and {b}; thus, for b>0, B_b has ranks r_j and β_j=b. Then, uniformly for every t>0 and 0<b≤a_0,

\[
 \omega_A(t;B_b)\asymp_K t\min\{1,(t/b)^{K-1}\}.
\]

The strong-bond leading coefficient is K^{−K/2}, and ω_A(t;B_0)=t. The background need not be diagonal, a product tensor, or a sum of two products. Rank profiles may vary across the chain.

**Proof.** For t≤b/2, (G2) supplies the upper bound C_Kt^K/b^{K−1}; otherwise the ambient upper bound t differs from the claimed rate by at most 2^{K−1}. For a lower bound use C+b⊗(v_j+u w_j). Its difference from B_b has squared norm b²{(1+u²)^K−1}; its target equals bu^K. It is feasible because a sum of a tensor of ranks s and a product has ranks at most s+1. Choose u²=(1+t²/b²)^{1/K}−1. Put x=t/b. For x≤1, the mean value theorem gives (1+x²)^{1/K}−1≥x²/(2K), yielding the lower constant (2K)^{−K/2}. For x≥1, the ratio of the expression in braces to x^{2/K} is (1+v)^{1/K}−v^{1/K}, v=x^{−2}≤1. This function decreases in v, so it is at least 2^{1/K}−1, giving a positive constant times t. At b=0, C+tA is feasible and attains the ambient bound. The sharp coefficient for t/b→0 follows from G1. ∎

## What these statements do and do not establish

The diagonal rank-two result is a special case with C=a e_0^{⊗K}. The new theorems extend both its geometry and its vanishing-component family. At a general fixed reference, the coefficient depends on every bond; for the weak-component family, all weakest bond singular values coincide, so a complete uniform transition is available.

Physical normality in every mode is essential. First-order tangent orthogonality alone does not imply order K. For example, a loading with only two active normal modes in a rank-one tensor model generally has order two. Likewise, losing rank at only one cut does not imply that adding an arbitrary product tensor respects every other cap. The all-bond weak-component construction supplies the needed feasible path.

The exact modulus constant is not an optimal confidence-interval constant. General dense loadings, partially normal loadings, simultaneous unequal rank losses and efficiently attainable sharp confidence constants remain open.

## Prior art and proof dependencies

The proof uses the standard left-orthonormal TT representation, singular values of its interface matrices, orthogonal physical-mode decompositions, Weyl's inequality and a feasible core perturbation. No external theorem about confidence intervals is imported into G1/G2. Relevant geometry precedents are [Kutschan, tangent cones](https://arxiv.org/pdf/1705.10152), [Wouters et al., higher-order MPS expansions](https://arxiv.org/pdf/1305.1761), and [Dolgov–Savostyanov, exact cross interpolation](https://cris.brighton.ac.uk/ws/files/6746392/1_s2.0_S0010465519302565_main.pdf). Novelty is the proposed sharp modulus/inference specialization; these underlying representations are established.
