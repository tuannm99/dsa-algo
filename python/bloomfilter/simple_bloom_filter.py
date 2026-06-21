from __future__ import annotations

from math import exp
from typing import Generic, TypeVar

from .bloomfilter import BloomFilter, Config

T = TypeVar("T")


class SimpleBloomFilter(Generic[T], BloomFilter[T]):

    def __init__(self, config: Config[T]) -> None:
        self._config = config
        self._bits: set[int] = set()
        self._count = 0

    def _hashes(self, value: T) -> list[int]:
        capacity = max(1, self._config.bit_capacity)
        first = self._config.hash1(value)
        second = self._config.hash2(value)
        return [(first + i * second + i * i) % capacity
                for i in range(max(1, self._config.num_hashes))]

    def bit_capacity(self) -> int:
        return self._config.bit_capacity

    def hash_count(self) -> int:
        return self._config.num_hashes

    def count(self) -> int:
        return self._count

    def is_empty(self) -> bool:
        return self._count == 0

    def add(self, value: T) -> bool:
        for bit in self._hashes(value):
            self._bits.add(bit)
        self._count += 1
        return True

    def may_contain(self, value: T) -> bool:
        return all(bit in self._bits for bit in self._hashes(value))

    def estimated_false_positive_rate(self) -> float:
        m = max(1, self._config.bit_capacity)
        k = max(1, self._config.num_hashes)
        n = self._count
        return (1 - exp(-k * n / m))**k

    def clear(self) -> None:
        self._bits.clear()
        self._count = 0
