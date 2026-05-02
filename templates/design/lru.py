class _LRUNode:
    def __init__(self, key: int = 0, value: int = 0) -> None:
        self.key = key
        self.value = value
        self.prev: _LRUNode | None = None
        self.next: _LRUNode | None = None


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.nodes: dict[int, _LRUNode] = {}
        self.head = _LRUNode()
        self.tail = _LRUNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        node = self.nodes.get(key)
        if node is None:
            return -1
        self._move_to_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.nodes.get(key)
        if node is not None:
            node.value = value
            self._move_to_front(node)
            return

        node = _LRUNode(key, value)
        self.nodes[key] = node
        self._insert_after_head(node)

        if len(self.nodes) > self.capacity:
            evicted = self.tail.prev
            assert evicted is not None and evicted is not self.head
            self._remove(evicted)
            del self.nodes[evicted.key]

    def _move_to_front(self, node: _LRUNode) -> None:
        self._remove(node)
        self._insert_after_head(node)

    def _insert_after_head(self, node: _LRUNode) -> None:
        first = self.head.next
        node.prev = self.head
        node.next = first
        self.head.next = node
        if first is not None:
            first.prev = node

    def _remove(self, node: _LRUNode) -> None:
        prev_node = node.prev
        next_node = node.next
        assert prev_node is not None and next_node is not None
        prev_node.next = next_node
        next_node.prev = prev_node
