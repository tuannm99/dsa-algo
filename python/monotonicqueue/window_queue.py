from __future__ import annotations

from collections import deque

from .monotonicqueue import Config, MonotonicQueue


class WindowMonotonicQueue(MonotonicQueue):

    def __init__(self, config: Config | None = None) -> None:
        self._config = config or Config()
        self._items: deque[int] = deque()

    def _should_remove_back(self, value: int) -> bool:
        if not self._items:
            return False
        if self._config.decreasing:
            return self._items[-1] < value
        return self._items[-1] > value

    def size(self) -> int:
        return len(self._items)

    def is_empty(self) -> bool:
        return not self._items

    def push(self, value: int) -> None:
        while self._should_remove_back(value):
            self._items.pop()
        self._items.append(value)

    def pop(self, value: int) -> bool:
        if self._items and self._items[0] == value:
            self._items.popleft()
            return True
        return False

    def front(self) -> tuple[int, bool]:
        if not self._items:
            return 0, False
        return self._items[0], True
