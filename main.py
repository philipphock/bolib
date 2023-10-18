import random
import matplotlib.pyplot as plt
import numpy as np
from botorch.models import SingleTaskGP
from botorch.acquisition import ExpectedImprovement
from botorch.optim import optimize_acqf
import torch

def visualize_colors(foreground_color, background_color):
    fig, ax = plt.subplots()
    ax.add_patch(plt.Circle((0.5, 0.5), 0.4, color=background_color))
    ax.add_patch(plt.Circle((0.5, 0.5), 0.2, color=foreground_color))
    ax.set_aspect('equal')
    ax.set_axis_off()
    plt.show()


def rate_contrast(foreground_color, background_color):
    visualize_colors(foreground_color, background_color)
    inp = input("Rate the likeness of the contrast (1-10): ")

    rating = float(inp)
    return rating

rcolor = lambda : (random.random(), random.random(), random.random())


# Define the optimization function
def optimize_color_contrast(iterations=10):
    best_foreground_color = rcolor()  # Initialize with default values (e.g., black)
    best_background_color = rcolor()  # Initialize with default values (e.g., white)

    for _ in range(iterations):
        # Display current best color contrast
        print(f"Best Color Contrast: Foreground: {best_foreground_color}, Background: {best_background_color}")

        # Get user rating for the current contrast
        current_rating = rate_contrast(best_foreground_color, best_background_color)

        # Create the acquisition function
        model = SingleTaskGP(torch.tensor([best_foreground_color]), torch.tensor([current_rating]))
        mll = ExactMarginalLogLikelihood(model.likelihood, model)
        fit_gpytorch_model(mll)
        EI = ExpectedImprovement(model, current_rating)

        # Optimize the acquisition function to get the next color contrast to be rated
        bounds = [(0, 1), (0, 1), (0, 1)]  # RGB values are between 0 and 1
        candidate, acq_value = optimize_acqf(EI, bounds=bounds, q=1, num_restarts=10, raw_samples=10)

        # Convert the candidate to RGB values
        new_foreground_color = tuple(candidate.squeeze().tolist())

        # Get user rating for the new contrast
        new_rating = rate_contrast(new_foreground_color, best_background_color)

        if new_rating > current_rating:
            best_foreground_color = new_foreground_color

    print("Optimization completed. Best color contrast:")
    print(f"Foreground: {best_foreground_color}, Background: {best_background_color}")

optimize_color_contrast()
