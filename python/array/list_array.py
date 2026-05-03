from __future__ import annotations

from typing import Generic, TypeVar, cast

from .array import Array, Config
from ..ds_types import CompareFunc, VisitFunc

T = TypeVar("T")


class ListArray(Generic[T], Array[T]):

    def __init__(self, config: Config[T] | None = None) -> None:
        self._config = config or Config()
        self._items: list[T] = []
        self._capacity = max(0, self._config.initial_capacity)

    def size(self) -> int:
        return len(self._items)

    def capacity(self) -> int:
        return max(self._capacity, len(self._items))

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def reserve(self, min_capacity: int) -> bool:
        if min_capacity <= self.capacity():
            return True
        self._capacity = min_capacity
        return True

    def shrink_to_fit(self) -> bool:
        self._capacity = len(self._items)
        return True

    def clear(self) -> None:
        if self._config.free_value is not None:
            for item in self._items:
                self._config.free_value(item)
        self._items.clear()

    def get(self, index: int) -> tuple[T, bool]:
        if not 0 <= index < len(self._items):
            return cast(T, None), False
        return self._items[index], True

    def set(self, index: int, value: T) -> bool:
        if not 0 <= index < len(self._items):
            return False
        self._items[index] = value
        return True

    def push(self, value: T) -> bool:
        if len(self._items) == self.capacity():
            next_capacity = 1 if self.capacity() == 0 else self.capacity() * 2
            self._capacity = next_capacity
        self._items.append(value)
        return True

    def pop(self) -> tuple[T, bool]:
        if not self._items:
            return cast(T, None), False
        return self._items.pop(), True

    def insert(self, index: int, value: T) -> bool:
        if not 0 <= index <= len(self._items):
            return False
        if len(self._items) == self.capacity():
            next_capacity = 1 if self.capacity() == 0 else self.capacity() * 2
            self._capacity = next_capacity
        self._items.insert(index, value)
        return True

    def remove(self, index: int) -> tuple[T, bool]:
        if not 0 <= index < len(self._items):
            return cast(T, None), False
        return self._items.pop(index), True

    def index_of(self, value: T, compare: CompareFunc[T]) -> int:
        for index, item in enumerate(self._items):
            if compare(item, value) == 0:
                return index
        return -1

    def for_each(self, visit: VisitFunc[T]) -> None:
        for item in self._items:
            visit(item)
