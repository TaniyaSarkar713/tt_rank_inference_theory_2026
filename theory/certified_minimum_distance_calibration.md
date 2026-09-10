# Scope of minimum-distance calibration certificates

The finite-sample F calibration and optimized cross numerator are implemented in the revision. This note records additional exact facts for minimum-distance testing and a rigorous route to numerical certification. It does not claim that sharp product-mean confidence intervals have been solved.

## M1. Exact worst-case calibration for the zero-product null

Observe Z∼N_K(h,I), test H_0:∏h_j=0, and use T_0(Z)=inf_{u:∏u_j=0}||Z−u||². The null is a union of coordinate hyperplanes, so

\[
 T_0(Z)=\min_j Z_j^2.
\]

At least one coordinate h_j is zero under the null. Therefore P_h(T_0>c)≤P(G²>c). Let that coordinate remain zero and all other |h_i|→∞. Independence gives convergence of the rejection probability to P(G²>c). The exact worst-case level-α critical value is χ²_{1,1−α}. At h=0 the rejection probability is α^K, not α. This proves that high boundary coverage can coexist with optimal worst-case calibration of this particular statistic. It does not justify χ²_1 for nonzero product targets or for h_1h_2h_3+κh_1 when κ≠0.

## M2. A finite computation certificate for a general target null

Let g:R^K→R be continuous with nonempty closed level set H_θ={h:g(h)=θ}, and T_θ(z)=dist(z,H_θ)². Fix β,η>0 with β+η<α before examining the data. Let C_β(Z) be a confidence set for the full mean with coverage at least 1−β; for example the Gaussian ball of radius sqrt(χ²_{K,1−β}).

Suppose a finite collection of centers h_1,...,h_N covers C_β(Z)∩H_θ within Euclidean distance ρ. Centers need not be on the null. Suppose the following two computational bounds are available:

1. A certified lower bound L≤T_θ(Z).
2. For each fresh simulation Z_{jl}∼N(h_j,I), a certified upper bound U_{jl}≥T_θ(Z_{jl}).

The simulations must be independent of observed Z conditional on their data-dependent centers. Fix their sample count N_MC and the bounding algorithm conditional on the observed data and centers, so each center supplies identically distributed Bernoulli trials. Adaptive stopping requires a separate anytime-valid bound. Let q_j be an upper Clopper–Pearson bound with error probability η/N for the Bernoulli success count Σ_l 1{U_{jl}≥L}. Define

\[
 p_{\mathrm{cert}}=
 \min\left\{1,\max_jq_j+
             2\Phi(\rho/2)-1+\beta+\eta\right\}. \tag{M1}
\]

If the intersection is empty, use p_cert=β+η, provided emptiness itself is certified; otherwise retain a conservative value such as one. Then rejection when p_cert≤α has type-I error at most α for every h∈H_θ, jointly over data and calibration randomness.

**Proof.** With probability at least 1−β the true h lies in C_β(Z)∩H_θ. Conditional on observed Z, simultaneous Clopper–Pearson coverage fails with probability at most η by the union bound. On their intersection, choose a center h_j with ||h−h_j||≤ρ. Gaussian laws with identity covariance have total variation distance 2Φ(||h−h_j||/2)−1: the likelihood-ratio comparison depends only on the projection along their mean difference, and the two one-dimensional Gaussian half-space probabilities give this formula. Thus

\[
 \begin{aligned}
 P_h\{T_\theta(Z')\ge T_\theta(Z)\}
 &\le P_h\{T_\theta(Z')\ge L\}\\
 &\le P_{h_j}\{T_\theta(Z')\ge L\}+2\Phi(\rho/2)-1\\
 &\le q_j+2\Phi(\rho/2)-1.
 \end{aligned}
\]

The first quantity is a super-uniform tail p-value under h, including atoms if present. Rejection on the two successful events implies that this p-value is at most α−β−η. Add their failure probabilities β and η. ∎

This is a specialization of the confidence-set maximization principle associated with Berger–Boos, with explicit discretization, simulation and optimization errors. It is not a novel general p-value construction. For the cubic target, certified constrained-distance bounds and an efficient covering of the null intersection still need implementation. A local optimizer provides a feasible-point upper bound on distance, which is the wrong direction for L. Using it as an observed-distance lower bound can invalidate the test.

The theorem is per tested θ. To make a jointly computed confidence interval, one must also certify its inversion over the continuum of θ; a finite grid followed by unqualified endpoint interpolation is insufficient. Pointwise valid tests give coverage at the true θ, but numerical interpolation has to preserve their acceptance set.

## Current status

- **PROVED and implemented elsewhere:** finite-sample F calibration of selected-coordinate regression, optimized numerator with a one-dimensional root bracket, and no-longer-than-baseline intervals.
- **PROVED:** zero-product worst-case χ²_1 calibration and the conditional numerical certificate M2.
- **PARTIAL:** efficient nonzero-target minimum-distance calibration and its interval inversion. The certificate specifies what must be bounded, but does not supply an efficient cubic optimizer.
- **OPEN:** exact optimal expected length, or a small certified ratio to that optimum. The previous analytic brackets 3.61839 and 34.94889 remain brackets in a separate Gaussian experiment.

## Sources

[Berger and Boos, P Values Maximized Over a Confidence Set for the Nuisance Parameter](https://doi.org/10.1080/01621459.1994.10476836), JASA 89 (1994), 1012–1016; [institutional preprint record](https://repository.lib.ncsu.edu/items/1e8c580a-c3db-46f8-93a3-9b963e2c9171). The institutional full text was blocked during this pass; M2 is proved directly above rather than importing an unchecked theorem. Glazer and Stark, [Fast Conservative Monte Carlo Confidence Sets](https://doi.org/10.1080/10618600.2025.2526416), JCGS 35 (2026), 273–282, is a direct calibration competitor. Its [full author preprint](https://arxiv.org/pdf/2405.05238), titled *Fast Conservative Monte Carlo Confidence Intervals*, was examined: the nuisance-parameter discussion on PDF pages 32–33 explicitly includes confidence-set maximization and full-region projection; pages 17–21 treat algorithms under shape conditions on the p-value function. Simulation reuse across target values does not itself require simultaneous-test adjustment. Neither source supports novelty for M2.
