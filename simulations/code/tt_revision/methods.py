"""Selected-coordinate TT intervals and the joint numerator bound."""
from itertools import product
import numpy as np


def coordinate_maps(K=4):
    pivots = [[(u,)*k+(v,)*(K-k) for u,v in product(range(2), repeat=2)]
              for k in range(1,K)]
    slices = [[(2,)+(v,)*(K-1) for v in range(2)]]
    slices += [[(u,)*k+(2,)+(v,)*(K-k-1) for u,v in product(range(2),repeat=2)]
               for k in range(1,K-1)]
    slices += [[(u,)*(K-1)+(2,) for u in range(2)]]
    target = (2,)*K
    coords = sorted(set([target]+[x for group in pivots+slices for x in group]))
    lookup = {x:i for i,x in enumerate(coords)}
    return coords, [np.array([lookup[x] for x in g]) for g in pivots], [
        np.array([lookup[x] for x in g]) for g in slices], lookup[target]


def numerator_bracket(c,e,iterations=60):
    """Exact-arithmetic brackets; returned floats have numerical tolerance."""
    c=np.asarray(c,float); e=np.asarray(e,float)
    low=np.zeros_like(e); high=e*e+e*np.max(c,axis=1)
    def delta(mu):
        den=np.sqrt(c*c+4*mu[:,None])+c
        return np.divide(2*mu[:,None],den,out=np.zeros_like(c),where=den>0)
    for _ in range(iterations):
        mid=(low+high)/2
        feasible=np.sum(delta(mid)**2,axis=1)<=e*e
        low=np.where(feasible,mid,low); high=np.where(feasible,high,mid)
    p_low=np.prod(c+delta(low),axis=1)
    p_high=np.prod(c+delta(high),axis=1)
    return p_low,p_high


def intervals(z,e,K=4):
    _,piv,slices,target=coordinate_maps(K)
    small=np.stack([np.linalg.svd(z[:,idx].reshape(-1,2,2),compute_uv=False)[:,-1]
                    for idx in piv],axis=1)-e[:,None]
    certified=np.all(small>0,axis=1)
    c=np.stack([np.linalg.norm(z[:,idx],axis=1) for idx in slices],axis=1)
    old_num=np.prod(c+e[:,None],axis=1)
    lower,upper=numerator_bracket(c,e)
    # This padding is a floating-point guard, not a formal interval-arithmetic proof.
    new_num=np.minimum(old_num,upper*(1+1e-12))
    left0=z[:,target]-e; right0=z[:,target]+e
    answers={}
    for name,num in [('cross_separate',old_num),('cross_joint',new_num)]:
        H=np.full(len(e),np.inf)
        H[certified]=num[certified]/np.prod(small[certified],axis=1)
        left=np.maximum(left0,-H); right=np.minimum(right0,H)
        empty=left>right
        left=np.where(empty,z[:,target],left); right=np.where(empty,z[:,target],right)
        answers[name]=(left,right)
    answers['ball_projection']=(left0,right0)
    gap=np.divide(upper,lower,out=np.ones_like(upper),where=lower>0)-1
    return answers,certified,gap
