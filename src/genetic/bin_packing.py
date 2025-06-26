import random

def fitness_bin_packing(chromosome, data):
    items = data["items"]
    capacity = data["bin_capacity"]

    bins = {}

    for item_idx, bin_idx in enumerate(chromosome):
        bins.setdefault(bin_idx, 0)
        bins[bin_idx] += items[item_idx]

    used_bins = len(bins)
    valid_bins = 0
    penalty = 0

    for total_weight in bins.values():
        if total_weight <= capacity:
            valid_bins += 1
        else:
            # Penalty for exceeding capacity
            penalty += (total_weight - capacity) * 10

    if used_bins == 0:
        return 0

    fitness = (1000 * valid_bins / used_bins) - penalty
    return max(fitness, 0)



def bin_packing_individual(num_items):
    import random
    return [random.randint(0, num_items - 1) for _ in range(num_items)]

def recursive_bin_packing(items, bin_capacity=1.0):
    best = {"bins": None, "assignment": None, "num_bins": float('inf')}

    def backtrack(index, bins, assignment):
        if index == len(items):
            if len(bins) < best["num_bins"]:
                best["num_bins"] = len(bins)
                best["bins"] = bins[:]
                best["assignment"] = assignment[:]
            return

        item = items[index]

        for i in range(len(bins)):
            if bins[i] + item <= bin_capacity:
                bins[i] += item
                assignment.append(i)
                backtrack(index + 1, bins, assignment)
                assignment.pop()
                bins[i] -= item

        bins.append(item)
        assignment.append(len(bins) - 1)
        backtrack(index + 1, bins, assignment)
        assignment.pop()
        bins.pop()

    backtrack(0, [], [])
    return best["assignment"]

def dp_bin_packing(items, bin_capacity=1.0):
    SCALE = 100
    items_scaled = [int(i * SCALE) for i in items]
    bin_capacity = int(bin_capacity * SCALE)
    n = len(items_scaled)
    memo = {}

    def helper(index, bins, assignment):
        key = (index, tuple(sorted(bins)))
        if key in memo:
            return memo[key]

        if index == n:
            return len(bins), assignment[:]

        item = items_scaled[index]
        best_bins = float('inf')
        best_assignment = []

        for i in range(len(bins)):
            if bins[i] + item <= bin_capacity:
                bins[i] += item
                assignment.append(i)
                used, assign = helper(index + 1, bins, assignment)
                if used < best_bins:
                    best_bins = used
                    best_assignment = assign[:]
                assignment.pop()
                bins[i] -= item

        bins.append(item)
        assignment.append(len(bins) - 1)
        used, assign = helper(index + 1, bins, assignment)
        if used < best_bins:
            best_bins = used
            best_assignment = assign[:]
        assignment.pop()
        bins.pop()

        memo[key] = (best_bins, best_assignment)
        return memo[key]

    _, best_assignment = helper(0, [], [])
    return best_assignment


def bin_packing_individual(num_items):
    return [random.randint(0, num_items - 1) for _ in range(num_items)]