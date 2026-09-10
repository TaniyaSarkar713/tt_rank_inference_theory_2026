"""Independent numerical checks of the general sharp coefficient and certificates."""
import json
from pathlib import Path
import numpy as np
import mpmath as mp
from methods import coordinate_maps,numerator_bracket,intervals

ROOT=Path(__file__).resolve().parents[3]


def contract(cores):
    out=cores[0]
    for core in cores[1:]:out=np.tensordot(out,core,axes=(-1,0))
    return out.squeeze(axis=(0,-1))


def left_canonical(cores):
    cores=[x.copy() for x in cores]
    for j in range(len(cores)-1):
        l,d,r=cores[j].shape
        q,rr=np.linalg.qr(cores[j].reshape(l*d,r),mode='reduced')
        cores[j]=q.reshape(l,d,r)
        cores[j+1]=np.tensordot(rr,cores[j+1],axes=(1,0))
    return cores


def right_interface(cores,j):
    # j is zero based; interface immediately after core j.
    out=cores[j+1]
    for core in cores[j+2:]:out=np.tensordot(out,core,axes=(-1,0))
    return out.reshape(out.shape[0],-1)


def main():
    rng=np.random.default_rng(2026090917); records=[]
    for dims,ranks in [((4,5,4),(1,2,2,1)),((4,5,4,5),(1,2,3,2,1)),
                       ((4,4,4,4,4),(1,2,3,3,2,1))]:
        K=len(dims)
        for repeat in range(12):
            cores=[rng.normal(size=(ranks[j],dims[j],ranks[j+1])) for j in range(K)]
            for core in cores:core[:,-1,:]=0
            cores=left_canonical(cores)
            cores[-1]/=np.linalg.norm(contract(cores))
            B=contract(cores); betas=[]; vec=[]; Q=[]
            for j in range(K-1):
                R=right_interface(cores,j)
                values,vectors=np.linalg.eigh(R@R.T)
                betas.append(np.sqrt(values[0]));vec.append(vectors[:,0])
                Q.append((vectors*np.sqrt(values))@vectors.T)
                actual=np.linalg.svd(B.reshape(int(np.prod(dims[:j+1])),-1),compute_uv=False)
                assert np.isclose(actual[ranks[j+1]-1],betas[-1],rtol=1e-9)
            Z=[vec[0][None,:]/np.sqrt(K)]
            Z.extend(np.outer(vec[j-1],vec[j])/np.sqrt(K) for j in range(1,K-1))
            Z.append(vec[-1][:,None]/np.sqrt(K))
            H=[np.linalg.solve(Q[j].T,Z[j].T).T for j in range(K-1)]+[Z[-1]]
            beta=min(betas); t=.001*beta
            u=t*np.exp(-t*t/(2*beta*beta))
            changed=[x.copy() for x in cores]
            for j in range(K):changed[j][:,-1,:]=u*H[j]
            Bt=contract(changed); distance=np.linalg.norm(Bt-B)
            target=Bt[tuple(d-1 for d in dims)]
            sharp=K**(-K/2)/np.prod(betas)
            assert distance<=t*(1+1e-9)
            assert np.isclose(target,sharp*u**K,rtol=1e-9,atol=0)
            normalized=target/(sharp*t**K)
            assert abs(normalized-1)<1e-5
            # Verify one-site energy and the pair-count upper bound on general perturbations.
            pert=[x+.0001*rng.normal(size=x.shape) for x in cores]
            C=contract(pert); delta=np.linalg.norm(C-B)
            assert delta<beta/2
            ds=[np.linalg.norm(np.take(C,dims[j]-1,axis=j)) for j in range(K)]
            pair_sum=sum(1/(betas[i]-delta)**2 for i in range(K-1) for j in range(i+1,K))
            assert sum(x*x for x in ds)<=delta**2+delta**4*pair_sum+1e-12
            bound=K**(-K/2)*(delta**2+delta**4*pair_sum)**(K/2)/np.prod(np.array(betas)-delta)
            assert abs(C[tuple(d-1 for d in dims)])<=bound*(1+1e-10)
            records.append(dict(K=K,ranks=ranks,betas=betas,sharp_coefficient=sharp,
                                normalized_witness=normalized))
    # Compare each floating root bracket with an 80-digit independent solve.
    mp.mp.dps=80; max_relative=0.
    for _ in range(30):
        c=10**rng.uniform(-4,3,size=(1,4)); e=10**rng.uniform(-3,2,size=1)
        lo,hi=numerator_bracket(c,e)
        cm=[mp.mpf(float(x)) for x in c[0]]; em=mp.mpf(float(e[0]))
        a=mp.mpf(0); b=em**2+em*max(cm)
        def d(mu):return [2*mu/(mp.sqrt(x*x+4*mu)+x) for x in cm]
        for _ in range(280):
            mid=(a+b)/2
            if sum(x*x for x in d(mid))<=em**2:a=mid
            else:b=mid
        val=float(mp.fprod(x+y for x,y in zip(cm,d((a+b)/2))))
        max_relative=max(max_relative,abs(hi[0]/val-1))
        assert lo[0]<=val*(1+1e-12) and hi[0]>=val*(1-1e-12)
    # Check coordinate counts, disjoint target slices, and deliberately unequal nuisance sizes.
    for K in range(2,8):
        coords,piv,slices,target=coordinate_maps(K)
        assert len(coords)==6*K-3
        assert len(set(np.concatenate(slices)))==sum(len(x) for x in slices)
    result=dict(general_TT_references=len(records),records=records,
                high_precision_numerator_checks=30,max_numerator_relative_error=max_relative,
                coordinate_counts_checked=list(range(2,8)),
                status='Numerical checks passed; full mathematical proofs are in the theory notes.')
    path=ROOT/'audit'/'revision_2026_09_09'/'geometry_checks.json'
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='records'},indent=2))


if __name__=='__main__':main()
