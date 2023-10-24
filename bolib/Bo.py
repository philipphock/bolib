from typing import List
import torch
import random

import torch.nn.functional as F
from botorch.models import SingleTaskGP
from botorch.fit import fit_gpytorch_mll
from botorch.utils import standardize
from gpytorch.mlls import ExactMarginalLogLikelihood
from botorch.acquisition import UpperConfidenceBound
from botorch.optim import optimize_acqf
import torch.nn.functional as F
from botorch.acquisition import ExpectedImprovement

from bolib.Dimension import NumericDimension
from bolib.ComputeSpace import ComputeSpace
from botorch.sampling.normal import SobolQMCNormalSampler
from botorch.acquisition.monte_carlo import qExpectedImprovement
class Bo:
    def __init__(self, compSpace: ComputeSpace) -> None:
        self._cp = compSpace

    
    def probAQF(self, best_f, model):
        sampler = SobolQMCNormalSampler(1024)
        qEI = qExpectedImprovement(model, best_f, sampler)        
        #qei = qEI(x)
        #print("QEI", qei)
        return qEI
    
    def detAQF(self, best_f,  model):
        ei = ExpectedImprovement(model, best_f=best_f)        
        return ei
    

    def infer(self):
        xn, yn = self._cp.normalized
        
        xt = torch.tensor(xn, dtype=torch.double)
        yt = torch.tensor(yn, dtype=torch.double)

        Y =  F.normalize(yt, dim=None, p=2)
        train_Y = standardize(Y)

        gp = SingleTaskGP(xt, train_Y)
        mll = ExactMarginalLogLikelihood(gp.likelihood, gp)
        fit_gpytorch_mll(mll)
        bounds = torch.stack([torch.zeros(self._cp.xdim), torch.ones(self._cp.xdim)])
        
        
        #af = self.detAQF(train_Y, gp)
        #best_f = torch.max(yt)
        best_f = torch.max(train_Y)

        af = self.probAQF(best_f, gp)
        

        candidate, acq_value = optimize_acqf(
            af, bounds=bounds, q=1, num_restarts=20, raw_samples=30,
        )
        c = candidate[0].detach().cpu().numpy().tolist()
        return c
        
        

if __name__ == "__main__":

    x0 = NumericDimension(min=0, max=100, name="p0")
    x1 = NumericDimension(min=0, max=3, name="p1")
    ranking_y = NumericDimension(min=0, max=10, name="Ranking")

    compSpace = ComputeSpace([x0, x1], [ranking_y])


    # target is [34, 2]
    compSpace.add_floats(xs = [[35, 2], [10, 1]], ys=[[9],[0]])    
    bo = Bo(compSpace)
    inf = bo.infer()
    denorm = compSpace.denormalize(inf)

    print("inf: ", inf)
    print("")
    print("denorm:\n ", denorm)
    
    