from .selection import select_parents
from .crossover import crossover
from .mutation import mutate
from .utils import should_stop

import random


def genetic_algorithm(fitness_func, data, *,
                      population_size=50, generations=200,
                      crossover_rate=0.8, mutation_rate=0.01,
                      elitism_count=2, selection_method="ranking",
                      max_no_improvement=30, verbose=False,
                      create_individual=None):

    population = [create_individual(len(data["items"])) for _ in range(population_size)]
    best_solution = None
    best_fitness = float('-inf')
    fitness_history = []
    no_improvement = 0

    for gen in range(generations):
        evaluated = [(chrom, fitness_func(chrom, data)) for chrom in population]
        evaluated.sort(key=lambda x: x[1], reverse=True)

        if evaluated[0][1] > best_fitness:
            best_fitness = evaluated[0][1]
            best_solution = evaluated[0][0]
            no_improvement = 0
        else:
            no_improvement += 1

        if verbose:
            print(f"Gen {gen}: Best fitness = {best_fitness}")

        if no_improvement >= max_no_improvement:
            if verbose:
                print(f"Converged at generation {gen}")
            break

        elites = [chrom for chrom, _ in evaluated[:elitism_count]]
        population = [chrom for chrom, _ in evaluated]
        fitness_scores = [fit for _, fit in evaluated]

        params = {
            "selection_method": selection_method,
            "tournament_size": 3
        }

        children = []
        while len(children) < population_size - elitism_count:
            parent1, parent2 = select_parents(population, fitness_scores, params)
            child = crossover(parent1, parent2, crossover_rate)
            child = mutate(child, mutation_rate)
            children.append(child)

        population = elites + children
        fitness_history.append(best_fitness)

    return best_solution, best_fitness, fitness_history