import random


# Pure recursive solution to the Subset Sum problem
def recursive_subset_sum(data, n=None, target=None):
    nums = data["items"]            # List of numbers to consider
    if target is None:
        target = data["target"]     # Target sum we want to find a subset for
    if n is None:
        n = len(nums)               # Number of items left to consider

    # Base case: target achieved
    if target == 0:
        return True
    # Base case: no items left but target not reached
    if n == 0:
        return False
    # If current item is larger than target, skip it
    if nums[n - 1] > target:
        return recursive_subset_sum(data, n - 1, target)
    
    # Check by excluding or including current item
    return (
        recursive_subset_sum(data, n - 1, target) or
        recursive_subset_sum(data, n - 1, target - nums[n - 1])
    )


# Top-down dynamic programming solution with memoization for Subset Sum
def subset_sum_top_down(data, n=None, target=None, memo=None):
    nums = data["items"]
    if target is None:
        target = data["target"]
    if n is None:
        n = len(nums)
    if memo is None:
        memo = {}                   # Memoization dictionary

    # Base case: target reached
    if target == 0:
        return True
    # Base case: no items left
    if n == 0:
        return False

    key = (n, target)              # State key for memoization
    if key in memo:
        return memo[key]

    # If current item is too big, skip it
    if nums[n - 1] > target:
        result = subset_sum_top_down(data, n - 1, target, memo)
    else:
        # Try excluding or including current item
        result = (
            subset_sum_top_down(data, n - 1, target, memo) or
            subset_sum_top_down(data, n - 1, target - nums[n - 1], memo)
        )

    memo[key] = result             # Memoize result
    return result


# Fitness function to evaluate chromosome for subset sum problem
def fitness_subset_sum(chromosome, data):
    items = data["items"]
    target = data["target"]

    # Sum values of items selected by the chromosome
    total = sum(item for gene, item in zip(chromosome, items) if gene)

    # Penalize if sum exceeds the target
    if total > target:
        return 0
    else:
        # Return sum as fitness (closer to target is better)
        return total


# Generate a random chromosome (individual) for subset sum problem
def subset_individual(num_items, data):
    # Random binary selection of items
    return [random.randint(0, 1) for _ in range(num_items)]


# Heuristic to generate initial chromosome for subset sum, picking largest items first
def heuristic_individual_subset(n_items, data):
    target = data["target"]
    chromosome = [0] * n_items
    current_sum = 0
    # Sort items by value descending while keeping track of original indices
    items_sorted = sorted(enumerate(data["items"]), key=lambda x: x[1], reverse=True)
    for i, val in items_sorted:
        # Add item if it doesn't exceed target sum
        if current_sum + val <= target:
            chromosome[i] = 1
            current_sum += val
    return chromosome