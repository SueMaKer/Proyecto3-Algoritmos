# Function to check if the genetic algorithm should stop due to lack of improvement
def should_stop(no_improvement, max_no_improvement):
    """
    Checks whether the genetic algorithm should stop because of no improvement.

    Args:
        no_improvement (int): Number of generations without improvement.
        max_no_improvement (int): Maximum allowed generations without improvement.

    Returns:
        bool: True if the algorithm should stop, False otherwise.
    """
    return no_improvement >= max_no_improvement


# Function to update the best fitness and solution if improvement occurs
def track_best(evaluated, best_fitness, best_solution):
    """
    Updates the best fitness and solution if there is an improvement.

    Args:
        evaluated (list): List of tuples (chromosome, fitness).
        best_fitness (float): Current best fitness value.
        best_solution (list): Current best solution.

    Returns:
        tuple: (new_best_solution, new_best_fitness, improved_flag)
    """
    current_best = evaluated[0]
    if current_best[1] > best_fitness:
        # Return new best solution and fitness, and a flag indicating improvement
        return current_best[0], current_best[1], True
    # Otherwise return the old best and indicate no improvement
    return best_solution, best_fitness, False


# Function to set the random seed for reproducibility
def seed_everything(seed_value):
    """
    Sets the random seed for reproducibility.

    Args:
        seed_value (int): Desired seed value.
    """
    import random
    import numpy as np

    random.seed(seed_value)
    np.random.seed(seed_value)