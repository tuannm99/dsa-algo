package trie

type Node struct {
	children [26]*Node
	isWord   bool
}

type Trie struct {
	root *Node
}

func NewTrie() *Trie {
	return &Trie{root: &Node{}}
}

func (t *Trie) Insert(word string) {
	cur := t.root
	for i := 0; i < len(word); i++ {
		idx := word[i] - 'a'
		if cur.children[idx] == nil {
			cur.children[idx] = &Node{}
		}
		cur = cur.children[idx]
	}
	cur.isWord = true
}

func (t *Trie) Search(word string) bool {
	node := t.walk(word)
	return node != nil && node.isWord
}

func (t *Trie) StartsWith(prefix string) bool {
	return t.walk(prefix) != nil
}

func (t *Trie) walk(s string) *Node {
	cur := t.root
	for i := 0; i < len(s); i++ {
		idx := s[i] - 'a'
		if cur.children[idx] == nil {
			return nil
		}
		cur = cur.children[idx]
	}
	return cur
}
