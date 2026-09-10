# Audit update, 8 September 2026

The original review below is retained. The current matrix has 28 entries, adding Devroye et al. (2016), Lugosi–Mendelson (2019), and bibliographic context for Bahadur–Savage (1956). The last source's full text was unavailable in this pass; the regression impossibility proof is self-contained. The loading-uniform TT modulus and median-localized finite-variance extension are assessed in [the focused audit](../audit/external_results_and_prior_art.md); no first claim is made for generic degeneracy, robust mean estimation, or confidence-region inversion.

# Skeptical literature assessment

Audience: theoretical statistics researchers. Evidence cutoff: 7 September 2026. Future work later in 2026 is not covered. Primary articles, author manuscripts, arXiv and official proceedings were used. Search absence is not a proof of novelty.

## Decision

The original proposal, framed as higher-order uncertainty quantification for a TT adapter, is **Incremental — reformulate**. Uniform inference under degeneracy, singular Wald laws, tensor tangent cones and bias-aware inference all predate it. The revised project is **Promising — theory requires further work**: the completed contribution is a fixed-dimensional classification of honest linear-functional length from cap-one TT cuts at rank-one signals, together with a tube threshold and a computable honest interval. No reviewed source states this combined classification, but a specialist could regard parts as consequences of known product geometry and modulus theory.

## Mathematical relationships

**Generic degeneracy.** [Chen–Fang](https://arxiv.org/pdf/1901.04861), [Pillai–Meng](https://arxiv.org/pdf/1505.01957), [Dufour–Renault–Zinde-Walsh](https://arxiv.org/abs/1312.0569) and [Bei–Navjeevan](https://arxiv.org/html/2602.07377v1) rule out claims to have discovered higher-order delta inference or the monomial Wald limit. The exact boundary and uniform neighborhoods are different questions. In particular, the Pillai–Meng calibration must be tested on local nonzero alternatives, not dismissed using only a poorly chosen Wald baseline.

**Geometry.** [Kutschan](https://arxiv.org/pdf/1705.10152) and [Yang–Gao–Yuan](https://arxiv.org/html/2511.22613v2) occupy general TT tangent geometry. [Araujo–Massarenti–Rischter](https://arxiv.org/pdf/1611.01674) supplies the known osculating block grading. Our additional structural calculation is the feasibility of minimal-degree elementary paths under every internal cap, even at an internally singular point. The six-mode example makes that scope explicit. It does not establish that internal singularity generates a new exponent.

**Honesty and approximation.** [Cai–Low](https://arxiv.org/pdf/math/0503662) supplies the modulus perspective. [Andrews–Mikusheva](https://economics.mit.edu/sites/default/files/publications/ecta12030-%20final%20version.pdf) already constructs geometry-based conservative inference. Bias and model neighborhoods are established in [Bonhomme–Weidner](https://arxiv.org/pdf/1807.02161) and the Armstrong papers in the matrix. Our tube sandwich is generic; the new candidate content is its contact-dependent scale in a specified TT class. Unknown eta is not silently estimated.

**Tensor inference and estimation.** [Xu–Chen–Han](https://arxiv.org/pdf/2501.16223) and [Ma–Xia](https://arxiv.org/pdf/2410.11225) provide much stronger high-dimensional regular inference than this draft. Our comparison concerns their nondegenerate alignment regime versus a zero-alignment boundary with fixed p. [Qin–Zhu](https://arxiv.org/html/2406.06002v2) already proves TT estimation guarantees. The revised project proposes no improved TT estimation rate.

**Other terminology.** Product-of-coefficients mediation, singular restrictions, nonlinear minimum distance, osculating varieties, weak-factor panels, low-rank completion confidence sets, and conformal tensor completion were searched. These are consequential competing viewpoints, not cosmetic related work. [Sun–Chen](https://doi.org/10.1080/10618600.2025.2554671) establishes existing TT-based predictive UQ, while the target here is a coefficient functional. The 2026 dual-channel preprint was checked at theorem level: its displayed AUC comparison guarantee has additional assumptions and an asymptotic limit.

## Exact gap and limits of novelty

Let q be the least nonzero loading degree after splitting at cap-one cuts. The candidate gap is the explicit theorem

    inf_(honest intervals over Theta_eta) E_B0[length]
       asymp (sigma/sqrt(n))^q/lambda^(q-1) + min(eta,sigma/sqrt(n)),

for every positive TT cap profile and original-mode rank-one B0, with a computable procedure attaining the exponent. No reviewed source gives this precise cap-profile rule with the approximation threshold. We do not claim an optimal constant, a growing-dimensional minimax rate, a general TT boundary theory, or novelty of the lower-bound technique.

## Coverage and stopping rule

The old 18-file, 519-page corpus review was retained and reassessed for this direction; see local_corpus_review.md. Current searches concentrated on missing mathematical neighbors rather than repeating compression benchmarks. Searches covered statistics/econometrics, ML theory, algebraic and variational geometry, information bounds, optimization, and tensor computational complexity. Fixed-dimensional Gaussian theory does not need a new empirical-process inequality; the closest generalization results are recorded rather than artificially invoked in proofs.

Targeted queries included: tensor train confidence rank inference 2026; tensor contact order inference; tensor train local modulus; first-order degeneracy uniform inference; singular Wald monomial; tensor train tangent cone second order; low-rank confidence set unknown variance; model misspecification sensitivity; tensor spectral norm hardness; Segre osculating spaces; conformal tensor completion. Two independent bounded literature lanes were reconciled with parent-source spot checks. Discovery stopped after the major competing theories had primary support and repeated targeted queries no longer changed the proposed scope. This is a thorough targeted survey, not exhaustive proof that no unpublished or inaccessible result overlaps.

## Source caveats

Bei–Navjeevan's HTML date and version metadata differ; we record the displayed August 2026 manuscript but do not infer a separate arXiv revision. Dufour theorem-number details refer to an author version. Sun–Chen is online 2025 and in the 2026 journal issue. A publisher fetch initially failed but its full article was recovered through search. Bibliographic publication status is separated from the version used for mathematical reading. The local surveys and adjacent ML papers were reviewed for relevant guarantees; their complete proofs were not all independently certified.
