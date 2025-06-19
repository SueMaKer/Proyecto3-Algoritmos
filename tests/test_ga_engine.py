import random
from genetic.ga_engine import genetic_algorithm

# Longitud del cromosoma (binario)
chromosome_length = 10

# Función de aptitud: suma de unos (máximo: 10)
def fitness_max_ones(chromosome):
    return sum(chromosome)

# Generador de cromosomas aleatorios binarios
def chromosome_generator():
    return [random.randint(0, 1) for _ in range(chromosome_length)]

# Parámetros del algoritmo genético
params = {
    'population_size': 20,
    'max_generations': 50,
    'patience': 10,
    'elitism_rate': 0.2,
    'selection_method': 'tournament',
    'tournament_size': 3,
    'crossover_type': '1point',
    'crossover_rate': 0.8,
    'mutation_type': 'bitflip',
    'mutation_rate': 0.05
}

# Ejecución del test
if __name__ == "__main__":
    best_solution, best_fitness = genetic_algorithm(
        fitness_max_ones,
        chromosome_generator,
        params
    )

    print(" Mejor solución encontrada:", best_solution)
    print(" Fitness de la mejor solución:", best_fitness)
