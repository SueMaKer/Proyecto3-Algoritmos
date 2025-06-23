import random

def crossover(parent1, parent2, crossover_rate):
    if random.random() > crossover_rate:
        return parent1.copy()

    point = random.randint(1, len(parent1) - 1)
    return parent1[:point] + parent2[point:]


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
