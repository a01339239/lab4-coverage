from lab2.converters import str_to_int, int_to_str
import unittest


class TestConvertersCases(unittest.TestCase):

    def test_str_to_int___success(self):
        for num, test_case in enumerate(
                ["1", "95", "-4568", "0", "-5465465465415156468515""17", "019", "1322", "15300", "-1003250"], start=1):
            with self.subTest(msg=f"Test {num}: {test_case}"):
                str_to_int_res = str_to_int(test_case)
                self.assertEqual(str_to_int_res, int(test_case))

    def test_str_to_int___failed(self):
        for num, test_case in enumerate(["a", "0.15", "0.95", "1j", "", "-"], start=1):
            with self.subTest(msg=f"Test {num}: {test_case}"):
                str_to_int_res = str_to_int(test_case)
                self.assertIsNone(str_to_int_res)

    def test_int_to_str__success(self):
        for num, test_case in enumerate([1, 12, 0, -1321231231, 321, -12132,
                          1516, -2, 2036, 29560, -1500132], start=1):
            with self.subTest(msg=f"Test {num}: {test_case}"):
                int_to_str_res = int_to_str(test_case)
                self.assertEqual(int_to_str_res, str(test_case))