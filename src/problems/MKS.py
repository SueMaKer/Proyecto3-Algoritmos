import random

def recursive_knapsack(data, index=0, remaining_caps=None):
    if remaining_caps is None:
        remaining_caps = data["capacities"].copy()
    item_weights = data["weights"]
    item_values = data["values"]
    num_dimensions = data.get("num_dimensions", 1)

    if index == len(item_weights):
        return 0

    max_value = recursive_knapsack(data, index + 1, remaining_caps)

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
            item_values[index] + recursive_knapsack(data, index + 1, updated_caps)
        )

    return max_value


def dp_topdown_knapsack(data, index=0, remaining_caps=None, memo_table=None):
    if remaining_caps is None:
        remaining_caps = data["capacities"].copy()
    if memo_table is None:
        memo_table = {}

    item_weights = data["weights"]
    item_values = data["values"]
    num_dimensions = data.get("num_dimensions", 1)

    state_key = (index, tuple(remaining_caps))
    if index == len(item_weights):
        return 0

    if state_key in memo_table:
        return memo_table[state_key]

    max_value = dp_topdown_knapsack(data, index + 1, remaining_caps, memo_table)

    if all(item_weights[index][d] <= remaining_caps[d] for d in range(num_dimensions)):
        updated_caps = list(remaining_caps)
        for d in range(num_dimensions):
            updated_caps[d] -= item_weights[index][d]
        max_value = max(
            max_value,
            item_values[index] + dp_topdown_knapsack(data, index + 1, updated_caps, memo_table)
        )

    memo_table[state_key] = max_value
    return max_value

def fitness_knapsack(chromosome, data):
    item_weights = data["weights"]
    item_values = data["values"]
    capacities = data["capacities"]
    num_dimensions = data["num_dimensions"]

    remaining = capacities[:]
    total_value = 0

    for i, selected in enumerate(chromosome):
        if selected:
            for d in range(num_dimensions):
                remaining[d] -= item_weights[i][d]
                if remaining[d] < 0:
                    return 0  # Penalización por sobrecapacidad
            total_value += item_values[i]

    return total_value

def knapsack_individual(n_items, data=None):
    return [random.randint(0, 1) for _ in range(n_items)]

def heuristic_individual_knapsack(n_items, data):
    ratios = [(v / sum(w), i) for i, (v, w) in enumerate(zip(data["values"], data["weights"]))]
    ratios.sort(reverse=True)
    chromosome = [0] * n_items
    current = [0] * data["num_dimensions"]
    for _, i in ratios:
        fits = all(current[d] + data["weights"][i][d] <= data["capacities"][d] for d in range(data["num_dimensions"]))
        if fits:
            chromosome[i] = 1
            for d in range(data["num_dimensions"]):
                current[d] += data["weights"][i][d]
    return chromosome