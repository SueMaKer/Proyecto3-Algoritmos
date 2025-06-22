import random

# -----------------------------------------------------------
# Recursive Exhaustive Search for Multi-dimensional Knapsack
# -----------------------------------------------------------
def recursive_knapsack(index, remaining_caps, item_weights, item_values, num_dimensions):
    if index == len(item_weights):
        return 0  # Base case: no more items

    max_value = recursive_knapsack(index + 1, remaining_caps, item_weights, item_values, num_dimensions)

    can_include = True
    for d in range(num_dimensions):
        if item_weights[index][d] > remaining_caps[d]:
            can_include = False
            break

    if can_include:
        updated_caps = remaining_caps.copy()
        for d in range(num_dimensions):
            updated_caps[d] -= item_weights[index][d]
        max_value = max(
            max_value,
            item_values[index] + recursive_knapsack(index + 1, updated_caps, item_weights, item_values, num_dimensions)
        )

    return max_value

# -----------------------------------------------------------
# Top-down Dynamic Programming with Memoization
# -----------------------------------------------------------
def dp_topdown_knapsack(index, remaining_caps, item_weights, item_values, num_dimensions, memo_table):
    state_key = (index, tuple(remaining_caps))
    if index == len(item_weights):
        return 0

    if state_key in memo_table:
        return memo_table[state_key]

    max_value = dp_topdown_knapsack(index + 1, remaining_caps, item_weights, item_values, num_dimensions, memo_table)

    if all(item_weights[index][d] <= remaining_caps[d] for d in range(num_dimensions)):
        updated_caps = list(remaining_caps)
        for d in range(num_dimensions):
            updated_caps[d] -= item_weights[index][d]
        max_value = max(
            max_value,
            item_values[index] + dp_topdown_knapsack(index + 1, updated_caps, item_weights, item_values, num_dimensions, memo_table)
        )

    memo_table[state_key] = max_value
    return max_value

# -----------------------------------------------------------
# Fitness Function for Genetic Algorithm
# -----------------------------------------------------------
def evaluate_fitness(chromosome, item_weights, item_values, capacities, num_dimensions):
    remaining_caps = capacities.copy()
    total_value = 0

    for i, selected in enumerate(chromosome):
        if selected:
            for d in range(num_dimensions):
                remaining_caps[d] -= item_weights[i][d]
                if remaining_caps[d] < 0:
                    return 0  # Penalize infeasible solutions
            total_value += item_values[i]

    return total_value

# -----------------------------------------------------------
# Selection Methods for Genetic Algorithm
# -----------------------------------------------------------
def select_parents(evaluated, method, population_size, tournament_size=3):
    if method == "ranking":
        return [chrom for chrom, _ in evaluated[:population_size // 2]]

    elif method == "ruleta":
        total_fitness = sum(f for _, f in evaluated)
        if total_fitness == 0:
            return random.choices([chrom for chrom, _ in evaluated], k=population_size // 2)
        weights = [f / total_fitness for _, f in evaluated]
        return random.choices([chrom for chrom, _ in evaluated], weights=weights, k=population_size // 2)

    elif method == "torneo":
        parents = []
        while len(parents) < population_size // 2:
            competitors = random.sample(evaluated, tournament_size)
            winner = max(competitors, key=lambda x: x[1])[0]
            parents.append(winner)
        return parents

    else:
        raise ValueError("Método de selección no válido. Usa 'ranking', 'ruleta' o 'torneo'.")

# -----------------------------------------------------------
# Genetic Algorithm for Multi-dimensional Knapsack (Enhanced)
# -----------------------------------------------------------
def genetic_knapsack_solver(item_weights, item_values, capacities, num_dimensions,
                            population_size=50, generations=200,
                            crossover_rate=0.8, mutation_rate=0.01,
                            elitism_count=2, selection_method="ranking"):
    num_items = len(item_weights)
    population = [[random.randint(0, 1) for _ in range(num_items)] for _ in range(population_size)]
    best_solution = None
    best_fitness = 0

    for gen in range(generations):
        evaluated = [(chrom, evaluate_fitness(chrom, item_weights, item_values, capacities, num_dimensions))
                     for chrom in population]
        evaluated.sort(key=lambda x: x[1], reverse=True)

        if evaluated[0][1] > best_fitness:
            best_fitness = evaluated[0][1]
            best_solution = evaluated[0][0]

        elites = [chrom for chrom, _ in evaluated[:elitism_count]]

        parents = select_parents(evaluated, selection_method, population_size)

        children = []
        while len(children) < population_size - elitism_count:
            parent1, parent2 = random.sample(parents, 2)

            if random.random() < crossover_rate:
                crossover_point = random.randint(1, num_items - 1)
                child = parent1[:crossover_point] + parent2[crossover_point:]
            else:
                child = parent1.copy()

            child = [gene ^ 1 if random.random() < mutation_rate else gene for gene in child]
            children.append(child)

        population = elites + children

    return best_solution, best_fitness
