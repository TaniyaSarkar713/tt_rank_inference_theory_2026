"""Build the audit workbook from canonical CSV/JSON artifacts."""
from pathlib import Path
import json
import pandas as pd
ROOT=Path(__file__).resolve().parents[1];A=ROOT/'audit'

def main():
    tables={
      'Energy summaries':ROOT/'simulations/results/audit/summary.csv',
      'Paired comparisons':ROOT/'simulations/results/audit/paired_comparison.csv',
      'Finite variance summaries':ROOT/'simulations/results/robust_audit/summary.csv',
      'Finite variance slopes':ROOT/'simulations/results/robust_audit/slopes.csv',
      'Theorem inventory':A/'theorem_inventory.csv',
      'Essential claims':A/'essential_claim_inventory.csv',
      'Assumption audit':A/'assumption_audit.csv',
      'Assumption relaxations':A/'assumption_relaxation_matrix.csv',
      'Theorem strengthening':A/'theorem_strengthening_matrix.csv',
      'Source comparisons':ROOT/'literature/novelty_matrix.csv'}
    with pd.ExcelWriter(A/'audit_companion.xlsx',engine='openpyxl') as writer:
        for name,path in tables.items():
            d=pd.read_csv(path);d.to_excel(writer,sheet_name=name,index=False)
            ws=writer.sheets[name];ws.freeze_panes='A2';ws.auto_filter.ref=ws.dimensions
        for study in ['audit','robust_audit']:
            meta=json.loads((ROOT/'simulations/results'/study/'metadata.json').read_text())
            pd.DataFrame([{'key':k,'value':json.dumps(v)} for k,v in meta.items()]).to_excel(writer,sheet_name=study+' metadata',index=False)
    for name,path in tables.items():
        actual=pd.read_excel(A/'audit_companion.xlsx',sheet_name=name)
        expected=pd.read_csv(path)
        pd.testing.assert_frame_equal(actual,expected,check_dtype=False,check_exact=False,rtol=1e-12,atol=1e-15)
    print('PASS audit workbook: 12 sheets, numerical summaries and all comparison tables verified')
if __name__=='__main__':main()
