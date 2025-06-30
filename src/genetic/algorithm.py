from .selection import select_parents
from .crossover import crossover
from .mutation import mutate
from .elitism import apply_elitism
from .utils import should_stop

import random


def genetic_algorithm(fitness_func, data, *,
                      population_size=50, generations=200,
                      crossover_rate=0.8, mutation_rate=0.01,
                      elitism_rate=0.05,
                      selection_method="ranking",
                      max_no_improvement=30, verbose=False,
                      create_individual=None, crossover_operator="uniform",
                      mutation_operator="bit_flip", tournament_size=3):

    population = [create_individual(len(data["items"]), data) for _ in range(population_size)]
    best_solution = None
    best_fitness = float('-inf')
    best_avg_fitness = float('-inf')
    fitness_history = []
    no_improvement = 0

    for gen in range(generations):
        evaluated = [(chrom, fitness_func(chrom, data)) for chrom in population]
        evaluated.sort(key=lambda x: x[1], reverse=True)

        population = [chrom for chrom, _ in evaluated]
        fitness_scores = [fit for _, fit in evaluated]

        avg_fitness = sum(fitness_scores) / len(fitness_scores)

        if evaluated[0][1] > best_fitness:
            best_fitness = evaluated[0][1]
            best_solution = evaluated[0][0]
            best_avg_fitness = avg_fitness
            no_improvement = 0
        elif avg_fitness > best_avg_fitness + 1e-5:  # mejora general leve
            best_avg_fitness = avg_fitness
            no_improvement = 0
        else:
            no_improvement += 1

        if verbose:
            print(f"Gen {gen}: Best fitness = {best_fitness:.6f}, Avg fitness = {avg_fitness:.6f}")

        if no_improvement >= max_no_improvement:
            if verbose:
                print(f"Converged at generation {gen}")
            break

        # Aplicar elitismo y reproducción
        params = {
            "selection_method": selection_method,
            "tournament_size": tournament_size,
            "elitism_rate": elitism_rate
        }

        elites = apply_elitism(population, fitness_scores, params)
        elite_count = len(elites)

        children = []
        while len(children) < population_size - elite_count:
            parent1, parent2 = select_parents(population, fitness_scores, params)
            child = crossover(parent1, parent2, crossover_rate, crossover_operator)
            child = mutate(child, mutation_rate, mutation_operator)
            children.append(child)

        population = elites + children
        fitness_history.append(best_fitness)

    return best_solution, best_fitness, fitness_history
