"""Audit revision: energy certificate; original methods.py stays immutable."""
import numpy as np
from math import comb


def energy_interval(data,a,blocks,eta=0.,unknown=False,pure=None,variance_bound=False):
    pilot,v,shat,resid=data.fit(blocks)
    if variance_bound:
        # data.sigma is the KNOWN conditional covariance upper-bound scale.
        e=data.sigma*np.sqrt(np.trace(data.inv)/.05)
    else:
        e=data.radius(unknown)
    rho=resid+e+eta; anorm=np.linalg.norm(a); J=len(blocks)
    H=anorm*rho; fallback=rho>=shat/2 or shat==0
    if not fallback:
        norms,_=data.info(a,blocks,pure)
        val=np.hypot(norms[0],norms[1])*rho
        for ell in range(2,J+1):
            kappa=np.sqrt(comb(J,ell))/J**(ell/2)
            val+=kappa*norms[ell]*rho**ell/(shat-rho)**(ell-1)
        H=min(H,val)
    center=float(a@pilot); half=H+eta*anorm; ambient=float(a@data.z)
    lo=max(center-half,ambient-anorm*e);hi=min(center+half,ambient+anorm*e)
    empty=lo>hi
    if empty:lo=hi=ambient
    return float(lo),float(hi),center,int(fallback),int(empty)
