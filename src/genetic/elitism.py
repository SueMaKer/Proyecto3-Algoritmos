# Function to apply elitism: keeps the best individuals from the current population
def apply_elitism(population, fitness_scores, params):
    # Get the elitism rate from parameters (default is 5%)
    elitism_rate = params.get('elitism_rate', 0.05)
    # Calculate the number of elite individuals (at least 1)
    elite_count = max(1, int(elitism_rate * len(population)))

    # Pair fitness scores with individuals and sort them in descending order of fitness
    sorted_pop = [ind for _, ind in sorted(zip(fitness_scores, population), key=lambda x: x[0], reverse=True)]

    # Select the top 'elite_count' individuals as elites
    elites = sorted_pop[:elite_count]
    return elites  # Return the elite individuals