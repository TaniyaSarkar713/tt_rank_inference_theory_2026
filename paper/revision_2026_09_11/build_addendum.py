"""Build the new proof addendum while preserving the September 9 manuscript."""
from pathlib import Path
import os
import re
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def relocate_links(text, source):
    def replace(match):
        label, target = match.groups()
        if '://' in target or target.startswith('#'):
            return match.group(0)
        path, _, fragment = target.partition('#')
        relative = os.path.relpath((source.parent / path).resolve(), HERE)
        return f'[{label}]({relative}' + (f'#{fragment}' if fragment else '') + ')'
    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)', replace, text)


def main():
    text = '''---
title: "Unequal Bond Strengths and Partial Rank Loss in Honest Tensor-Train Inference"
subtitle: "Proof addendum to the 9 September 2026 manuscript"
date: "11 September 2026"
fontsize: 11pt
geometry: margin=1in
mainfont: DejaVu Serif
sansfont: DejaVu Sans
monofont: DejaVu Sans Mono
colorlinks: true
toc: true
toc-depth: 2
---

# Purpose and scope

This addendum proves an all-radius modulus for fully normal product loadings
with unequal TT bond strengths. It derives matching fixed-dimensional honest
length, removes the balanced-gap premise from the learned-compression bound,
and gives a computable 23-feature interval for an explicit single-cut rank loss.
The existing September 9 manuscript supplies the finite-radius normal-modulus
bound, Gaussian OLS moments, and training-pilot result used here.

Proof status is internal. Unknown weak orientations, general loadings, optimal
confidence constants, and an efficient general pilot remain unresolved. The new
checks are algebraic falsification checks, not a Monte Carlo coverage study.

'''
    for name in ['unequal_bond_modulus.md', 'unequal_bond_inference.md']:
        source = ROOT / 'theory' / name
        text += '\n\\newpage\n\n' + relocate_links(source.read_text(), source) + '\n'
    (HERE / 'addendum.md').write_text(text.rstrip() + '\n')
    preamble = HERE / 'preamble.tex'
    preamble.write_text('\\usepackage{amsmath,amssymb,microtype}\n'
                        '\\setlength{\\emergencystretch}{3em}\n\\allowdisplaybreaks\n')
    subprocess.run(['pandoc', 'addendum.md', '--from=markdown+tex_math_dollars+tex_math_single_backslash',
                    '--standalone', '--to=latex', '--output=addendum.tex',
                    '--include-in-header=preamble.tex', '--variable=linestretch:1.05'],
                   cwd=HERE, check=True)
    cache = Path('/tmp/tt_unequal_bond_texcache')
    cache.mkdir(exist_ok=True)
    environment = dict(os.environ, TEXMFCACHE=str(cache), TEXMFVAR=str(cache))
    for _ in range(2):
        with (HERE / 'compile_output.txt').open('w') as output:
            subprocess.run(['lualatex', '-interaction=nonstopmode', '-halt-on-error', 'addendum.tex'],
                           cwd=HERE, env=environment, stdout=output, stderr=subprocess.STDOUT, check=True)
    output_path = HERE / 'compile_output.txt'
    output_path.write_text(''.join(line.rstrip() + '\n' for line in output_path.read_text().splitlines()))
    print(HERE / 'addendum.pdf')


if __name__ == '__main__':
    main()
