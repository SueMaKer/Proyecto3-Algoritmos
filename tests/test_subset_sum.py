import random
import sys
import os

# Paso 1: Añadir ruta al módulo ga_engine
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'genetic')))

# Paso 2: Importar desde ga_engine.py
from genetic.ga_engine import genetic_algorithm


items = [3, 34, 4, 12, 5, 2]
target = 9
chromosome_length = len(items)

#Genera de cromosomas binarios 
def chromosome_generator():
    return [random.randint(0, 1) for _ in range(chromosome_length)]

#Función de fitness para Subset Sum 
def fitness_subset_sum(chromosome):
    total = sum(gene * item for gene, item in zip(chromosome, items))
    return total if total <= target else 0  # penaliza si se pasa del target


params = {
    'population_size': 30,
    'max_generations': 100,
    'patience': 15,
    'elitism_rate': 0.2,
    'selection_method': 'tournament',
    'tournament_size': 3,
    'crossover_type': '1point',
    'crossover_rate': 0.9,
    'mutation_type': 'bitflip',
    'mutation_rate': 0.1
}

if __name__ == "__main__":
    best_solution, best_fitness = genetic_algorithm(
        fitness_subset_sum,
        chromosome_generator,
        params
    )

    
    subset = [item for gene, item in zip(best_solution, items) if gene == 1]

    print(" Mejor cromosoma:", best_solution)
    print(" Subconjunto elegido:", subset)
    print(" Suma alcanzada:", sum(subset))
    print(" Fitness (cercanía al target):", best_fitness)
    print(" Objetivo:", target)
