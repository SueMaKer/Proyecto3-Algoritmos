import random

# cambiar n a cantidad de elementos
def recursive_subset_sum(data, n=None, target=None):
    nums = data["items"]
    if target is None:
        target = data["target"]
    if n is None:
        n = len(nums)

    if target == 0:
        return True
    if n == 0:
        return False
    if nums[n - 1] > target:
        return recursive_subset_sum(data, n - 1, target)
    
    return (
        recursive_subset_sum(data, n - 1, target) or
        recursive_subset_sum(data, n - 1, target - nums[n - 1])
    )



def subset_sum_top_down(data, n=None, target=None, memo=None):
    nums = data["items"]
    if target is None:
        target = data["target"]
    if n is None:
        n = len(nums)
    if memo is None:
        memo = {}

    if target == 0:
        return True
    if n == 0:
        return False

    key = (n, target)
    if key in memo:
        return memo[key]

    if nums[n - 1] > target:
        result = subset_sum_top_down(data, n - 1, target, memo)
    else:
        result = (
            subset_sum_top_down(data, n - 1, target, memo) or
            subset_sum_top_down(data, n - 1, target - nums[n - 1], memo)
        )

    memo[key] = result
    return result

def fitness_subset_sum(chromosome, data):
    items = data["items"]
    target = data["target"]

    total = sum(item for gene, item in zip(chromosome, items) if gene)

    if total > target:
        return 0  # Penalización por exceder el target
    else:
        return total  # Cuanto más cerca del target, mejor

def subset_individual(num_items, data):
    return [random.randint(0, 1) for _ in range(num_items)]


def heuristic_individual_subset(n_items, data):
    target = data["target"]
    chromosome = [0] * n_items
    current_sum = 0
    items_sorted = sorted(enumerate(data["items"]), key=lambda x: x[1], reverse=True)
    for i, val in items_sorted:
        if current_sum + val <= target:
            chromosome[i] = 1
            current_sum += val
    return chromosome