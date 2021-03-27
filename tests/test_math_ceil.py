from collections import namedtuple
import unittest
from math import ceil, floor, inf
from time import time


class TestMathCeilCases(unittest.TestCase):
    """Test cases for math ceil function."""

    def test_math_ceil__boundary_conditions(self):
        """
        Test boundary conditions.

        - 0
        - almost 0 that should lead to 1.
        - almost 1 that should lead to 1.
        - almost -1 that should lead to 0.
        - almost 0 (from left) that should lead to 0.
        """
        SubTestCase = namedtuple("SubTestCase", ("ceil_arg", "expected"))

        sub_tests = (
            SubTestCase(ceil_arg=0, expected=0),
            SubTestCase(ceil_arg=0.00000000000000000001, expected=1),
            SubTestCase(ceil_arg=0.99999999999999999999, expected=1),
            SubTestCase(ceil_arg=-0.9999999999999999, expected=0),
            SubTestCase(ceil_arg=-0.00000000000000000001, expected=0),
        )
        for num, sub_test in enumerate(sub_tests, start=1):
            with self.subTest(
                msg=f"Test Case {num}: {sub_test.ceil_arg}, {sub_test.expected}"
            ):
                self.assertEqual(ceil(sub_test.ceil_arg), sub_test.expected)

    def test_math_ceil__inverse_relationships(self):
        """Inverse relationship tests with floor()."""
        SubTestCase = namedtuple("SubTestCase", ("ceil_arg", "floor_arg"))

        sub_tests = (
            SubTestCase(ceil_arg=0.5, floor_arg=1.5),
            SubTestCase(ceil_arg=127.1, floor_arg=128.9),
            SubTestCase(ceil_arg=256.0000000000001, floor_arg=257.9999999999999),
            SubTestCase(ceil_arg=-128.9999999999999, floor_arg=-127.0000000000001),
            SubTestCase(ceil_arg=-65535.15, floor_arg=-65534.99),
        )
        for num, sub_test in enumerate(sub_tests, start=1):
            with self.subTest(
                msg=f"Test Case {num}: {sub_test.ceil_arg}, {sub_test.floor_arg}"
            ):
                self.assertEqual(ceil(sub_test.ceil_arg), floor(sub_test.floor_arg))

    def test_math_ceil__cross_checking(self):
        """Cross-checking tests with round."""
        SubTestCase = namedtuple("SubTestCase", ("ceil_arg", "round_arg"))

        sub_tests = (
            SubTestCase(ceil_arg=0.5, round_arg=0.51),
            SubTestCase(ceil_arg=127.1, round_arg=127.6),
            SubTestCase(ceil_arg=256.0000000000001, round_arg=256.50999999999999),
            SubTestCase(ceil_arg=-128.9999999999999, round_arg=-127.50999999999999),
            SubTestCase(ceil_arg=-65535.15, round_arg=-65534.99),
        )
        for num, sub_test in enumerate(sub_tests, start=1):
            with self.subTest(
                msg=f"Test Case {num}: {sub_test.ceil_arg}, {sub_test.round_arg}"
            ):
                self.assertEqual(ceil(sub_test.ceil_arg), round(sub_test.round_arg))

    def test_math_ceil__error_conditions(self):
        """
        Test error conditions.

        - inf/-inf number.
        - numeric string.
        - tuple of integers.
        - None.
        """
        SubTestCase = namedtuple("SubTestCase", ("ceil_arg", "exc"))

        sub_tests = (
            SubTestCase(ceil_arg=inf, exc=OverflowError),
            SubTestCase(ceil_arg=-inf, exc=OverflowError),
            SubTestCase(ceil_arg="0.5", exc=TypeError),
            SubTestCase(ceil_arg=(1.15, 2.14), exc=TypeError),
            SubTestCase(ceil_arg=None, exc=TypeError),
        )
        for num, sub_test in enumerate(sub_tests, start=1):
            with self.subTest(
                msg=f"Test Case {num}: {sub_test.ceil_arg}, {sub_test.exc.__name__}"
            ):
                with self.assertRaises(sub_test.exc):
                    ceil(sub_test.ceil_arg)

    def test_math_ceil__performance(self):
        """Test performance by executing ceil() many times and requiring a maximum execution time."""
        start = time()
        for arg in (
            0,
            0.00000000000000000001,
            0.99999999999999999999,
            -0.9999999999999999,
            -0.00000000000000000001,
        ):
            ceil(arg)
        self.assertLessEqual(time() - start, 5e-6)
