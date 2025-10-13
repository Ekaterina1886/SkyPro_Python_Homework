import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" Skypro", "Skypro"),
    ("  hello world", "hello world"),
    (" 123abc. ", "123abc. "),
    ("   ", "")
])
def test_trim_positive (input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("w o r l d", "w o r l d")
])
def test_trim_negative (input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Skypro", "S", True),
    ("Banana", "na", True),
    ("Sky Pro", " ", True),
    ("123abc", "2", True)
])
def test_contains_positive (input_str,symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Skypro", "U", False),
    ("", "A", False),
    ("Hello", " ", False),
    ("Python", "p", False)
])
def test_contains_negative (input_str,symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected
    
@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Skypro", "k", "Sypro"),
    ("SkyPro", "Pro", "Sky"),
    ("Banana", "a", "Bnn"),
    ("1First", "1", "First")
])
def test_delete_symbol_positive (input_str,symbol, expected):
    assert string_utils.delete_symbol (input_str, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "X", "SkyPro"),
    ("Hello", "", "Hello"),
    ("", "a", ""),
    ("SkyPro", "s", "SkyPro")
])
def test_delete_symbol_negative (input_str,symbol, expected):
    assert string_utils.delete_symbol (input_str, symbol) == expected
        