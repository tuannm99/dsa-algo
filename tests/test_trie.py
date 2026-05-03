from __future__ import annotations

from python.trie.trie import Config


def test_trie_insert_lookup_and_remove(trie_factory) -> None:
    trie = trie_factory(Config())

    assert trie.get("missing") == (None, False)
    assert trie.contains("missing") is False
    assert trie.remove("missing") == (None, False)
    assert trie.insert("cat", 1) is True
    assert trie.insert("car", 2) is True
    assert trie.insert("cat", 3) is True
    assert trie.size() == 2
    assert trie.contains("cat") is True
    assert trie.get("cat") == (3, True)
    assert trie.get("car") == (2, True)
    assert trie.get("cab") == (None, False)
    assert trie.remove("cat") == (3, True)
    assert trie.remove("cat") == (None, False)


def test_trie_prefix_queries_and_clear(trie_factory) -> None:
    freed: list[int] = []
    trie = trie_factory(Config(free_value=freed.append))
    seen: dict[str, int] = {}

    assert trie.insert("app", 1) is True
    assert trie.insert("apple", 2) is True
    assert trie.insert("ape", 3) is True
    assert trie.has_prefix("ap") is True
    assert trie.has_prefix("zzz") is False
    assert trie.prefix_count("app") == 2
    assert trie.prefix_count("zzz") == 0

    trie.for_each_prefix("app",
                         lambda key, value: seen.__setitem__(key, value))
    assert seen == {"app": 1, "apple": 2}

    trie.clear()
    assert sorted(freed) == [1, 2, 3]
    assert trie.is_empty() is True
