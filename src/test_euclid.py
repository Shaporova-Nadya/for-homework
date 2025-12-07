import pytest

from euclid import gcd

def test_gcd():
    g, x, y = gcd(48, 18)
    assert g == 6
    assert 48 * x + 18 * y == g

def test_gcd_zero():
    g, x, y = gcd(0, 5)
    assert g == 5
    assert 0 * x + 5 * y == g
