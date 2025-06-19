import random
from genetic.selection import select_parents

# ---------- Configuración ----------
# Simulamos una población de cromosomas (por simplicidad, números binarios)
population = [
    [0, 0, 1, 1],
    [1, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 1, 1, 0]
]

# Asignamos valores ficticios de fitness
fitness_scores = [10, 30, 50, 40, 70]

# ---------- Diferentes pruebas ----------

print("\n=== Prueba: ROULETTE ===")
params_roulette = {
    'selection_method': 'roulette'
}
p1, p2 = select_parents(population, fitness_scores, params_roulette)
print("Padre 1:", p1)
print("Padre 2:", p2)

print("\n=== Prueba: RANKING ===")
params_ranking = {
    'selection_method': 'ranking'
}
p1, p2 = select_parents(population, fitness_scores, params_ranking)
print("Padre 1:", p1)
print("Padre 2:", p2)

print("\n=== Prueba: TOURNAMENT (k=3) ===")
params_tournament = {
    'selection_method': 'tournament',
    'tournament_size': 3
}
p1, p2 = select_parents(population, fitness_scores, params_tournament)
print("Padre 1:", p1)
print("Padre 2:", p2)
