# Test for Multi-Dimensional Knapsack Problem (MKS)
# -----------------------------------------------------------
from MKS import recursive_knapsack, dp_topdown_knapsack, genetic_knapsack_solver

class MultiDimensionalKnapsackTester:
    def __init__(self):
        self.item_weights = [
            [2, 3],  # Item 0
            [3, 4],  # Item 1
            [4, 2],  # Item 2
            [4, 3],  # Item 3
            [5, 5]   # Item 4
        ]
        self.item_values = [3, 4, 5, 6, 8]
        self.capacity_limits = [10, 10]
        self.num_dimensions = 2

    def is_solution_feasible(self, chromosome):
        remaining = self.capacity_limits.copy()
        for i, selected in enumerate(chromosome):
            if selected:
                for d in range(self.num_dimensions):
                    remaining[d] -= self.item_weights[i][d]
                    if remaining[d] < 0:
                        return False
        return True

    def run_all_algorithms(self):
        print("=== Multi-Dimensional Knapsack Problem ===\n")
        print("Item Weights :", self.item_weights)
        print("Item Values  :", self.item_values)
        print("Capacities   :", self.capacity_limits)

        # 1. Recursive Exhaustive Search
        print("\n[1] Recursive Exhaustive Search:")
        result_recursive = recursive_knapsack(
            0, self.capacity_limits, self.item_weights, self.item_values, self.num_dimensions
        )
        print("Max Value:", result_recursive)

        # 2. Top-down Dynamic Programming
        print("\n[2] Top-Down Dynamic Programming:")
        memo_table = {}
        result_dp = dp_topdown_knapsack(
            0, self.capacity_limits, self.item_weights, self.item_values, self.num_dimensions, memo_table
        )
        print("Max Value:", result_dp)

        # ✅ Assert: Recursive and DP must match
        assert result_recursive == result_dp, "Mismatch: Recursive and DP solutions must be equal"

        # 3. Genetic Algorithm with different selection methods
        print("\n[3] Genetic Algorithm (Ranking, Ruleta, Torneo):")
        for method in ["ranking", "ruleta", "torneo"]:
            print(f"\n → Method: {method}")
            best_chromosome, best_value = genetic_knapsack_solver(
                self.item_weights,
                self.item_values,
                self.capacity_limits,
                self.num_dimensions,
                population_size=50,
                generations=200,
                mutation_rate=0.05,
                crossover_rate=0.8,
                elitism_count=3,
                selection_method=method
            )
            print("   Best Chromosome:", best_chromosome)
            print("   Fitness (Value):", best_value)

            # ✅ Assert: Genetic value must not exceed optimal
            assert best_value <= result_dp, f"Genetic algorithm ({method}) exceeded optimal value"

            # ✅ Assert: Genetic solution must be feasible
            assert self.is_solution_feasible(best_chromosome), f"Genetic solution with method '{method}' is infeasible"

        print("\n✅ All tests passed successfully.")

if __name__ == "__main__":
    tester = MultiDimensionalKnapsackTester()
    tester.run_all_algorithms()
