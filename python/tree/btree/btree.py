from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Protocol, TypeVar

from ...ds_types import CompareFunc, FreeFunc, KVVisitFunc

K = TypeVar("K")
V = TypeVar("V")


@dataclass(frozen=True)
class Config(Generic[K, V]):
    min_degree: int
    compare_key: CompareFunc[K]
    free_key: FreeFunc[K] | None = None
    free_value: FreeFunc[V] | None = None


class BTree(Protocol[K, V]):

    def size(self) -> int:
        ...

    def is_empty(self) -> bool:
        ...

    def min_degree(self) -> int:
        ...

    def insert(self, key: K, value: V) -> bool:
        ...

    def get(self, key: K) -> tuple[V, bool]:
        ...

    def contains(self, key: K) -> bool:
        ...

    def remove(self, key: K) -> tuple[K, V, bool]:
        ...

    def min_key(self) -> tuple[K, bool]:
        ...

    def max_key(self) -> tuple[K, bool]:
        ...

    def clear(self) -> None:
        ...

    def traverse(self, visit: KVVisitFunc[K, V]) -> None:
        ...
