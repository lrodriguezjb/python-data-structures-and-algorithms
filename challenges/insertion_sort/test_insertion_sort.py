from insertion_sort import insertion_sort
import pytest

def test_sorted_array_returns_same_sorted_array():
    sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert insertion_sort(sorted_list) == sorted_list


def test_backward_sorted_array_returns_sorted_array():
    sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    backward_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert insertion_sort(backward_list) == sorted_list


def test_mixed_array_returns_sorted_array():
    sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    mixed_list = [7, 5, 2, 4, 3, 8, 9, 10, 1, 6]
    assert insertion_sort(mixed_list) == sorted_list


def test_mixed_string_array_returns_sorted_array():
    sorted_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    mixed_list = ['G', 'C', 'A', 'B', 'F', 'E', 'D']
    assert insertion_sort(mixed_list) == sorted_list


def test_empty_array():
    assert insertion_sort([]) == []


def test_single_element_array():
    assert insertion_sort([1]) == [1]