import random

# Mutation function for a chromosome
def mutate(chromosome, mutation_rate, mutation_operator="bit_flip"):
    # If the mutation operator is 'bit_flip' (commonly used for binary chromosomes)
    if mutation_operator == "bit_flip":
        # For each gene, flip its value (0 -> 1 or 1 -> 0) with a probability equal to mutation_rate
        return [gene ^ 1 if random.random() < mutation_rate else gene for gene in chromosome]

    # If the mutation operator is 'swap' (commonly used for permutation-based representations)
    elif mutation_operator == "swap":
        # Apply swap mutation with a probability equal to mutation_rate
        if random.random() < mutation_rate:
            # Select two random positions in the chromosome
            i, j = random.sample(range(len(chromosome)), 2)
            # Swap the genes at those positions
            chromosome[i], chromosome[j] = chromosome[j], chromosome[i]
        return chromosome  # Return the (possibly mutated) chromosome

    # If the mutation operator is not recognized, raise an error
    else:
        raise ValueError(f"Unknown mutation operator: {mutation_operator}")