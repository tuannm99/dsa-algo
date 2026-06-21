from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class Config:
    decreasing: bool = True


class MonotonicQueue(Protocol):

    def size(self) -> int:
        ...

    def is_empty(self) -> bool:
        ...

    def push(self, value: int) -> None:
        ...

    def pop(self, value: int) -> bool:
        ...

    def front(self) -> tuple[int, bool]:
        ...
