"""Prespecified-design addendum: check convergence of finite-n length slopes.

Added after the primary run revealed visible inverse-Gram transients. No method
or tuning parameter changes. Exact sufficient statistics avoid allocating n rows.
"""
import csv,json,hashlib
from pathlib import Path
from run_study import configurations,one_setting,ROOT

def main():
    out=ROOT/'results'/'asymptotic';out.mkdir(parents=True,exist_ok=True)
    base=[c for c in configurations() if c['family']=='classification' and c['n']==8192]
    cfg=[]
    for c in base:
        for n in (131072,2097152):
            d=dict(c);d['id']=81+len(cfg);d['n']=n;cfg.append(d)
    meta=dict(seed=20260907,reps=2000,settings=cfg,reason='Additional large-n points to resolve finite-p inverse-Gram effects in the mean-length slope; methods unchanged',
              code_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__).parent/name for name in ('gaussian_base.py','methods.py','run_study.py','run_asymptotic.py')]})
    (out/'metadata.json').write_text(json.dumps(meta,indent=2));rows=[]
    for c in cfg:rows.extend(one_setting(c,2000,20260907,out))
    with (out/'summary.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    print('FINISHED addendum: 24000 datasets; methods and tuning unchanged.')
if __name__=='__main__':main()
