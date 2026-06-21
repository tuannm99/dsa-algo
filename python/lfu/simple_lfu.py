from __future__ import annotations

from collections import OrderedDict
from typing import Generic, TypeVar, cast

from ..ds_types import Entry, KVVisitFunc
from .lfu import Config, LFU

K = TypeVar("K")
V = TypeVar("V")


class SimpleLFU(Generic[K, V], LFU[K, V]):

    def __init__(self, config: Config[K, V]) -> None:
        self._config = config
        self._capacity = max(0, config.capacity)
        self._items: OrderedDict[K, tuple[V, int]] = OrderedDict()

    def size(self) -> int:
        return len(self._items)

    def capacity(self) -> int:
        return self._capacity

    def is_empty(self) -> bool:
        return not self._items

    def _evict_key(self) -> K:
        return min(self._items.keys(), key=lambda key: self._items[key][1])

    def put(self, key: K, value: V) -> tuple[K, V, bool, bool]:
        if key in self._items:
            old_value, freq = self._items[key]
            self._items[key] = (value, freq)
            return key, old_value, True, False
        if self._capacity == 0:
            return key, value, False, True
        self._items[key] = (value, 1)
        if len(self._items) > self._capacity:
            evicted_key = self._evict_key()
            evicted_value, _ = self._items.pop(evicted_key)
            return evicted_key, evicted_value, False, True
        return cast(K, None), cast(V, None), False, False

    def get(self, key: K) -> tuple[V, bool]:
        if key not in self._items:
            return cast(V, None), False
        value, freq = self._items[key]
        self._items[key] = (value, freq + 1)
        return value, True

    def contains(self, key: K) -> bool:
        return key in self._items

    def peek(self, key: K) -> tuple[V, bool]:
        if key not in self._items:
            return cast(V, None), False
        return self._items[key][0], True

    def remove(self, key: K) -> tuple[K, V, bool]:
        if key not in self._items:
            return cast(K, None), cast(V, None), False
        value, _ = self._items.pop(key)
        return key, value, True

    def frequency(self, key: K) -> tuple[int, bool]:
        if key not in self._items:
            return 0, False
        return self._items[key][1], True

    def touch(self, key: K) -> bool:
        if key not in self._items:
            return False
        value, freq = self._items[key]
        self._items[key] = (value, freq + 1)
        return True

    def resize(self, new_capacity: int) -> tuple[list[Entry[K, V]], bool]:
        self._capacity = max(0, new_capacity)
        evicted: list[Entry[K, V]] = []
        while len(self._items) > self._capacity:
            key = self._evict_key()
            value, _ = self._items.pop(key)
            evicted.append(Entry(key, value))
        return evicted, True

    def clear(self) -> None:
        if self._config.free_key is not None:
            for key in self._items.keys():
                self._config.free_key(key)
        if self._config.free_value is not None:
            for value, _ in self._items.values():
                self._config.free_value(value)
        self._items.clear()

    def for_each(self, visit: KVVisitFunc[K, V]) -> None:
        for key, (value, _) in self._items.items():
            visit(key, value)
