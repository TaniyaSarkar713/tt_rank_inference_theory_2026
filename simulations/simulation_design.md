# Locked simulation design — 7 September 2026

This design was written after complete derivations of T1–T7 and before executing new Monte Carlo experiments. Old project results are not pooled with this study. No tuning is chosen by observed coverage.

## Shared design
Nominal coverage 0.95; independent seeds from a master SeedSequence; 2,000 repetitions per setting. Report coverage, binomial Monte Carlo standard error, Wilson 95% interval, mean length with Monte Carlo SE, mean squared target error, rank selection frequency where relevant, and localization fallback frequency. At 95% coverage the Monte Carlo SE for 2,000 runs is 0.487 percentage points. Use the exact Bartlett sufficient-statistic sampler for iid Gaussian-design/Gaussian-error experiments; stress settings generate raw observations.

## A: contact classification
n in {512,2048,8192}, sigma=.2, lambda=3, B0=lambda E_00...0, A=E_11...1. Profiles: three binary modes/caps(1,1); four binary modes/caps(1,1,1), (1,2,1), (2,1,2), (2,2,2); six binary modes/caps(1,2,2,2,1). These give q=3,4,3,2,1,3 and p=8,16,16,16,16,64. Predicted mean-length log-n slopes are -q/2 for the graded interval, -1/2 for ambient intervals. The six-mode profile is internally singular. Constant inflation with p is an intended diagnostic, not a claim of a dimension-optimal method.

Baselines: graded honest interval; exact ambient scalar normal interval; one prefix-matrix envelope (rank-one two-block inversion when a cap-one cut exists, ambient otherwise); ordinary tangent plug-in Wald; degree-calibrated Wald with critical value z_.975/q motivated by Pillai–Meng's pointwise monomial law. The latter is not uniformly honest over drifting alternatives. Include the F-ball version for unknown sigma.

## B: local rank activation and singular-value sweep
Four binary modes, caps(1,2,1), lambda=3, sigma=.2; block factors (e0+u e1), (e00+u e11), (e0+u e1), with u=c sigma/(lambda sqrt(n)), c in {0,1,2,4,8}, n in {512,2048,8192}. Report the actual smallest nonzero central bond singular value, which equals lambda |u|(1+u²) for |u|<1. Prespecified loadings A_tan=(E0000+.35 E0110)/sqrt(1+.35²) and A_normal=E1111. The first has a substantial tangent component; the second is cubic-normal at the boundary and nearly normal under local drift. Compare graded, ambient, known-rank plug-in Wald, selected-rank plug-in Wald, and boundary-degree Wald. Select central rank two if its OLS singular value exceeds kappa sigma sqrt(2/n), kappa in {1,2,3}; otherwise use original-mode rank one. The selection constants are diagnostic rather than a rank-consistency prescription. Known-rank means the actual central rank is supplied, not the coefficient. Rank fits use HOSVD envelopes and their derivatives; no global nonlinear least-squares claim.

## C: sensitivity to approximate structure
Four binary modes/caps(1,2,1), cubic loading, same n and sigma/lambda. Let s_n=(sigma/sqrt(n))³/lambda². Allowances eta in {0,s_n,100 s_n,10000 s_n,(sigma/sqrt(n))²/lambda,sigma/sqrt(n)}. Evaluate both B0 and B0+eta A (omit duplicate eta=0). Compare exact-model graded intervals, tube-aware graded intervals, ambient scalar intervals and boundary-degree Wald. T4 predicts a transition when eta overtakes s_n, eventually ambient order. Wide finite-sample constants can delay visible separation. Undercoverage of exact-model methods is not required at every small perturbation.

## D: assumption and constant diagnostics
At n=512 and 2048, q=3: vary lambda among {.5,1,3}; dense modewise rotation of signal/loading; AR(1) design covariance with correlation .5; unknown sigma. For raw-observation stress runs at n=512 use standardized t5 errors, heteroskedastic Gaussian errors with scale sigma sqrt(.3+.7 X_i1²), AR(1) error dependence .6, and Gaussian scale-mixture contamination fractions .01 and .05 with outlier SD 5 sigma. These last settings are outside the finite-sample theorem and are labeled accordingly. No contamination/dependence robustness is claimed. Sparsity is not a model assumption; dense rotations test this directly rather than introducing an unrelated sparsity grid.

## Scope
Primary conclusions are about coverage and expected length. Prediction-risk, support recovery and rank-optimal estimation are not theorems of this paper, so no unrelated benchmark is used to imply such claims. Generic minimum-distance confidence-set inversion is a theoretical benchmark; globally optimizing its nonconvex endpoints is not implemented or misrepresented by the outer interval.

## Transparent addendum after the primary run

The 81-setting primary study showed mean-length slopes over n=512–8192 of -1.776 in the six-mode case versus limiting -1.5, consistent with nonnegligible inverse-Gram radius inflation. To resolve this uncertainty, add n=131072 and 2097152 for the six classification profiles, 2,000 repetitions each. The exact sufficient-statistic law makes these sample sizes inexpensive. All methods, coefficients, loadings and critical values remain unchanged. The addendum is stored separately and is not described as originally prespecified. Its sole purpose is asymptotic slope validation, not finding a favorable coverage setting.


# Adversarial-audit addenda, 7–8 September 2026

The original experiment and its large-n addendum are preserved with their original certificate and hashes. The energy/transition addendum uses 6,000 new datasets in three cohorts of 2,000, paired across seven deterministic loadings and five methods; run `run_audit.py` then `analyze_audit.py`. Its 210,000 interval records have separate metadata, MCSE and Wilson bounds. The independent finite-variance addendum uses Gaussian and standardized t2.5 noise at n=512,2048,8192, with six cohorts of 1,000; q=3 and q=4 share data within each cohort. Run `run_robust_audit.py` then `analyze_robust_audit.py`; it adds 6,000 datasets and 12,000 interval records. Both addenda were designed after the relevant new proofs, not before the original experiment. The finite-grid robust slopes are not described as exact asymptotic confirmation.
