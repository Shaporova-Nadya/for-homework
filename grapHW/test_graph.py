import pytest
from graph import Graph

def test_simple_graph():
    vertices = [1, 2, 3, 4]
    edges = [(1, 2), (2, 3), (3, 4)]
    graph = Graph(vertices, edges)
    
    expected_order = [1, 2, 3, 4]
    assert list(graph) == expected_order

def test_complex_graph():
    vertices = [1, 2, 3, 4, 5, 6]
    edges = [(1, 2), (1, 3), (2, 4), (3, 4), (5, 6)]
    graph = Graph(vertices, edges)

    expected_order = [1, 2, 3, 4, 5, 6]
    assert list(graph) == expected_order

def test_disconnected():
    vertices = [1, 2, 3, 4]
    edges = [(1, 2), (3, 4)]
    graph = Graph(vertices, edges)

    expected_order = [1, 2, 3, 4]
    assert list(graph) == expected_order

def test_empty():
    vertices = []
    edges = []
    graph = Graph(vertices, edges)

    expected_order = []
    assert list(graph) == expected_order