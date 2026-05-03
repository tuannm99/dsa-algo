from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Protocol, TypeVar

from ..ds_types import CompareFunc, FreeFunc, HashFunc, KVVisitFunc

K = TypeVar("K")
V = TypeVar("V")


@dataclass(frozen=True)
class Config(Generic[K, V]):
    initial_capacity: int
    hash_key: HashFunc[K]
    compare_key: CompareFunc[K]
    free_key: FreeFunc[K] | None = None
    free_value: FreeFunc[V] | None = None


class HashTable(Protocol[K, V]):

    def size(self) -> int:
        ...

    def capacity(self) -> int:
        ...

    def is_empty(self) -> bool:
        ...

    def set(self, key: K, value: V) -> bool:
        ...

    def get(self, key: K) -> tuple[V, bool]:
        ...

    def contains(self, key: K) -> bool:
        ...

    def delete(self, key: K) -> tuple[K, V, bool]:
        ...

    def resize(self, new_capacity: int) -> bool:
        ...

    def clear(self) -> None:
        ...

    def for_each(self, visit: KVVisitFunc[K, V]) -> None:
        ...
