from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class Config:
    size: int


class FenwickTree(Protocol):

    def size(self) -> int:
        ...

    def add(self, index: int, delta: int) -> bool:
        ...

    def prefix_sum(self, index: int) -> tuple[int, bool]:
        ...

    def range_sum(self, left: int, right: int) -> tuple[int, bool]:
        ...

    def get(self, index: int) -> tuple[int, bool]:
        ...
