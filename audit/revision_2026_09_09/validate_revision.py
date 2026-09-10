"""Validate the dated revision, frozen inputs, study hashes and document build.

Use --refresh-manifest only after reviewing intentional changes. The old 303-file
manifest is preserved separately and its non-README artifacts must remain intact.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def manifest_rows(path):
    return [line.split('  ',1) for line in path.read_text().splitlines() if line]


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--refresh-manifest',action='store_true')
    args=parser.parse_args()
    frozen=json.loads((HERE/'input_hashes.json').read_text())
    for name,value in frozen.items():
        assert digest(HERE/'input_snapshot'/name)==value,name
    old=manifest_rows(HERE/'input_snapshot'/'MANIFEST.sha256')
    changed=[]
    for value,name in old:
        if digest(ROOT/name)!=value:changed.append(name)
    assert changed==['README.md'],changed

    out=ROOT/'simulations/results/tt_revision_2026_09_09'
    metadata=json.loads((out/'metadata.json').read_text())
    assert metadata['independent_datasets']==95000
    assert metadata['interval_records']==380000
    for setting in metadata['settings']:
        assert digest(out/f"setting_{setting['setting']:02}.npz")==setting['sha256']
    result=json.loads((out/'validation.json').read_text())
    for key in ['all_hashes_verified','raw_summaries_verified',
                'all_common_ball_inclusions','all_joint_lengths_no_greater']:
        assert result[key],key
    geom=json.loads((HERE/'geometry_checks.json').read_text())
    assert geom

    paper=ROOT/'paper/revision_2026_09_09'
    log=(paper/'main.log').read_text()
    for bad in ['Missing character:', 'Overfull', 'Undefined control sequence',
                'undefined references','Fatal error','Label(s) may have changed']:
        assert bad not in log,bad
    assert re.search(r'Output written on main.pdf \(32 pages,',log)
    tex=(paper/'main.tex').read_text()
    assert r'\$' not in tex,'Unparsed inline math dollar'
    assert (paper/'main.pdf').stat().st_size>100000
    # Readme local navigation is the user's entry point.
    for target in re.findall(r'\]\(([^)]+)\)',(ROOT/'README.md').read_text()):
        if '://' not in target:assert (ROOT/target.split('#')[0]).exists(),target

    if args.refresh_manifest:
        paths={name for _,name in old}
        additions=[HERE, paper, ROOT/'simulations/code/tt_revision',
                   out, ROOT/'simulations/figures/tt_revision_2026_09_09']
        for folder in additions:
            for path in folder.rglob('*'):
                if not path.is_file() or '__pycache__' in path.parts:continue
                if path.suffix in {'.aux','.log','.out','.toc','.pyc'}:continue
                paths.add(str(path.relative_to(ROOT)))
        for name in ['theory/general_normal_modulus.md',
                     'theory/certified_cross_inference.md',
                     'theory/growing_dimension_general_tt.md',
                     'theory/certified_minimum_distance_calibration.md',
                     'literature/revision_2026_09_09_novelty.md',
                     'simulations/tt_revision_design.md']:
            paths.add(name)
        (ROOT/'MANIFEST.sha256').write_text(''.join(
            f'{digest(ROOT/name)}  {name}\n' for name in sorted(paths)))
    rows=manifest_rows(ROOT/'MANIFEST.sha256')
    for value,name in rows:assert digest(ROOT/name)==value,name
    print(json.dumps(dict(frozen_inputs=len(frozen),historical_artifacts=len(old),
                         intentional_historical_changes=changed,
                         manifest_artifacts=len(rows),raw_settings=len(metadata['settings']),
                         independent_datasets=95000,interval_records=380000,
                         manuscript_pages=32,latex_diagnostics='clean',
                         all_checks_passed=True),indent=2))


if __name__=='__main__':main()
