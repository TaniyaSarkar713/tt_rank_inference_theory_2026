"""Separate, prespecified-after-proof finite-variance addendum.

The Gaussian and t_2.5 errors have variance sigma_bound². The t_2.5 law lacks
third/fourth moments. All observations are independent; no contamination.
"""
from pathlib import Path
import json,hashlib
import numpy as np
import pandas as pd
from robust_localizer import median_ols_ball,BallData
from audit_methods import energy_interval
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'simulations/results/robust_audit';OUT.mkdir(parents=True,exist_ok=True)

def main():
    seed=2026090801;reps=1000;ns=[512,2048,8192];sigma=.2;lam=3.;p=16
    for noiseid,noise in enumerate(['Gaussian','t2.5']):
        for n in ns:
            rng=np.random.default_rng(np.random.SeedSequence([seed,noiseid,n]));rows=[]
            b=np.zeros(p);b[0]=lam;a=np.zeros(p);a[-1]=1
            for rep in range(reps):
                X=rng.normal(size=(n,p))
                eps=sigma*(rng.normal(size=n) if noise=='Gaussian' else rng.standard_t(2.5,size=n)*np.sqrt(.5/2.5))
                Y=X@b+eps
                for blocks in [(2,4,2),(2,2,2,2)]:
                    J=len(blocks);z,e=median_ols_ball(X,Y,sigma,J)
                    data=BallData(z,e,n);lo,hi,center,fallback,empty=energy_interval(data,a,blocks)
                    ball=int(np.linalg.norm(z-b)<=e)
                    if ball:assert lo-1e-12<=0<=hi+1e-12
                    rows.append((noise,n,rep,J,lo,hi,hi-lo,int(lo<=0<=hi),center,e,np.linalg.norm(z-b),ball,fallback,empty))
            df=pd.DataFrame(rows,columns=['noise','n','rep','q','lower','upper','length','covered','center','radius','localization_error','ball_covered','fallback','empty'])
            df.to_csv(OUT/f'replicates_{noise}_n{n}.csv.gz',index=False,compression={'method':'gzip','mtime':0})
            print(f'Finished robust {noise}, n={n}: {reps} datasets',flush=True)
    deps=['gaussian_base.py','methods.py','audit_methods.py','robust_localizer.py','run_robust_audit.py']
    meta={'date':'2026-09-08','stage':'finite-variance post-proof addendum','seed':seed,'replications_per_cohort':reps,'n':ns,'noise':['Gaussian','t2.5'],'paired_profiles':[3,4],'unique_datasets':6000,'sigma_bound':sigma,'lambda':lam,'code_hashes':{f:hashlib.sha256((ROOT/'simulations/code'/f).read_bytes()).hexdigest() for f in deps}}
    (OUT/'metadata.json').write_text(json.dumps(meta,indent=2)+'\n')
if __name__=='__main__':main()
