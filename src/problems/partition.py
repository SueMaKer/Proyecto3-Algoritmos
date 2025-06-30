import random
import math
import random  # (imported twice, but left as is)

# PURE RECURSIVE SOLUTION for the Partition problem
def recursive_partition(data):
    print("entra recursive")  # Debug print: entering recursive method
    nums = data["items"]       # List of numbers to partition
    total_sum = sum(nums)
    # If total sum is odd, partition into two equal subsets is impossible
    if total_sum % 2 != 0:
        return False

    target = total_sum // 2    # Target sum for each subset

    # Recursive helper to try subsets starting from index i with current_sum
    def helper(i, current_sum):
        # Found a subset that sums exactly to target
        if current_sum == target:
            return True
        # Reached end of list or exceeded target sum, no solution here
        if i == len(nums) or current_sum > target:
            return False
        # Explore including current number or excluding it
        return helper(i + 1, current_sum + nums[i]) or helper(i + 1, current_sum)

    return helper(0, 0)


# TOP-DOWN DYNAMIC PROGRAMMING SOLUTION with memoization for Partition problem
def dp_topdown_partition(data):
    print("entra dp")  # Debug print: entering DP method
    nums = data["items"]
    total_sum = sum(nums)
    # Odd total sum means no equal partition possible
    if total_sum % 2 != 0:
        return False

    target = total_sum // 2
    memo = {}  # Memo dictionary to store computed states

    # Recursive helper with memoization
    def helper(i, current_sum):
        if current_sum == target:
            return True
        if i == len(nums) or current_sum > target:
            return False
        # Return memoized result if available
        if (i, current_sum) in memo:
            return memo[(i, current_sum)]

        # Compute results including or excluding current number
        include = helper(i + 1, current_sum + nums[i])
        exclude = helper(i + 1, current_sum)
        memo[(i, current_sum)] = include or exclude
        return memo[(i, current_sum)]

    return helper(0, 0)


# Improved fitness function for Partition problem
def fitness_partition(chromosome, data):
    items = data["items"]
    # Sum of items assigned to group A (genes == 1)
    group_a = sum(item for gene, item in zip(chromosome, items) if gene == 1)
    # Sum of items assigned to group B (genes == 0)
    group_b = sum(item for gene, item in zip(chromosome, items) if gene == 0)
    diff = abs(group_a - group_b)
    # Fitness penalizes squared difference; smoother and more effective penalty
    return 1 / (1 + diff**2)


# Generate a random individual (chromosome) for partition problem (binary assignment)
def partition_individual(num_items, data=None):
    return [random.randint(0, 1) for _ in range(num_items)]


# Improved heuristic individual for partition problem with optional noise
def heuristic_individual_partition(n_items, data):
    chromosome = [0] * n_items
    sum_a = 0
    sum_b = 0
    items = data["items"]
    for i in range(n_items):
        # With some probability, randomly assign gene when sums are close to add noise
        if abs(sum_a - sum_b) < 5 and random.random() < 0.3:
            gene = random.randint(0, 1)
        else:
            # Otherwise assign item to the group with smaller current sum to balance
            gene = 1 if sum_a <= sum_b else 0
        chromosome[i] = gene
        if gene == 1:
            sum_a += items[i]
        else:
            sum_b += items[i]
    return chromosome