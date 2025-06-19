def fitness_subset_sum(chromosome, items, target):
    total = sum(gene * item for gene, item in zip(chromosome, items))
    if total > target:
        return 0  # penalización por pasarse
    else:
        return total  # cuanto más cerca al target, mejor
