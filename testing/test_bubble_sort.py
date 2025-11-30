import pytest
from bubble import bubble_sort
from hypothesis import given, strategies as st

@given(st.lists(st.integers()))
def test_bubble(arr):
    assert list(arr) == sorted(arr)
    assert len(list(arr)) == len(arr)
    assert sorted(list(arr)) == sorted(arr)
