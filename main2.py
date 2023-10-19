import torch
from botorch.models import SingleTaskGP
from botorch.fit import fit_gpytorch_mll
from botorch.utils import standardize
from botorch.models.transforms.outcome import Standardize

from gpytorch.mlls import ExactMarginalLogLikelihood
from botorch.acquisition import UpperConfidenceBound
from botorch.optim import optimize_acqf

train_X = torch.rand(1,1, dtype=torch.double)
print(train_X)
mnum = float(input("type a number: "))
Y = torch.tensor([[mnum]], dtype=torch.double)
#train_Y = standardize(Y)
train_Y = Y
print(train_Y)

#gp = SingleTaskGP(train_X, train_Y, outcome_transform=Standardize(m=train_Y.shape[-1]))
gp = SingleTaskGP(train_X, train_Y)
mll = ExactMarginalLogLikelihood(gp.likelihood, gp)
fit_gpytorch_mll(mll)
UCB = UpperConfidenceBound(gp, beta=0.1)

bounds = torch.stack([torch.zeros(1), torch.ones(1)])
print(f"bounds = ${bounds}")
candidate, acq_value = optimize_acqf(
    UCB, bounds=bounds, q=1, num_restarts=5, raw_samples=20,
)
candidate  # tensor([0.4887, 0.5063])
print(candidate)
