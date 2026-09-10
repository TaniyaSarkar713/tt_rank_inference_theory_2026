# Theory-driven selected-cross experiment

The experiment tests C3's dataset-wise length improvement and C4's weak-bond length transition. It does not estimate an optimal confidence constant.

Use K=4, nominal coverage 0.95, σ=0.2, a=3, and embed the first-three-coordinate coefficient in dimensions (40,40,40,40). The ambient parameter dimension is 2,560,000. The procedure uses the 21 distinct selected cross/target coordinates specified before sampling.

There are 19 settings and 5,000 independent replications per setting. Seeds are 2026090900 plus setting index. Methods on the same replication are paired.

- At n=512 and 8192, use B=a e0^4+b e1^4 and b/(σ/√n) in {0,2,8,32,128}.
- At both sample sizes, use the nonzero-target path a e0^4+b(e1+s e2)^4, s=2σ/(b√n), and b/(σ/√n) in {2,8,32}.
- For a fixed bond b=0.3, use n in {512,8192,131072} to inspect approach to n^{-2} length.

Compare the separate cross bound, optimized joint cross bound, projection of the common F ball, and a scalar Student-t interval from the same selected regression. The scalar interval is already valid under the Gaussian marginal experiment; the structured method seeks shorter intervals at special references, not universal dominance over Student-t. Earlier rank-selected and known-rank experiments remain available in the historical simulation cohorts and were not rerun here.

The simulation samples the exact sufficient-statistic law: Bartlett Wishart design Gram matrix, conditional normal OLS error, and independent residual chi-square. For nonzero-target paths, omitted coefficient energy is explicitly added to σ². This is exactly equivalent to the selected regression induced by the stated ambient Gaussian model; it avoids allocating a huge unused design matrix.

Store centers, radii, true coefficients and targets, effective variances, interval endpoints, pivot certification and numerator-bracket diagnostics. Verify raw-file hashes before analysis. Report coverage, binomial Monte Carlo SE, Wilson intervals, mean length and its SE, and paired differences/ratios with paired SE. An all-success row has plug-in SE zero but a nontrivial Wilson lower endpoint. At true 0.95 coverage the nominal Monte Carlo SE is about 0.00308.

Fixed-bond log-log slopes use the three settings and independent-setting delta-method Monte Carlo errors. They are descriptive finite-grid slopes, not confidence intervals for the asymptotic exponent. The observed joint slope −2.225 differs materially from −2; finite-sample localization constants remain visible.

Reproduce from the project root:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python simulations/code/tt_revision/check_geometry.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python simulations/code/tt_revision/run.py
MPLCONFIGDIR=/tmp/tt_revision_mpl python simulations/code/tt_revision/analyze.py
```

The geometry check also constructs 36 non-diagonal TT references and compares the numerator solver with 80-digit arithmetic. Those are falsification checks of formulas, not Monte Carlo confidence experiments.
