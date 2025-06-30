# Import necessary functions from other modules
from .selection import select_parents
from .crossover import crossover
from .mutation import mutate
from .elitism import apply_elitism
from .utils import should_stop

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

    # Initialize population with random individuals
    population = [create_individual(len(data["items"]), data) for _ in range(population_size)]
    best_solution = None
    best_fitness = float('-inf')
    best_avg_fitness = float('-inf')
    fitness_history = []
    no_improvement = 0

    # Start the evolutionary loop
    for gen in range(generations):
        # Evaluate the fitness of each individual
        evaluated = [(chrom, fitness_func(chrom, data)) for chrom in population]
        evaluated.sort(key=lambda x: x[1], reverse=True)  # Sort by fitness (descending)

        # Extract sorted population and fitness scores
        population = [chrom for chrom, _ in evaluated]
        fitness_scores = [fit for _, fit in evaluated]

        # Calculate average fitness of the current generation
        avg_fitness = sum(fitness_scores) / len(fitness_scores)

        # Check if the best individual improves
        if evaluated[0][1] > best_fitness:
            best_fitness = evaluated[0][1]
            best_solution = evaluated[0][0]
            best_avg_fitness = avg_fitness
            no_improvement = 0  # Reset stagnation counter
        # Check if the average fitness improves slightly
        elif avg_fitness > best_avg_fitness + 1e-5:
            best_avg_fitness = avg_fitness
            no_improvement = 0
        else:
            no_improvement += 1  # Increase stagnation counter

        # Print progress if verbose mode is enabled
        if verbose:
            print(f"Gen {gen}: Best fitness = {best_fitness:.6f}, Avg fitness = {avg_fitness:.6f}")

        # Check if the algorithm should stop due to stagnation
        if no_improvement >= max_no_improvement:
            if verbose:
                print(f"Converged at generation {gen}")
            break

        # Apply elitism and reproduction to create the next generation
        params = {
            "selection_method": selection_method,
            "tournament_size": tournament_size,
            "elitism_rate": elitism_rate
        }

        # Select elite individuals
        elites = apply_elitism(population, fitness_scores, params)
        elite_count = len(elites)

        # Generate children until the population is full
        children = []
        while len(children) < population_size - elite_count:
            parent1, parent2 = select_parents(population, fitness_scores, params)
            child = crossover(parent1, parent2, crossover_rate, crossover_operator)
            child = mutate(child, mutation_rate, mutation_operator)
            children.append(child)

        # Form the new population with elites and children
        population = elites + children
        fitness_history.append(best_fitness)

    # Return the best solution found, its fitness, and the fitness history
    return best_solution, best_fitness, fitness_history