import torch
from botorch import fit_gpytorch_model
from botorch.models import SingleTaskGP
from botorch.acquisition import UpperConfidenceBound
from botorch.optim import optimize_acqf
from gpytorch.mlls import ExactMarginalLogLikelihood

# Define the objective function that returns the negative feedback value
def objective(feedback):
    # You want to maximize this function, so return the negative feedback
    return -feedback

def optimize(train_X, train_Y):
    # Define the parameter bounds for est_age and est_gender
    parameter_bounds = [(1, 100), (1, 3)]

    # Convert the problem into a Botorch-compatible format
    bounds = torch.tensor(parameter_bounds, dtype=torch.double)
    
  
    # Initialize a model
    model = SingleTaskGP(train_X, train_Y)

    # The objective function we want to maximize
    #f = objective

    # Initialize a model
    #feedback = f(est_age, est_gender, feedback)
    
    # Define the acquisition function (Upper Confidence Bound)
    mll = ExactMarginalLogLikelihood(model.likelihood, model)
    fit_gpytorch_model(mll)
    UCB = UpperConfidenceBound(model, beta=0.1)

    # Optimize the acquisition function to get the next point to evaluate
    candidate, _ = optimize_acqf(
        UCB, bounds=bounds, q=1, num_restarts=5, raw_samples=20
    )

    # Update the estimated values
    est_age, est_gender = candidate.tolist()[0]

    return est_age, est_gender