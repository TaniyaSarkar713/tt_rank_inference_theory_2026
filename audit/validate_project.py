"""Structural/provenance audit. Numerical studies have their own validators."""
from pathlib import Path
import hashlib,json,re,csv
ROOT=Path(__file__).resolve().parents[1]
AUDIT=ROOT/'audit'

def main():
    baseline=json.loads((AUDIT/'baseline_hashes.json').read_text())
    for f,h in baseline.items():assert hashlib.sha256((AUDIT/'baseline_2026-09-07'/f).read_bytes()).hexdigest()==h,f
    texfiles=sorted((ROOT/'paper').rglob('*.tex'))
    text='\n'.join(f.read_text() for f in texfiles)
    labels=re.findall(r'\\label\{([^}]+)\}',text);assert len(labels)==len(set(labels))
    refs=re.findall(r'\\(?:eqref|ref)\{([^}]+)\}',text);assert set(refs)<=set(labels)
    eqs=[]
    for chunk in re.findall(r'\\begin\{(?:equation|align)\}(.*?)\\end\{(?:equation|align)\}',text,re.S):eqs+=re.findall(r'\\label\{([^}]+)\}',chunk)
    assert set(eqs)<=set(refs),set(eqs)-set(refs)
    bib=(ROOT/'paper/references.bib').read_text();keys=re.findall(r'@\w+\{([^,]+),',bib);assert len(keys)==len(set(keys))
    cites=[]
    for group in re.findall(r'\\cite\w*\{([^}]+)\}',text):cites.extend(x.strip() for x in group.split(','))
    assert set(cites)<=set(keys)
    log=(ROOT/'build/paper/main.log').read_text()
    assert not re.search(r'undefined|Overfull|Underfull|LaTeX Warning|Package .* Warning',log,re.I)
    aux=(ROOT/'build/paper/main.aux').read_text()
    rows=list(csv.DictReader((AUDIT/'theorem_inventory.csv').open()))
    assert len(rows)==17
    mapping={}
    for row in rows:
        label=row['LaTeX label'];m=re.search(r'\\newlabel\{'+re.escape(label)+r'\}\{\{([^}]+)\}\{([^}]+)\}',aux)
        assert m,label;mapping[row['ID']]={'label':label,'printed_number':m.group(1),'page':int(m.group(2)),'status':row['Final status']}
    (AUDIT/'theorem_number_map.json').write_text(json.dumps(mapping,indent=2)+'\n')
    sources=json.loads((ROOT/'literature/references/source_cards.json').read_text());assert len(sources)==28
    assert len({s['key'] for s in sources})==28
    for name in ['reconstructed_framework.md','theorem_inventory.md','essential_claim_inventory.md','assumption_audit.md','assumption_relaxation_matrix.md','theorem_strengthening_matrix.md','proof_audit.md','dependency_graph.md','external_results_and_prior_art.md','theoretical_comparison.md','referee_attack.md','open_and_resolved.md','final_verdict.md']:
        assert (AUDIT/name).stat().st_size>200,name
    val={'baseline_files_unchanged':len(baseline),'numbered_results':len(rows),'essential_claims':len(list(csv.DictReader((AUDIT/'essential_claim_inventory.csv').open()))),'counterexamples':len(re.findall(r'\\paragraph\{C\d+:',text)),'labels':len(labels),'numbered_equations_referenced':len(eqs),'bibliography_entries':len(keys),'cited_references':len(set(cites)),'literature_comparisons':len(sources),'latex_log_clean':True,'all_internal_references_resolved':True,'all_inventory_labels_resolved':True}
    (AUDIT/'structural_validation.json').write_text(json.dumps(val,indent=2)+'\n');print(json.dumps(val,indent=2))
if __name__=='__main__':main()
