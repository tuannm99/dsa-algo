from __future__ import annotations

from .unionfind import Config, UnionFind


class DisjointSet(UnionFind):

    def __init__(self, config: Config) -> None:
        self._parent = list(range(max(0, config.size)))
        self._rank = [0] * len(self._parent)
        self._component_size = [1] * len(self._parent)
        self._components = len(self._parent)

    def _valid(self, value: int) -> bool:
        return 0 <= value < len(self._parent)

    def size(self) -> int:
        return len(self._parent)

    def component_count(self) -> int:
        return self._components

    def find(self, value: int) -> tuple[int, bool]:
        if not self._valid(value):
            return -1, False
        if self._parent[value] != value:
            root, _ = self.find(self._parent[value])
            self._parent[value] = root
        return self._parent[value], True

    def union(self, left: int, right: int) -> bool:
        left_root, left_ok = self.find(left)
        right_root, right_ok = self.find(right)
        if not left_ok or not right_ok or left_root == right_root:
            return False

        if self._rank[left_root] < self._rank[right_root]:
            left_root, right_root = right_root, left_root
        self._parent[right_root] = left_root
        self._component_size[left_root] += self._component_size[right_root]
        if self._rank[left_root] == self._rank[right_root]:
            self._rank[left_root] += 1
        self._components -= 1
        return True

    def connected(self, left: int, right: int) -> bool:
        left_root, left_ok = self.find(left)
        right_root, right_ok = self.find(right)
        return left_ok and right_ok and left_root == right_root

    def component_size(self, value: int) -> tuple[int, bool]:
        root, ok = self.find(value)
        if not ok:
            return 0, False
        return self._component_size[root], True
