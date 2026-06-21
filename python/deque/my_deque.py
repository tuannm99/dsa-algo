from __future__ import annotations

from typing import Generic, TypeVar, cast

from python.deque.deque import Config, Deque
from python.ds_types import VisitFunc

T = TypeVar("T")


class MyDeque(Generic[T], Deque[T]):

    def __init__(self, config: Config[T] | None = None) -> None:
        self._config = config or Config()
        self._items: list[T] = []
        self._capacity = max(0, self._config.initial_capacity)

    def size(self) -> int:
        return len(self._items)

    def is_empty(self) -> int:
        return len(self._items) == 0

    def push_front(self, value: T) -> bool:
        self._items.insert(0, value)
        return True

    def push_back(self, value: T) -> bool:
        self._items.append(value)
        return True

    def pop_front(self) -> tuple[T, bool]:
        if not self._items:
            return cast(T, None), False
        return self._items.pop(0), True

    def pop_back(self) -> tuple[T, bool]:
        if not self._items:
            return cast(T, None), False
        return self._items.pop(), True

    def peek_front(self) -> tuple[T, bool]:
        if not self._items:
            return cast(T, None), False
        return self._items[0], True

    def peek_back(self) -> tuple[T, bool]:
        if not self._items:
            return cast(T, None), False
        return self._items[-1], True

    def clear(self) -> None:
        if self._config.free_value is not None:
            for item in self._items:
                self._config.free_value(item)
        self._items.clear()

    def for_each(self, visit: VisitFunc[T]) -> None:
        for item in self._items:
            visit(item)
