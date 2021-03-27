from unittest import TestCase
from unittest.mock import call, patch
import random

from ddt import ddt, file_data, unpack

from lab1.find_number import find_number


def mock_input_generator(return_values: tuple) -> str:
    """Mock input function returning next item from return_values in each execution."""
    yield from return_values


@ddt
@patch("builtins.input")
@patch("builtins.print")
@patch("builtins.open")
@patch.object(random, "randint")
class TestFindNumberCases(TestCase):
    """Test cases for find numbers function."""

    @file_data("test_find_number_data.json")
    @unpack
    def test_find_number(
            self, mock_random_randint, mock_open, mock_print, mock_input,
            randint: int, user_inputs: list, print_calls: list
    ):
        """Tests for find_number() using ddt."""
        mock_random_randint.return_value = randint
        mock_input.side_effect = mock_input_generator(tuple(map(lambda ui: str(ui), user_inputs)))
        calls = [call(pc) for pc in print_calls]
        calls.append(call(print_calls[-1], file=mock_open.return_value))

        find_number()
        self.assertListEqual(calls, mock_print.call_args_list)
        mock_open.assert_called_with("find_number_guess.txt", mode="a")
        mock_open.return_value.close.assert_called()