from unittest import TestCase
from unittest.mock import patch, MagicMock
import sys

from ddt import ddt, file_data, unpack

from lab1.find_words import find_words, FILE_NAME


@ddt
class TestFindWordCases(TestCase):
    """Test cases for find words function."""

    @patch.object(sys, "exit")
    def test_find_words__no_words_provided(self, mock_sys_exit):
        """Test sys.exit arguments when no word list is provided."""
        mock_sys_exit.side_effect = Exception()
        with self.assertRaises(Exception):
            find_words(words=None)
            mock_sys_exit.assert_called_once_with("No words provided")

    @patch("builtins.open")
    @patch.object(sys, "exit")
    def test_find_words__file_does_not_exist(self, mock_sys_exit, mock_open):
        """Test sys.exit arguments when file does not exist."""
        mock_sys_exit.side_effect = Exception()
        mock_open.side_effect = IOError()
        with self.assertRaises(Exception):
            find_words(words=["word"])
            mock_sys_exit.assert_called_once_with("File does not exist")

    @patch("builtins.open")
    @patch("builtins.print")
    @unpack
    @file_data("test_find_words_data.yaml")
    def test_find_words__word_list(
            self, mock_print, mock_open,
            words: list, lines: list, results: str
    ):
        """Tests for find_words() using ddt."""
        mock_file = MagicMock()
        mock_file.__iter__.return_value = lines
        mock_open.return_value = mock_file

        find_words(words=words)
        mock_open.assert_called_with(FILE_NAME, "r", encoding="utf8")
        mock_open.return_value.close.assert_called()
        mock_print.assert_called_with(results)