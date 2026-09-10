"""Execute the prespecified study. Per-setting seeds do not depend on ordering."""
import argparse,csv,gzip,json,hashlib,time
from pathlib import Path
import numpy as np
from scipy.stats import norm
from methods import (Data,sufficient,raw_observations,graded,ambient,wald,
                     elementary_loading,block_dimensions,outer)
ROOT=Path(__file__).resolve().parents[1]


def configurations():
    cfg=[]
    def add(**kw):
        base=dict(sigma=.2,lam=3.,covariance=0.,noise='gaussian',dense=False,c=0.,eta_kind='zero',departure=False)
        base.update(kw); base['id']=len(cfg); cfg.append(base)
    profiles=[('three_product',[2]*3,[1,1],3),('four_product',[2]*4,[1,1,1],4),
              ('four_three_blocks',[2]*4,[1,2,1],3),('four_two_blocks',[2]*4,[2,1,2],2),
              ('four_slack',[2]*4,[2,2,2],1),('six_singular',[2]*6,[1,2,2,2,1],3)]
    for name,dims,caps,q in profiles:
        for n in (512,2048,8192): add(family='classification',profile=name,dims=dims,caps=caps,q=q,n=n)
    for n in (512,2048,8192):
        for c in (0,1,2,4,8): add(family='activation',profile='four_three_blocks',dims=[2]*4,caps=[1,2,1],q=3,n=n,c=c)
    for n in (512,2048,8192):
        for eta_kind in ('zero','fast','100fast','10000fast','quadratic','ambient'):
            for departure in ([False] if eta_kind=='zero' else [False,True]):
                add(family='tube',profile='four_three_blocks',dims=[2]*4,caps=[1,2,1],q=3,n=n,eta_kind=eta_kind,departure=departure)
    for n in (512,2048):
        for lam in (.5,1.,3.): add(family='diagnostic',profile='signal',dims=[2]*4,caps=[1,2,1],q=3,n=n,lam=lam)
        add(family='diagnostic',profile='dense',dims=[2]*4,caps=[1,2,1],q=3,n=n,dense=True)
        add(family='diagnostic',profile='correlated_design',dims=[2]*4,caps=[1,2,1],q=3,n=n,covariance=.5)
    for noise in ('t5','heteroskedastic','dependent','contamination_0.01','contamination_0.05'):
        add(family='stress',profile=noise,dims=[2]*4,caps=[1,2,1],q=3,n=512,noise=noise)
    return cfg


def truth_and_loadings(c):
    p=int(np.prod(c['dims'])); blocks=block_dimensions(c['dims'],c['caps'])
    b=np.zeros(p); b[0]=c['lam']; a=np.zeros(p); a[-1]=1.
    pure=elementary_loading(blocks); tn=c['sigma']/np.sqrt(c['n']); fast=tn**c['q']/c['lam']**(c['q']-1)
    eta={'zero':0.,'fast':fast,'100fast':100*fast,'10000fast':10000*fast,'quadratic':tn**2/c['lam'],'ambient':tn}[c['eta_kind']]
    weak=0.
    if c['family']=='activation':
        u=c['c']*tn/c['lam']; factors=[]
        for d in blocks:
            v=np.zeros(d); v[0]=1; v[-1]=u; factors.append(v)
        b=c['lam']*outer(factors).ravel(); weak=c['lam']*abs(u)*(1+u*u)
    elif c['departure']: b=b+eta*a
    if c['dense']:
        us=[]; ws=[]
        for k in range(len(c['dims'])):
            angle=.31+.17*k; us.append(np.array([np.cos(angle),np.sin(angle)])); ws.append(np.array([-np.sin(angle),np.cos(angle)]))
        b=c['lam']*outer(us).ravel(); a=outer(ws).ravel()
        pure=[ws[0],outer(ws[1:3]).ravel(),ws[3]]
    loads=[('normal',a,pure,c['q'])]
    if c['family']=='activation':
        at=np.zeros(p); at[0]=1; at[6]=.35; at/=np.linalg.norm(at)
        loads.append(('tangent',at,None,1))
    return b,loads,blocks,eta,weak


def one_setting(c,reps,seed,out):
    rng=np.random.default_rng(np.random.SeedSequence([seed,c['id']]))
    beta,loads,blocks,eta,weak=truth_and_loadings(c); p=len(beta)
    cov=None if not c['covariance'] else c['covariance']**np.abs(np.arange(p)[:,None]-np.arange(p)[None,:])
    fields=['rep','loading','method','covered','length','center','target','squared_error','fallback','empty','selected_rank','lower','upper']
    vals={}; start=time.time()
    path=out/f"replicates_{c['id']:03d}.csv.gz"
    with gzip.open(path,'wt',newline='') as fh:
        writer=csv.writer(fh); writer.writerow(fields)
        for rep in range(reps):
            if c['noise']=='gaussian': z,S,scale=sufficient(rng,c['n'],beta,c['sigma'],cov)
            else: z,S,scale=raw_observations(rng,c['n'],beta,c['sigma'],c['noise'])
            data=Data(z,S,scale,c['n'],c['sigma'])
            if c['family']=='activation': sv2=np.linalg.svd(z.reshape(4,4),compute_uv=False)[1]
            for lname,a,pure,q in loads:
                methods={
                    'graded':(graded(data,a,blocks,pure=pure),np.nan),
                    'ambient':(ambient(data,a),np.nan),
                    'wald':(wald(data,a,blocks,pure=pure),np.nan),
                    'degree_wald':(wald(data,a,blocks,degree=q,pure=pure),np.nan)}
                if c['family'] in ('classification','diagnostic','stress'):
                    methods['graded_unknown_sigma']=(graded(data,a,blocks,unknown=True,pure=pure),np.nan)
                    methods['ambient_unknown_sigma']=(ambient(data,a,unknown=True),np.nan)
                if c['family']=='classification':
                    first=next((k for k,r in enumerate(c['caps']) if r==1),None)
                    if first is None: ans=ambient(data,a)
                    else:
                        mb=(int(np.prod(c['dims'][:first+1])),int(np.prod(c['dims'][first+1:])))
                        ans=graded(data,a,mb,pure=elementary_loading(mb))
                    methods['single_matrix']=(ans,np.nan)
                elif c['family']=='activation':
                    known=2 if c['c'] else 1; bd=blocks if known==2 else tuple(c['dims'])
                    pp=elementary_loading(bd) if lname=='normal' else None
                    methods['known_rank_wald']=(wald(data,a,bd,pure=pp),known)
                    for kappa in (1,2,3):
                        selected=2 if sv2>kappa*c['sigma']*np.sqrt(2/c['n']) else 1
                        bd=blocks if selected==2 else tuple(c['dims']); pp=elementary_loading(bd) if lname=='normal' else None
                        methods[f'selected_rank_wald_k{kappa}']=(wald(data,a,bd,pure=pp),selected)
                elif c['family']=='tube': methods['tube_graded']=(graded(data,a,blocks,eta=eta,pure=pure),np.nan)
                target=float(a@beta)
                for method,(ans,selected) in methods.items():
                    lo,hi,center,fallback,empty=ans
                    if not (np.isfinite(lo) and np.isfinite(hi) and lo<=hi): raise ValueError((c,rep,method,ans))
                    covered=int(lo<=target<=hi); length=hi-lo; se=(center-target)**2
                    writer.writerow([rep,lname,method,covered,length,center,target,se,fallback,empty,selected,lo,hi])
                    vals.setdefault((lname,method),[]).append([covered,length,se,fallback,empty,float(selected==2) if np.isfinite(selected) else np.nan])
    rows=[]
    for (lname,method),vv in vals.items():
        v=np.array(vv); coverage=v[:,0].mean(); zcrit=norm.ppf(.975); den=1+zcrit*zcrit/reps
        wilson_center=(coverage+zcrit*zcrit/(2*reps))/den
        wilson_half=zcrit*np.sqrt(coverage*(1-coverage)/reps+zcrit*zcrit/(4*reps*reps))/den
        row=dict(setting=c['id'],family=c['family'],profile=c['profile'],n=c['n'],p=p,q=c['q'] if lname=='normal' else 1,
                 lam=c['lam'],sigma=c['sigma'],c=c['c'],eta=eta,eta_kind=c['eta_kind'],departure=c['departure'],weak_bond=weak,
                 noise=c['noise'],covariance=c['covariance'],loading=lname,method=method,reps=reps,coverage=coverage,
                 coverage_mcse=np.sqrt(coverage*(1-coverage)/reps),coverage_lo=wilson_center-wilson_half,coverage_hi=wilson_center+wilson_half,
                 mean_length=v[:,1].mean(),length_mcse=v[:,1].std(ddof=1)/np.sqrt(reps),mse=v[:,2].mean(),
                 mse_mcse=v[:,2].std(ddof=1)/np.sqrt(reps),fallback_rate=v[:,3].mean(),empty_rate=v[:,4].mean(),
                 rank2_frequency=np.nan if np.all(np.isnan(v[:,5])) else np.nanmean(v[:,5]))
        rows.append(row)
    print(f"setting {c['id']+1:02d}/{len(configurations())}: {c['family']} {c['profile']} n={c['n']}, {reps} repetitions, {time.time()-start:.1f}s",flush=True)
    return rows


def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--reps',type=int,default=2000); parser.add_argument('--seed',type=int,default=20260907); parser.add_argument('--smoke',action='store_true'); args=parser.parse_args()
    out=ROOT/'results'/('smoke' if args.smoke else 'study'); out.mkdir(parents=True,exist_ok=True)
    cfg=configurations(); cfg=cfg[:1]+cfg[18:19]+cfg[35:36]+cfg[-1:] if args.smoke else cfg
    hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__).parent/name for name in ('gaussian_base.py','methods.py','run_study.py')]}
    metadata=dict(seed=args.seed,reps=args.reps,settings=cfg,code_sha256=hashes,numpy=np.__version__,sampler='Exact Bartlett law for Gaussian settings; raw observations for stress settings',design_locked='2026-09-07')
    (out/'metadata.json').write_text(json.dumps(metadata,indent=2))
    rows=[]
    for c in cfg: rows.extend(one_setting(c,args.reps,args.seed,out))
    with (out/'summary.csv').open('w',newline='') as fh:
        writer=csv.DictWriter(fh,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    print(f"FINISHED: {len(cfg)*args.reps} independent datasets; {len(rows)} summary rows",flush=True)
if __name__=='__main__': main()
