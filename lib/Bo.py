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

from Computable import Computable
from Normalizer import Normalizer

# todo add dimension checks

class Bo:
    def __init__(self, x_dim: int, y_dim: int, x_norm: Normalizer,  y_norm: Normalizer) -> None:
        self._x_dim = x_dim
        self._y_dim = y_dim
        
        self._raw_x:  List[Computable] = []
        self._raw_y:  List[Computable] = []
        
        self._x_norm = x_norm
        self._y_norm = y_norm
    

    def add_floats(self, xs: List[List[float]] | None, ys: List[List[float]]| None):
        if xs == None: xs = []
        if ys == None: ys = []

        tmpx = []
        tmpy = []

        for x in xs:
            tmpx.append(Computable(x, self._x_norm))
        
        for y in ys:
            tmpy.append(Computable(y, self._y_norm))


        self._add_data(tmpx, tmpy)


    
    def _clear(self):
        self._raw_x = []
        self._raw_y = []

    def set_floats(self, xs: List[List[float]], ys: List[List[float]]):
        # TODO this can be more efficient using _set_data instead
        self._clear()
        self.add_floats(xs, ys)

    def _add_data(self, xs: List[Computable], ys: List[Computable]):
        self._raw_x += xs
        self._raw_y += ys

    def _set_data(self, x: List[Computable], y: List[Computable]):
        self._raw_x = x
        self._raw_y = y

    def _to_tensor(self, raw):
        return torch.tensor(list(map(lambda o: o.values, raw)))
    
    def get_x_tensors(self):
        return self._to_tensor(self._raw_x)        

    def get_y_tensors(self):
        return self._to_tensor(self._raw_y)        

    def inspect_data(self):
        xo = map(lambda o: o.original, self._raw_x)
        yo = map(lambda o: o.original, self._raw_y)

        xc = map(lambda o: o.values, self._raw_x)
        yc = map(lambda o: o.values, self._raw_y)

        po = zip(xo, yo)
        pc = zip(xc, yc)
        
        print("original: ")
        print(list(po))
        print("-------")
        print("computable: ")
        print(list(pc))

    def infer(self):
        xt = bo.get_x_tensors()
        yt = bo.get_y_tensors()
        
        Y =  F.normalize(yt, dim=None, p=2)
        train_Y = standardize(Y)

        gp = SingleTaskGP(xt, train_Y)
        mll = ExactMarginalLogLikelihood(gp.likelihood, gp)
        fit_gpytorch_mll(mll)
        bounds = torch.stack([torch.zeros(self._x_dim), torch.ones(self._x_dim)])
        
        # Define the Expected Improvement (EI) acquisition function
        ei = ExpectedImprovement(gp, best_f=torch.max(Y))

        # 'best_observed_value' is the best observed value from your optimization process so far
        bounds = torch.stack([torch.zeros(2), torch.ones(2)])

        # Optimize the EI acquisition function to find the next candidate point
        candidate, acq_value = optimize_acqf(
            ei, bounds=bounds, q=1, num_restarts=20, raw_samples=150,
        )
        c = candidate[0].detach().cpu().numpy().tolist()
        
        ret = self._x_norm.to_original_space(c)
        
        return c

if __name__ == "__main__":
    x_norm = Normalizer(0, 100)
    y_norm = Normalizer(0, 10)
    bo = Bo(x_dim=2, y_dim=1, x_norm=x_norm, y_norm=y_norm)

    bo.add_floats([[10, 1], [30, 2], [70, 1]], 
                  [[6],     [8],     [2]])
    
    bo.add_floats([[100, 0]], 
                  [[0]])
    
    # bo.inspect_data()

    xt = bo.get_x_tensors()
    yt = bo.get_y_tensors()
    
    print(bo.infer())