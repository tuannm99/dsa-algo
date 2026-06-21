from __future__ import annotations

from typing import Generic, TypeVar, cast

from ..ds_types import KVVisitFunc
from .trie import Config, Trie

V = TypeVar("V")


class SimpleTrie(Generic[V], Trie[V]):

    def __init__(self, config: Config[V] | None = None) -> None:
        self._config = config or Config()
        self._items: dict[str, V] = {}

    def size(self) -> int:
        return len(self._items)

    def is_empty(self) -> bool:
        return not self._items

    def insert(self, key: str, value: V) -> bool:
        self._items[key] = value
        return True

    def get(self, key: str) -> tuple[V, bool]:
        if key not in self._items:
            return cast(V, None), False
        return self._items[key], True

    def contains(self, key: str) -> bool:
        return key in self._items

    def remove(self, key: str) -> tuple[V, bool]:
        if key not in self._items:
            return cast(V, None), False
        return self._items.pop(key), True

    def has_prefix(self, prefix: str) -> bool:
        return any(key.startswith(prefix) for key in self._items)

    def prefix_count(self, prefix: str) -> int:
        return sum(1 for key in self._items if key.startswith(prefix))

    def for_each_prefix(self, prefix: str, visit: KVVisitFunc[str, V]) -> None:
        for key, value in self._items.items():
            if key.startswith(prefix):
                visit(key, value)

    def clear(self) -> None:
        if self._config.free_value is not None:
            for value in self._items.values():
                self._config.free_value(value)
        self._items.clear()
