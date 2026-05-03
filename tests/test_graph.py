from __future__ import annotations

from python.graph.graph import Config, Kind


def test_directed_graph_vertex_and_edge_lifecycle(graph_factory) -> None:
    graph = graph_factory(
        Config(
            kind=Kind.DIRECTED,
            hash_vertex_id=hash,
            compare_vertex_id=lambda a, b: 0 if a == b else 1,
        ))

    assert graph.is_directed() is True
    assert graph.get_vertex("missing") == (None, False)
    assert graph.remove_vertex("missing") == (None, None, False)
    assert graph.get_edge("a", "b") == (None, False)
    assert graph.has_edge("a", "b") is False
    assert graph.remove_edge("a", "b") == (None, False)
    assert graph.add_vertex("a", 1) is True
    assert graph.add_vertex("b", 2) is True
    assert graph.add_vertex("a", 99) is False
    assert graph.vertex_count() == 2
    assert graph.set_vertex("a", 10) == (1, True)
    assert graph.get_vertex("a") == (10, True)
    assert graph.set_vertex("missing", 0) == (None, False)

    assert graph.add_edge("a", "b", 5) is True
    assert graph.add_edge("a", "missing", 5) is False
    assert graph.has_edge("a", "b") is True
    assert graph.get_edge("a", "b") == (5, True)
    assert graph.out_degree("a") == 1
    assert graph.in_degree("b") == 1
    assert graph.remove_edge("a", "b") == (5, True)
    assert graph.remove_edge("a", "b") == (None, False)
    assert graph.remove_vertex("a") == ("a", 10, True)


def test_undirected_graph_iteration(graph_factory) -> None:
    graph = graph_factory(
        Config(
            kind=Kind.UNDIRECTED,
            hash_vertex_id=hash,
            compare_vertex_id=lambda a, b: 0 if a == b else 1,
        ))
    vertices: dict[str, int] = {}
    neighbors: dict[str, int] = {}

    assert graph.add_vertex("x", 1) is True
    assert graph.add_vertex("y", 2) is True
    assert graph.add_edge("x", "y", 7) is True

    graph.for_each_vertex(lambda key, value: vertices.__setitem__(key, value))
    graph.for_each_neighbor(
        "x", lambda key, value: neighbors.__setitem__(key, value))
    assert vertices == {"x": 1, "y": 2}
    assert neighbors == {"y": 7}
    assert graph.out_degree("x") == 1
    assert graph.in_degree("x") == 1
