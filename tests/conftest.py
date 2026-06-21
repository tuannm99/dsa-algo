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
from python.bloomfilter.simple_bloom_filter import SimpleBloomFilter
from python.deque.my_deque import MyDeque
from python.graph.simple_graph import SimpleGraph
from python.hashset.simple_hash_set import SimpleHashSet
from python.hashtable.simple_hash_table import SimpleHashTable
from python.heap.simple_heap import SimpleHeap
from python.lfu.simple_lfu import SimpleLFU
from python.linkedlist.doublylinkedlist import DoublyLinkedList
from python.lru.simple_lru import SimpleLRU
from python.queue.list_queue import ListQueue
from python.stack.list_stack import ListStack
from python.tree.bst.simple_bst import SimpleBST
from python.tree.btree.simple_btree import SimpleBTree
from python.tree.rbtree.simple_rbtree import SimpleRBTree
from python.trie.simple_trie import SimpleTrie


@pytest.fixture
def array_factory() -> Callable[..., Any]:
    return lambda config=None: ListArray(config or ArrayConfig())


@pytest.fixture
def linked_list_factory() -> Callable[..., Any]:
    return lambda config=None: DoublyLinkedList(config)


@pytest.fixture
def stack_factory() -> Callable[..., Any]:
    return lambda config=None: ListStack(config)


@pytest.fixture
def queue_factory() -> Callable[..., Any]:
    return lambda config=None: ListQueue(config)


@pytest.fixture
def deque_factory() -> Callable[..., Any]:
    return lambda config=None: MyDeque(config)


@pytest.fixture
def heap_factory() -> Callable[..., Any]:
    return lambda config: SimpleHeap(config)


@pytest.fixture
def hash_table_factory() -> Callable[..., Any]:
    return lambda config: SimpleHashTable(config)


@pytest.fixture
def hash_set_factory() -> Callable[..., Any]:
    return lambda config: SimpleHashSet(config)


@pytest.fixture
def bloom_filter_factory() -> Callable[..., Any]:
    return lambda config: SimpleBloomFilter(config)


@pytest.fixture
def trie_factory() -> Callable[..., Any]:
    return lambda config=None: SimpleTrie(config)


@pytest.fixture
def lru_factory() -> Callable[..., Any]:
    return lambda config: SimpleLRU(config)


@pytest.fixture
def lfu_factory() -> Callable[..., Any]:
    return lambda config: SimpleLFU(config)


@pytest.fixture
def graph_factory() -> Callable[..., Any]:
    return lambda config: SimpleGraph(config)


@pytest.fixture
def bst_factory() -> Callable[..., Any]:
    return lambda config: SimpleBST(config)


@pytest.fixture
def btree_factory() -> Callable[..., Any]:
    return lambda config: SimpleBTree(config)


@pytest.fixture
def rbtree_factory() -> Callable[..., Any]:
    return lambda config: SimpleRBTree(config)
