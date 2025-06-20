import unittest
from subset_sum import subset_sum_top_down  # importa la función correcta

class TestSubsetSum(unittest.TestCase):

    def test_caso_positivo(self):
        nums = [3, 34, 4, 12, 5, 2]
        target = 9
        self.assertTrue(subset_sum_top_down(nums, len(nums), target))

    def test_caso_negativo(self):
        nums = [3, 34, 4, 12, 5, 2]
        target = 30
        self.assertFalse(subset_sum_top_down(nums, len(nums), target))

    def test_subset_vacio_con_target_cero(self):
        nums = []
        target = 0
        self.assertTrue(subset_sum_top_down(nums, len(nums), target))

    def test_subset_vacio_con_target_no_cero(self):
        nums = [3,1]
        target = 5
        self.assertFalse(subset_sum_top_down(nums, len(nums), target))

    def test_con_elementos_repetidos(self):
        nums = [1, 2, 2, 3]
        target = 6
        self.assertTrue(subset_sum_top_down(nums, len(nums), target))

    def test_todos_elementos_iguales(self):
        nums = [5, 5, 5, 5]
        target = 10
        self.assertTrue(subset_sum_top_down(nums, len(nums), target))

if __name__ == '__main__':
    unittest.main()