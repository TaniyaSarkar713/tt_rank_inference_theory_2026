# Final manuscript and project review

Reviewed 7 September 2026. Scientific recommendation: **Needs major revision before submission**; project classification: **Promising — theory requires further work**. This review distinguishes a complete research draft from a journal-ready contribution.

Summary: 0 identified CRITICAL defects in the stated, limited theorem/proof chain; 3 MAJOR research limitations; 1 MINOR venue-format issue. Absence of an identified proof defect is not a guarantee of correctness. Priority and independent mathematical review remain necessary.

## Macro logic and research substance

| Finding, with exact manuscript text | Severity | Concrete next step |
|---|---|---|
| “Higher block-degree spans for product varieties appear in the osculating geometry of Araujo et al.” and “We use that grading and verify feasible lower-bound paths inside the additional TT constraints.” Much of the mechanism is inherited geometry. | MAJOR | Obtain a specialist comparison of the exact cap-profile classification with existing osculating and nonregular-inference results; retain the narrow claim or strengthen to non-rank-one points. |
| “No matching dimension-dependent minimax length, efficient confidence constant, or general classification at non-rank-one TT points has been established.” | MAJOR | Prove one substantial extension with explicit dimension dependence or a genuinely different singular local experiment before an AoS submission. Do not extrapolate the current fixed-p theorem. |
| “The OLS ball can incur large dimension constants, and the experiments show that the computable interval is far from a sharp constant procedure.” | MAJOR | Develop sharper calibrated inversion and compare against strong minimum-distance methods under identical assumptions. Rate optimality in n alone does not establish practical competitiveness. |

The introduction’s three contributions map to the contact theorem, tube/length theorem and computable procedure. Complete derivations include witness feasibility, every displayed geometric bound, the information inequality, OLS moments, projector mixing, fallback-event expectation and the supporting Wald limit. PARTIAL/CONJECTURED items remain discussion questions, not theorem claims.

## Writing details and grammar

Abstract, introduction, method, theory and empirical findings were checked for consistent scope. Generic “first tensor inference” and “first higher-order inference” claims are absent. The ordinary Wald and boundary-degree Wald baselines are distinguished. The six-mode internal singularity is described accurately: it does not create the cubic exponent. No outstanding grammatical defect was identified under the skill’s G1–G8 checks; statements of mathematical results use present tense, and completed empirical outputs are described explicitly as outputs. This is an internal editorial review, not an external copy-edit certificate.

## LaTeX and references

The final PDF has 22 pages. All references resolve; all numbered equations are referenced; the final TeX log has no warnings or overfull boxes. The bibliography has 30 entries, 25 used in this manuscript. Metadata for the ICML oracle-regression paper were checked against the official proceedings; preprint/journal-version distinctions are recorded in the literature files.

MINOR: `\documentclass[11pt]{article}` is a neutral research-draft layout. Journal-specific formatting and any venue page limits have not been checked because a submission venue has not been selected. Apply the selected journal’s current template at submission preparation.

## Figures and visual review

Three vector PDF figures use a consistent palette with marker/line encoding and readable fonts at insertion size. Captions state the result, setting, replication count and uncertainty measure. The figure on local rank activation uses the introduction’s specified four-way example. The log-n slope addendum is disclosed; the geometric midpoint on the slope panel is labeled. Small numerical roundoff in Wilson endpoints was clipped only for plotting error-bar magnitudes, not used to alter coverage observations.

Structural extraction checked all 22 pages and found no replacement glyphs. Visual inspection was **sampled**, covering pages 1, 3, 6, 7, 10, 11, 12, 16, 19, 21 and 22, including the opening, every figure, the dense table, central theorems, proof pages and ending. Pages affected by the final caption/reference changes were inspected again. No clipping or overlapping content remained in that sample. The other pages were not individually visually inspected; their text and TeX diagnostics were checked.

## Full-source vocabulary scan

All nine manuscript/main/appendix/section source files were scanned, not sampled, for the skill’s banned phrases and sentence-connecting em-dashes. No hits remained. The source audit also checked duplicate/undefined labels and citation keys; none remained. No outside plagiarism checker was run, and no claim of such a check is made.

## Numerical and reproducibility verification

- Geometric checks passed: orthogonal grading, fast pure-loading projection agreement, exact witness distances, TT cap feasibility and elementary leading constants, including the singular six-mode example.
- 720 computed interval certificates were checked on explicitly verified localization events for known and unknown variance.
- Every one of 1,410,000 saved interval records was checked directly using its endpoints and target; every coverage and length summary was reaggregated.
- All 705 summary rows agree with the workbook’s plotted inputs. Dataset-generation source hashes match execution metadata.
- Fixed seeds and the raw endpoint-schema rerun are recorded; duplicate executions are not counted as additional independent data.
- The 12-setting large-n addendum and post-primary supporting Wald derivation are identified as such. No tuning parameters changed in response to coverage.

Integrity gate: evidence-specific findings PASS; actionable MAJOR findings PASS; no invented manuscript quotes PASS; severity separates research scope from typography PASS; complete vocabulary scan PASS; numerical claims trace to data PASS. Internal readiness score: **6.5/10** for submission, reflecting the three unresolved substantive limitations. The research draft and reproducible project are complete at the explicitly stated scope.
