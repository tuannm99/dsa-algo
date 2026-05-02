from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Protocol, TypeVar

from ..ds_types import HashFunc

T = TypeVar("T")


@dataclass(frozen=True)
class Config(Generic[T]):
    bit_capacity: int
    num_hashes: int
    hash1: HashFunc[T]
    hash2: HashFunc[T]


@dataclass(frozen=True)
class RateConfig(Generic[T]):
    expected_items: int
    false_positive_rate: float
    hash1: HashFunc[T]
    hash2: HashFunc[T]


class BloomFilter(Protocol[T]):
    def bit_capacity(self) -> int: ...
    def hash_count(self) -> int: ...
    def count(self) -> int: ...
    def is_empty(self) -> bool: ...

    def add(self, value: T) -> bool: ...
    def may_contain(self, value: T) -> bool: ...

    def estimated_false_positive_rate(self) -> float: ...
    def clear(self) -> None: ...
