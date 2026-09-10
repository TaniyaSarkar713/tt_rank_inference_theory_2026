# Closest references and reading order

Checked 10 September 2026 against the project's September 9 manuscript. This folder contains eight papers and one supplement, downloaded from publisher or arXiv sources. The order below is a relevance assessment for this project, not an exhaustive novelty verdict.

**Start with Ke, Song, Zhao and Wang (2026), _Efficient Inference for Low-rank Regression via Covariance-Weighted Projection_.** It is the closest statistical comparison among the inspected papers because it combines structured regression, linear-functional inference, local geometry, and a confidence-length lower bound. For the geometric argument itself, read Wouters et al.; for inference near a vanishing first derivative, read Bei and Navjeevan.

| Order | Paper and local copy | Connection and difference | Where to start in the downloaded PDF |
|---|---|---|---|
| 1 | Ke, Song, Zhao and Wang (2026), [Efficient Inference for Low-rank Regression via Covariance-Weighted Projection](01_ke_2026_covariance_weighted_projection.pdf); [supplement](01_ke_2026_supplement.pdf); [publisher record](https://www3.stat.sinica.edu.tw/statistica/fp/SS-2026-0222.html). | Covariance-weighted tangent projection, one-step inference, and a local interval-length lower bound. The normal-limit theory requires positive projected variance. This project's fully normal targets instead have zero first-order variance and require higher-order TT geometry. | Theorems 1–2, PDF p. 18; Theorem 3, PDF p. 21. |
| 2 | Xu, Chen and Han (2025), [Statistical Inference for Low-Rank Tensor Models](02_xu_2025_low_rank_tensor_inference.pdf); [arXiv record](https://arxiv.org/abs/2501.16223v1). | Direct tensor-functional inference with debiasing and tangent projection for Tucker models. Its alignment requirement keeps the leading variance from degenerating. The current project studies a different loading regime and TT rank constraints. | Corollary 3.1 and alignment condition (10), PDF p. 10; studentization in Theorem 3.3, PDF p. 15. |
| 3 | Bei and Navjeevan (2026), [Inference under First-Order Degeneracy](03_bei_2026_first_order_degeneracy.pdf); [arXiv record](https://arxiv.org/abs/2602.07377v1). | Closest general inferential phenomenon: first-order approximations fail near degeneracy, and minimum-distance procedures provide uniform inference. The TT contact exponent and product of bond singular values are the project's more specialized objects. Generic inference under degeneracy is established prior work. | Sections 3–4: the local experiment, impossibility results, and minimum-distance inference. |
| 4 | Wouters, Nakatani, Van Neck and Chan (2013), [The Thouless theorem for matrix product states and subsequent post-density matrix renormalization group methods](04_wouters_2013_thouless_mps.pdf); [arXiv record](https://arxiv.org/abs/1305.1761v3). | Closest higher-order geometry precedent. MPS is the tensor-train representation in physics terminology. The paper develops core perturbations and higher-order tangent constructions, including inverse density factors. The project's candidate addition is the optimized Frobenius-neighborhood modulus and its honest-inference consequence. | Sections V–VI, PDF pp. 6–8; second-order expansion and inverse density factors in equation (51), PDF p. 8. |
| 5 | Kutschan (2017 preprint; 2018 journal article), [Tangent Cones to TT Varieties](05_kutschan_2017_tt_tangent_cones.pdf); [arXiv record](https://arxiv.org/abs/1705.10152v1). | Direct precedent for rank-capped TT geometry at singular points. It describes first-order feasible directions; the project analyzes how a particular functional varies at higher orders and how this constrains confidence length. | Theorem 14 and Remarks 15–16, PDF pp. 8–9. |
| 6 | Dolgov and Savostyanov (2019 preprint; 2020 journal article), [Parallel cross interpolation for high-precision calculation of high-dimensional integrals](06_dolgov_2019_parallel_tt_cross.pdf); [arXiv record](https://arxiv.org/abs/1903.11554v1). | The algebraic reconstruction tool behind the computable interval: selected entries and invertible pivots recover an exact-rank TT tensor. The cross identity is prior work; the project applies it to certified statistical bounds and weak-bond rates. | Formula (3) and Theorem 2, PDF p. 7. This preprint's formula (3) corresponds to the formula cited as (5) in the project's comparison with the published version. |
| 7 | Cai and Low (2004), [An Adaptation Theory for Nonparametric Confidence Intervals](07_cai_low_2004_adaptive_confidence_intervals.pdf); [arXiv record](https://arxiv.org/abs/math/0503662v1). | Foundational connection between a modulus of continuity, coverage over a parameter class, and unavoidable expected interval length. It supplies the inferential viewpoint; calculating the relevant modulus for intersecting TT constraints is the project's specific geometric task. | Modulus definitions, PDF p. 3; Section 2.1 and Theorem 1, PDF pp. 4–6. |
| 8 | Zhang, Luo, Raskutti and Yuan (2020), [ISLET: Fast and Optimal Low-Rank Tensor Regression via Importance Sketching](08_zhang_2020_islet.pdf); [arXiv record](https://arxiv.org/abs/1911.03804v2). | Closest compression/estimation ingredient: learn subspaces and solve a smaller tensor regression, including sample-splitting analysis. The current project's distinctive objective is honest functional length at degenerate references; it does not introduce sketching or improve the general ISLET estimation guarantee. | Theorem 4, PDF pp. 23–24; Remark 5 on sample splitting, PDF p. 24. |

For the first comparison, Ke et al. use a positive variance of the form

\[
V=\sigma^2\|\Phi(A)\|_\Sigma^2>0.
\]

The project's fully normal loading has vanishing first-order tangent projection under isotropic design. Its local variation is instead governed by

\[
\omega_A(t;B_*)\sim
\frac{t^K}{K^{K/2}\prod_{j=1}^{K-1}\beta_j}.
\]

The second expression requires exact reference ranks and per-mode annihilation, with \(t/\min_j\beta_j\to0\). Thus the comparison identifies different assumptions, rather than showing that regular projection-based confidence intervals fail within their stated domain. The project's proof is in [the general modulus note](../theory/general_normal_modulus.md), and its statistical result is in [the selected-cross inference note](../theory/certified_cross_inference.md).

## Versions, provenance, and scope

- [sources.json](sources.json) records each title, authors, publication year, retrieved version, original and resolved PDF URL, access date, page count, byte count, and SHA-256 hash. All nine PDFs were parsed and their opening pages checked against their intended identities.
- [references.bib](references.bib) contains the eight paper citations. The supplement shares the Ke et al. citation. The article bibliography is preserved separately in `paper/`; this reference collection does not rebuild or revise the manuscript.
- Ke et al.'s publisher record was marked **FUTURE**, with DOI `10.5705/ss.202026.0222`, when checked. No final issue or pagination is assigned here.
- ArXiv PDFs use explicit version URLs. Archive submission dates, dates printed inside PDFs, and journal years can differ. In particular, the downloaded Kutschan v1 has a 2017 archive identifier but prints 30 July 2021 on its first page; the journal citation is 2018. The saved URL and hash identify the exact copy used for the reading pointers.
- Page pointers refer to one-based PDF pages, including any cover. They need not match a journal's page numbers.
- The PDFs retain their original copyright and license notices. This private research collection does not grant a new license to the papers.

This is a focused reading collection. Broader comparisons, including regular low-rank tensor inference, TT estimation, and conservative Monte Carlo calibration, remain in the [September 9 novelty review](../literature/revision_2026_09_09_novelty.md) and the [earlier literature review](../literature/literature_review.md).
