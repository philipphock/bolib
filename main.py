import torch
from botorch.models import SingleTaskGP
from botorch.fit import fit_gpytorch_mll
from botorch.utils import standardize
from gpytorch.mlls import ExactMarginalLogLikelihood
from botorch.acquisition import UpperConfidenceBound
from botorch.optim import optimize_acqf

train_X = torch.tensor([[0.8], [0.2]], dtype=torch.double)
Y = torch.tensor([[0.2], [0.8]], dtype=torch.double)
train_Y = standardize(Y)

gp = SingleTaskGP(train_X, train_Y)
mll = ExactMarginalLogLikelihood(gp.likelihood, gp)
fit_gpytorch_mll(mll)

UCB = UpperConfidenceBound(gp, beta=0.1)

bounds = torch.stack([torch.zeros(2), torch.ones(2)])

#parameter_bounds = [(0, 1)]
#bounds = torch.tensor(parameter_bounds, dtype=torch.double)

candidate, acq_value = optimize_acqf(
    UCB, bounds=bounds, q=1, num_restarts=5, raw_samples=20
)
print(f"candidate: {candidate}")
