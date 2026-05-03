from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Protocol, TypeVar

from ..ds_types import CompareFunc, FreeFunc, HashFunc, VisitFunc

T = TypeVar("T")


@dataclass(frozen=True)
class Config(Generic[T]):
    initial_capacity: int
    hash_value: HashFunc[T]
    compare_value: CompareFunc[T]
    free_value: FreeFunc[T] | None = None


class HashSet(Protocol[T]):

    def size(self) -> int:
        ...

    def is_empty(self) -> bool:
        ...

    def add(self, value: T) -> bool:
        ...

    def contains(self, value: T) -> bool:
        ...

    def remove(self, value: T) -> tuple[T, bool]:
        ...

    def clear(self) -> None:
        ...

    def for_each(self, visit: VisitFunc[T]) -> None:
        ...
