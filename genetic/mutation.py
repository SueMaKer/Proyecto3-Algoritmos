import random

def mutate(individual, params):
    """
    Aplica mutación a un cromosoma según el tipo y tasa definidos.

    Args:
        individual (list): Cromosoma a mutar.
        params (dict): Debe incluir:
            - 'mutation_rate': probabilidad de mutar cada gen (float entre 0 y 1)
            - 'mutation_type': 'bitflip' o 'swap'

    Returns:
        list: Cromosoma mutado (nueva lista)
    """
    mutation_type = params.get('mutation_type', 'bitflip')
    rate = params.get('mutation_rate', 0.01)

    if mutation_type == 'bitflip':
        return bitflip_mutation(individual, rate)
    elif mutation_type == 'swap':
        return swap_mutation(individual, rate) #	swap: Intercambia posiciones de dos genes.
    else:
        raise ValueError(f"Tipo de mutación no soportado: {mutation_type}")


# === Métodos de mutación ===

def bitflip_mutation(individual, rate):
    # Aplica mutación bit a bit con cierta probabilidad
    mutated = []
    for bit in individual:
        if random.random() < rate:
            mutated.append(1 - bit)  # invierte 0↔1
        else:
            mutated.append(bit)
    return mutated


def swap_mutation(individual, rate):
    # Aplica una o más permutaciones por pares aleatorios
    mutated = individual[:]
    n = len(individual)
    for _ in range(int(rate * n)):
        i, j = random.sample(range(n), 2)
        mutated[i], mutated[j] = mutated[j], mutated[i]
    return mutated
