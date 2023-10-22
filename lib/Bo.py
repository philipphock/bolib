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
from lib.Normalizer import Normalizer, OptimizeFor


class Bo:
    def __init__(self, x_dim: int, y_dim: int, x_norm: Normalizer,  y_norm: Normalizer) -> None:
        self._x_dim = x_dim
        self._y_dim = y_dim
        
        self._raw_x:  List[Computable]
        self._raw_y:  List[Computable]
    

    def add_data(self, x: Computable):
        pass

    def set_data(self, x: Computable):
        self._raw = x

    def inspect_data(self):
        print(self._raw)

    def infer(self):
        train_Y = standardize(Y)
        #train_Y = Y
        gp = SingleTaskGP(X, train_Y)
        mll = ExactMarginalLogLikelihood(gp.likelihood, gp)
        fit_gpytorch_mll(mll)

        bounds = torch.stack([torch.zeros(2), torch.ones(2)])
        # Define the Expected Improvement (EI) acquisition function
        ei = ExpectedImprovement(gp, best_f=torch.max(Y))

        # 'best_observed_value' is the best observed value from your optimization process so far
        bounds = torch.stack([torch.zeros(2), torch.ones(2)])

        # Optimize the EI acquisition function to find the next candidate point
        candidate, acq_value = optimize_acqf(
            ei, bounds=bounds, q=1, num_restarts=20, raw_samples=150,
        )

        print(candidate)

if __name__ == "__main__":
    x_norm = Normalizer(0, 100)
    y_norm = Normalizer(0, 10)
    bo = Bo(2, 1, )