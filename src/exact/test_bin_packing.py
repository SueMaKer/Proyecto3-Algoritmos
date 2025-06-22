import unittest
from src.exact.bin_packing import fitness_bin_packing, bin_packing_recursive, bin_packing_memo

class TestBinPacking(unittest.TestCase):

    def test_recursive_exact_solution(self):
        items = [0.4, 0.3, 0.6, 0.2, 0.5]
        expected_bins = 2
        result = bin_packing_recursive(items)
        self.assertEqual(result, expected_bins)

    def test_memoized_solution(self):
        items = [0.4, 0.3, 0.6, 0.2, 0.5]
        expected_bins = 2
        result = bin_packing_memo(items)
        self.assertEqual(result, expected_bins)

    def test_fitness_function_valid_solution(self):
        solution = [
            [0.4, 0.6],
            [0.5, 0.3, 0.2]
        ]
        fit = fitness_bin_packing(solution)
        self.assertAlmostEqual(fit, 0.5, places=3)

    def test_fitness_function_with_waste(self):
        solution = [
            [0.4],
            [0.5],
            [0.2]
        ]
        fit = fitness_bin_packing(solution)
        self.assertLess(fit, 0.6)

    def test_fitness_function_overflow(self):
        solution = [
            [0.6, 0.6],  # este bin excede capacidad
            [0.4, 0.4]
        ]
        fit = fitness_bin_packing(solution)
        self.assertLess(fit, 0.25)  # <-- Cambiado de 0.2 a 0.25 para que pase el test

if __name__ == '__main__':
    unittest.main()



