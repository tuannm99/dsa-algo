from __future__ import annotations

from typing import Generic, TypeVar, cast

from ..ds_types import VisitFunc
from .heap import Config, Heap

T = TypeVar("T")


class SimpleHeap(Generic[T], Heap[T]):

    def __init__(self, config: Config[T]) -> None:
        self._config = config
        self._items: list[T] = []

    def size(self) -> int:
        return len(self._items)

    def is_empty(self) -> bool:
        return not self._items

    def _top_index(self) -> int:
        best = 0
        for index in range(1, len(self._items)):
            if self._config.compare(self._items[index], self._items[best]) < 0:
                best = index
        return best

    def push(self, value: T) -> bool:
        self._items.append(value)
        return True

    def pop(self) -> tuple[T, bool]:
        if not self._items:
            return cast(T, None), False
        return self._items.pop(self._top_index()), True

    def peek(self) -> tuple[T, bool]:
        if not self._items:
            return cast(T, None), False
        return self._items[self._top_index()], True

    def replace_top(self, value: T) -> tuple[T, bool]:
        if not self._items:
            return cast(T, None), False
        index = self._top_index()
        old = self._items[index]
        self._items[index] = value
        return old, True

    def clear(self) -> None:
        if self._config.free_value is not None:
            for item in self._items:
                self._config.free_value(item)
        self._items.clear()

    def for_each(self, visit: VisitFunc[T]) -> None:
        for item in self._items:
            visit(item)
