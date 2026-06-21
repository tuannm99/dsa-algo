from __future__ import annotations

from typing import Generic, TypeVar, cast

from ..ds_types import VisitFunc
from .queue import Config, Queue

T = TypeVar("T")


class ListQueue(Generic[T], Queue[T]):

    def __init__(self, config: Config[T] | None = None) -> None:
        self._config = config or Config()
        self._items: list[T] = []

    def size(self) -> int:
        return len(self._items)

    def is_empty(self) -> bool:
        return not self._items

    def enqueue(self, value: T) -> bool:
        self._items.append(value)
        return True

    def dequeue(self) -> tuple[T, bool]:
        if not self._items:
            return cast(T, None), False
        return self._items.pop(0), True

    def peek(self) -> tuple[T, bool]:
        if not self._items:
            return cast(T, None), False
        return self._items[0], True

    def clear(self) -> None:
        if self._config.free_value is not None:
            for item in self._items:
                self._config.free_value(item)
        self._items.clear()

    def for_each(self, visit: VisitFunc[T]) -> None:
        for item in self._items:
            visit(item)
