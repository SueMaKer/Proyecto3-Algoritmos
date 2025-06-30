from genetic.algorithm import genetic_algorithm
from problems.MKS import fitness_knapsack, recursive_knapsack, dp_topdown_knapsack, knapsack_individual, heuristic_individual_knapsack
from problems.bin_packing import fitness_bin_packing, bin_packing_individual, recursive_bin_packing, dp_bin_packing, heuristic_individual_binpacking
from problems.subset_sum import fitness_subset_sum, subset_individual, recursive_subset_sum, subset_sum_top_down, heuristic_individual_subset
from problems.partition import fitness_partition, partition_individual, recursive_partition, dp_topdown_partition, heuristic_individual_partition

import time
import random


# Measures the average execution time of a function over multiple repetitions
def measure_average_time(func, data, repetitions=30):
    times = []
    for _ in range(repetitions):
        start = time.perf_counter()
        func(data)
        end = time.perf_counter()
        times.append(end - start)
    return sum(times) / len(times)


# Runs experiments for different problems using genetic algorithm and exact methods
def run_all_experiments(
    population_size=200,
    generations=100,
    repetitions=30,
    num_items=10,
    init_method="random",
    selection_method="tournament",
    tournament_size=3,
    crossover_rate=0.8,
    mutation_rate=0.1,
    crossover_operator="uniform",
    mutation_operator="bit_flip",
    elitism_proportion=0.05
):
    random.seed(42)  # Set seed for reproducibility

    # Generate random problem data for experiments
    items_generated = [random.randint(1, 10) for _ in range(num_items)]
    weights_generated = [[random.randint(1, 6), random.randint(1, 6)] for _ in range(num_items)]
    values_generated = [random.randint(10, 100) for _ in range(num_items)]

    # Define a list of problem configurations, including their data and associated functions
    problems = [
        {
            "name": "Knapsack",
            "data": {
                "weights": weights_generated,
                "values": values_generated,
                "capacities": [15, 15],
                "num_dimensions": 2,
                "items": list(range(num_items))
            },
            "fitness": fitness_knapsack,
            "exact_recursive": recursive_knapsack,
            "exact_dp": dp_topdown_knapsack,
            "individual": knapsack_individual,
            "heuristic_individual": heuristic_individual_knapsack
        },
        {
            "name": "Subset Sum",
            "data": {
                "items": items_generated,
                "target": sum(items_generated) // 2
            },
            "fitness": fitness_subset_sum,
            "exact_recursive": recursive_subset_sum,
            "exact_dp": subset_sum_top_down,
            "individual": subset_individual,
            "heuristic_individual": heuristic_individual_subset
        },
        {
            "name": "Bin Packing",
            "data": {
                "items": items_generated,
                "bin_capacity": 10
            },
            "fitness": fitness_bin_packing,
            "exact_recursive": recursive_bin_packing,
            "exact_dp": dp_bin_packing,
            "individual": bin_packing_individual,
            "heuristic_individual": heuristic_individual_binpacking
        },
        {
            "name": "Partition",
            "data": {
                "items": items_generated
            },
            "fitness": fitness_partition,
            "exact_recursive": recursive_partition,
            "exact_dp": dp_topdown_partition,
            "individual": partition_individual,
            "heuristic_individual": heuristic_individual_partition
        }
    ]

    latex_rows = []

    # Iterate through each problem, solve with GA and exact methods, measure time and fitness
    for problem in problems:
        print(f"\n--- Problema {problem['name']} ---")

        create_individual = problem["individual"]
        # Choose heuristic initialization if specified and available
        if init_method == "heuristic" and "heuristic_individual" in problem:
            create_individual = problem["heuristic_individual"]

        # Run genetic algorithm and measure elapsed time
        start = time.perf_counter()
        solution, fitness, history = genetic_algorithm(
            fitness_func=problem["fitness"],
            data=problem["data"],
            create_individual=create_individual,
            generations=generations,
            population_size=population_size,
            crossover_rate=crossover_rate,
            mutation_rate=mutation_rate,
            elitism_rate=elitism_proportion,
            selection_method=selection_method,
            tournament_size=tournament_size,
            crossover_operator=crossover_operator,
            mutation_operator=mutation_operator,
            verbose=False
        )
        end = time.perf_counter()
        time_ga = end - start

        # Measure average execution times of exact recursive and DP solutions
        time_recursive = measure_average_time(problem["exact_recursive"], problem["data"], repetitions)
        time_dp = measure_average_time(problem["exact_dp"], problem["data"], repetitions)

        # Prepare LaTeX table row for the problem results
        latex_rows.append(f"{problem['name']} & {fitness:.4f} & {time_ga:.6f} & {time_recursive:.6f} & {time_dp:.6f} \\\\")

    # Print LaTeX document preamble and parameters summary
    print("\\documentclass{article}")
    print("\\usepackage[utf8]{inputenc}")
    print("\\usepackage[spanish]{babel}")
    print("\\usepackage{float}")  # For [H] float placement
    print("\\usepackage{amsmath}")
    print("\\usepackage{graphicx}")
    print("\\begin{document}")

    print("\\noindent\\textbf{Parámetros de la prueba:}\\\\")
    print(f"- Tamaño del conjunto de \\textit{{items}}: {num_items}\\\\")
    print(f"- Inicialización: {init_method}\\\\")
    print(f"- Algoritmo genético: población = {population_size}, generaciones = {generations}\\\\")
    print(f"- Método de selección: {selection_method}\\\\")
    if selection_method == "tournament":
        print(f"- Tamaño de torneo: {tournament_size}\\\\")
    print(f"- Tasa de cruce: {crossover_rate}\\\\")
    print(f"- Operador de cruce: {crossover_operator}\\\\")
    print(f"- Tasa de mutación: {mutation_rate}\\\\")
    print(f"- Operador de mutación: {mutation_operator}\\\\")
    print(f"- Proporción de elitismo: {elitism_proportion}\\\\")
    print(f"- Métodos exactos: {repetitions} repeticiones promedio para medir tiempo\\\\\n")

    # Print LaTeX table header and rows with results
    print("\\begin{table}[H]")
    print("\\centering")
    print("\\begin{tabular}{|l|c|c|c|c|}")
    print("\\hline")
    print("\\textbf{Problema} & \\textbf{Fitness GA} & \\textbf{Tiempo GA (ms)} & \\textbf{Tiempo Recursivo (ms)} & \\textbf{Tiempo DP (ms)} \\\\")
    print("\\hline")
    for row in latex_rows:
        row = row.strip()
        if not row.endswith("\\\\"):
            row += " \\\\"
        print(row)
    print("\\hline")
    print("\\end{tabular}")
    print("\\caption{Comparación de algoritmos genéticos, recursivos y programación dinámica (tiempos en milisegundos)}")
    print("\\label{tab:comparacion_algoritmos}")
    print("\\end{table}")

    print("\\end{document}")


# Main execution block to run experiments with specified parameters
if __name__ == "__main__":
    run_all_experiments(
        population_size=500,
        generations=50,
        repetitions=1,
        num_items=15,
        init_method="random",            # Options: "heuristic" or "random"
        selection_method="tournament",   # Options: "tournament", "ranking", "roulette"
        tournament_size=4,
        mutation_rate=0.6,
        crossover_rate=0.7,
        crossover_operator="one_point",  # Options: "one_point", "two_point", "uniform"
        mutation_operator="bit_flip",    # Options: "bit_flip", "swap"
        elitism_proportion=0.6            # Proportion of elite individuals to keep
    )