"""Check extension freshness, navigation, build evidence, and historical integrity.

Run after intentionally updating MANIFEST.sha256. This validator does not write
files, rerun experiments, or replace a mathematical proof audit.
"""
import hashlib
import json
from pathlib import Path
import re
import runpy
import subprocess
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def main():
    checks = json.loads((HERE / 'checks.json').read_text())
    assert checks['all_checks_passed']
    assert checks['selected_coordinate_count'] == 23
    for name, expected in checks['source_sha256'].items():
        assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == expected, name

    paper = ROOT / 'paper/revision_2026_09_11'
    build = runpy.run_path(str(paper / 'build_addendum.py'))
    assembled = (paper / 'addendum.md').read_text()
    for name in ['unequal_bond_modulus.md', 'unequal_bond_inference.md']:
        source = ROOT / 'theory' / name
        assert build['relocate_links'](source.read_text(), source) in assembled, name

    output = (paper / 'compile_output.txt').read_text()
    for diagnostic in ['Missing character:', 'Overfull', 'Underfull',
                       'Undefined control sequence', 'undefined references',
                       'Fatal error', 'Label(s) may have changed']:
        assert diagnostic not in output, diagnostic
    match = re.search(r'Output written on addendum.pdf \((\d+) pages, (\d+) bytes\)', output)
    assert match, 'Missing final successful LaTeX build evidence'
    pdf = (paper / 'addendum.pdf').read_bytes()
    assert pdf.startswith(b'%PDF-') and len(pdf) == int(match[2])
    assert r'\$' not in (paper / 'addendum.tex').read_text(), 'Unparsed inline math'

    documents = [ROOT / 'README.md', *HERE.glob('*.md'), paper / 'addendum.md',
                 ROOT / 'theory/unequal_bond_modulus.md',
                 ROOT / 'theory/unequal_bond_inference.md',
                 ROOT / 'literature/unequal_bond_comparison_2026_09_11.md']
    local_links = 0
    for source in documents:
        for target in re.findall(r'\]\(([^)]+)\)', source.read_text()):
            if '://' in target or target.startswith('#'):
                continue
            assert (source.parent / target.split('#')[0]).exists(), (source, target)
            local_links += 1

    historical = subprocess.run(
        [sys.executable, str(ROOT / 'audit/revision_2026_09_09/validate_revision.py')],
        cwd=ROOT, capture_output=True, text=True, check=True)
    print(json.dumps({
        'all_checks_passed': True,
        'checked_source_hashes': len(checks['source_sha256']),
        'assembled_proofs_current': True,
        'addendum_pages': int(match[1]),
        'addendum_latex_diagnostics': 'clean',
        'local_links_checked': local_links,
        'historical_and_manifest_validation': json.loads(historical.stdout),
        'scope': 'Artifact consistency only; mathematical status is in proof_audit.md.',
    }, indent=2))


if __name__ == '__main__':
    main()
