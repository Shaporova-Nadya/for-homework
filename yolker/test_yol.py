import pytest
from yol import Yolker

def test_get_random():
    distribution = [("A", 0.5), ("B", 0.5)]
    yolker = Yolker(distribution)
    
    for _ in range(100):
        result = yolker.get_random()
        assert result in ["A", "B"]