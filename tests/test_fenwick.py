from __future__ import annotations

from python.fenwick import Config, SumFenwickTree


def test_fenwick_prefix_range_and_point_queries() -> None:
    fenwick = SumFenwickTree.from_values([1, 2, 3, 4])

    assert fenwick.size() == 4
    assert fenwick.prefix_sum(0) == (1, True)
    assert fenwick.prefix_sum(3) == (10, True)
    assert fenwick.range_sum(1, 2) == (5, True)
    assert fenwick.get(2) == (3, True)

    assert fenwick.add(1, 5) is True
    assert fenwick.get(1) == (7, True)
    assert fenwick.range_sum(0, 3) == (15, True)


def test_fenwick_rejects_invalid_ranges() -> None:
    fenwick = SumFenwickTree(Config(size=2))

    assert fenwick.add(2, 1) is False
    assert fenwick.prefix_sum(-1) == (0, False)
    assert fenwick.range_sum(1, 0) == (0, False)
    assert fenwick.range_sum(0, 2) == (0, False)
