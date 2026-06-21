from __future__ import annotations

from typing import Generic, TypeVar

from ...ds_types import KVVisitFunc
from ..sorted_map import SortedMap
from .btree import BTree, Config

K = TypeVar("K")
V = TypeVar("V")


class SimpleBTree(Generic[K, V], BTree[K, V]):

    def __init__(self, config: Config[K, V]) -> None:
        self._config = config
        self._map: SortedMap[K, V] = SortedMap(
            config.compare_key, config.free_key, config.free_value)

    def size(self) -> int:
        return self._map.size()

    def is_empty(self) -> bool:
        return self._map.is_empty()

    def min_degree(self) -> int:
        return self._config.min_degree

    def insert(self, key: K, value: V) -> bool:
        return self._map.insert(key, value)

    def get(self, key: K) -> tuple[V, bool]:
        return self._map.get(key)

    def contains(self, key: K) -> bool:
        return self._map.contains(key)

    def remove(self, key: K) -> tuple[K, V, bool]:
        return self._map.remove(key)

    def min_key(self) -> tuple[K, bool]:
        return self._map.min_key()

    def max_key(self) -> tuple[K, bool]:
        return self._map.max_key()

    def clear(self) -> None:
        self._map.clear()

    def traverse(self, visit: KVVisitFunc[K, V]) -> None:
        self._map.traverse(visit)
