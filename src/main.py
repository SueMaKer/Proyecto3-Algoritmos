from genetic.algorithm import genetic_algorithm
from genetic.MKS import fitness_knapsack, recursive_knapsack, dp_topdown_knapsack, binary_individual as knapsack_individual
from genetic.bin_packing import fitness_bin_packing, bin_packing_individual
from genetic.subset_sum import fitness_subset_sum, binary_individual

import time

# --- Problema Knapsack ---

data_knapsack = {
    "weights": [
        [2, 2],
        [4, 2],
        [3, 4],
        [6, 1],
        [1, 3],
        [2, 5],
        [5, 3],
        [4, 4],
        [3, 2],
        [2, 1]
    ],
    "values": [40, 50, 60, 30, 20, 70, 80, 55, 25, 15],
    "capacities": [15, 15],
    "num_dimensions": 2,
    "items": list(range(10))
}

start = time.perf_counter()
solution, fitness, history = genetic_algorithm(
    fitness_func=fitness_knapsack,
    data=data_knapsack,
    create_individual=knapsack_individual,
    generations=100,
    population_size=200,
    crossover_rate=0.8,
    mutation_rate=0.2,
    elitism_count=3,
    selection_method="roulette",
    verbose=True
)
end = time.perf_counter()

print("\nMejor solución knapsack:", solution)
print("Fitness knapsack:", fitness)
print(f"Tiempo solución genética knapsack: {end - start:.6f} segundos")

start = time.perf_counter()
resultado_recursivo = recursive_knapsack(data_knapsack)
end = time.perf_counter()
print(f"Solución recursiva knapsack: {resultado_recursivo}, tiempo: {end - start:.6f} segundos")

start = time.perf_counter()
resultado_dp = dp_topdown_knapsack(data_knapsack)
end = time.perf_counter()
print(f"Solución DP top-down knapsack: {resultado_dp}, tiempo: {end - start:.6f} segundos")


# --- Problema Subset Sum ---

data_subset = {
    "items": [3, 34, 4, 12, 5, 2],
    "target": 9
}

start = time.perf_counter()
solution, fitness, history = genetic_algorithm(
    fitness_func=fitness_subset_sum,
    data=data_subset,
    create_individual=binary_individual,
    generations=100,
    population_size=200,
    crossover_rate=0.8,
    mutation_rate=0.1,
    elitism_count=3,
    selection_method="tournament",
    verbose=True
)
end = time.perf_counter()
print(f"Tiempo solución genética subset_sum: {end - start:.6f} segundos")

print("\nMejor solución subset sum:", solution)
print("Suma alcanzada subset sum:", fitness)
items_elegidos = [item for gene, item in zip(solution, data_subset["items"]) if gene]
print("Ítems seleccionados subset sum:", items_elegidos)


# --- Problema Bin Packing ---

data_binpacking = {
    "items": [4, 8, 1, 4, 2, 1, 7, 3],
    "bin_capacity": 10
}

start = time.perf_counter()
solution, fitness, history = genetic_algorithm(
    fitness_func=fitness_bin_packing,
    data=data_binpacking,
    create_individual=bin_packing_individual,
    population_size=100,
    generations=200,
    crossover_rate=0.8,
    mutation_rate=0.02,
    elitism_count=2,
    selection_method="ranking",
    verbose=True
)
end = time.perf_counter()
print(f"Tiempo solución genética bin_packing: {end - start:.6f} segundos")

print("\nMejor solución bin packing:", solution)
print("Fitness bin packing:", fitness)

# Mostrar bins con sus items
bins = {}
for item, bin_idx in zip(data_binpacking["items"], solution):
    bins.setdefault(bin_idx, []).append(item)

print("Items agrupados en bins:")
for b, items_in_bin in bins.items():
    print(f"Bin {b}: {items_in_bin}")