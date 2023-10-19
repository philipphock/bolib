import torch
from botorch.models import SingleTaskGP
from botorch.fit import fit_gpytorch_mll
from botorch.utils import standardize
from gpytorch.mlls import ExactMarginalLogLikelihood
from botorch.acquisition import UpperConfidenceBound
from botorch.optim import optimize_acqf


# we seek 0.34 and 0.2 
train_X = torch.tensor([[0.7, 0.2],[0.4, 0.1],[0.8, 0.1],[0.3, 0.2],[0.5, 0.2], [0.33, 0.21]], dtype=torch.double)


print(f"trainX: {train_X}")

# thus, we rate the variables accordingly: A value closer to 0.34, 0.2 is rated with a lower number
Y = torch.tensor([[0.7],[0.3],[0.8],[0.1],[0.3],[0.01]], dtype=torch.double)

train_Y = standardize(Y)
print(f"trainY: {train_Y}")

gp = SingleTaskGP(train_X, train_Y)
mll = ExactMarginalLogLikelihood(gp.likelihood, gp)
fit_gpytorch_mll(mll)


UCB = UpperConfidenceBound(gp, beta=0.1)


bounds = torch.stack([torch.zeros(2), torch.ones(2)])
candidate, acq_value = optimize_acqf(
    UCB, bounds=bounds, q=1, num_restarts=5, raw_samples=20,
)

print(candidate)
