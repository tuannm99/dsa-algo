from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class Config:
    size: int


class UnionFind(Protocol):

    def size(self) -> int:
        ...

    def component_count(self) -> int:
        ...

    def find(self, value: int) -> tuple[int, bool]:
        ...

    def union(self, left: int, right: int) -> bool:
        ...

    def connected(self, left: int, right: int) -> bool:
        ...

    def component_size(self, value: int) -> tuple[int, bool]:
        ...
