# Post-audit paired experiment

6,000 new independent datasets: three cohorts of 2,000. The seven deterministic loadings and five methods reuse each cohort; they are not independent experiments. Total 210,000 interval records, 105 summary rows. The original 186,000 datasets and primary figures remain unchanged.

The loading is (E1111 + epsilon E1000)/sqrt(1+epsilon²), epsilon=kappa*t_n²/lambda². lambda=3, sigma=.2, caps=(1,2,1), truth=lambda E0000. The proved reference is R_A(t_n)=(epsilon*t_n+t_n³/lambda²)/sqrt(1+epsilon²).

|    n |   kappa | method   |   coverage |   coverage_mcse |   wilson_lower |   mean_length |   length_mcse |   length_over_rate |
|-----:|--------:|:---------|-----------:|----------------:|---------------:|--------------:|--------------:|-------------------:|
| 8192 |       0 | ambient  |     0.957  |     0.004536022 |      0.9471989 |  0.008671228  |  1.53444e-06  |      7232993       |
| 8192 |       0 | energy   |     1      |     0           |      0.998083  |  4.657828e-07 |  2.941648e-09 |          388.5267  |
| 8192 |       0 | original |     1      |     0           |      0.998083  |  1.971453e-06 |  1.111483e-08 |         1644.462   |
| 8192 |       1 | ambient  |     0.957  |     0.004536022 |      0.9471989 |  0.008671228  |  1.53444e-06  |      3616497       |
| 8192 |       1 | energy   |     1      |     0           |      0.998083  |  4.741584e-07 |  2.890683e-09 |          197.7566  |
| 8192 |       1 | original |     1      |     0           |      0.998083  |  1.979829e-06 |  1.108431e-08 |          825.7243  |
| 8192 |     100 | ambient  |     0.957  |     0.004536022 |      0.9471989 |  0.008671228  |  1.534443e-06 |        71613.8     |
| 8192 |     100 | energy   |     1      |     0           |      0.998083  |  2.458954e-06 |  6.020493e-09 |           20.30797 |
| 8192 |     100 | original |     1      |     0           |      0.998083  |  3.964624e-06 |  1.429902e-08 |           32.74297 |
| 8192 |   10000 | ambient  |     0.9555 |     0.004610843 |      0.9455562 |  0.008671241  |  1.53481e-06  |          723.2387  |
| 8192 |   10000 | energy   |     1      |     0           |      0.998083  |  0.0002023034 |  3.691041e-07 |           16.87344 |
| 8192 |   10000 | original |     1      |     0           |      0.998083  |  0.0002038091 |  3.768481e-07 |           16.99902 |

|    n |   kappa | noise   |   mean_length_ratio |   ratio_mcse |   mean_length_reduction |   reduction_mcse |
|-----:|--------:|:--------|--------------------:|-------------:|------------------------:|-----------------:|
| 8192 |     0   | known   |           0.2362637 | 0.0004142662 |            1.50567e-06  |     8.318805e-09 |
| 8192 |     0.1 | known   |           0.2363157 | 0.0004129457 |            1.50567e-06  |     8.318805e-09 |
| 8192 |     1   | known   |           0.2394947 | 0.0003748412 |            1.50567e-06  |     8.318805e-09 |
| 8192 |    10   | known   |           0.2995487 | 0.0003086605 |            1.50567e-06  |     8.318805e-09 |
| 8192 |   100   | known   |           0.6202237 | 0.0007365072 |            1.50567e-06  |     8.318805e-09 |
| 8192 |  1000   | known   |           0.9319698 | 0.0002411925 |            1.505672e-06 |     8.318801e-09 |
| 8192 | 10000   | known   |           0.9926123 | 2.851043e-05 |            1.505672e-06 |     8.318688e-09 |

Coverage MCSE is the binomial plug-in standard error; at 2,000/2,000 successes it is zero, so the Wilson interval is also reported and no perfect-population-coverage claim is made. Ratio MCSE uses the paired influence variable (new − ratio*old)/mean(old), preserving within-dataset dependence. Error bars are pointwise Monte Carlo intervals, not simultaneous confidence bands.

The energy certificate reduces length on every replicate, as predicted by the deterministic theorem. Conservative constants remain large. The normalized curves examine the uniform multiscale bound; they do not estimate a sharp minimax constant or prove the theorem. At large kappa the tangent term dominates and the two certificates approach each other. No non-Gaussian optimality claim is assessed by this Gaussian study.
