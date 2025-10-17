import pytest
from sorting import heap_sort

def test_heap_sort():
    assert heap_sort([3, 9, 66, 10, 4]) == [3, 4, 9, 10, 66]

def test_heap_sort_empty():
    assert heap_sort([]) == []

def test_heap_sort_sorted():
    assert heap_sort([1, 2, 3, 4]) == [1, 2, 3, 4]

def test_heap_sort_bignumbers():
    assert heap_sort([333, 100, 78343775, 9889, 99]) == [99, 100, 333, 9889, 78343775]
