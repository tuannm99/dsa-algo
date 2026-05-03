from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Protocol, TypeVar

from ..ds_types import CompareFunc, Entry, FreeFunc, HashFunc, KVVisitFunc

K = TypeVar("K")
V = TypeVar("V")


@dataclass(frozen=True)
class Config(Generic[K, V]):
    capacity: int
    hash_key: HashFunc[K]
    compare_key: CompareFunc[K]
    free_key: FreeFunc[K] | None = None
    free_value: FreeFunc[V] | None = None


class LRU(Protocol[K, V]):

    def size(self) -> int:
        ...

    def capacity(self) -> int:
        ...

    def is_empty(self) -> bool:
        ...

    def put(self, key: K, value: V) -> tuple[K, V, bool, bool]:
        ...

    def get(self, key: K) -> tuple[V, bool]:
        ...

    def contains(self, key: K) -> bool:
        ...

    def peek(self, key: K) -> tuple[V, bool]:
        ...

    def remove(self, key: K) -> tuple[K, V, bool]:
        ...

    def resize(self, new_capacity: int) -> tuple[list[Entry[K, V]], bool]:
        ...

    def clear(self) -> None:
        ...

    def for_each(self, visit: KVVisitFunc[K, V]) -> None:
        ...
