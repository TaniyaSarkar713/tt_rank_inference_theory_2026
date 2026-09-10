"""Exact Gaussian sufficient-statistic simulation for the proved 21-feature method."""
import hashlib,json,platform
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.stats import f,t as student_t,norm
from methods import coordinate_maps,intervals

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'simulations'/'results'/'tt_revision_2026_09_09'


def settings():
    specs=[]
    for n in (512,8192):
        for c in (0,2,8,32,128):specs.append(dict(n=n,c=c,h=0.,family='boundary'))
        for c in (2,8,32):specs.append(dict(n=n,c=c,h=2.,family='local_departure'))
    for n in (512,8192,131072):specs.append(dict(n=n,b=.3,h=0.,family='fixed_bond'))
    return specs


def wilson(phat,N):
    z=norm.ppf(.975); den=1+z*z/N
    center=(phat+z*z/(2*N))/den
    radius=z*np.sqrt(phat*(1-phat)/N+z*z/(4*N*N))/den
    return center-radius,center+radius


def main():
    OUT.mkdir(parents=True,exist_ok=True)
    N=5000; K=4; sigma=.2; amplitude=3.; alpha=.05
    coords,_,_,target=coordinate_maps(K); m=len(coords)
    assert m==6*K-3==21
    rows=[]; metadata=[]
    for idx,spec in enumerate(settings()):
        seed=2026090900+idx; rng=np.random.default_rng(seed)
        n=spec['n']; tn=sigma/np.sqrt(n); b=spec.get('b',spec.get('c',0)*tn)
        h=spec['h']; s=0. if h==0 else h*tn/b
        v=np.array([0.,1.,s]); B=b*v
        for _ in range(K-1):B=np.multiply.outer(B,v)
        B[(0,)*K]+=amplitude
        theta=np.array([B[q] for q in coords]); psi=B[(2,)*K]
        # Direct summation over omitted coordinates avoids cancellation.
        selected=set(coords)
        omitted2=sum(float(B[q]**2) for q in np.ndindex(B.shape) if q not in selected)
        tau=np.sqrt(sigma*sigma+omitted2)
        L=np.zeros((N,m,m)); ii,jj=np.tril_indices(m,-1)
        L[:,ii,jj]=rng.normal(size=(N,len(ii)))
        for j in range(m):L[:,j,j]=np.sqrt(rng.chisquare(n-j,size=N))
        S=L@np.swapaxes(L,1,2)
        g=rng.normal(size=(N,m))
        z=theta+tau*np.linalg.solve(np.swapaxes(L,1,2),g[...,None])[...,0]
        tauhat=tau*np.sqrt(rng.chisquare(n-m,size=N)/(n-m))
        e=tauhat*np.sqrt(m*f.ppf(1-alpha,m,n-m)/np.linalg.eigvalsh(S)[:,0])
        answers,certified,gap=intervals(z,e,K)
        unit=np.zeros((N,m,1)); unit[:,target,0]=1.
        sea=tauhat*np.linalg.norm(np.linalg.solve(L,unit)[...,0],axis=1)
        critical=student_t.ppf(1-alpha/2,n-m)
        answers['scalar_t']=(z[:,target]-critical*sea,z[:,target]+critical*sea)
        ball=np.linalg.norm(z-theta,axis=1)<=e
        raw={'z':z,'radius':e,'theta':theta,'psi':np.array(psi),
             'tauhat':tauhat,'pivot_certified':certified,'ball_covered':ball,
             'numerator_relative_bracket_gap':gap}
        length_by={}
        for method,(lo,hi) in answers.items():
            length=hi-lo; coverage=(lo<=psi)&(psi<=hi); phat=coverage.mean()
            assert np.all(length>=0)
            length_by[method]=length
            if method!='scalar_t':assert np.all(coverage[ball])
            ci=wilson(phat,N)
            raw[method+'_lower']=lo;raw[method+'_upper']=hi
            scale=tn if b==0 else tn*min(1.,(tn/b)**(K-1))
            rows.append(dict(setting=idx,seed=seed,replications=N,**{**spec,'b':b},
                bond_over_tn=b/tn,target=psi,tau=tau,method=method,
                coverage=phat,coverage_mcse=np.sqrt(phat*(1-phat)/N),
                coverage_low=ci[0],coverage_high=ci[1],
                mean_length=length.mean(),length_mcse=length.std(ddof=1)/np.sqrt(N),
                rate_scale=scale,mean_length_over_scale=length.mean()/scale,
                pivot_certified=certified.mean(),ball_coverage=ball.mean()))
        old=length_by['cross_separate']; new=length_by['cross_joint']
        assert np.all(new<=old+1e-12)
        raw['paired_length_difference']=new-old
        fn=OUT/f'setting_{idx:02}.npz'; np.savez_compressed(fn,**raw)
        metadata.append(dict(setting=idx,seed=seed,**{**spec,'b':b},tau=tau,
            original_sigma=sigma,amplitude=amplitude,omitted_signal_squared=omitted2,
            sha256=hashlib.sha256(fn.read_bytes()).hexdigest(),
            joint_to_separate_ratio=new.mean()/old.mean(),
            paired_difference_mcse=(new-old).std(ddof=1)/np.sqrt(N),
            max_numerator_bracket_gap=float(gap.max())))
        print(f"setting {idx+1}/19: n={n}, b/t={b/tn:.3g}, family={spec['family']}",flush=True)
    pd.DataFrame(rows).to_csv(OUT/'summary.csv',index=False)
    meta=dict(seed_rule='2026090900 + setting index',settings=metadata,
              independent_datasets=N*len(metadata),interval_records=N*len(metadata)*4,
              m=m,ambient_dimensions=[40]*K,ambient_p=40**K,
              replications_per_setting=N,alpha=alpha,python=platform.python_version(),
              sampling='Exact Wishart/normal/chi-square law of Gaussian OLS sufficient statistics; independent settings. No full ambient design is materialized.',
              coefficient_embedding='The displayed 3^4 tensor is embedded in the first three coordinates of each 40-dimensional mode.',
              scope='Prespecified-coordinate theorem; no learned-subspace or sharp minimum-distance simulation is claimed.')
    (OUT/'metadata.json').write_text(json.dumps(meta,indent=2)+'\n')


if __name__=='__main__':main()
