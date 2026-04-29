package design

type lruNode struct {
	key  int
	val  int
	prev *lruNode
	next *lruNode
}

type LRUCache struct {
	capacity int
	nodes    map[int]*lruNode
	head     *lruNode
	tail     *lruNode
}

func NewLRUCache(capacity int) *LRUCache {
	head := &lruNode{}
	tail := &lruNode{}
	head.next = tail
	tail.prev = head
	return &LRUCache{
		capacity: capacity,
		nodes:    map[int]*lruNode{},
		head:     head,
		tail:     tail,
	}
}

func (c *LRUCache) Get(key int) int {
	node, ok := c.nodes[key]
	if !ok {
		return -1
	}
	c.moveToFront(node)
	return node.val
}

func (c *LRUCache) Put(key, value int) {
	if node, ok := c.nodes[key]; ok {
		node.val = value
		c.moveToFront(node)
		return
	}

	node := &lruNode{key: key, val: value}
	c.nodes[key] = node
	c.insertAfterHead(node)

	if len(c.nodes) > c.capacity {
		evicted := c.tail.prev
		c.remove(evicted)
		delete(c.nodes, evicted.key)
	}
}

func (c *LRUCache) moveToFront(node *lruNode) {
	c.remove(node)
	c.insertAfterHead(node)
}

func (c *LRUCache) insertAfterHead(node *lruNode) {
	node.next = c.head.next
	node.prev = c.head
	c.head.next.prev = node
	c.head.next = node
}

func (c *LRUCache) remove(node *lruNode) {
	node.prev.next = node.next
	node.next.prev = node.prev
}
