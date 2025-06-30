# Import necessary functions from other modules
from .selection import select_parents   # Function to select parents from the population
from .crossover import crossover         # Function to perform crossover between parents
from .mutation import mutate             # Function to mutate an individual
from .elitism import apply_elitism       # Function to preserve the best individuals (elitism)
from .utils import should_stop           # Utility function to check stopping criteria

import random


# Genetic Algorithm main function
def genetic_algorithm(fitness_func, data, *,
                      population_size=50, generations=200,
                      crossover_rate=0.8, mutation_rate=0.01,
                      elitism_rate=0.05,
                      selection_method="ranking",
                      max_no_improvement=30, verbose=False,
                      create_individual=None, crossover_operator="uniform",
                      mutation_operator="bit_flip", tournament_size=3):

    # Initialize the population with random individuals
    population = [create_individual(len(data["items"]), data) for _ in range(population_size)]
    best_solution = None                          # Store the best solution found
    best_fitness = float('-inf')                  # Store the best fitness value found
    best_avg_fitness = float('-inf')              # Store the best average fitness observed
    fitness_history = []                          # Store the fitness history over generations
    no_improvement = 0                            # Counter for generations without improvement

    # Start the main loop for evolution over generations
    for gen in range(generations):
        # Evaluate the fitness of each individual in the population
        evaluated = [(chrom, fitness_func(chrom, data)) for chrom in population]
        evaluated.sort(key=lambda x: x[1], reverse=True)  # Sort individuals by fitness (best first)

        # Extract the sorted chromosomes and their fitness scores
        population = [chrom for chrom, _ in evaluated]
        fitness_scores = [fit for _, fit in evaluated]

        # Calculate the average fitness of the current generation
        avg_fitness = sum(fitness_scores) / len(fitness_scores)

        # Check if the best fitness in this generation is better than the global best
        if evaluated[0][1] > best_fitness:
            best_fitness = evaluated[0][1]             # Update best fitness
            best_solution = evaluated[0][0]            # Update best solution
            best_avg_fitness = avg_fitness             # Update best average fitness
            no_improvement = 0                         # Reset stagnation counter
        # Check if the average fitness has improved slightly
        elif avg_fitness > best_avg_fitness + 1e-5:
            best_avg_fitness = avg_fitness             # Update best average fitness
            no_improvement = 0                         # Reset stagnation counter
        else:
            no_improvement += 1                        # Increase stagnation counter

        # Print progress if verbose mode is enabled
        if verbose:
            print(f"Gen {gen}: Best fitness = {best_fitness:.6f}, Avg fitness = {avg_fitness:.6f}")

        # Check if the algorithm should stop due to lack of improvement
        if no_improvement >= max_no_improvement:
            if verbose:
                print(f"Converged at generation {gen}")
            break  # Stop the algorithm early due to convergence

        # Prepare parameters for selection and elitism
        params = {
            "selection_method": selection_method,
            "tournament_size": tournament_size,
            "elitism_rate": elitism_rate
        }

        # Apply elitism to preserve the top-performing individuals
        elites = apply_elitism(population, fitness_scores, params)
        elite_count = len(elites)

        # Initialize the children population
        children = []
        # Generate new individuals until the population is replenished (excluding elites)
        while len(children) < population_size - elite_count:
            # Select two parents based on the selection method
            parent1, parent2 = select_parents(population, fitness_scores, params)
            # Apply crossover to generate a child
            child = crossover(parent1, parent2, crossover_rate, crossover_operator)
            # Apply mutation to the child
            child = mutate(child, mutation_rate, mutation_operator)
            # Add the child to the children population
            children.append(child)

        # Form the new population by combining elites and children
        population = elites + children
        # Record the best fitness of this generation for analysis
        fitness_history.append(best_fitness)

    # Return the best solution found, its fitness, and the fitness history across generations
    return best_solution, best_fitness, fitness_history