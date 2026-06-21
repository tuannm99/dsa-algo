from __future__ import annotations

from python.segmenttree import Config, SumSegmentTree


def test_segment_tree_query_and_update() -> None:
    tree = SumSegmentTree(Config(values=[2, 1, 5, 3]))

    assert tree.size() == 4
    assert tree.query(0, 3) == (11, True)
    assert tree.query(1, 2) == (6, True)
    assert tree.update(2, 10) is True
    assert tree.query(1, 2) == (11, True)
    assert tree.query(2, 2) == (10, True)


def test_segment_tree_rejects_invalid_ranges() -> None:
    tree = SumSegmentTree(Config(values=[1, 2]))
    empty = SumSegmentTree(Config(values=[]))

    assert tree.update(-1, 0) is False
    assert tree.update(2, 0) is False
    assert tree.query(1, 0) == (0, False)
    assert tree.query(0, 2) == (0, False)
    assert empty.query(0, 0) == (0, False)
