# Prior-art check for the strengthening program

Checked 8 September 2026. This adds to the audited 28-paper matrix without retrospectively changing that audit's counts. Negative search findings are bounded evidence, not proof of priority.

| Source | Setup and method | Assumptions and checked result | Our proposed difference and limitation |
|---|---|---|---|
| Zhang, Luo, Raskutti and Yuan, ISLET (2020) | Gaussian tensor regression with Tucker structure; estimate subspaces, sketch regression and reconstruct | Theorem 4 gives estimation bounds; Remark 5 splits samples for sketches and reduced regression. Supplementary arguments explicitly treat omitted Gaussian signal as additional noise | Compression, splitting and the variance identity are prior ingredients. The proposed additional target is honest higher-order functional length. Our global pilot is not an algorithmic improvement |
| Ke, Song, Zhao and Wang, Statistica Sinica accepted preprint SS-2026-0222 | Regression on a smooth low-rank manifold, design covariance Σ; covariance-weighted one-step inference | Theorem 1 defines V=σ²||Φ(A)||²_Σ>0; Theorems 1–2 give normal limits. Theorem 3 bounds local worst-case length below by cσ||Φ(A)||_Σ/√N. Tucker conditions include positive signal, consistent subspaces and alignment | Regular projection efficiency and first-order geometric lower bounds are occupied. Our target has zero first-order projection and a higher-order weak-bond length transition |
| Dolgov and Savostyanov, accepted 2019 author version, DOI 10.1016/j.cpc.2019.106869 | TT reconstruction from cross fibers and inverse pivots | Theorem 2/equation (5) reconstruct exact-rank tensors with nonsingular crosses; no statistical model is needed for the identity | The new calculation uses this identity for a sharp modulus and honest interval. Cross interpolation is not new |
| Wouters, Nakatani, Van Neck and Chan (2013), Phys. Rev. B 88, 075122 | Matrix product state manifolds, reference parametrizations and excitation expansions | Sections VI–VII develop parametrizations and higher-order tangent/excitation constructions under MPS regularity conditions | Higher-order tensor-network geometry is prior art. The proposed additional object is a statistical modulus and uniformly honest expected length. A broad geometric classification needs closer comparison |
| Xu, Chen and Han (2025), rechecked existing source | Tucker regression/PCA, debiasing/projection and functional inference | Corollary 3.1 equation (10) imposes alignment so the first-order Gaussian term dominates; Theorem 3.3 studentizes it | A normal loading cannot simply be inserted into that regular standardized theorem |
| Bei and Navjeevan (2026), rechecked existing source | Smooth transformations near first-order degeneracy; limiting experiments and minimum-distance inference | Sections 3–4 establish impossibility results and uniform procedures; remarks discuss higher-order extensions | Generic degeneracy and minimum-distance inversion are occupied. Cubic calibration alone may be incremental; compatible TT constraints and sharp weak-bond length are the stronger target |

## Sources and locators

- ISLET: [primary PDF](https://arxiv.org/pdf/1911.03804), Theorem 4, Remark 5 and supplementary projection-noise analysis; [journal metadata](https://epubs.siam.org/doi/epdf/10.1137/19M126476X).
- Ke et al.: [publisher record](https://www3.stat.sinica.edu.tw/statistica/fp/SS-2026-0222.html), [accepted PDF](https://www3.stat.sinica.edu.tw/ss_newpaper/SS-2026-0222_na.pdf), PDF pages 18–24, Theorems 1–3 and Tucker assumptions. Record marked FUTURE and updated 2026-09-08; not treated as a final issue citation.
- Dolgov–Savostyanov: [author PDF](https://cris.brighton.ac.uk/ws/files/6746392/1_s2.0_S0010465519302565_main.pdf), PDF page 4, Theorem 2.
- Wouters et al.: [primary PDF](https://arxiv.org/pdf/1305.1761), Sections VI–VII; [journal metadata](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.88.075122).
- Xu et al.: [primary PDF](https://arxiv.org/pdf/2501.16223), Corollary 3.1/equation (10), Theorem 3.3.
- Bei–Navjeevan: [accessed arXiv version](https://arxiv.org/html/2602.07377v1), Sections 3–4. The metadata/displayed-date discrepancy remains documented.

## Search scope and status

Queries covered tensor functional inference at zero variance, target-preserving projection, confidence intervals after tensor sketching, TT cross interpolation, TT local moduli, MPS osculating spaces and higher-order tangent geometry. This targeted pass supplements the original broad survey; it does not repeat a complete review of every related paper.

No exact match to the all-rank-two formula omega(t;b)≍t min{1,(t/b)^(K−1)} together with its honest regression-length theorem was located in the inspected sources. That is the current candidate statistical contribution. Independent specialist review of tensor-network geometry and degenerate inference remains a priority.
