from __future__ import annotations

from .fenwick import Config, FenwickTree


class SumFenwickTree(FenwickTree):

    def __init__(self, config: Config) -> None:
        self._size = max(0, config.size)
        self._tree = [0] * (self._size + 1)

    @classmethod
    def from_values(cls, values: list[int]) -> "SumFenwickTree":
        tree = cls(Config(len(values)))
        for index, value in enumerate(values):
            tree.add(index, value)
        return tree

    def _valid_index(self, index: int) -> bool:
        return 0 <= index < self._size

    def size(self) -> int:
        return self._size

    def add(self, index: int, delta: int) -> bool:
        if not self._valid_index(index):
            return False
        cursor = index + 1
        while cursor <= self._size:
            self._tree[cursor] += delta
            cursor += cursor & -cursor
        return True

    def prefix_sum(self, index: int) -> tuple[int, bool]:
        if not self._valid_index(index):
            return 0, False
        total = 0
        cursor = index + 1
        while cursor > 0:
            total += self._tree[cursor]
            cursor -= cursor & -cursor
        return total, True

    def range_sum(self, left: int, right: int) -> tuple[int, bool]:
        if not self._valid_index(left) or not self._valid_index(right):
            return 0, False
        if left > right:
            return 0, False
        right_sum, _ = self.prefix_sum(right)
        if left == 0:
            return right_sum, True
        left_sum, _ = self.prefix_sum(left - 1)
        return right_sum - left_sum, True

    def get(self, index: int) -> tuple[int, bool]:
        return self.range_sum(index, index)
