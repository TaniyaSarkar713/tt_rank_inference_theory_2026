"""Numerical falsification checks for substantive geometric claims."""
import numpy as np
from math import comb
from methods import outer,components,loading_info,Data,sufficient,graded,block_dimensions

def main():
    rng=np.random.default_rng(702609)
    # Fast pure-product projector evaluation versus direct tensor projections.
    for dims in [(2,2,2,2),(2,4,2),(2,16,2)]:
        for _ in range(20):
            vv=[rng.normal(size=d) for d in dims];vv=[v/np.linalg.norm(v) for v in vv]
            aa=[rng.normal(size=d) for d in dims];aa=[a/np.linalg.norm(a) for a in aa]
            a=outer(aa).ravel(); parts=components(a,vv); norms,pa=loading_info(a,vv,aa)
            assert np.allclose(sum(parts),a,atol=2e-12)
            assert np.allclose(norms,[np.linalg.norm(x) for x in parts],atol=2e-12)
            assert np.allclose(pa,parts[0]+parts[1],atol=2e-12)
    print('PASS orthogonal grading and fast pure-loading computation')
    # Exact witness path: all TT caps, distance, target, limiting constant.
    for caps in [(1,1,1),(1,2,1),(2,1,2),(2,2,2),(1,2,2,2,1)]:
        dims=[2]*(len(caps)+1); blocks=block_dimensions(dims,caps); q=len(blocks);lam=3.
        b0=np.zeros(np.prod(dims));b0[0]=lam
        for relative_t in (.01,.001):
            # expm1 avoids cancellation in the exact small-radius formula.
            t=lam*relative_t;s=np.sqrt(np.expm1(np.log1p(relative_t**2)/q))
            factors=[]
            for d in blocks:
                v=np.zeros(d);v[0]=1;v[-1]=s;factors.append(v)
            b=lam*outer(factors).ravel()
            assert np.isclose(np.linalg.norm(b-b0),t,rtol=1e-9)
            for k,cap in enumerate(caps):
                singular=np.linalg.svd(b.reshape(2**(k+1),-1),compute_uv=False)
                assert (singular>1e-10).sum()<=cap
            ratio=b[-1]*lam**(q-1)/t**q
            assert abs(ratio*q**(q/2)-1)<1e-4
    print('PASS TT feasibility, exact path distances, contact constants, singular six-mode example')
    # Random points inside known tubes: on the actual OLS ball event the
    # computed interval must contain the target, including unknown sigma.
    checked=0
    for Jdims in [(2,2,2,2),(2,4,2),(2,16,2)]:
        p=int(np.prod(Jdims));n=3*p+32
        for _ in range(120):
            vv=[rng.normal(size=d) for d in Jdims]; vv=[v/np.linalg.norm(v) for v in vv]
            b0=2*outer(vv).ravel(); a=rng.normal(size=p);a/=np.linalg.norm(a)
            eta=rng.uniform(0,.03); direction=rng.normal(size=p);direction/=np.linalg.norm(direction)
            b=b0+eta*direction
            z,S,scale=sufficient(rng,n,b,.1); data=Data(z,S,scale,n,.1)
            for unknown in (False,True):
                if np.linalg.norm(z-b)<=data.radius(unknown):
                    lo,hi,*_=graded(data,a,Jdims,eta=eta,unknown=unknown)
                    assert lo-1e-12<=a@b<=hi+1e-12
                    checked+=1
    print(f'PASS {checked} interval certificates on verified localization events')
if __name__=='__main__':main()
