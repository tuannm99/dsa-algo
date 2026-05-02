class Node:
    def __init__(self) -> None:
        self.children: dict[str, Node] = {}
        self.is_word = False


class Trie:
    def __init__(self) -> None:
        self.root = Node()

    def insert(self, word: str) -> None:
        current = self.root
        for ch in word:
            current = current.children.setdefault(ch, Node())
        current.is_word = True

    def search(self, word: str) -> bool:
        node = self._walk(word)
        return node is not None and node.is_word

    def starts_with(self, prefix: str) -> bool:
        return self._walk(prefix) is not None

    def _walk(self, text: str) -> Node | None:
        current = self.root
        for ch in text:
            if ch not in current.children:
                return None
            current = current.children[ch]
        return current
