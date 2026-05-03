from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Protocol, TypeVar

from ..ds_types import FreeFunc, VisitFunc

T = TypeVar("T")


@dataclass(frozen=True)
class Config(Generic[T]):
    initial_capacity: int = 0
    free_value: FreeFunc[T] | None = None


class Deque(Protocol[T]):

    def size(self) -> int:
        ...

    def is_empty(self) -> bool:
        ...

    def push_front(self, value: T) -> bool:
        ...

    def push_back(self, value: T) -> bool:
        ...

    def pop_front(self) -> tuple[T, bool]:
        ...

    def pop_back(self) -> tuple[T, bool]:
        ...

    def peek_front(self) -> tuple[T, bool]:
        ...

    def peek_back(self) -> tuple[T, bool]:
        ...

    def clear(self) -> None:
        ...

    def for_each(self, visit: VisitFunc[T]) -> None:
        ...
