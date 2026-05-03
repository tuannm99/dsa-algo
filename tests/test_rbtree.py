from __future__ import annotations

from python.tree.rbtree.rbtree import Config


def test_rbtree_insert_lookup_remove_and_extrema(rbtree_factory) -> None:
    rbtree = rbtree_factory(Config(compare_key=lambda a, b: a - b))

    assert rbtree.get(1) == (None, False)
    assert rbtree.remove(1) == (None, None, False)
    assert rbtree.min_key() == (None, False)
    assert rbtree.max_key() == (None, False)
    assert rbtree.insert(2, "b") is True
    assert rbtree.insert(1, "a") is True
    assert rbtree.insert(3, "c") is True
    assert rbtree.insert(2, "bb") is True
    assert rbtree.get(2) == ("bb", True)
    assert rbtree.contains(4) is False
    assert rbtree.min_key() == (1, True)
    assert rbtree.max_key() == (3, True)
    assert rbtree.remove(2) == (2, "bb", True)
    assert rbtree.remove(2) == (None, None, False)


def test_rbtree_in_order_and_clear(rbtree_factory) -> None:
    freed_keys: list[int] = []
    freed_values: list[str] = []
    rbtree = rbtree_factory(
        Config(
            compare_key=lambda a, b: a - b,
            free_key=freed_keys.append,
            free_value=freed_values.append,
        ))
    traversed: list[int] = []

    for key, value in ((2, "b"), (1, "a"), (3, "c")):
        assert rbtree.insert(key, value) is True

    rbtree.in_order(lambda key, value: traversed.append(key))
    assert traversed == [1, 2, 3]

    rbtree.clear()
    assert sorted(freed_keys) == [1, 2, 3]
    assert sorted(freed_values) == ["a", "b", "c"]
    assert rbtree.is_empty() is True
