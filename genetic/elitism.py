def apply_elitism(population, fitness_scores, params):
    
    elitism_rate = params['elitism_rate']  # Por ejemplo 0.2 (20%)

    elite_count = int(elitism_rate * len(population))
   
    sorted_population = [ind for _, ind in sorted(zip(fitness_scores, population), key=lambda x: x[0], reverse=True)]
    elites = sorted_population[:elite_count]

    return elites

