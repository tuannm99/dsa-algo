from __future__ import annotations

from python.unionfind import Config, DisjointSet


def test_union_find_connectivity_and_component_sizes() -> None:
    union_find = DisjointSet(Config(size=5))

    assert union_find.size() == 5
    assert union_find.component_count() == 5
    assert union_find.connected(0, 1) is False
    assert union_find.union(0, 1) is True
    assert union_find.union(1, 2) is True
    assert union_find.union(0, 2) is False
    assert union_find.connected(0, 2) is True
    assert union_find.component_count() == 3
    assert union_find.component_size(0) == (3, True)
    assert union_find.component_size(4) == (1, True)


def test_union_find_rejects_invalid_indexes() -> None:
    union_find = DisjointSet(Config(size=2))

    assert union_find.find(-1) == (-1, False)
    assert union_find.find(2) == (-1, False)
    assert union_find.union(0, 2) is False
    assert union_find.connected(0, 2) is False
    assert union_find.component_size(2) == (0, False)
