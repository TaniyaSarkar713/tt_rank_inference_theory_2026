"""General block-product confidence certificate; no contact order is selected.

All tensors use NumPy C order. The scalar interval and ball use the same data.
The exact scalar interval is a baseline, not the interval used in the proof's
intersection (which must use the common simultaneous ball event).
"""
from functools import lru_cache
from math import comb
import numpy as np
from scipy.stats import chi2, f, norm, t
from gaussian_base import outer, block_dimensions, rank_one_hosvd

@lru_cache(None)
def criticals(n,p,alpha):
    return (chi2.ppf(1-alpha,p),p*f.ppf(1-alpha,p,n-p),
            norm.ppf(1-alpha/2),t.ppf(1-alpha/2,n-p))


def sufficient(rng,n,beta,sigma,cov=None):
    p=len(beta)
    bart=np.tril(rng.normal(size=(p,p)),-1)
    np.fill_diagonal(bart,np.sqrt(rng.chisquare(n-np.arange(p))))
    L=bart if cov is None else np.linalg.cholesky(cov)@bart
    gram=L@L.T
    g=rng.normal(size=p)
    z=beta+sigma*np.linalg.solve(L.T,g)
    residual_scale=sigma*np.sqrt(rng.chisquare(n-p)/(n-p))
    return z,gram,residual_scale


def raw_observations(rng,n,beta,sigma,noise):
    p=len(beta); X=rng.normal(size=(n,p))
    if noise=='t5': eps=sigma*rng.standard_t(5,n)*np.sqrt(3/5)
    elif noise=='heteroskedastic': eps=sigma*rng.normal(size=n)*np.sqrt(.3+.7*X[:,0]**2)
    elif noise=='dependent':
        eps=np.empty(n); eps[0]=sigma*rng.normal()
        for i in range(1,n): eps[i]=.6*eps[i-1]+sigma*.8*rng.normal()
    elif noise.startswith('contamination'):
        rate=float(noise.split('_')[1]); eps=sigma*rng.normal(size=n)*np.where(rng.random(n)<rate,5.,1.)
    else: raise ValueError(noise)
    Y=X@beta+eps; gram=X.T@X; z=np.linalg.solve(gram,X.T@Y)
    scale=np.linalg.norm(Y-X@z)/np.sqrt(n-p)
    return z,gram,scale


def components(a,vectors):
    """Exact loading projections by tensor contractions (small J only)."""
    dims=tuple(map(len,vectors)); arr=a.reshape(dims)
    pieces=[np.zeros(dims) for _ in range(len(dims)+1)]
    for mask in range(1<<len(dims)):
        part=arr
        for j,v in enumerate(vectors):
            P=np.outer(v,v); op=np.eye(len(v))-P if mask&(1<<j) else P
            part=np.moveaxis(np.tensordot(op,part,axes=(1,j)),0,j)
        pieces[mask.bit_count()]+=part
    return [x.ravel() for x in pieces]


def loading_info(a, vectors, pure=None):
    if pure is None:
        parts=components(a,vectors)
        return np.array([np.linalg.norm(x) for x in parts]),parts[0]+parts[1]
    # Pure product: squared projection norms are coefficients of a polynomial.
    ps=[v*(v@w) for v,w in zip(vectors,pure)]
    qs=[w-p for w,p in zip(pure,ps)]
    coeff=np.array([1.])
    for p,q in zip(ps,qs): coeff=np.convolve(coeff,[p@p,q@q])
    tangent=outer(ps).ravel()
    for j in range(len(ps)):
        vv=list(ps); vv[j]=qs[j]; tangent=tangent+outer(vv).ravel()
    return np.sqrt(np.maximum(coeff,0)),tangent


class Data:
    def __init__(self,z,gram,scale,n,sigma,alpha=.05):
        self.z=z; self.gram=gram; self.scale=scale; self.n=n; self.sigma=sigma
        self.inv=np.linalg.inv(gram); self.mineig=np.linalg.eigvalsh(gram)[0]
        self.crit=criticals(n,len(z),alpha); self.fits={}; self.infos={}
    def fit(self,blocks):
        key=tuple(blocks)
        if key not in self.fits:
            pilot,v,coef=rank_one_hosvd(self.z,key)
            self.fits[key]=(pilot,v,float(np.linalg.norm(pilot)),float(np.linalg.norm(self.z-pilot)))
        return self.fits[key]
    def radius(self,unknown=False):
        return (self.scale if unknown else self.sigma)*np.sqrt(self.crit[1 if unknown else 0]/self.mineig)
    def info(self,a,blocks,pure=None):
        key=(tuple(blocks),a.tobytes())
        if key not in self.infos: self.infos[key]=loading_info(a,self.fit(blocks)[1],pure)
        return self.infos[key]


def graded(data,a,blocks,eta=0.,unknown=False,pure=None):
    pilot,v,shat,resid=data.fit(blocks); e=data.radius(unknown)
    rho=resid+e+eta; anorm=np.linalg.norm(a)
    H=anorm*rho; fallback=rho>=shat/2 or shat==0
    if not fallback:
        norms,_=data.info(a,blocks,pure)
        val=np.hypot(norms[0],norms[1])*rho
        for ell in range(2,len(blocks)+1):
            val+=np.sqrt(comb(len(blocks),ell))*norms[ell]*rho**ell/(shat-rho)**(ell-1)
        H=min(H,val)
    center=float(a@pilot); half=H+eta*anorm
    ambient=float(a@data.z); lo=max(center-half,ambient-anorm*e); hi=min(center+half,ambient+anorm*e)
    empty=lo>hi
    if empty: lo=hi=ambient
    return float(lo),float(hi),center,int(fallback),int(empty)


def ambient(data,a,unknown=False):
    center=float(a@data.z)
    se=(data.scale if unknown else data.sigma)*np.sqrt(max(0,a@data.inv@a))
    half=data.crit[3 if unknown else 2]*se
    return center-half,center+half,center,0,0


def wald(data,a,blocks,degree=1,pure=None):
    pilot,_,_,_=data.fit(blocks); _,pa=data.info(a,blocks,pure)
    se=data.sigma*np.sqrt(max(0,pa@data.inv@pa)); center=float(a@pilot)
    half=data.crit[2]*se/degree
    return center-half,center+half,center,0,0


def elementary_loading(blocks):
    factors=[]
    for d in blocks:
        v=np.zeros(d); v[-1]=1; factors.append(v)
    return factors
