import random

def mutate(chromosome, mutation_rate):
    return [gene ^ 1 if random.random() < mutation_rate else gene for gene in chromosome]

