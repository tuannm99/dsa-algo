from __future__ import annotations

from typing import Generic, TypeVar, cast

from ..ds_types import VisitFunc
from .hashset import Config, HashSet

T = TypeVar("T")


class SimpleHashSet(Generic[T], HashSet[T]):

    def __init__(self, config: Config[T]) -> None:
        self._config = config
        self._items: list[T] = []

    def _index(self, value: T) -> int:
        for index, item in enumerate(self._items):
            if self._config.compare_value(item, value) == 0:
                return index
        return -1

    def size(self) -> int:
        return len(self._items)

    def is_empty(self) -> bool:
        return not self._items

    def add(self, value: T) -> bool:
        if self._index(value) < 0:
            self._items.append(value)
        return True

    def contains(self, value: T) -> bool:
        return self._index(value) >= 0

    def remove(self, value: T) -> tuple[T, bool]:
        index = self._index(value)
        if index < 0:
            return cast(T, None), False
        return self._items.pop(index), True

    def clear(self) -> None:
        if self._config.free_value is not None:
            for item in self._items:
                self._config.free_value(item)
        self._items.clear()

    def for_each(self, visit: VisitFunc[T]) -> None:
        for item in self._items:
            visit(item)
