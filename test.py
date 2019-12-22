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


if __name__ == "__main__":
    unittest.main()
