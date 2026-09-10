# Finite-variance audit experiment

6,000 new independent datasets in six cohorts. Each cohort has 1,000 replications; the q=3 and q=4 procedures share those observations. There are 12,000 interval records. The t2.5 noise is centered and scaled to variance .2²; it has no finite third or fourth moment. No outliers were artificially labeled and no contamination model is asserted.

| noise    |    n |   q |   reps |   coverage |   coverage_mcse |   wilson_lower |   wilson_upper |   mean_length |   length_mcse |   ball_coverage |   mean_radius |   fallback_rate |
|:---------|-----:|----:|-------:|-----------:|----------------:|---------------:|---------------:|--------------:|--------------:|----------------:|--------------:|----------------:|
| Gaussian |  512 |   3 |   1000 |          1 |               0 |      0.9961732 |              1 |  0.009328     |  1.809547e-05 |               1 |     0.4830013 |               0 |
| Gaussian |  512 |   4 |   1000 |          1 |               0 |      0.9961732 |              1 |  0.0004292142 |  1.280271e-06 |               1 |     0.4300278 |               0 |
| Gaussian | 2048 |   3 |   1000 |          1 |               0 |      0.9961732 |              1 |  0.0009508218 |  1.756687e-06 |               1 |     0.2411463 |               0 |
| Gaussian | 2048 |   4 |   1000 |          1 |               0 |      0.9961732 |              1 |  2.019625e-05 |  5.6489e-08   |               1 |     0.2147509 |               0 |
| Gaussian | 8192 |   3 |   1000 |          1 |               0 |      0.9961732 |              1 |  0.0001080834 |  1.890564e-07 |               1 |     0.120529  |               0 |
| Gaussian | 8192 |   4 |   1000 |          1 |               0 |      0.9961732 |              1 |  1.10354e-06  |  2.904325e-09 |               1 |     0.1073099 |               0 |
| t2.5     |  512 |   3 |   1000 |          1 |               0 |      0.9961732 |              1 |  0.008947581  |  1.849574e-05 |               1 |     0.4830013 |               0 |
| t2.5     |  512 |   4 |   1000 |          1 |               0 |      0.9961732 |              1 |  0.0003949052 |  1.197951e-06 |               1 |     0.4300278 |               0 |
| t2.5     | 2048 |   3 |   1000 |          1 |               0 |      0.9961732 |              1 |  0.0009224619 |  1.686332e-06 |               1 |     0.2411463 |               0 |
| t2.5     | 2048 |   4 |   1000 |          1 |               0 |      0.9961732 |              1 |  1.910342e-05 |  5.256498e-08 |               1 |     0.2147509 |               0 |
| t2.5     | 8192 |   3 |   1000 |          1 |               0 |      0.9961732 |              1 |  0.0001064269 |  1.967817e-07 |               1 |     0.120529  |               0 |
| t2.5     | 8192 |   4 |   1000 |          1 |               0 |      0.9961732 |              1 |  1.066953e-06 |  2.939927e-09 |               1 |     0.1073099 |               0 |

| noise    |   q |     slope |   slope_mcse |   predicted |
|:---------|----:|----------:|-------------:|------------:|
| Gaussian |   3 | -1.607838 | 0.0009421009 |        -1.5 |
| t2.5     |   3 | -1.598391 | 0.001000292  |        -1.5 |
| Gaussian |   4 | -2.150854 | 0.001434727  |        -2   |
| t2.5     |   4 | -2.132967 | 0.001478089  |        -2   |

Slopes are finite-sample descriptive fits over n=512,2048,8192, not exact verification of the asymptotic slope. Monte Carlo standard errors account for independent n cohorts; q comparisons are paired. At 1,000/1,000 successes the binomial plug-in MCSE is zero; the Wilson interval, approximately [0.9962,1], expresses uncertainty. The radius has deliberately large fixed-dimension constants, so conservative coverage is expected. The theorem gives worst-noise expected-length order with a known variance bound; these simulations do not establish sharp constants.
