from __future__ import annotations

import heapq
from typing import Generic, TypeVar, cast

from ..ds_types import VisitFunc
from .priorityqueue import Config, PriorityQueue

T = TypeVar("T")


class HeapPriorityQueue(Generic[T], PriorityQueue[T]):

    def __init__(self, config: Config[T] | None = None) -> None:
        self._config = config or Config()
        self._items: list[tuple[int, int, T]] = []
        self._sequence = 0

    def _heap_priority(self, priority: int) -> int:
        return priority if self._config.min_first else -priority

    def _public_priority(self, heap_priority: int) -> int:
        return heap_priority if self._config.min_first else -heap_priority

    def size(self) -> int:
        return len(self._items)

    def is_empty(self) -> bool:
        return not self._items

    def push(self, priority: int, value: T) -> bool:
        heapq.heappush(self._items,
                       (self._heap_priority(priority), self._sequence, value))
        self._sequence += 1
        return True

    def pop(self) -> tuple[int, T, bool]:
        if not self._items:
            return 0, cast(T, None), False
        priority, _, value = heapq.heappop(self._items)
        return self._public_priority(priority), value, True

    def peek(self) -> tuple[int, T, bool]:
        if not self._items:
            return 0, cast(T, None), False
        priority, _, value = self._items[0]
        return self._public_priority(priority), value, True

    def clear(self) -> None:
        if self._config.free_value is not None:
            for _, _, value in self._items:
                self._config.free_value(value)
        self._items.clear()

    def for_each(self, visit: VisitFunc[T]) -> None:
        for _, _, value in sorted(self._items):
            visit(value)
