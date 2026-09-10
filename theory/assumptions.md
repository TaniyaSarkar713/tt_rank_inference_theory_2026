# Revised assumption set, 8 September 2026

The complete necessity/relaxation/counterexample table is [audit/assumption_audit.md](../audit/assumption_audit.md), with a separate [relaxation matrix](../audit/assumption_relaxation_matrix.md). The reconstructed experiment and identifiability analysis are in [reconstructed framework](../audit/reconstructed_framework.md).

The geometric core fixes finite real mode dimensions and positive specified TT caps. Length is evaluated at an original-mode rank-one B0=lambda⊗u_k with unit factors and lambda>0. The actual coefficient coverage class contains all ranks under the caps and a known eta coefficient-distance tube. The bounded presentation uses ||B||≤M and lambda<M/2; the unbounded-class corollary removes this norm cap. The local scale must remain small relative to lambda. Constants are allowed to depend on dimensions and confidence level, but are uniform over deterministic loadings and unit signal directions.

The common confidence event gives coverage for every loading simultaneously. The all-degree expected-length formula is uniform over deterministic loadings, including A_n, but does not allow factoring loading weights from localization moments for an arbitrary data-selected loading. Coverage for a selected random target is distinct from coverage conditional on its selection event. A=0 has trivial modulus/interval; q is defined only for nonzero A.

| Branch | Design | Noise assumptions | Localization | Sample/moment condition | Guarantee |
|---|---|---|---|---|---|
| Primary Gaussian | Iid N_p(0,I) | Independent N(0,sigma²), sigma known or unknown | OLS chi-square or residual-F ball | n>p for residual coverage; n≥p+max(J,2) for proved moments | Conditional simultaneous coverage and matched uniform loading length |
| General-design Gaussian | Common design law with S positive definite | Conditional N_n(0,sigma²I) | Same pivots | E S≤LnI; E lambda_min(S)^(-k/2)≤C_k n^(-k/2) through max(J,2) | Same scale with design constants; row dependence permitted |
| General covariance-bound errors | Arbitrary full-rank X | E(ε|X)=0; Cov(ε|X)≤sigma_bar²I with known bound | OLS Markov ball | E tr(S^-1)≤C/n for length | Conditional coverage; proved degrees capped at two |
| Independent finite-variance errors | Iid Gaussian design | Iid pairs; conditional error mean zero and variance≤sigma_bar²; known bound | Coordinate median of g independent group OLS fits | h=floor(J/2)+1, g=2h−1, floor(n/g)≥2p+2 | Unconditional simultaneous coverage; full contact order and worst-noise matched expected length |
| Abstract transfer | Any experiment with a valid ball | Encoded in ball guarantee | Any measurable (z,e) | E(||z−b0||+e)^k≤C r_n^k through m | Coverage; degrees truncated at m in proved upper bound |

These branches must not be combined into a claim with the weakest design, noise, sample size and rate from different rows. In particular the independent finite-variance theorem does not supply conditional-on-design coverage, unknown-variance adaptation, or arbitrary dependent-noise validity. C12 shows a nonshrinking-length obstruction if the variance-bound requirement is removed with no other distributional restriction.

Fixed dimension is a rate-theorem restriction, not an assertion that p≥n is unidentifiable in every structured model. The current OLS-based algorithms need enough observations per fitted ambient regression. No sparse model, contamination guarantee, rank-recovery theorem, bootstrap guarantee or neural-network generalization bound is implied.
