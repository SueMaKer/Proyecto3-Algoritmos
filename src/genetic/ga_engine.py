import random
#from genetic.selection import select_parents
#from genetic.crossover import crossover
#from genetic.mutation import mutate
#from genetic.elitism import apply_elitism

from .selection import select_parents
from .crossover import crossover
from .mutation import mutate
from .elitism import apply_elitism

def genetic_algorithm(fitness_fn, chromosome_generator, params):
  
    population = [chromosome_generator() for _ in range(params['population_size'])]
    fitness_scores = [fitness_fn(ind) for ind in population]

    best_solution = max(zip(population, fitness_scores), key=lambda x: x[1])
    generations_without_improvement = 0

    for generation in range(params['max_generations']):
        new_population = apply_elitism(population, fitness_scores, params)

        while len(new_population) < params['population_size']:
            parent1, parent2 = select_parents(population, fitness_scores, params)
            child1, child2 = crossover(parent1, parent2, params)
            child1 = mutate(child1, params)
            child2 = mutate(child2, params)
            new_population.extend([child1, child2])

        
        population = new_population[:params['population_size']]
        fitness_scores = [fitness_fn(ind) for ind in population]

        current_best = max(zip(population, fitness_scores), key=lambda x: x[1])
        if current_best[1] > best_solution[1]:
            best_solution = current_best
            generations_without_improvement = 0
        else:
            generations_without_improvement += 1

        if generations_without_improvement >= params['patience']:
            print(f" Sin mejora en {params['patience']} generaciones. Parando en la gen {generation}")
            break

    return best_solution
