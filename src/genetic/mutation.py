import random

def mutate(chromosome, mutation_rate, mutation_operator="bit_flip"):
    if mutation_operator == "bit_flip":
        return [gene ^ 1 if random.random() < mutation_rate else gene for gene in chromosome]
    elif mutation_operator == "swap":
        if random.random() < mutation_rate:
            i, j = random.sample(range(len(chromosome)), 2)
            chromosome[i], chromosome[j] = chromosome[j], chromosome[i]
        return chromosome
    else:
        raise ValueError(f"Unknown mutation operator: {mutation_operator}")


