"""Post-audit paired experiment; no primary result is overwritten.

One independent cohort of 2,000 datasets for each of three n values. All seven
prespecified loading choices and five intervals reuse each dataset (pairing).
"""
from pathlib import Path
import hashlib,json,sys
import numpy as np
import pandas as pd
from methods import Data,sufficient,graded,ambient
from audit_methods import energy_interval
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'simulations/results/audit';OUT.mkdir(parents=True,exist_ok=True)

def main():
    seed=2026090717;reps=2000;lam=3.;sigma=.2;blocks=(2,4,2);p=16
    kappas=[0.,.1,1.,10.,100.,1000.,10000.];ns=[512,8192,131072]
    for n in ns:
        rng=np.random.default_rng(np.random.SeedSequence([seed,n]));rows=[]
        tn=sigma/np.sqrt(n);sn=tn**3/lam**2;b=np.zeros(p);b[0]=lam
        for rep in range(reps):
            z,S,scale=sufficient(rng,n,b,sigma);data=Data(z,S,scale,n,sigma)
            for kappa in kappas:
                eps=kappa*tn**2/lam**2;a=np.zeros(p);a[-1]=1;a[8]=eps;a/=np.linalg.norm(a)
                oracle_scale=(eps*tn+sn)/np.sqrt(1+eps**2)
                old=graded(data,a,blocks);new=energy_interval(data,a,blocks)
                oldu=graded(data,a,blocks,unknown=True);newu=energy_interval(data,a,blocks,unknown=True)
                for prev,nxt in [(old,new),(oldu,newu)]:
                    assert nxt[1]-nxt[0]<=prev[1]-prev[0]+1e-12
                for method,result in [('original',old),('energy',new),('original_unknown',oldu),('energy_unknown',newu),('ambient',ambient(data,a))]:
                    lo,hi,center,fallback,empty=result;target=float(a@b)
                    rows.append((n,rep,kappa,eps,method,lo,hi,target,hi-lo,int(lo<=target<=hi),center,fallback,empty,oracle_scale,sn))
        df=pd.DataFrame(rows,columns=['n','rep','kappa','epsilon','method','lower','upper','target','length','covered','center','fallback','empty','rate_scale','pure_cubic_scale'])
        df.to_csv(OUT/f'replicates_n{n}.csv.gz',index=False,compression={'method':'gzip','mtime':0})
        print(f'Finished n={n}: {reps} datasets, {len(df)} intervals',flush=True)
    deps=['gaussian_base.py','methods.py','audit_methods.py','run_audit.py']
    meta={'date':'2026-09-07','stage':'post-audit addendum; designed after original experiment','seed':seed,'replications_per_cohort':reps,'n':ns,'kappa':kappas,'unique_datasets':reps*len(ns),'paired_loadings_and_methods':True,'lambda':lam,'sigma':sigma,'blocks':blocks,'code_hashes':{f:hashlib.sha256((ROOT/'simulations/code'/f).read_bytes()).hexdigest() for f in deps}}
    (OUT/'metadata.json').write_text(json.dumps(meta,indent=2)+'\n')
if __name__=='__main__':main()
