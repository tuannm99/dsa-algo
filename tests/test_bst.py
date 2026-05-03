from __future__ import annotations

from python.tree.bst.bst import Config


def test_bst_insert_lookup_remove_and_extrema(bst_factory) -> None:
    bst = bst_factory(Config(compare_key=lambda a, b: a - b))

    assert bst.get(1) == (None, False)
    assert bst.remove(1) == (None, None, False)
    assert bst.min_key() == (None, False)
    assert bst.max_key() == (None, False)
    assert bst.insert(2, "b") is True
    assert bst.insert(1, "a") is True
    assert bst.insert(3, "c") is True
    assert bst.insert(2, "bb") is True
    assert bst.size() == 3
    assert bst.get(2) == ("bb", True)
    assert bst.contains(4) is False
    assert bst.min_key() == (1, True)
    assert bst.max_key() == (3, True)
    assert bst.remove(2) == (2, "bb", True)
    assert bst.remove(2) == (None, None, False)


def test_bst_traversals_and_clear(bst_factory) -> None:
    freed_keys: list[int] = []
    freed_values: list[str] = []
    bst = bst_factory(
        Config(
            compare_key=lambda a, b: a - b,
            free_key=freed_keys.append,
            free_value=freed_values.append,
        ))
    in_order: list[int] = []
    pre_order: list[int] = []
    post_order: list[int] = []

    for key, value in ((2, "b"), (1, "a"), (3, "c")):
        assert bst.insert(key, value) is True

    bst.in_order(lambda key, value: in_order.append(key))
    bst.pre_order(lambda key, value: pre_order.append(key))
    bst.post_order(lambda key, value: post_order.append(key))

    assert in_order == [1, 2, 3]
    assert sorted(pre_order) == [1, 2, 3]
    assert sorted(post_order) == [1, 2, 3]

    bst.clear()
    assert sorted(freed_keys) == [1, 2, 3]
    assert sorted(freed_values) == ["a", "b", "c"]
    assert bst.is_empty() is True
