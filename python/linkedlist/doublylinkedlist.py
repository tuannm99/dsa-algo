from __future__ import annotations

from typing import Generic, TypeVar, cast

from python.linkedlist.linkedlist import Config, LinkedList
from python.ds_types import CompareFunc, VisitFunc

T = TypeVar("T")


class DoublyLinkedList(Generic[T], LinkedList[T]):
    def __init__(self, config: Config[T] | None = None) -> None:
        self._config = config or Config()
        self._items: list[T] = []
        self._cleanup_items: list[T] = []

    def _forget_cleanup_item(self, value: T) -> None:
        for index, item in enumerate(self._cleanup_items):
            if item is value:
                self._cleanup_items.pop(index)
                return
        self._cleanup_items.remove(value)

    def size(self) -> int:
        return len(self._items)

    def is_empty(self) -> bool:
        return not self._items

    def push_front(self, value: T) -> bool:
        self._items.insert(0, value)
        self._cleanup_items.insert(0, value)
        return True

    def push_back(self, value: T) -> bool:
        self._items.append(value)
        self._cleanup_items.append(value)
        return True

    def pop_front(self) -> tuple[T, bool]:
        if not self._items:
            return cast(T, None), False
        value = self._items.pop(0)
        self._forget_cleanup_item(value)
        return value, True

    def pop_back(self) -> tuple[T, bool]:
        if not self._items:
            return cast(T, None), False
        value = self._items.pop()
        self._forget_cleanup_item(value)
        return value, True

    def front(self) -> tuple[T, bool]:
        if not self._items:
            return cast(T, None), False
        return self._items[0], True

    def back(self) -> tuple[T, bool]:
        if not self._items:
            return cast(T, None), False
        return self._items[-1], True

    def get(self, index: int) -> tuple[T, bool]:
        if not 0 <= index < len(self._items):
            return cast(T, None), False
        return self._items[index], True

    def insert(self, index: int, value: T) -> bool:
        if not 0 <= index <= len(self._items):
            return False
        self._items.insert(index, value)
        self._cleanup_items.insert(index, value)
        return True

    def remove_at(self, index: int) -> tuple[T, bool]:
        if not 0 <= index < len(self._items):
            return cast(T, None), False
        value = self._items.pop(index)
        self._forget_cleanup_item(value)
        return value, True

    def remove_value(self, value: T,
                     compare: CompareFunc[T]) -> tuple[T, bool]:
        for index, item in enumerate(self._items):
            if compare(item, value) == 0:
                removed = self._items.pop(index)
                self._forget_cleanup_item(removed)
                return removed, True
        return cast(T, None), False

    def reverse(self) -> None:
        self._items.reverse()

    def clear(self) -> None:
        if self._config.free_value is not None:
            for item in self._cleanup_items:
                self._config.free_value(item)
        self._items.clear()
        self._cleanup_items.clear()

    def for_each(self, visit: VisitFunc[T]) -> None:
        for item in self._items:
            visit(item)
