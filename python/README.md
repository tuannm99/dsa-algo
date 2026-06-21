# Python Data Structure Interfaces

This tree is the Python translation of the original C-style container interfaces.

Shared callback and helper types:
- `python/ds_types.py`

Core data structure packages:
- `python/array/array.py`
- `python/linkedlist/linkedlist.py`
- `python/stack/stack.py`
- `python/queue/queue.py`
- `python/deque/deque.py`
- `python/heap/heap.py`
- `python/priorityqueue/priorityqueue.py`
- `python/hashtable/hashtable.py`
- `python/hashset/hashset.py`
- `python/bloomfilter/bloomfilter.py`
- `python/lru/lru.py`
- `python/lfu/lfu.py`
- `python/unionfind/unionfind.py`
- `python/fenwick/fenwick.py`
- `python/segmenttree/segmenttree.py`
- `python/monotonicqueue/monotonicqueue.py`
- `python/trie/trie.py`
- `python/graph/graph.py`
- `python/tree/btree/btree.py`
- `python/tree/bst/bst.py`
- `python/tree/rbtree/rbtree.py`

Design choices:
- Each package exposes a typed Python `Protocol` instead of an opaque C struct.
- Constructor arguments from the C API are represented as `Config` dataclasses.
- `void *` becomes Python type parameters.
- C callback types become typed callables in `python/ds_types.py`.
- Out-parameters become tuple return values.
