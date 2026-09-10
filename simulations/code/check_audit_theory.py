"""Independent falsification checks for new substantive inequalities."""
from itertools import combinations,product
from math import comb
import numpy as np
from methods import Data,sufficient,graded,outer,components
from audit_methods import energy_interval

def main():
    rng=np.random.default_rng(2026090703)
    for J in range(2,8):
        for _ in range(100):
            x=np.exp(rng.normal(size=J)*3)
            for ell in range(2,J+1):
                e=sum(np.prod(x[list(S)]) for S in combinations(range(J),ell))
                bound=comb(J,ell)*(sum(x)/J)**ell
                assert e<=bound*(1+1e-12)
    print('PASS 2,100 elementary-symmetric energy inequalities')
    # Walsh isolation with arbitrary lower-degree components; masks and basis
    # coefficients chosen in all grades, not only the first nonzero grade.
    walsh_checks=0
    for dims in [(2,4,2),(2,2,2,2),(2,16,2)]:
        J=len(dims);p=np.prod(dims);b0=np.zeros(p);b0[0]=2.;v=[]
        for d in dims:w=np.zeros(d);w[0]=1;v.append(w)
        for _ in range(15):
            a=rng.normal(size=p);a/=np.linalg.norm(a)
            t=.2;lam=2.
            for ell in range(1,J+1):
                S=tuple(range(ell));s=np.sqrt(np.expm1(np.log1p((t/lam)**2)/ell))
                index=tuple(dims[j]-1 if j in S else 0 for j in range(J))
                coef=a.reshape(dims)[index];values=[];chars=[]
                for signs in product([-1,1],repeat=ell):
                    factors=[w.copy() for w in v]
                    for j,sign in zip(S,signs):factors[j][-1]=sign*s
                    b=lam*outer(factors).ravel()
                    assert np.isclose(np.linalg.norm(b-b0),t,rtol=1e-12)
                    values.append(a@(b-b0));chars.append(np.prod(signs))
                lhs=np.mean(np.array(values)*chars);rhs=lam*coef*s**ell
                assert np.isclose(lhs,rhs,rtol=1e-8,atol=2e-14)
                assert max(np.abs(values))+1e-14>=abs(rhs)
                walsh_checks+=1
    print(f'PASS {walsh_checks} Walsh coefficient isolations with cancellation')
    checked=0;paired=0
    for dims in [(2,4,2),(2,2,2,2),(2,16,2)]:
        p=np.prod(dims);n=3*p+20
        for _ in range(150):
            vv=[rng.normal(size=d) for d in dims];vv=[x/np.linalg.norm(x) for x in vv]
            b0=3*outer(vv).ravel();eta=rng.uniform(0,.02)
            h=rng.normal(size=p);h/=np.linalg.norm(h);b=b0+eta*h
            a=rng.normal(size=p);a/=np.linalg.norm(a)
            z,S,scale=sufficient(rng,n,b,.2);data=Data(z,S,scale,n,.2)
            for unknown in (False,True):
                prev=graded(data,a,dims,eta,unknown);nxt=energy_interval(data,a,dims,eta,unknown)
                assert nxt[1]-nxt[0]<=prev[1]-prev[0]+1e-12;paired+=1
                if np.linalg.norm(z-b)<=data.radius(unknown):
                    assert nxt[0]-1e-12<=a@b<=nxt[1]+1e-12;checked+=1
    print(f'PASS {paired} paired length inequalities and {checked} coverage certificates')
    # Minimum revised sample size and edge dimensions: inversion works; numerical
    # draws do not prove inverse-moment finiteness (proved analytically).
    for dims in [(1,),(2,4,2)]:
        p=np.prod(dims);n=p+max(len(dims),2);b=np.zeros(p);b[0]=1
        for _ in range(20):
            z,S,scale=sufficient(rng,n,b,.1);data=Data(z,S,scale,n,.1);a=np.ones(p)
            out=energy_interval(data,a,dims,unknown=True)
            assert np.isfinite(out[:3]).all()
    print('PASS revised sample threshold and scalar edge case')
if __name__=='__main__':main()
