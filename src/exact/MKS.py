import random

# -----------------------------------------------------------
# Recursive Exhaustive Search for Multi-dimensional Knapsack
# -----------------------------------------------------------
def recursive_knapsack(index, remaining_caps, item_weights, item_values, num_dimensions):
    if index == len(item_weights):
        return 0  # Base case: no more items

    # Option 1: exclude current item
    max_value = recursive_knapsack(index + 1, remaining_caps, item_weights, item_values, num_dimensions)

    # Option 2: include current item if it fits in all dimensions
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
        return 0  # Base case

    if state_key in memo_table:
        return memo_table[state_key]  # Retrieve from memo if already computed

    # Exclude current item
    max_value = dp_topdown_knapsack(index + 1, remaining_caps, item_weights, item_values, num_dimensions, memo_table)

    # Try including the item if it fits
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
            # Check if item fits in all dimensions
            for d in range(num_dimensions):
                remaining_caps[d] -= item_weights[i][d]
                if remaining_caps[d] < 0:
                    return 0  # Penalize infeasible solutions
            total_value += item_values[i]

    return total_value

# -----------------------------------------------------------
# Genetic Algorithm for Multi-dimensional Knapsack
# -----------------------------------------------------------
def genetic_knapsack_solver(item_weights, item_values, capacities, num_dimensions,
                            population_size=50, generations=200, mutation_rate=0.01):
    num_items = len(item_weights)
    population = [[random.randint(0, 1) for _ in range(num_items)] for _ in range(population_size)]
    best_solution = None
    best_fitness = 0

    for gen in range(generations):
        # Evaluate fitness of all chromosomes
        evaluated = [(chrom, evaluate_fitness(chrom, item_weights, item_values, capacities, num_dimensions))
                     for chrom in population]
        evaluated.sort(key=lambda x: x[1], reverse=True)

        # Keep the best half
        population = [chrom for chrom, _ in evaluated[:population_size // 2]]

        # Update best solution found
        if evaluated[0][1] > best_fitness:
            best_fitness = evaluated[0][1]
            best_solution = evaluated[0][0]

        # Generate new children via crossover and mutation
        children = []
        while len(children) < population_size - len(population):
            parent1, parent2 = random.sample(population, 2)
            crossover_point = random.randint(1, num_items - 1)
            child = parent1[:crossover_point] + parent2[crossover_point:]
            # Apply mutation
            child = [gene ^ 1 if random.random() < mutation_rate else gene for gene in child]
            children.append(child)

        population += children  # Add new children to the population

    return best_solution, best_fitness