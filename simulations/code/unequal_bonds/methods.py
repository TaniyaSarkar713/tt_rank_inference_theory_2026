"""The V3 two-pattern interval for a four-mode tensor with one weak cut.

Coverage is mathematical under the specified Gaussian experiment. These
floating-point calculations are not an interval-arithmetic certificate.
"""
from itertools import product

import numpy as np
from scipy.stats import f


def coordinate_maps():
    """Return the 23 coordinates and maps for full and grouped TT crosses."""
    prefixes = [[(0,), (1,)], [(0, 0), (0, 1)], [(0, 0, 0), (0, 1, 1)]]
    suffixes = [[(0, 0, 0), (1, 1, 1)], [(0, 0), (1, 1)], [(0,), (1,)]]
    pivots = [[p + q for p, q in product(prefixes[k], suffixes[k])]
              for k in range(3)]
    slices = [[(2,) + q for q in suffixes[0]]]
    slices += [[p + (2,) + q for p, q in product(prefixes[k - 1], suffixes[k])]
               for k in (1, 2)]
    slices += [[p + (2,) for p in prefixes[2]]]
    grouped_first = [(2, 2) + q for q in suffixes[1]]
    target = (2, 2, 2, 2)
    coordinates = sorted({target, *grouped_first,
                          *(x for group in pivots + slices for x in group)})
    lookup = {x: i for i, x in enumerate(coordinates)}
    pivot_maps = [np.array([lookup[x] for x in group]) for group in pivots]
    full_maps = [np.array([lookup[x] for x in group]) for group in slices]
    grouped_maps = [np.array([lookup[x] for x in grouped_first]), *full_maps[2:]]
    return coordinates, pivot_maps, full_maps, grouped_maps, lookup[target]


def intervals(z, radius):
    """Evaluate both cross bounds and their intersection for batched OLS input."""
    coordinates, pivots, full, grouped, target = coordinate_maps()
    z = np.asarray(z, dtype=float)
    if z.ndim != 2 or z.shape[1] != len(coordinates):
        raise ValueError("z must have shape (batch, 23)")
    radius = np.broadcast_to(np.asarray(radius, dtype=float), (len(z),))
    if not np.isfinite(z).all() or not np.isfinite(radius).all() or (radius < 0).any():
        raise ValueError("centers and nonnegative radii must be finite")
    gaps = np.stack([
        np.linalg.svd(z[:, idx].reshape(-1, 2, 2), compute_uv=False)[:, -1]
        for idx in pivots
    ], axis=1) - radius[:, None]

    def bound(slices, required):
        certified = np.all(gaps[:, required] > 0, axis=1)
        norms = np.stack([np.linalg.norm(z[:, idx], axis=1) for idx in slices], axis=1)
        numerator = np.prod(norms + radius[:, None], axis=1)
        value = np.full(len(z), np.inf)
        value[certified] = numerator[certified] / np.prod(gaps[certified][:, required], axis=1)
        return value, certified

    full_bound, full_certified = bound(full, [0, 1, 2])
    grouped_bound, grouped_certified = bound(grouped, [1, 2])
    center = z[:, target]

    def intersect(half_bound):
        lower = np.maximum(center - radius, -half_bound)
        upper = np.minimum(center + radius, half_bound)
        empty = lower > upper
        return np.where(empty, center, lower), np.where(empty, center, upper)

    answers = {
        "full_cross": intersect(full_bound),
        "grouped_cross": intersect(grouped_bound),
        "adaptive_cross": intersect(np.minimum(full_bound, grouped_bound)),
    }
    diagnostics = {"full_certified": full_certified, "grouped_certified": grouped_certified}
    return answers, diagnostics


def fit_interval(selected_design, response, alpha=0.05):
    """Fit the selected regression; n > 23 gives coverage and n >= 27 the rate."""
    design = np.asarray(selected_design, dtype=float)
    response = np.asarray(response, dtype=float)
    if design.ndim != 2 or design.shape[1] != 23 or response.shape != (len(design),):
        raise ValueError("use a design of shape (n, 23) and a response of shape (n,)")
    n, m = design.shape
    if n <= m or not 0 < alpha < 1:
        raise ValueError("require n > 23 and 0 < alpha < 1")
    if not np.isfinite(design).all() or not np.isfinite(response).all():
        raise ValueError("observations must be finite")
    gram = design.T @ design
    smallest = np.linalg.eigvalsh(gram)[0]
    if smallest <= 0:
        raise ValueError("the selected design must have full column rank")
    z = np.linalg.solve(gram, design.T @ response)
    residual = response - design @ z
    tauhat = np.sqrt(residual @ residual / (n - m))
    radius = tauhat * np.sqrt(m * f.ppf(1 - alpha, m, n - m) / smallest)
    answers, diagnostics = intervals(z[None, :], radius)
    return {
        "intervals": {name: (float(lo[0]), float(hi[0])) for name, (lo, hi) in answers.items()},
        "center": z,
        "radius": float(radius),
        "effective_noise_estimate": float(tauhat),
        "diagnostics": {name: bool(value[0]) for name, value in diagnostics.items()},
    }
