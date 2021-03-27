from unittest import TestCase

from lab1.convert_2x import decimal_to_bin, decimal_to_hex


class TestConvert2xCases(TestCase):
    def test_decimal_to_bin__success(self):
        for n in range(0, 1000):
            with self.subTest(msg=f"Test {n}: Number {n}"):
                bin_num = decimal_to_bin(n)
                self.assertEqual(bin_num, bin(n))

    def test_decimal_to_hex__success(self):
        for n in range(0, 1000):
            with self.subTest(msg=f"Test {n}: Number {n}"):
                hex_num = decimal_to_hex(n)
                self.assertEqual(hex_num, hex(n))