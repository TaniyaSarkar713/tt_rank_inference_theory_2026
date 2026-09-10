# Revised theorem ledger, 8 September 2026

PROVED means a complete internal derivation with explicit assumptions and checks. VERIFIED is the audit's corresponding result-level judgment. Neither label is formal verification, independent peer review, or a novelty certificate. The historical candidate statements in `proposals_v1.md` are preserved as historical documents only.

The full 17-result inventory, including every numbered lemma, original status, sharpness and final label, is in [theorem inventory](../audit/theorem_inventory.md). The final printed number map is in `../audit/theorem_number_map.json`. The mathematical statements in `paper/sections/theory.tex`, `paper/sections/extensions.tex` and the appendices are canonical.

Let a_l=||Π_l A|| and R_A(t)=(a_0+a_1)t+Σ_{l=2}^J a_l t^l/lambda^{l−1}.

| Stable ID | Status | Final statement | Scope |
|---|---|---|---|
| R1 / old T1 | PROVED / VERIFIED | omega_A(t) ≍ R_A(t), uniformly in deterministic loading and unit factors; fixed-A order q follows; pure elementary leading coefficient q^(−q/2) | Fixed dimensions/caps; original-mode rank-one point; 0<t≤lambda/2 |
| R2 / old T2 | PROVED / VERIFIED | Slack at every cut gives omega_A(t) ≍ t for nonzero A | Any interior coefficient with at least one rank of slack at every cut; constants not efficient variance |
| R3 / old T3,T4 | PROVED / VERIFIED | L ≍ R_A(t_n)+||A||min(eta,t_n) | Gaussian model, n≥p+max(J,2), local signal; uniform deterministic A_n allowed |
| R4 / old T6 | PROVED / VERIFIED | Undetectable departures force length eta in the intermediate regime | Global tube honesty; unit loading; s_n≪eta_n≪t_n |
| R5 / old T7 | PROVED / VERIFIED | Full-normal cubic coefficient = ||T||inj/(3√3) | Unrestricted three-block product model; inherited norm hardness only |
| R6 / old T5 | PROVED / VERIFIED | Energy certificate is honest and attains R3; shared event covers all loadings, including selected random targets | Gaussian conditional pivot; weighted expected-length theorem stated for deterministic A |
| R7 / old T8 | PROVED / VERIFIED | Cubic shifted-Gaussian Wald experiment and iterated coverage limit 2Φ(z/3)−1 | Fixed c,lambda,sigma,p; supporting specialization of existing theory |
| R12 | PROVED / VERIFIED | Any honest confidence ball transfers coverage and moment-limited expected length; degree l becomes min(max(1,l),m) with only m localizer moments | No distributional assumption beyond the explicit ball and moment premises |
| R13 | PROVED / VERIFIED | Same scale under arbitrary common design laws with information and inverse-Gram moment bounds | Conditional Gaussian errors; includes well-conditioned deterministic and Gaussian-covariance designs |
| R14 | PROVED / VERIFIED | Known conditional covariance bound gives Markov-ball coverage and degree-capped upper bound through order two | Can permit dependent errors satisfying the bound; not optimality for this larger noise class |
| R15 | PROVED / VERIFIED | Norm cap removable | Unbounded closed TT class; lambda>0 and local conditions remain |
| R16 | PROVED / VERIFIED | Energy coefficients sqrt(C(J,l))/J^(l/2); interval length never exceeds the original on the same dataset | Deterministic product-chart inequality; entire interval constants not sharp |
| R17 | PROVED / VERIFIED | Median of independent-group OLS gives the full R_A(tbar_n)+||A||min(eta,tbar_n) rate under finite conditional variance; matching inf-I sup-noise expected-length order | Iid pairs, Gaussian design, known variance upper bound; groups k≥2p+2; unconditional coverage over design |

Supporting baseline lemmas R8–R11 (block factorization, two-point bound, OLS moments, HOSVD/projector mixing) all have complete proofs. The Gaussian sufficient sample condition has been weakened from n≥2p+2J+8 to n≥p+max(J,2). The median procedure has its own explicit group-size condition; it does not inherit the smaller Gaussian threshold.

Twelve counterexamples and failure mechanisms are proved in `paper/appendix_counterexamples.tex`. C12 establishes that uniformly honest shrinking intervals cannot cover the union of all finite conditional variance bounds without a bound or additional noise-family restrictions. It is an explicit regression adaptation of a classical nonparametric impossibility mechanism, not a new general impossibility principle.

PARTIAL: sharp growing-dimensional constants and computationally optimal calibration. OPEN: general higher-rank TT contact geometry; fast rates under sufficiently broad dependent-noise models; unknown variance under additional specified tail restrictions; expected-length adaptation for arbitrary selected loadings. No universal rates for these problems are asserted.
