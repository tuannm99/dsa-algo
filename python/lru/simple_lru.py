from __future__ import annotations

from collections import OrderedDict
from typing import Generic, TypeVar, cast

from ..ds_types import Entry, KVVisitFunc
from .lru import Config, LRU

K = TypeVar("K")
V = TypeVar("V")


class SimpleLRU(Generic[K, V], LRU[K, V]):

    def __init__(self, config: Config[K, V]) -> None:
        self._config = config
        self._capacity = max(0, config.capacity)
        self._items: OrderedDict[K, V] = OrderedDict()

    def size(self) -> int:
        return len(self._items)

    def capacity(self) -> int:
        return self._capacity

    def is_empty(self) -> bool:
        return not self._items

    def put(self, key: K, value: V) -> tuple[K, V, bool, bool]:
        if key in self._items:
            old = self._items[key]
            del self._items[key]
            self._items[key] = value
            return key, old, True, False
        self._items[key] = value
        if self._capacity == 0 or len(self._items) > self._capacity:
            evicted_key, evicted_value = self._items.popitem(last=False)
            return evicted_key, evicted_value, False, True
        return cast(K, None), cast(V, None), False, False

    def get(self, key: K) -> tuple[V, bool]:
        if key not in self._items:
            return cast(V, None), False
        value = self._items.pop(key)
        self._items[key] = value
        return value, True

    def contains(self, key: K) -> bool:
        return key in self._items

    def peek(self, key: K) -> tuple[V, bool]:
        if key not in self._items:
            return cast(V, None), False
        return self._items[key], True

    def remove(self, key: K) -> tuple[K, V, bool]:
        if key not in self._items:
            return cast(K, None), cast(V, None), False
        return key, self._items.pop(key), True

    def resize(self, new_capacity: int) -> tuple[list[Entry[K, V]], bool]:
        self._capacity = max(0, new_capacity)
        evicted: list[Entry[K, V]] = []
        while len(self._items) > self._capacity:
            key, value = self._items.popitem(last=False)
            evicted.append(Entry(key, value))
        return evicted, True

    def clear(self) -> None:
        if self._config.free_key is not None:
            for key in self._items.keys():
                self._config.free_key(key)
        if self._config.free_value is not None:
            for value in self._items.values():
                self._config.free_value(value)
        self._items.clear()

    def for_each(self, visit: KVVisitFunc[K, V]) -> None:
        for key, value in self._items.items():
            visit(key, value)
