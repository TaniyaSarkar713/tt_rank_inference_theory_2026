# Application status and a defensible follow-up protocol

No real-data or LLM experiment was run or claimed in this project. The user explicitly allowed omitting an application when its connection would be superficial. Current theorems concern a fixed-dimensional coefficient, not a trained transformer's weights or stochastic optimizer trajectory.

A meaningful follow-up is a tensor regression head on a frozen, externally trained feature map phi. Observe iid outcomes Y_i and fixed-feature tensors X_i=phi(Z_i), and define the population coefficient by E[X(Y-<X,B>)]=0. A fixed contrast A can encode an externally specified task comparison or a held-out prompt contrast. Before claiming this paper's exact theorem applies, establish an exact linear conditional mean, iid homoskedastic Gaussian residuals, full-column-rank design with n>p, and a structural cap or independently justified approximation allowance. Conditional coverage does not require Gaussian features, but the current expected-length theorem does.

Protocol:
1. Fix the model checkpoint, tensorization and population target before inspecting the inferential sample. Checkpoint compression alone is a deterministic problem.
2. Use a separate sample for learned feature maps or estimated loadings; propagate the remaining loading error rather than treating it as known.
3. Declare cap-one restrictions substantively. Do not certify them using a rank pretest at a scale below the sampling noise.
4. Compare exact-model, known-tube sensitivity and ambient inference across a prespecified allowance grid. Explain the coefficient units of eta.
5. Assess whether the linear approximation remainder contributes an additional bias bound. Without such a bound, call the exercise exploratory and do not claim exact coverage for a nonlinear LLM.
6. Show a scientifically interpretable contrast for which the contact geometry matters. If the tensorization is arbitrary and has no such interpretation, do not force this application into the paper.

This is a protocol, not completed empirical evidence. No dataset access, model training, or external publication is represented as having occurred.


Audit note, 8 September 2026: a common confidence ball protects data-selected contrasts for their random targets, but does not make that target a fixed scientific estimand or supply coverage conditional on selection. The finite-variance extension still requires independent observation pairs, a justified conditional variance upper bound, and sufficient ambient regression observations per group. No new real-data experiment was run in this audit.
