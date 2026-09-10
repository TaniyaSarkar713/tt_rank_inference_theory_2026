# Figure design and audit plan

Three figures are sufficient for this theory-focused paper; no decorative pipeline is needed.

1. Motivating experimental comparison: two panels for the prespecified tangent and nearly normal loadings. Coverage versus the second central bond divided by sigma/sqrt(n), common 0–1.04 vertical range, nominal95% line, Wilson Monte Carlo intervals. This is the introduction's four-way example.
2. Theory validation: mean length versus n on logarithmic axes, then adjacent log–log slopes with reference values -q/2. Six cap/dimension profiles; distinguish the original grid from the disclosed large-n addendum in the caption.
3. Approximation sensitivity: length at B0 versus eta/tn and coverage at B0+eta A. Log scales only where positive; eta=0 is omitted from the log display but retained in the full tables.

Implementation: Matplotlib vector PDF, shared plot_utils.py, colorblind-safe palette with markers and line styles, serif fonts at least8pt at manuscript insertion size. Captions state the finding and give n, signal/noise, reps, error-bar meaning. No 3D effects, truncated coverage axes or manual editing of data. Full mathematical procedure is short enough to specify in equations, so a solution-overview illustration would duplicate it.

The running example was checked directly against the introduction; no missing user confirmation is needed because both sources are in this project. Final visual checks are recorded in pre_submission_review.md.
