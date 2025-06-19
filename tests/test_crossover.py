import random
from genetic.crossover import crossover

# Semilla para reproducibilidad en pruebas
random.seed(42)

# Padres de ejemplo (cromosomas binarios)
parent1 = [1, 0, 1, 1, 0, 0, 1, 1]
parent2 = [0, 1, 0, 0, 1, 1, 0, 0]

print("PADRE 1:", parent1)
print("PADRE 2:", parent2)

# === Prueba: 1-point crossover ===
params_1p = {
    'crossover_rate': 1.0,          # Siempre aplica cruce
    'crossover_type': '1point'
}
child1, child2 = crossover(parent1, parent2, params_1p)
print("\n[1-POINT CROSSOVER]")
print("Hijo 1:", child1)
print("Hijo 2:", child2)

# === Prueba: 2-point crossover ===
params_2p = {
    'crossover_rate': 1.0,
    'crossover_type': '2point'
}
child1, child2 = crossover(parent1, parent2, params_2p)
print("\n[2-POINT CROSSOVER]")
print("Hijo 1:", child1)
print("Hijo 2:", child2)

# === Prueba: Uniform crossover ===
params_uniform = {
    'crossover_rate': 1.0,
    'crossover_type': 'uniform'
}
child1, child2 = crossover(parent1, parent2, params_uniform)
print("\n[UNIFORM CROSSOVER]")
print("Hijo 1:", child1)
print("Hijo 2:", child2)
