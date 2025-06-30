import random
import math
import random

# RECURSIVO PURO
def recursive_partition(data):
    print("entra recursive")
    nums = data["items"]
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False

    target = total_sum // 2

    def helper(i, current_sum):
        if current_sum == target:
            return True
        if i == len(nums) or current_sum > target:
            return False
        return helper(i + 1, current_sum + nums[i]) or helper(i + 1, current_sum)

    return helper(0, 0)

# DP TOPDOWN (CON MEMOIZACIÓN)
def dp_topdown_partition(data):
    print("entra dp")
    nums = data["items"]
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False

    target = total_sum // 2
    memo = {}

    def helper(i, current_sum):
        if current_sum == target:
            return True
        if i == len(nums) or current_sum > target:
            return False
        if (i, current_sum) in memo:
            return memo[(i, current_sum)]

        include = helper(i + 1, current_sum + nums[i])
        exclude = helper(i + 1, current_sum)
        memo[(i, current_sum)] = include or exclude
        return memo[(i, current_sum)]

    return helper(0, 0)


# FITNESS FUNCTION MEJORADA
def fitness_partition(chromosome, data):
    items = data["items"]
    group_a = sum(item for gene, item in zip(chromosome, items) if gene == 1)
    group_b = sum(item for gene, item in zip(chromosome, items) if gene == 0)
    diff = abs(group_a - group_b)
    return 1 / (1 + diff**2)  # penalización más suave pero más efectiva

def partition_individual(num_items, data=None):
    return [random.randint(0, 1) for _ in range(num_items)]

# INDIVIDUO HEURÍSTICO MEJORADO (con ruido opcional)
def heuristic_individual_partition(n_items, data):
    chromosome = [0] * n_items
    sum_a = 0
    sum_b = 0
    items = data["items"]
    for i in range(n_items):
        if abs(sum_a - sum_b) < 5 and random.random() < 0.3:
            gene = random.randint(0, 1)
        else:
            gene = 1 if sum_a <= sum_b else 0
        chromosome[i] = gene
        if gene == 1:
            sum_a += items[i]
        else:
            sum_b += items[i]
    return chromosome



