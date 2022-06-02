# pylint: disable=no-self-use, wildcard-import, unused-wildcard-import

import pytest
from mock import mock_open, patch

from line_length_analysis.line_length_analysis import *


@pytest.fixture
def empty_file():
    mocked_etc_release_data = mock_open(read_data="")
    patch("builtins.open", mocked_etc_release_data)


@pytest.fixture
def single_line_file():
    mocked_etc_release_data = mock_open(read_data="a\r")
    patch("builtins.open", mocked_etc_release_data)


class TestGetLineLengthFrequency:
    def test_should_return_empty_dict_when_input_is_empty_list(self):
        input_list = []
        expected = {}
        result = line_length_frequency(input_list)
        assert result == expected

    def test_1_element_1_character_input_list(self):
        input_list = ["a"]
        expected = {1: 1}
        result = line_length_frequency(input_list)
        assert result == expected

    def test_2_element_1_character_input_list(self):
        input_list = ["a", "b"]
        expected = {1: 2}
        result = line_length_frequency(input_list)
        assert result == expected

    def test_1_element_2_character_input_list(self):
        input_list = ["ab"]
        expected = {2: 1}
        result = line_length_frequency(input_list)
        assert result == expected

    def test_2_element_1_and_2_character_input_list(self):
        input_list = ["a", "bc"]
        expected = {1: 1, 2: 1}
        result = line_length_frequency(input_list)
        assert result == expected

    def test_should_return_empty_dict_when_input_contains_a_non_string_element(
        self,
    ):
        input_list = [1]
        expected = {}
        result = line_length_frequency(input_list)
        assert result == expected


class TestGetFileLines:
    def test_should_return_empty_list_when_open_throws_filenotfounderror(self):
        file_name = "file_does_not_exist.txt"
        expected = []
        result = file_lines(file_name)
        assert result == expected

    @pytest.mark.skip("don't yet know how to test this")
    def test_should_return_1_element_list_when_file_has_1_line(self):
        file_name = "single_line_file.txt"
        expected = ["a"]
        result = file_lines(file_name)
        assert result == expected
