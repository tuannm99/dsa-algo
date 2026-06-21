from __future__ import annotations

from functools import cmp_to_key
from typing import Generic, TypeVar, cast

from ..ds_types import KVVisitFunc

K = TypeVar("K")
V = TypeVar("V")


class SortedMap(Generic[K, V]):

    def __init__(self, compare_key, free_key=None, free_value=None) -> None:
        self._compare_key = compare_key
        self._free_key = free_key
        self._free_value = free_value
        self._items: list[tuple[K, V]] = []

    def _index(self, key: K) -> int:
        for index, (item_key, _) in enumerate(self._items):
            if self._compare_key(item_key, key) == 0:
                return index
        return -1

    def _sort(self) -> None:
        self._items.sort(
            key=cmp_to_key(lambda a, b: self._compare_key(a[0], b[0])))

    def size(self) -> int:
        return len(self._items)

    def is_empty(self) -> bool:
        return not self._items

    def insert(self, key: K, value: V) -> bool:
        index = self._index(key)
        if index >= 0:
            self._items[index] = (self._items[index][0], value)
        else:
            self._items.append((key, value))
            self._sort()
        return True

    def get(self, key: K) -> tuple[V, bool]:
        index = self._index(key)
        if index < 0:
            return cast(V, None), False
        return self._items[index][1], True

    def contains(self, key: K) -> bool:
        return self._index(key) >= 0

    def remove(self, key: K) -> tuple[K, V, bool]:
        index = self._index(key)
        if index < 0:
            return cast(K, None), cast(V, None), False
        item_key, value = self._items.pop(index)
        return item_key, value, True

    def min_key(self) -> tuple[K, bool]:
        if not self._items:
            return cast(K, None), False
        return self._items[0][0], True

    def max_key(self) -> tuple[K, bool]:
        if not self._items:
            return cast(K, None), False
        return self._items[-1][0], True

    def clear(self) -> None:
        if self._free_key is not None:
            for key, _ in self._items:
                self._free_key(key)
        if self._free_value is not None:
            for _, value in self._items:
                self._free_value(value)
        self._items.clear()

    def traverse(self, visit: KVVisitFunc[K, V]) -> None:
        for key, value in self._items:
            visit(key, value)
