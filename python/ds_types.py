from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Generic, TypeVar

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")

CompareFunc = Callable[[T, T], int]
HashFunc = Callable[[T], int]
FreeFunc = Callable[[T], None]
PredicateFunc = Callable[[T], bool]
VisitFunc = Callable[[T], None]
KVVisitFunc = Callable[[K, V], None]


@dataclass(frozen=True)
class Entry(Generic[K, V]):
    key: K
    value: V
