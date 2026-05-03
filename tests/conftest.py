from __future__ import annotations

from collections.abc import Callable
from pathlib import Path
import sys
from typing import Any

import pytest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from python.array import Config as ArrayConfig
from python.array import ListArray


def _unimplemented(name: str) -> Any:
    pytest.skip(f"No implementation factory configured for {name}. "
                "Provide or override the fixture in tests/conftest.py.")


@pytest.fixture
def array_factory() -> Callable[..., Any]:
    return lambda config=None: ListArray(config or ArrayConfig())


@pytest.fixture
def linked_list_factory() -> Callable[..., Any]:
    return lambda config=None: _unimplemented("LinkedList")


@pytest.fixture
def stack_factory() -> Callable[..., Any]:
    return lambda config=None: _unimplemented("Stack")


@pytest.fixture
def queue_factory() -> Callable[..., Any]:
    return lambda config=None: _unimplemented("Queue")


@pytest.fixture
def deque_factory() -> Callable[..., Any]:
    return lambda config=None: _unimplemented("Deque")


@pytest.fixture
def heap_factory() -> Callable[..., Any]:
    return lambda config: _unimplemented("Heap")


@pytest.fixture
def hash_table_factory() -> Callable[..., Any]:
    return lambda config: _unimplemented("HashTable")


@pytest.fixture
def hash_set_factory() -> Callable[..., Any]:
    return lambda config: _unimplemented("HashSet")


@pytest.fixture
def bloom_filter_factory() -> Callable[..., Any]:
    return lambda config: _unimplemented("BloomFilter")


@pytest.fixture
def trie_factory() -> Callable[..., Any]:
    return lambda config=None: _unimplemented("Trie")


@pytest.fixture
def lru_factory() -> Callable[..., Any]:
    return lambda config: _unimplemented("LRU")


@pytest.fixture
def lfu_factory() -> Callable[..., Any]:
    return lambda config: _unimplemented("LFU")


@pytest.fixture
def graph_factory() -> Callable[..., Any]:
    return lambda config: _unimplemented("Graph")


@pytest.fixture
def bst_factory() -> Callable[..., Any]:
    return lambda config: _unimplemented("BST")


@pytest.fixture
def btree_factory() -> Callable[..., Any]:
    return lambda config: _unimplemented("BTree")


@pytest.fixture
def rbtree_factory() -> Callable[..., Any]:
    return lambda config: _unimplemented("RBTree")
