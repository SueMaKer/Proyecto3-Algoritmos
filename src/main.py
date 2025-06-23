from genetic.algorithm import genetic_algorithm
from genetic.knapsack import fitness_knapsack
from genetic.knapsack import recursive_knapsack
from genetic.knapsack import dp_topdown_knapsack

import time
# Datos de ejemplo (mochila multidimensional)
data = {
    "weights": [
        [2, 2],  # Item 0
        [4, 2],  # Item 1
        [3, 4],  # Item 2
        [6, 1],  # Item 3
        [1, 3],  # Item 4
        [2, 5],  # Item 5
        [5, 3],  # Item 6
        [4, 4],  # Item 7
        [3, 2],  # Item 8
        [2, 1]   # Item 9
    ],
    "values": [40, 50, 60, 30, 20, 70, 80, 55, 25, 15],
    "capacities": [15, 15],
    "num_dimensions": 2,
    "items": list(range(10))
}

start = time.perf_counter()
solution, fitness, history = genetic_algorithm(
    fitness_func=fitness_knapsack,
    data=data,
    generations=100,
    population_size=200,
    crossover_rate=0.8,
    mutation_rate=0.2,
    elitism_count=3,
    selection_method="roulette",
    verbose=True
)
end = time.perf_counter()

print("\nMejor solución:", solution)
print("Fitness:", fitness)
print(f"Genetic solution: time: {end - start:.6f} seconds")

start = time.perf_counter()
resultado_recursivo = recursive_knapsack(data)
end = time.perf_counter()
print(f"Recursive solution: {resultado_recursivo}, time: {end - start:.6f} seconds")

start = time.perf_counter()
resultado_dp = dp_topdown_knapsack(data)
end = time.perf_counter()
print(f"DP top-down solution: {resultado_dp}, time: {end - start:.6f} seconds")