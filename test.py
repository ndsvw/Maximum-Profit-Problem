import unittest
from maximum_profit_dp import *


class MaxProfitTest(unittest.TestCase):

    def assert_limited_methods_result_equals_n(self, G, k, n):
        self.assertEqual(maximum_profit_limited_dp(G, k), n)
        self.assertEqual(maximum_profit_limited_spaceoptimized1_dp(G, k), n)
        self.assertEqual(maximum_profit_limited_spaceoptimized2_dp(G, k), n)

    def test_empty(self):
        G = []
        self.assertEqual(maximum_profit_unlimited_dp(G), 0)
        self.assert_limited_methods_result_equals_n(G, 0, 0)
        self.assert_limited_methods_result_equals_n(G, 10, 0)

    def test_1_element(self):
        G = [1]
        self.assertEqual(maximum_profit_unlimited_dp(G), 0)
        self.assert_limited_methods_result_equals_n(G, 1, 0)
        self.assert_limited_methods_result_equals_n(G, 10, 0)

    def test_2_elements(self):
        G = [1, 9]
        self.assertEqual(maximum_profit_unlimited_dp(G), 8)
        self.assert_limited_methods_result_equals_n(G, 1, 8)
        self.assert_limited_methods_result_equals_n(G, 10, 8)

    def test_k_equals_zero(self):
        G1 = [1, 8]
        G2 = [1, 8, 3, 8]
        G3 = [8, 10, 11, 4, 3]
        self.assert_limited_methods_result_equals_n(G1, 0, 0)
        self.assert_limited_methods_result_equals_n(G2, 0, 0)
        self.assert_limited_methods_result_equals_n(G3, 0, 0)

    def test_large_k(self):
        G1 = [1, 8]
        G2 = [1, 8, 3, 8]
        G3 = [8, 10, 11, 4, 3]
        self.assert_limited_methods_result_equals_n(G1, 100, 7)
        self.assert_limited_methods_result_equals_n(G2, 100, 12)
        self.assert_limited_methods_result_equals_n(G3, 100, 3)

    def test_decreasing(self):
        G1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        G2 = [-10, -11, -12, -110, -111, -112]
        self.assert_limited_methods_result_equals_n(G1, 10, 0)
        self.assert_limited_methods_result_equals_n(G2, 100, 0)

    def test_negative_numbers(self):
        G1 = [-9, 9]
        G2 = [-9, -10, -11]
        G3 = [-10, 10, -10, 10]
        self.assertEqual(maximum_profit_unlimited_dp(G1), 18)
        self.assertEqual(maximum_profit_unlimited_dp(G2), 0)
        self.assertEqual(maximum_profit_unlimited_dp(G3), 40)
        self.assert_limited_methods_result_equals_n(G1, 1, 18)
        self.assert_limited_methods_result_equals_n(G2, 1, 0)
        self.assert_limited_methods_result_equals_n(G3, 1, 20)
        self.assert_limited_methods_result_equals_n(G3, 2, 40)

    def test_example_1(self):
        G = [10, 22, 5, 75, 65, 80]
        self.assertEqual(maximum_profit_unlimited_dp(G), 97)
        self.assert_limited_methods_result_equals_n(G, 0, 0)
        self.assert_limited_methods_result_equals_n(G, 1, 75)
        self.assert_limited_methods_result_equals_n(G, 2, 87)
        self.assert_limited_methods_result_equals_n(G, 3, 97)

    def test_example_2(self):
        G = [20, 580, 420, 900]
        self.assertEqual(maximum_profit_unlimited_dp(G), 1040)
        self.assert_limited_methods_result_equals_n(G, 0, 0)
        self.assert_limited_methods_result_equals_n(G, 1, 880)
        self.assert_limited_methods_result_equals_n(G, 2, 1040)


if __name__ == "__main__":
    unittest.main()
