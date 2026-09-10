# Strengthening the tensor-rank inference project

The strongest next paper should focus on **how several compatible tensor-rank constraints change the inferential effect of a weak bond**. Dimension reduction and sharper calibration should support that statistical question. Further noise-model extensions and an LLM demonstration are lower priorities.

Three development notes now provide concrete progress beyond the completed audit. Their complete internal proofs are separate from the audited manuscript; its verdict and numbered inventory remain a historical snapshot. Publication novelty is still provisional.

## 1. A stronger statistical phenomenon

The previous result evaluated original-mode rank-one tensors and obtained higher contact order from cap-one block factorization. The new example has every cap equal to two:

\[
 \Theta_2=\{B:\operatorname{rank}(B^{[k]})\le2\ \forall k\},\quad
 B_b=a e_0^{\otimes K}+b e_1^{\otimes K},\quad
 A=e_2^{\otimes K},\quad0\le b\le a.
\]

For b>0 every TT bond has rank two and smallest singular value b. The new internally proved results are

\[
 \omega_A(t;B_b)\asymp_K t\min\{1,(t/b)^{K-1}\},\qquad
 \omega_A(t;B_b)\sim\frac{t^K}{K^{K/2}b^{K-1}}
 \quad(t/b\to0).
\]

Each single matrix unfolding instead gives order t min(1,t/b), with leading term t²/(2b). For four modes, this is **quartic versus quadratic**, without rank-one cuts. A computable interval based on cross slices gives the matching fixed-dimensional honest-length scale

\[
 L_{\alpha,n}(B_b;\sigma)\asymp
 t_n\min\{1,(t_n/b)^{K-1}\},\qquad t_n=\sigma/\sqrt n.
\]

Thus four-way inference has length order σ⁴/(b³n²) when b≫σ/√n and order σ/√n when b≲σ/√n. The procedure is honest over the entire rank-capped class, including points outside the displayed diagonal family. These are proved statements in the new note, not conjectured rates.

This is a stronger answer to the matrix-embedding criticism. Exact TT cross interpolation and higher-order matrix-product-state geometry are prior tools.[^cross][^mps] The candidate contribution is the sharp modulus, the weak-bond transition and its honest-inference consequence, subject to further novelty review.

**Next theorem:** replace the diagonal family by a class of TT points with invertible cross pivots. Identify which products of perturbed cross slices can first be nonzero, then prove a loading-uniform modulus with quantitative dependence on weak pivot singular values. An upper bound over every nearby feasible tensor and an attaining feasible path are both required. A Taylor expansion alone does not solve the problem.

Full derivation: [active rank-two modulus](../theory/active_rank_two_modulus.md).

## 2. Growing dimension through compression

The current OLS-based manuscript needs n>p. Replacing p by a TT parameter count in an existing formula is unjustified. In particular, applying a functional modulus to a Frobenius radius σ√(d_eff/n) need not give the optimal functional rate.

For the block-product special case, a more targeted route now has a complete existence proof. Let A=w_1⊗⋯⊗w_J. Learn directions h_j⊥w_j using training data, then regress on the product subspace ⊗_j span(h_j,w_j) using independent inference data. Its dimension is 2^J. The target is preserved exactly and the Gaussian residual variance becomes

\[
 \sigma_P^2=\sigma^2+\|(I-P)B\|^2.
\]

This variance identity is already used in ISLET.[^islet] The additional target is globally honest higher-order functional length. With a global rank-one least-squares pilot, fixed J, and signal and noise scales in fixed compact subsets of (0,∞), the new note proves that

\[
 n\ge C\{\textstyle\sum_jD_j+\log n\}
 \quad\Longrightarrow\quad
 \sup_{B_0\in\mathcal N_D(\lambda)}E|I_n|
 \lesssim\frac{\sigma^J}{\lambda^{J-1}n^{J/2}}.
\]

Here N_D(λ) consists of unit-product directions orthogonal to w_j in every block, with amplitude λ. Coverage is uniform over the full block-product model and every σ>0. The lower bound matches. The explicit finite-sample theorem states the dependence on σ²/λ² and the training-failure probability; the sample constant above includes the fixed signal-to-noise restrictions.

For four-way caps (1,2,1), training complexity involves d_1+d_2d_3+d_4 instead of p=d_1d_2d_3d_4; the inference regression has eight coefficients. This is a growing-dimension special case. It keeps J fixed and is not a theorem for arbitrary TT loadings or rank profiles.

**Next steps:** replace the global tensor optimizer by a computationally certified pilot, carrying through its actual initialization and signal conditions. Then combine compression with the all-rank-two weak-bond example. The two new proofs currently address different branches and must not be presented as an already unified theorem.

The difficult statistical gap is a sharp characterization of

\[
 \inf_{I\ \mathrm{globally\ honest}}
       \sup_{B_0\in\mathcal N_D(\lambda)} E_{B_0}|I|
\]

outside the sufficient orientation-learning regime. A pointwise infimum can hide the cost of learning unknown directions, because a globally valid procedure may be optimized for one preselected reference point. The supremum makes adaptation explicit. Mixture lower bounds are needed to decide whether a dimension penalty is necessary. No weak-regime rate or sharp dimension threshold is established yet.

Full construction: [growing-dimension compression](../theory/growing_dimension_compression.md).

## 3. Constants require calibrated inference

The audit's energy improvement shortened one cubic interval by about 76%, but its mean length remained about 389 times the bare rate scale, with 2,000/2,000 observed coverages. This is evidence of conservatism. The number 389 is not a ratio to a known exact optimum.

Separate the cost of a simultaneous confidence ball, the bound on its nonlinear image, and the critical value needed for uniform inference. The new rank-two modulus already has a sharp leading constant, so interval conservatism cannot be attributed entirely to an unknown geometric coefficient.

For a focused calibration problem, take Z∼N_3(h,I) and g_κ(h)=h_1h_2h_3+κh_1. This includes the cubic target and the tangent/normal transition. The new benchmark note proves

\[
 3.61839\le\inf_{I\ \mathrm{honest}}E_0|I|\le34.94889
 \quad(\alpha=.05,\ \kappa=0).
\]

These are analytic brackets in a Gaussian limiting experiment, not exact optimal constants or a claimed regression improvement factor. Next optimize minimum-distance inversion with a rigorous supremum over each nuisance level set. Curvature calibration and inference under degeneracy have strong precedents.[^am][^bei] A finite grid of nuisance values is a diagnostic, not proof of uniform coverage. The objective is a certified length ratio to a valid benchmark and uniform validity through the transition. Transfer back to regression, including estimated scale and anchors, remains additional work.

Exact decision problem: [Gaussian product benchmark](../theory/gaussian_product_benchmark.md).

## 4. Experiments tied to the new theorems

| Question | Controlled experiment | Evidence |
|---|---|---|
| Higher-rank weak-bond transition | Four modes, d_j=3, all caps two; vary b/t_n | Coverage and length of the cross interval versus single-unfolding baselines; compare with t_n min{1,(t_n/b)³} |
| Inference with p>n | Four-way (1,2,1), growing block dimensions; report ΣD_j/n and p/n | Coverage, pilot error, effective residual variance, length, training failures and actual solver qualifications |
| Source of conservatism | Paired ball inversion, certified image bounds and minimum-distance inversion | Paired length ratios, local worst-case coverage, calibration error |

Use at least 5,000 evaluation replications per key setting when distinguishing coverage differences near one percentage point: the Monte Carlo standard error at 95% is about 0.31 percentage points. Report binomial intervals and paired uncertainty. Separate calibration and evaluation random streams. No new large Monte Carlo study has been run for these development notes.

## 5. Novelty and publication gates

A newly checked Statistica Sinica accepted paper already develops covariance-weighted projection inference and a local geometric length lower bound. Its Theorem 1 explicitly requires positive first-order variance.[^ke] This reinforces the need to center our claim on vanishing first-order variance and compatible TT constraints. Generic higher-order inference, projection efficiency and tensor sketching are already occupied topics.

| Venue | What would materially strengthen the case |
|---|---|
| Annals of Statistics | A general boundary-dependent inference principle, matched bounds across growing dimensions or weak identification, and a meaningful class beyond one diagonal example |
| JASA / JRSS-B | A usable honest procedure with competitive length, a broader range of tensor points, and practical evidence tied to the model assumptions |
| Biometrika | A focused sharp result, such as the all-rank-two transition with certified calibration and a clean single-unfolding comparison |
| Bernoulli / Statistica Sinica | A coherent theory contribution with complete uniformity and clear separation from regular tensor inference |
| COLT / ML theory | A dimension/SNR phase diagram or an actual computational-statistical separation |

**Recommended order:** independently audit and challenge the novelty of the all-rank-two result; generalize its cross-slice argument; certify calibration; then unify it with growing-dimension inference. Efficient pilots and large experiments should follow exact theorem assumptions. The project remains **Promising**, with a stronger mathematical basis than at verdict B, but a submission recommendation is premature.

## Sources

[^cross]: Dolgov and Savostyanov, [Parallel cross interpolation for high-precision calculation of high-dimensional integrals](https://cris.brighton.ac.uk/ws/files/6746392/1_s2.0_S0010465519302565_main.pdf), accepted 2019, Theorem 2 and equation (5).
[^mps]: Wouters, Nakatani, Van Neck and Chan (2013), [The Thouless theorem for matrix product states and subsequent post-density matrix renormalization group methods](https://arxiv.org/pdf/1305.1761), Sections VI–VII.
[^islet]: Zhang, Luo, Raskutti and Yuan (2020), [ISLET: Fast and Optimal Low-Rank Tensor Regression via Importance Sketching](https://arxiv.org/pdf/1911.03804), Theorem 4, Remark 5 and supplementary projection-noise calculations.
[^am]: Andrews and Mikusheva (2016), [A Geometric Approach to Nonlinear Econometric Models](https://economics.mit.edu/sites/default/files/publications/ecta12030-%20final%20version.pdf), curvature-based minimum-distance inference.
[^bei]: Bei and Navjeevan (2026), [Inference under First-Order Degeneracy](https://arxiv.org/html/2602.07377v1), Sections 3–4. The arXiv metadata and HTML displayed date differ; no unverified revision chronology is inferred.
[^ke]: Ke, Song, Zhao and Wang, [Efficient Inference for Low-rank Regression via Covariance-Weighted Projection](https://www3.stat.sinica.edu.tw/ss_newpaper/SS-2026-0222_na.pdf), accepted preprint SS-2026-0222, Theorems 1–3; publisher record checked 8 September 2026, with no final issue assignment inferred.
