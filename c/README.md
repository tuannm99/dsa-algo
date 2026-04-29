# C Data Structure Interfaces

This tree is set up as a C-first implementation repo.

Shared type helpers:
- `c/ds_types.h`

Core data structures:
- `c/array/array.h`
- `c/linkedlist/linkedlist.h`
- `c/stack/stack.h`
- `c/queue/queue.h`
- `c/deque/deque.h`
- `c/heap/heap.h`
- `c/hashtable/hashtable.h`
- `c/hashset/hashset.h`
- `c/bloomfilter/bloomfilter.h`
- `c/lru/lru.h`
- `c/lfu/lfu.h`
- `c/trie/trie.h`
- `c/graph/graph.h`
- `c/tree/binarytree/btree.h`
- `c/tree/bst/bst.h`
- `c/tree/rbtree/rbtree.h`

Design choices:
- All containers are opaque structs.
- Generic storage uses `void *`.
- Ownership is explicit through `ds_free_fn` callbacks.
- Ordered structures depend on `ds_compare_fn`.
- Hash-based structures depend on `ds_hash_fn` and `ds_compare_fn`.
- Cache structures use generic key/value ownership and explicit eviction outputs.
- The bloom filter API uses double hashing (`hash1`, `hash2`) to derive `k` probes.
