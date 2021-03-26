import unittest

from lab2.profit import profit


class TestProfitTestCases(unittest.TestCase):
    def test_profit__success(self):
        test_cases = (
            (
                {
                    "cost_price": 32.67,
                    "sell_price": 45.00,
                    "inventory": 1200
                }, 14796
            ),
            (
                {
                    "cost_price": 225.89,
                    "sell_price": 550.00,
                    "inventory": 100
                }, 32411
            ),
            (
                {
                    "cost_price": 2.77,
                    "sell_price": 7.95,
                    "inventory": 8500
                }, 44030
            ),
            (
                {
                    "cost_price": 1.00,
                    "sell_price": 0.50,
                    "inventory": 1000
                }, -500
            ),
            (
                {
                    "cost_price": 100.00,
                    "sell_price": 99.00,
                    "inventory": 2
                }, -2
            ),
            (
                {
                    "cost_price": 1273812.00,
                    "sell_price": 812893718237.00,
                    "inventory": 0
                }, 0
            ),
            (
                {
                    "cost_price": 0.00,
                    "sell_price": 15.32,
                    "inventory": 8500
                }, 130220
            ),
            (
                {
                    "cost_price": 1231212.00,
                    "sell_price": 0.00,
                    "inventory": 13
                }, -16005756
            ),
            (
                {
                    "cost_price": -14.15,
                    "sell_price": 15.00,
                    "inventory": 1121
                }, None
            ),
            (
                {
                    "cost_price": 0.15,
                    "sell_price": 0.10,
                    "inventory": -15
                }, None
            )
        )
        for num, (args, res) in enumerate(test_cases, start=1):
            with self.subTest(msg=f"Test {num}: {args} - {res}"):
                profit_res = profit(args)
                self.assertEqual(profit_res, res)