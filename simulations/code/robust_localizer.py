"""Independent-group coordinate-median OLS confidence ball, known variance bound."""
from math import comb
import numpy as np
from methods import Data


def median_ols_ball(X,Y,sigma_bound,J,alpha=.05):
    n,p=X.shape;h=J//2+1;g=2*h-1;k=n//g
    if k<2*p+2:raise ValueError('Need floor(n/g) >= 2*p+2')
    fits=[]
    for s in range(g):
        xx=X[s*k:(s+1)*k];yy=Y[s*k:(s+1)*k]
        fits.append(np.linalg.solve(xx.T@xx,xx.T@yy))
    center=np.median(np.asarray(fits),axis=0)
    D=(p*comb(g,h))**(1/(2*h))*sigma_bound*np.sqrt(2*p/k)
    return center,D*alpha**(-1/(2*h))


class BallData(Data):
    """Reuse tensor contractions with an externally proved confidence ball.

    The identity Gram is a storage placeholder and must not be used for a Wald
    or scalar OLS interval. Only fit(), info(), and radius() are used here.
    """
    def __init__(self,z,radius,n):
        super().__init__(z,np.eye(len(z)),0.,n,1.)
        self.proved_radius=radius
    def radius(self,unknown=False):
        if unknown:raise ValueError('This localizer needs a known variance bound')
        return self.proved_radius
