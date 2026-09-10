# Finite-sample calibration and inference from selected cross entries

Status: **PROVED** for the statements below. Exact finite-sample coverage means a mathematical probability guarantee under the stated Gaussian experiment, not equality of coverage to the nominal level at every parameter. Numerical code uses floating-point arithmetic and is separately checked; it is not a formal machine-arithmetic proof.

## C1. A regression with only the required coordinates

Consider independent x_i∼N_p(0,I_p), Y_i=〈x_i,B〉+ε_i, ε_i∼N(0,σ²), σ>0 unknown. Let Θ_2 be the all-rank-at-most-two TT class from the audited rank-two note. Fix its cross pivots S_k, target slices C_j and target A=e_2^{⊗K} before looking at inference data.

Let F be the set of distinct tensor coordinates used by all S_k, all C_j and A. There are exactly

\[
 m=|F|=2K+(4K-4)+1=6K-3
\]

coordinates: the two diagonal pivot entries are shared by all cuts, each cut adds two distinct off-diagonal pivot entries, the target slices are disjoint, and the target entry is new. Let θ=B_F and W=(x_{i,F})_{i=1}^n. Then

\[
 Y=W\theta+\xi,\qquad
 \xi\mid W\sim N_n(0,\tau_B^2I_n),\qquad
 \tau_B^2=\sigma^2+\|B_{F^c}\|^2.
\]

**Proof.** The Gaussian coordinate blocks x_{i,F} and x_{i,F^c} are independent. The omitted linear predictor is independent Gaussian noise with the displayed variance. Independence holds across observations. This is conditional on W, not on the full original design. ∎

The vector θ is not falsely asserted to be a TT tensor. It is a vector of coordinates satisfying the cross relation inherited from the original B. This relation is all the procedure requires. The variance τ_B, rather than σ, must be estimated in this regression.

## C2. Exact calibration with unknown effective variance

For n>m define

\[
 \begin{gathered}
 S=W^TW,\quad z=S^{-1}W^TY,\quad
 \widehat\tau^2=\|Y-Wz\|^2/(n-m),\\
 e=\widehat\tau\sqrt{mF_{m,n-m;1-\alpha}/\lambda_{\min}(S)}.
 \end{gathered}
\]

Then P_{B,σ}(||z−θ||≤e | W)≥1−α, uniformly over every B and σ>0. Indeed, conditional on W, S^{1/2}(z−θ)/τ_B is standard normal, RSS/τ_B² is χ²_{n−m}, and these are independent orthogonal projections of Gaussian noise. Their ratio gives

\[
 \frac{(z-\theta)^TS(z-\theta)}{m\widehat\tau^2}
       \sim F_{m,n-m}.
\]

The ellipsoid event implies the ball event by λ_min(S)||z−θ||²≤(z−θ)^TS(z−θ). Thus the finite-sample critical value is calibrated without a rank-selected reference distribution or a nuisance-parameter grid.

Extract all cross slices from z using their coordinate maps. If d_k=σ_min(S_k(z))−e>0 for every k, define the old numerator P_old=∏_j(c_j+e), c_j=||C_j(z)||_F, and denominator D=∏_k d_k. Intersect [−P_old/D,P_old/D] with [z_A−e,z_A+e], using the singleton {z_A} if empty. If any d_k≤0 use [z_A−e,z_A+e]. The cross identity proves coverage on the common ball event for every B∈Θ_2.

## C3. An optimized numerator certificate

The disjoint target slices share the same error budget. On the ball event, δ_j=||C_j(θ)−C_j(z)|| satisfies Σδ_j²≤e². Replace P_old by

\[
 P_*(c,e)=\max_{\delta_j\ge0,\ \sum_j\delta_j^2\le e^2}
                   \prod_{j=1}^K(c_j+\delta_j). \tag{C1}
\]

This replacement preserves coverage and cannot increase interval length on any dataset. It optimizes the numerator relaxation, not the entire confidence-region image: errors in the pivots also consume budget, which this relaxation does not exploit.

For e=0, P_*=∏c_j. For e>0 the unique optimizing δ has

\[
 \delta_j(\mu)=\frac{\sqrt{c_j^2+4\mu}-c_j}{2},\qquad
 \sum_j\delta_j(\mu)^2=e^2,\quad\mu>0. \tag{C2}
\]

**Proof.** A positive feasible product exists. Its log is strictly concave on positive factors and increases in every δ_j, so the constraint is active. At an optimum every δ_j>0: with c_j>0, the derivative at δ_j=0 is positive while the ball's derivative in that coordinate is zero; with c_j=0 a positive product requires δ_j>0. The Lagrange equations are 1/(c_j+δ_j)=2λδ_j, λ>0. Set μ=(2λ)^{-1} to obtain (C2). Its left side is continuous, strictly increasing from zero to infinity, proving existence and uniqueness. Concavity makes this stationary point the global optimum. ∎

Bisection provides an explicit certificate. Start with μ_l=0 and μ_u=e²+e max_j c_j; the latter gives δ_j(μ_u)≥e, hence Σδ_j²≥e². Maintain the bracket and stop when

\[
 \frac{\prod_j(c_j+\delta_j(\mu_u))}
      {\prod_j(c_j+\delta_j(\mu_l))}\le1+\varepsilon.
\]

The two products bracket P_*; use the upper product. To retain dataset-wise dominance over the old numerator even with a deliberately loose stopping tolerance, take its minimum with P_old. Both quantities are valid upper bounds. The stable formula δ_j=2μ/(sqrt(c_j²+4μ)+c_j) avoids cancellation. Exact-arithmetic certification and the numerical stopping tolerance are different statements; the code records the achieved bracket ratio.

If c_j=0 for every j, P_*=e^K/K^{K/2}, whereas P_old=e^K. This is a deterministic bound on a particular input, not an asserted average efficiency factor.

## C4. A complete growing-dimension weak-bond theorem

Let B_b=a e_0^{⊗K}+b e_1^{⊗K}, 0≤b≤a, in arbitrary dimensions d_j≥3. Fix 0<α<1/2 and K≥3. With n≥m+max(K,2) and t_n=σ/√n, the procedure above, including its optimized-numerator version, is globally honest over Θ_2 and all σ>0 and satisfies

\[
 E_{B_b,\sigma}|I_n|\le C_{K,\alpha}
 t_n\min\{1,(t_n/b)^{K-1}\}. \tag{C3}
\]

The constant is independent of p, the d_j, a and b. At b=0 interpret the right side as C t_n. The corresponding pointwise optimal expected length under global honesty has the same order, with dimension-free lower constants. This combines the weak-bond theorem with growing ambient dimensions and requires neither a global tensor optimizer nor n>p.

**Proof of moments.** At B_b, all nonzero coefficients are in F, so τ_{B_b}=σ. The compressed experiment has fixed dimension m. Conditional Gaussianity and the residual independence above reduce moments of ||z−θ|| and e to inverse moments of λ_min(S), with S∼Wishart_m(n,I). For each diagonal entry of S^{-1}, the reciprocal has χ²_{n−m+1} law by residualizing one design column against the others. Its order k/2 inverse moment equals 2^{−k/2}Γ((n−m+1−k)/2)/Γ((n−m+1)/2), finite when n−m+1>k. Since λ_min(S)^{-1}≤tr(S^{-1}), sum-power inequalities give E λ_min(S)^{−k/2}≤C_{m,k}n^{−k/2} for 2≤k≤K; Jensen and the second moment give k=1. Positive moments of RSS/(n−m) are bounded, and F quantiles remain bounded for fixed m,α and n−m≥max(K,2). Hence E(||z−θ||+e)^k≤C_{K,α}t_n^k for k≤K. The gamma-ratio bound follows from its finite limit after multiplication by n^{k/2} and boundedness over the remaining finitely many admissible integer n; this is sufficient because m,K are fixed.

**Proof of length.** Put T=||z−θ||+e. At B_b, C_j(θ)=0 and each pivot's smallest singular value is b. On T≤b/2 the old interval length is at most 2^K T^K/b^{K−1}. On T>b/2, it is at most 2e≤2T≤2^K T^K/b^{K−1}. It is always at most 2e. Take expectations and the smaller of these two bounds. The optimized interval is no longer on every outcome. At b=0 the ambient bound suffices.

**Proof of lower bound.** Conditional on a design row, the two response means differ by 〈x,B−B'〉. The conditional normal KL is its square divided by 2σ²; expectation over x gives ||B−B'||²/(2σ²), and independence multiplies this by n. Thus the full-data KL is n||B−B'||²/(2σ²), regardless of ambient dimension. The feasible weak-component path in the rank-two proof gives target displacement Δψ at least a constant times t min{1,(t/b)^{K−1}} at distance t. For a globally honest interval, under B the probability it contains both ψ(B) and ψ(B') is at least 1−2α−TV(P_B,P_B'): transport coverage of ψ(B') from P_B' to P_B, then use a union bound. Hence E_B|I|≥|Δψ|[1−2α−TV]. Choose t=(1−2α)σ/√n. Pinsker gives TV≤(1−2α)/2, and the bracket is positive. Finally f(ct,b)≥c^K f(t,b) for 0<c≤1 and f(t,b)=t min{1,(t/b)^{K−1}}. This proves the matching lower bound for every globally honest procedure, including procedures that use all covariates. ∎

This is a prespecified-coordinate result. It does not prove that one procedure adapts at the same cost to every unknown rotation of B_b. The selected features are fixed parts of the procedure, not true directions supplied after observing the parameter. Global honesty nevertheless holds at rotated tensors; only the short-length assertion is restricted to the stated family.

## C5. Extension to other fixed cross patterns

For caps r, use fixed nonsingular crosses with target-slice coordinates disjoint from pivots and one another. The number of selected coordinates is at most

\[
 1+\sum_{k=1}^{K-1}r_k^2+\sum_{j=1}^K r_{j-1}r_j.
\]

The same coverage and optimized-numerator proofs apply. If all target slices vanish at a reference, the effective noise is τ_*²=σ²+||B_{*,F^c}||² and pivot strengths, rather than full unfolding singular values, control the interval's length. When these strengths are between γ and κγ for fixed κ, the same proof gives an upper bound C_{K,r,α,κ}(τ_*/√n)min{1,(τ_*/(γ√n))^{K−1}}. This is an upper bound; no general weak-pivot lower bound is asserted. A pivot can become small because a particular cross is poor even when the full unfolding remains well conditioned.

## Calibration status

Finite-sample F calibration, the numerator maximization and dataset-wise length dominance are proved. Exact optimal expected-length constants remain unknown. A sharper likelihood-ratio calibration is a separate problem; the existing cubic benchmark and generic minimum-distance literature do not establish a universal χ²_1 reference distribution for all nonzero product targets.
