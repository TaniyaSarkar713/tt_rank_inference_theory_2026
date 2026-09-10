# Result ledger, 7 September 2026

PROVED means a complete internal derivation has been written and audited. It does not mean novelty has been certified or that an independent reviewer has verified the result.

| ID | Status | Statement | Assumptions / limitation | Canonical source |
|---|---|---|---|---|
| T1 | PROVED | Cap-one cuts partition the modes into J blocks. With q=max(1,min nonzero block degree of A), omega(t) is comparable to t^q/lambda^(q-1) at every original-mode rank-one point. | Fixed geometry; positive caps; interior norm constraint; constants depend on A. | paper/sections/theory.tex, contact-order theorem; appendix proof |
| T1b | PROVED | For an elementary unit contrast in exactly q blocks, the leading coefficient is q^(-q/2). | Elementary within-block products; not arbitrary loadings or non-rank-one signals. | Same theorem |
| T2 | PROVED | Slack of at least one rank at every cut implies first-order modulus for every nonzero A. | Interior point; exponent statement, not ambient variance efficiency. | Slack proposition |
| T3 | PROVED | Optimal pointwise expected length among intervals honest over the whole TT class is comparable to (sigma/sqrt(n))^q/lambda^(q-1). | Fixed p; n>=2p+2J+8; signal larger than noise scale. | Honest-length theorem |
| T4 | PROVED | In a known eta coefficient tube, add eta wedge (sigma/sqrt(n)) to T3. | Known structural error bound, not contamination robustness. | Honest-length theorem and tube sandwich |
| T5 | PROVED | Graded HOSVD envelope inversion has conditional finite-sample coverage and attains T3–T4; unknown sigma uses an F ball. | Full-rank design and iid homoskedastic Gaussian errors for coverage; isotropic Gaussian design for expected length. | Procedure theorem |
| T6 | PROVED | Intermediate departures s_n << eta_n << sigma/sqrt(n) are asymptotically indistinguishable but rule out exact-model expected length. | Unit loading; coefficient alternatives within norm cap. | Undetectable-departures corollary |
| T7 | PROVED | A full-normal three-block loading has cubic constant ||T||_injective/(3 sqrt(3)); computing it inherits spectral-norm hardness. | Dimensions vary only for the computational observation. No computational-statistical gap theorem. | Complexity proposition |
| O1 | PARTIAL | Dimension-dependent optimal length. | Fixed-p upper/lower bounds available; constants unmatched as dimensions grow. | open_questions.md |
| O2 | CONJECTURED | Classification around non-rank-one signals with several weak bonds. | No proposed universal rate; needs new geometry. | open_questions.md |
| O3 | PARTIAL | Sharp computationally attainable confidence constants. | Existing norm hardness does not imply hardness of honest inference. | open_questions.md |
| O4 | CONJECTURED | Extensions to non-Gaussian/dependent observations. | Current exact pivot fails; must replace localization. | open_questions.md |

The classification includes six binary modes, caps (1,2,2,2,1), with a singular internal rank-at-most-two 4-by-4 matrix variety and q=3. The cubic exponent is caused by the three blocks, not the internal singularity. This distinction is essential to the novelty assessment.

T8 — PROVED (supporting baseline calculation, derived during analysis): for the three-block HOSVD pilot along the local four-way path, the scaled estimate/SE converge to a product of three shifted Gaussians and its gradient norm. The exact-boundary degree calibration has iterated local coverage limit 2 Phi(z_.975/3)-1 = approximately .4865. This explains the observed baseline failure, but is a specialization of established degeneracy theory and is not a novel main contribution. Complete proof: final subsection of paper/appendix.tex. This supporting derivation was added after the primary simulation; it is not described as a new prespecified hypothesis.
