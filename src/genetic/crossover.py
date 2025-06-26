import random

def crossover(parent1, parent2, crossover_rate, operator="uniform"):
    if random.random() > crossover_rate:
        return parent1.copy()

    if operator == "one_point":
        child1, _ = one_point_crossover(parent1, parent2)
    elif operator == "two_point":
        child1, _ = two_point_crossover(parent1, parent2)
    elif operator == "uniform":
        child1, _ = uniform_crossover(parent1, parent2)
    else:
        raise ValueError(f"Operador de cruce desconocido: {operator}")

    return child1


def one_point_crossover(p1, p2):
    point = random.randint(1, len(p1) - 1)
    child1 = p1[:point] + p2[point:]
    child2 = p2[:point] + p1[point:]
    return child1, child2

def two_point_crossover(p1, p2):
    point1 = random.randint(0, len(p1) - 2)
    point2 = random.randint(point1 + 1, len(p1) - 1)
    child1 = p1[:point1] + p2[point1:point2] + p1[point2:]
    child2 = p2[:point1] + p1[point1:point2] + p2[point2:]
    return child1, child2

def uniform_crossover(p1, p2):
    child1 = []
    child2 = []
    for gene1, gene2 in zip(p1, p2):
        if random.random() < 0.5:
            child1.append(gene1)
            child2.append(gene2)
        else:
            child1.append(gene2)
            child2.append(gene1)
    return child1, child2