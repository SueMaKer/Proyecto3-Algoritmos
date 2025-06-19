from genetic.elitism import apply_elitism

def test_apply_elitism():
    population = [
        [0,0,0],
        [1,1,1],
        [0,1,0],
        [1,0,1],
        [1,1,0]
    ]
    fitness_scores = [10, 50, 20, 30, 40]

    elitism_rate = 0.4  # 40% de la población = 2 individuos

    elites = apply_elitism(population, fitness_scores, elitism_rate)

    print(f"Elite count esperado: {int(elitism_rate * len(population))}")
    print("Individuos elite (mejores fitness):")
    for ind in elites:
        print(ind)

if __name__ == "__main__":
    test_apply_elitism()
