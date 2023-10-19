import torch
from botorch.models import SingleTaskGP
from gpytorch.mlls import ExactMarginalLogLikelihood
from botorch.fit import fit_gpytorch_model
from botorch.acquisition import UpperConfidenceBound
from botorch.optim import optimize_acqf
import gpytorch

# Define your black-box function that you want to optimize.
def black_box_function(x):
    # Simulate the function (replace with your real function)
    true_value = 2 * x[0] + 3 * x[1]  # Example function, optimize these parameters
    rating = torch.exp(-0.1 * torch.norm(x - torch.tensor([3.0, 4.0])))
    return true_value, rating

# Define the search space for optimization.
search_space = torch.tensor([[0.0, 0.0], [5.0, 5.0]])

# Create an initial random dataset for optimization.
initial_points = torch.rand(5, 2) * (search_space[1] - search_space[0]) + search_space[0]
initial_observations = [black_box_function(x) for x in initial_points]
train_x = torch.tensor(initial_points)
train_y = torch.tensor([obs[0] for obs in initial_observations]).unsqueeze(1)

# Initialize the Gaussian Process model and likelihood.
gp = SingleTaskGP(train_x, train_y)
likelihood = ExactMarginalLogLikelihood(likelihood=gpytorch.likelihoods.GaussianLikelihood(), model=gp)

# Fit the GP model to the current dataset.
fit_gpytorch_model(likelihood)

# Define the acquisition function (Upper Confidence Bound).
ucb = UpperConfidenceBound(gp, beta=0.1)  # You can adjust the beta parameter.

# Optimization loop.
for _ in range(10):
    # Find the next point to evaluate using the acquisition function.
    candidate, _ = optimize_acqf(ucb, bounds=search_space, q=1, num_restarts=5, raw_samples=20)

    # Evaluate the black-box function at the candidate point.
    true_value, rating = black_box_function(candidate)

    # Add the new observation to the dataset.
    new_observation = torch.tensor([[true_value]])
    train_x = torch.cat([train_x, candidate.unsqueeze(0)])
    train_y = torch.cat([train_y, new_observation])

    # Update the GP model and likelihood with the new data.
    gp = SingleTaskGP(train_x, train_y)
    likelihood = ExactMarginalLogLikelihood(likelihood=gpytorch.likelihoods.GaussianLikelihood(), model=gp)
    fit_gpytorch_model(likelihood)

# Get the best parameters found and the corresponding rating.
best_params = train_x[train_y.argmax()]
best_rating = rating.item()

print("Best Parameters:", best_params)
print("Best Rating:", best_rating)
