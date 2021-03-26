import unittest
from filecmp import cmp
from collections import namedtuple
from time import time
from pathlib import Path


class TestFilecmpCmpCases(unittest.TestCase):
    test_files_base_path = Path(Path.cwd(), "tests", "files")

    def test_filecmp_cmp__boundary_conditions(self):
        """
        Test boundary conditions with:
        - two different empty files.
        - the same file.
        - same file with different encoding.
        - two files with only a newline as difference.
        - a hidden file.
        - two files with only a character as difference.

        :return:
        """
        SubTestCase = namedtuple("SubTestCase", ("f1", "f2", "expected_cmp"))
        sub_tests = (
            SubTestCase(
                f1=self.test_files_base_path.joinpath("empty_file_1.txt"),
                f2=self.test_files_base_path.joinpath("empty_file_2.txt"),
                expected_cmp=True,
            ),
            SubTestCase(
                f1=self.test_files_base_path.joinpath("masters_of_war.txt"),
                f2=self.test_files_base_path.joinpath("masters_of_war.txt"),
                expected_cmp=True,
            ),
            SubTestCase(
                f1=self.test_files_base_path.joinpath("ascii_file.txt"),
                f2=self.test_files_base_path.joinpath("unicode_file.txt"),
                expected_cmp=False,
            ),
            SubTestCase(
                f1=self.test_files_base_path.joinpath("newline_file.txt"),
                f2=self.test_files_base_path.joinpath("no_newline_file.txt"),
                expected_cmp=False,
            ),
            SubTestCase(
                f1=self.test_files_base_path.joinpath(".hidden_file.txt"),
                f2=self.test_files_base_path.joinpath(".hidden_file.txt"),
                expected_cmp=True,
            ),
            SubTestCase(
                f1=self.test_files_base_path.joinpath("emojis.txt"),
                f2=self.test_files_base_path.joinpath("emojis__1_emoji_diff.txt"),
                expected_cmp=False,
            ),
        )
        for num, sub_test in enumerate(sub_tests, start=1):
            with self.subTest(
                msg=f"Test Case {num}: {sub_test.f1}, {sub_test.f2} , {sub_test.expected_cmp}"
            ):
                self.assertEqual(cmp(sub_test.f1, sub_test.f2), sub_test.expected_cmp)

    def test_filecmp_cmp__inverse_relationships(self):
        """ There's really no inverse for cmp. """
        pass

    @staticmethod
    def custom_file_compare(f1_name: str, f2_name: str) -> bool:
        """
        Compare two files by reading them and loading their contents to variables as strings.

        :param f1_name: first file name.
        :param f2_name: second file name.
        :return: True when equal, False otherwise.
        """
        with open(f1_name, encoding="utf-8") as f1:
            f1_content = f1.read()
        with open(f2_name, encoding="utf-8") as f2:
            f2_content = f2.read()
        return f1_content == f2_content

    def test_filecmp_cmp__cross_checking(self):
        """
        Cross-checking tests with custom_file_compare function.

        :return:
        """
        SubTestCase = namedtuple("SubTestCase", ("f1", "f2"))

        sub_tests = (
            SubTestCase(f1=self.test_files_base_path.joinpath("empty_file_1.txt"),
                        f2=self.test_files_base_path.joinpath("empty_file_2.txt")),
            SubTestCase(f1=self.test_files_base_path.joinpath("masters_of_war.txt"),
                        f2=self.test_files_base_path.joinpath("masters_of_war.txt")),
            SubTestCase(f1=self.test_files_base_path.joinpath("ascii_file.txt"),
                        f2=self.test_files_base_path.joinpath("unicode_file.txt")),
            SubTestCase(f1=self.test_files_base_path.joinpath("newline_file.txt"),
                        f2=self.test_files_base_path.joinpath("no_newline_file.txt")),
            SubTestCase(
                f1=self.test_files_base_path.joinpath("emojis.txt"),
                f2=self.test_files_base_path.joinpath("emojis__1_emoji_diff.txt"),
            ),
        )
        for num, sub_test in enumerate(sub_tests, start=1):
            with self.subTest(msg=f"Test Case {num}: {sub_test.f1}, {sub_test.f2}"):
                self.assertEqual(
                    cmp(sub_test.f1, sub_test.f2),
                    self.custom_file_compare(sub_test.f1, sub_test.f2),
                )

    def test_filecmp_cmp__error_conditions(self):
        """
        Test error conditions with:
        - file that does not exist.
        - numbers as filenames.
        - None as filenames.
        - filename inside a tuple.

        :return:
        """
        SubTestCase = namedtuple("SubTestCase", ("f1", "f2", "exc"))

        sub_tests = (
            SubTestCase(f1="", f2="", exc=FileNotFoundError),
            SubTestCase(
                f1=self.test_files_base_path.joinpath("does_not_exist.txt"),
                f2=self.test_files_base_path.joinpath("empty_file_1.txt"),
                exc=FileNotFoundError,
            ),
            SubTestCase(f1=128, f2=256, exc=OSError),
            SubTestCase(f1=None, f2=None, exc=TypeError),
            SubTestCase(
                f1=(self.test_files_base_path.joinpath("empty_file_1.txt"),),
                f2=(self.test_files_base_path.joinpath("empty_file_1.txt"),),
                exc=TypeError,
            ),
        )
        for num, sub_test in enumerate(sub_tests, start=1):
            with self.subTest(
                msg=f"Test Case {num}: {sub_test.f1}, {sub_test.f2}, {sub_test.exc}"
            ):
                with self.assertRaises(sub_test.exc):
                    cmp(sub_test.f1, sub_test.f2)

    def test_filecmp_cmp__performance(self):
        """
        Test performance by executing cmp many times with different files and establishing a maximum execution time.

        :return:
        """
        start = time()
        for f1, f2 in (
            (self.test_files_base_path.joinpath("empty_file_1.txt"),
             self.test_files_base_path.joinpath("empty_file_1.txt")),
            (self.test_files_base_path.joinpath("masters_of_war.txt"),
             self.test_files_base_path.joinpath("masters_of_war.txt")),
            (self.test_files_base_path.joinpath("emojis.txt"),
             self.test_files_base_path.joinpath("emojis__1_emoji_diff.txt")),
            (self.test_files_base_path.joinpath("ascii_file.txt"),
             self.test_files_base_path.joinpath("unicode_file.txt")),
            (self.test_files_base_path.joinpath("newline_file.txt"),
             self.test_files_base_path.joinpath("no_newline_file.txt")),
            (self.test_files_base_path.joinpath(".hidden_file.txt"),
             self.test_files_base_path.joinpath(".hidden_file.txt")),
        ):
            cmp(f1, f2)
        self.assertLessEqual(time() - start, 0.02)
