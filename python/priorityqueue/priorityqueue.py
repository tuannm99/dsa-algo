from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Protocol, TypeVar

from ..ds_types import FreeFunc, VisitFunc

T = TypeVar("T")


@dataclass(frozen=True)
class Config(Generic[T]):
    min_first: bool = True
    free_value: FreeFunc[T] | None = None


class PriorityQueue(Protocol[T]):

    def size(self) -> int:
        ...

    def is_empty(self) -> bool:
        ...

    def push(self, priority: int, value: T) -> bool:
        ...

    def pop(self) -> tuple[int, T, bool]:
        ...

    def peek(self) -> tuple[int, T, bool]:
        ...

    def clear(self) -> None:
        ...

    def for_each(self, visit: VisitFunc[T]) -> None:
        ...
