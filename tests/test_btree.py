from __future__ import annotations

from python.tree.btree.btree import Config


def test_btree_insert_lookup_remove_and_extrema(btree_factory) -> None:
    btree = btree_factory(Config(min_degree=2, compare_key=lambda a, b: a - b))

    assert btree.min_degree() == 2
    assert btree.get(1) == (None, False)
    assert btree.remove(1) == (None, None, False)
    assert btree.min_key() == (None, False)
    assert btree.max_key() == (None, False)
    assert btree.insert(2, "b") is True
    assert btree.insert(1, "a") is True
    assert btree.insert(3, "c") is True
    assert btree.insert(2, "bb") is True
    assert btree.get(2) == ("bb", True)
    assert btree.contains(4) is False
    assert btree.min_key() == (1, True)
    assert btree.max_key() == (3, True)
    assert btree.remove(2) == (2, "bb", True)
    assert btree.remove(2) == (None, None, False)


def test_btree_traverse_and_clear(btree_factory) -> None:
    freed_keys: list[int] = []
    freed_values: list[str] = []
    btree = btree_factory(
        Config(
            min_degree=2,
            compare_key=lambda a, b: a - b,
            free_key=freed_keys.append,
            free_value=freed_values.append,
        ))
    traversed: list[int] = []

    for key, value in ((2, "b"), (1, "a"), (3, "c")):
        assert btree.insert(key, value) is True

    btree.traverse(lambda key, value: traversed.append(key))
    assert traversed == [1, 2, 3]

    btree.clear()
    assert sorted(freed_keys) == [1, 2, 3]
    assert sorted(freed_values) == ["a", "b", "c"]
    assert btree.is_empty() is True
