def fitness_bin_packing(solution, bin_capacity=1.0, overflow_penalty=20):
    num_bins = len(solution)
    total_waste = 0
    for bin in solution:
        total_bin_weight = sum(bin)
        if total_bin_weight > bin_capacity:
            total_waste += (total_bin_weight - bin_capacity) * overflow_penalty
        else:
            total_waste += (bin_capacity - total_bin_weight)

    fitness = 1 / (num_bins + total_waste + 1e-6)
    return fitness

def bin_packing_recursive(items, bin_capacity=1.0):

    def pack(remaining_items, bins):
        if not remaining_items:
            return len(bins)
        
        item = remaining_items[0]
        rest = remaining_items[1:]
        
        min_bins = float('inf')

        for i in range(len(bins)):
            if bins[i] + item <= bin_capacity:
                bins[i] += item
                min_bins = min(min_bins, pack(rest, bins))
                bins[i] -= item  # backtrack

        bins.append(item)
        min_bins = min(min_bins, pack(rest, bins))
        bins.pop()  # backtrack

        return min_bins

    return pack(items, [])


def bin_packing_memo(items, bin_capacity=1.0):

    SCALE = 100
    items = [int(i * SCALE) for i in items]
    bin_capacity = int(bin_capacity * SCALE)
    n = len(items)

    cache = {}

    def pack(index, bins_tuple):
        key = (index, bins_tuple)

        if key in cache:
            return cache[key]

        if index == n:
            return len(bins_tuple)

        item = items[index]
        min_bins = float('inf')

        # Probar colocar en bins existentes
        for i in range(len(bins_tuple)):
            if bins_tuple[i] + item <= bin_capacity:
                new_bins = list(bins_tuple)
                new_bins[i] += item
                new_bins_sorted = tuple(sorted(new_bins))
                min_bins = min(min_bins, pack(index + 1, new_bins_sorted))

        # Probar abrir un nuevo bin
        new_bins = list(bins_tuple) + [item]
        new_bins_sorted = tuple(sorted(new_bins))
        min_bins = min(min_bins, pack(index + 1, new_bins_sorted))

        cache[key] = min_bins
        return min_bins

    return pack(0, tuple())
