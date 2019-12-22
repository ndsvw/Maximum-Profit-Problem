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


if __name__ == "__main__":
    unittest.main()
