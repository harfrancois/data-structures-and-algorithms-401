import pytest
from code_challenges.merge_sort import merge_sort


def test_merge_sort_exists():
    assert merge_sort


def test_num_sort():
    num_list = [8, 4, 23, 42, 16, 15]
    actual = merge_sort(num_list)
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected
