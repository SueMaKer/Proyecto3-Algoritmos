import random


# Recursive backtracking solution for the Bin Packing problem
def recursive_bin_packing(data):
    items = data["items"]              # List of item sizes
    bin_capacity = data["bin_capacity"]  # Capacity of each bin
    best = {"bins": None, "assignment": None, "num_bins": float('inf')}  # Track best solution found

    # Backtracking helper function
    def backtrack(index, bins, assignment):
        # If all items have been assigned
        if index == len(items):
            # Update best solution if fewer bins are used
            if len(bins) < best["num_bins"]:
                best["num_bins"] = len(bins)
                best["bins"] = bins[:]             # Copy current bins usage
                best["assignment"] = assignment[:] # Copy current assignment of items to bins
            return

        item = items[index]

        # Try to place current item into existing bins
        for i in range(len(bins)):
            if bins[i] + item <= bin_capacity:
                bins[i] += item
                assignment.append(i)      # Assign item to bin i
                backtrack(index + 1, bins, assignment)
                assignment.pop()          # Backtrack assignment
                bins[i] -= item           # Backtrack bin load

        # Try placing item in a new bin
        bins.append(item)
        assignment.append(len(bins) - 1)   # Assign item to new bin
        backtrack(index + 1, bins, assignment)
        assignment.pop()
        bins.pop()

    # Start backtracking from first item with empty bins and assignment
    backtrack(0, [], [])
    return best["assignment"]


# Dynamic programming solution for Bin Packing with scaling to integers
def dp_bin_packing(data):
    items = data["items"]
    bin_capacity = data["bin_capacity"]
    SCALE = 100                           # Scaling factor to convert floats to integers
    items_scaled = [int(i * SCALE) for i in items]  # Scale item sizes
    bin_capacity = int(bin_capacity * SCALE)        # Scale bin capacity
    n = len(items_scaled)
    memo = {}                            # Memoization dictionary

    # Recursive helper with memoization
    def helper(index, bins, assignment):
        # Use sorted tuple of bins to represent state for memoization
        key = (index, tuple(sorted(bins)))
        if key in memo:
            return memo[key]

        # Base case: all items assigned
        if index == n:
            return len(bins), assignment[:]

        item = items_scaled[index]
        best_bins = float('inf')
        best_assignment = []

        # Try placing current item into existing bins
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

        # Try placing current item in a new bin
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

    # Run helper from first item
    _, best_assignment = helper(0, [], [])
    return best_assignment


# Fitness function for bin packing chromosomes
def fitness_bin_packing(chromosome, data):
    items = data["items"]
    capacity = data["bin_capacity"]

    bins = {}

    # Calculate total load in each bin
    for item_idx, bin_idx in enumerate(chromosome):
        bins.setdefault(bin_idx, 0)
        bins[bin_idx] += items[item_idx]

    used_bins = len(bins)      # Number of bins used
    valid_bins = 0             # Count of bins not exceeding capacity
    penalty = 0                # Penalty for bins exceeding capacity

    for total_weight in bins.values():
        if total_weight <= capacity:
            valid_bins += 1
        else:
            # Penalize overweight bins heavily
            penalty += (total_weight - capacity) * 10

    if used_bins == 0:
        return 0

    # Fitness rewards valid bins and penalizes overweight bins
    fitness = (1000 * valid_bins / used_bins) - penalty
    return max(fitness, 0)  # Fitness cannot be negative


# Generates a random individual (chromosome) for bin packing
def bin_packing_individual(num_items, data=None):
    import random
    # Assign each item randomly to a bin index between 0 and num_items-1
    return [random.randint(0, num_items - 1) for _ in range(num_items)]


# Heuristic to generate an initial solution for bin packing
def heuristic_individual_binpacking(n_items, data):
    chromosome = [0] * n_items    # Initialize chromosome with zeros
    bins = []                    # Track current bin loads
    for i, item in enumerate(data["items"]):
        placed = False
        # Try placing item in an existing bin
        for b, bin_load in enumerate(bins):
            if bin_load + item <= data["bin_capacity"]:
                chromosome[i] = b
                bins[b] += item
                placed = True
                break
        # If item does not fit in any existing bin, create a new bin
        if not placed:
            chromosome[i] = len(bins)
            bins.append(item)
    return chromosome