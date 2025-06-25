import unittest
import random
from bin_packing import recursive_bin_packing, dp_bin_packing, fitness_bin_packing, bin_packing_individual

class TestBinPacking(unittest.TestCase):
    def setUp(self):
        self.items = [0.4, 0.7, 0.2, 0.5, 0.8, 0.3]
        self.capacity = 1.0
        self.data = {"items": self.items, "bin_capacity": self.capacity}

    def is_solution_feasible(self, assignment):
        bins = {}
        for item_idx, bin_idx in enumerate(assignment):
            bins.setdefault(bin_idx, 0)
            bins[bin_idx] += self.items[item_idx]
        return all(total <= self.capacity for total in bins.values())

    def count_bins(self, assignment):
        return len(set(assignment))

    def test_recursive_solution(self):
        assignment = recursive_bin_packing(self.items, self.capacity)
        bins_used = self.count_bins(assignment)
        print(f"[Recursive] Assignment: {assignment}")
        print(f"[Recursive] Number of bins used: {bins_used}")
        self.assertTrue(self.is_solution_feasible(assignment), "Recursive solution is infeasible")

    def test_dp_solution(self):
        assignment = dp_bin_packing(self.items, self.capacity)
        bins_used = self.count_bins(assignment)
        print(f"[DP] Assignment: {assignment}")
        print(f"[DP] Number of bins used: {bins_used}")
        self.assertTrue(self.is_solution_feasible(assignment), "DP solution is infeasible")

    def test_genetic_simulation(self):
        best_fitness = -1
        best_assignment = None
        for _ in range(1000):
            individual = bin_packing_individual(len(self.items))
            fitness = fitness_bin_packing(individual, self.data)
            if fitness > best_fitness:
                best_fitness = fitness
                best_assignment = individual

        bins_used = self.count_bins(best_assignment)
        print(f"[Genetic] Best assignment found: {best_assignment}")
        print(f"[Genetic] Fitness: {best_fitness}")
        print(f"[Genetic] Number of bins used: {bins_used}")
        self.assertTrue(self.is_solution_feasible(best_assignment), "Genetic solution is infeasible")

        rec_assignment = recursive_bin_packing(self.items, self.capacity)
        dp_assignment = dp_bin_packing(self.items, self.capacity)
        rec_bins = self.count_bins(rec_assignment)
        dp_bins = self.count_bins(dp_assignment)

        print(f"[Compare] Recursive bins: {rec_bins}, DP bins: {dp_bins}, Genetic bins: {bins_used}")

        self.assertLessEqual(rec_bins, bins_used, "Recursive solution worse que genética")
        self.assertLessEqual(dp_bins, bins_used, "DP solution peor que genética")

if __name__ == "__main__":
    unittest.main(verbosity=2)





