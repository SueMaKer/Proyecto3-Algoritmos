#Selección de padres:
# Ranking: ordenar por fitness; extraer top- aptos. (elegir a los 2 mejores)
# Ruleta: probabilidad proporcional al fitness.
# Torneo: competir grupos de tamaño. (elige al azar, gana el mayor fitness se haces dos veces)
import random

def select_parents(population, fitness_scores, params):
    

    method = params.get('selection_method', 'tournament')

    if method == 'roulette':
        return roulette_selection(population, fitness_scores)

    elif method == 'ranking':
        return ranking_selection(population, fitness_scores)

    elif method == 'tournament':
        k = params.get('tournament_size', 3)
        return tournament_selection(population, fitness_scores, k)

    else:
        raise ValueError(f"Método de selección desconocido: {method}")




def roulette_selection(population, fitness_scores):
    total_fitness = sum(fitness_scores)
    if total_fitness == 0:
        probs = [1/len(population)] * len(population)
    else:
        probs = [f / total_fitness for f in fitness_scores]

    selected = random.choices(population, weights=probs, k=2)
    return selected[0], selected[1]


def ranking_selection(population, fitness_scores):
    # Ordenar descendente por fitness
    sorted_population = [x for x, _ in sorted(zip(population, fitness_scores), key=lambda x: x[1], reverse=True)]
    return sorted_population[0], sorted_population[1]


def tournament_selection(population, fitness_scores, k):
    def tournament():
        candidates = random.sample(list(zip(population, fitness_scores)), k)
        return max(candidates, key=lambda x: x[1])[0]

    return tournament(), tournament()
      