import pytest
from code_challenges.insertion_sort import insertion_sort


def test_insertion_sort_exists():
    assert insertion_sort


def test_insertion_sort():
    num_list = [8, 4, 23, 42, 16]
    insertion_sort(num_list)
    expected = [4, 8, 16, 23, 42]
    assert num_list == expected



