# Parent selection methods:
# Ranking: sort by fitness; pick top-fit individuals (select the 2 best)
# Roulette: selection probability proportional to fitness
# Tournament: compete in groups of size k; randomly pick k individuals, winner is the one with highest fitness; repeat twice

import random

# Main function to select two parents based on the chosen selection method
def select_parents(population, fitness_scores, params):

    # Get selection method from params, default to 'tournament'
    method = params.get('selection_method', 'tournament')

    # Roulette wheel selection method
    if method == 'roulette':
        return roulette_selection(population, fitness_scores)

    # Ranking selection method
    elif method == 'ranking':
        return ranking_selection(population, fitness_scores)

    # Tournament selection method with tournament size k
    elif method == 'tournament':
        k = params.get('tournament_size', 3)
        return tournament_selection(population, fitness_scores, k)

    # Raise error if selection method is unknown
    else:
        raise ValueError(f"Unknown selection method: {method}")


# Roulette wheel selection: probability proportional to fitness
def roulette_selection(population, fitness_scores):
    total_fitness = sum(fitness_scores)
    # If total fitness is zero (all fitness zero), use uniform probabilities
    if total_fitness == 0:
        probs = [1 / len(population)] * len(population)
    else:
        probs = [f / total_fitness for f in fitness_scores]

    # Randomly select two individuals with weighted probabilities
    selected = random.choices(population, weights=probs, k=2)
    return selected[0], selected[1]


# Ranking selection: pick the two individuals with highest fitness
def ranking_selection(population, fitness_scores):
    # Sort population descending by fitness
    sorted_population = [x for x, _ in sorted(zip(population, fitness_scores), key=lambda x: x[1], reverse=True)]
    # Return the top two individuals
    return sorted_population[0], sorted_population[1]


# Tournament selection: pick k random individuals, winner is the best among them
def tournament_selection(population, fitness_scores, k):
    def tournament():
        # Randomly sample k candidates from population with fitness
        candidates = random.sample(list(zip(population, fitness_scores)), k)
        # Return the individual with the highest fitness
        return max(candidates, key=lambda x: x[1])[0]

    # Perform two tournaments to select two parents
    return tournament(), tournament()