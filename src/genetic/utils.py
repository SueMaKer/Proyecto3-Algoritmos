def should_stop(no_improvement, max_no_improvement):
    """
    Verifica si se debe detener el algoritmo genético por falta de mejora.
    
    Args:
        no_improvement (int): número de generaciones sin mejora.
        max_no_improvement (int): máximo permitido sin mejora.

    Returns:
        bool: True si se debe detener, False si se continúa.
    """
    return no_improvement >= max_no_improvement


def track_best(evaluated, best_fitness, best_solution):
    """
    Actualiza el mejor fitness y solución si hay mejora.

    Args:
        evaluated (list): lista de tuplas (chromosome, fitness).
        best_fitness (float): mejor fitness actual.
        best_solution (list): mejor solución actual.

    Returns:
        tuple: (nuevo_best_solution, nuevo_best_fitness, mejoró)
    """
    current_best = evaluated[0]
    if current_best[1] > best_fitness:
        return current_best[0], current_best[1], True
    return best_solution, best_fitness, False


def seed_everything(seed_value):
    """
    Configura la semilla aleatoria para reproducibilidad.

    Args:
        seed_value (int): semilla deseada.
    """
    import random
    import numpy as np

    random.seed(seed_value)
    np.random.seed(seed_value)