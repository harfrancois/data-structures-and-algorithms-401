import pytest

from code_challenges.roman_numerals import roman_to_numerical_value, convert_character


def test_convert_exists():
    assert roman_to_numerical_value


def test_convert_exists():
    assert convert_character


def test_simple_convert():
    roman = 'MCM'
    actual = roman_to_numerical_value(roman)
    expected = 1900
    assert actual == expected

def test_birth_year_convert():
    roman = 'MCMLXXXVII'
    actual = roman_to_numerical_value(roman)
    expected = 1987
    assert actual == expected

def test_random():
    roman = 'CIVIC'
    actual = roman_to_numerical_value(roman)
    expected = 203
    assert actual == expected


