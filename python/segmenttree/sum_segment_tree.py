from __future__ import annotations

from .segmenttree import Config, SegmentTree


class SumSegmentTree(SegmentTree):

    def __init__(self, config: Config) -> None:
        self._size = len(config.values)
        self._tree = [0] * (4 * max(1, self._size))
        if self._size > 0:
            self._build(1, 0, self._size - 1, config.values)

    def _build(self, node: int, left: int, right: int,
               values: list[int]) -> None:
        if left == right:
            self._tree[node] = values[left]
            return
        mid = left + (right - left) // 2
        self._build(node * 2, left, mid, values)
        self._build(node * 2 + 1, mid + 1, right, values)
        self._tree[node] = self._tree[node * 2] + self._tree[node * 2 + 1]

    def size(self) -> int:
        return self._size

    def update(self, index: int, value: int) -> bool:
        if not 0 <= index < self._size:
            return False
        self._update(1, 0, self._size - 1, index, value)
        return True

    def _update(self, node: int, left: int, right: int, index: int,
                value: int) -> None:
        if left == right:
            self._tree[node] = value
            return
        mid = left + (right - left) // 2
        if index <= mid:
            self._update(node * 2, left, mid, index, value)
        else:
            self._update(node * 2 + 1, mid + 1, right, index, value)
        self._tree[node] = self._tree[node * 2] + self._tree[node * 2 + 1]

    def query(self, left: int, right: int) -> tuple[int, bool]:
        if not 0 <= left <= right < self._size:
            return 0, False
        return self._query(1, 0, self._size - 1, left, right), True

    def _query(self, node: int, left: int, right: int, query_left: int,
               query_right: int) -> int:
        if query_left <= left and right <= query_right:
            return self._tree[node]
        if right < query_left or query_right < left:
            return 0
        mid = left + (right - left) // 2
        return self._query(node * 2, left, mid, query_left,
                           query_right) + self._query(
                               node * 2 + 1, mid + 1, right, query_left,
                               query_right)
