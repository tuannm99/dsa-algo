from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class Config:
    values: list[int]


class SegmentTree(Protocol):

    def size(self) -> int:
        ...

    def update(self, index: int, value: int) -> bool:
        ...

    def query(self, left: int, right: int) -> tuple[int, bool]:
        ...
