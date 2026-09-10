# Mathematical setup and assumptions

## Observations and distribution

Observe independent pairs (X_i,Y_i), i=1,...,n, with X_i in R^(d1 x ... x dK), x_i=vec(X_i) in R^p, p=product(dk), and Y_i=x_i' b + epsilon_i. The main rate experiment has x_i iid N_p(0,I_p), epsilon_i iid N(0,sigma²), independent of all designs. There are no latent structural factors in the observation model; tensor cores/factors are nonunique parameterizations of the observable coefficient B. Noise is unobserved. Vectorization is fixed NumPy C order, retaining mode order.

The noise standard deviation is either known or estimated from full ambient OLS residuals. Finite-sample interval coverage is conditional on any full-column-rank design under independent homoskedastic Gaussian errors. Gaussian identity random design is used for the KL expression and expected-length bounds.

Loss ell(B;x,y)=(y-x'vec(B))²/2. Under identity covariance, population excess risk is R(B)-R(B*)=||B-B*||_F²/2. Empirical risk is the sample average. Ambient OLS minimizes this empirical risk when n>p. The product HOSVD pilot is a computable approximation, not a claim to solve globally constrained TT least squares.

## Parameter spaces and target

Positive integer caps rbar_1,...,rbar_(K-1) are specified independently of the data. Theta0={B: rank(B^[k])<=rbar_k for every prefix unfolding, ||B||_F<=M}, M>0. Theta_eta={B: ||B||_F<=M, dist_F(B,Theta0)<=eta}, where eta>=0 is a known upper bound on structural approximation error. This is coefficient misspecification, not Huber contamination of observations.

A deterministic nonzero loading A defines psi_A(B)=<A,B>. Honesty means inf over B in Theta_eta and, for the unknown-noise procedure, sigma>0 of coverage >=1-alpha, 0<alpha<1/2. L is the infimum of expected interval length at a specified B0 over all measurable honest intervals. Intervals may be data-dependent; no regularity restriction is used for the length lower bound.

At the evaluation point B0=lambda u1⊗...⊗uK, original factors have unit norm and 0<lambda<M/2. Cuts with cap one determine consecutive blocks. Internal caps are at least two. The actual internal TT variety may be singular. Loading contact order is defined through the block projectors in theorem_statements.md.

## Regime and necessity

| Assumption | Role | Standard or restrictive? | Possible weakening |
|---|---|---|---|
| Fixed K, dimensions and rank caps | Controls constants and OLS inverse moments | Restrictive; no growing-p minimax theorem claimed | Requires intrinsic localization and dimension-dependent lower bounds |
| n>=2p+2J+8 | Sufficient for inverse-Wishart moments through degree J | Convenient, stronger than n>p needed for coverage | Moment threshold can be sharpened |
| sigma/sqrt(n)<=c lambda | Keeps lower-bound alternatives local and signal nonzero | Natural local condition | At weaker signal a separate transition analysis is needed |
| Rank-one evaluation point in original modes | Makes elementary within-block rank-two paths feasible | Main structural restriction | Non-rank-one TT points are open |
| Cap-one cuts known to be valid, or known eta tube | Determines which directions are excluded | Substantive and fragile | Cannot replace by an unvalidated rank pretest |
| Known nonrandom A | Avoids loading-selection and loading-estimation uncertainty | Common for functional inference | Independent estimated loadings need an extra error term |
| Gaussian homoskedastic errors | Gives exact chi-square/F confidence ball | Restrictive finite-sample assumption | Other honest localization regions could replace it |
| Identity Gaussian random design | Gives isotropic KL and tractable expected moments | Restrictive rate theorem | Well-conditioned covariance should permit norm-equivalent constants; not asserted without proof |
| Norm cap and lambda<M/2 | Compactness, attained distances, local alternatives inside class | Technical plus model specification | Local interior margin could replace M/2 |
| Nonzero loading | Makes contact order finite | Necessary | A=0 has trivial interval {0} |

The primary asymptotic regime fixes geometry, lambda, sigma and M while n increases; eta=eta_n may shrink. Quantitative inequalities display signal and noise scaling but do not suppress dimension dependence in constants. No sparsity, independence of tensor entries, contamination tolerance or rank-recovery guarantee is assumed or claimed.
