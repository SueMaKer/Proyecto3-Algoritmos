def apply_elitism(population, fitness_scores, params):
    elitism_rate = params.get('elitism_rate', 0.05)  # Por defecto 5%
    elite_count = max(1, int(elitism_rate * len(population)))

    # Empareja fitness con individuos y ordena descendente
    sorted_pop = [ind for _, ind in sorted(zip(fitness_scores, population), key=lambda x: x[0], reverse=True)]

    # Selecciona los mejores elite_count individuos
    elites = sorted_pop[:elite_count]
    return elites