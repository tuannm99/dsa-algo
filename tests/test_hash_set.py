from __future__ import annotations

from python.hashset.hashset import Config


def test_hash_set_add_contains_and_remove(hash_set_factory) -> None:
    hash_set = hash_set_factory(
        Config(
            initial_capacity=4,
            hash_value=hash,
            compare_value=lambda a, b: 0 if a == b else 1,
        ))

    assert hash_set.add("a") is True
    assert hash_set.add("b") is True
    assert hash_set.add("a") is True
    assert hash_set.contains("a") is True
    assert hash_set.contains("c") is False
    assert hash_set.remove("a") == ("a", True)
    assert hash_set.remove("a") == (None, False)


def test_hash_set_for_each_and_clear(hash_set_factory) -> None:
    freed: list[str] = []
    hash_set = hash_set_factory(
        Config(
            initial_capacity=4,
            hash_value=hash,
            compare_value=lambda a, b: 0 if a == b else 1,
            free_value=freed.append,
        ))
    seen: set[str] = set()

    assert hash_set.add("x") is True
    assert hash_set.add("y") is True
    hash_set.for_each(seen.add)
    assert seen == {"x", "y"}

    hash_set.clear()
    assert sorted(freed) == ["x", "y"]
    assert hash_set.is_empty() is True


def test_hash_set_clear_is_idempotent(hash_set_factory) -> None:
    freed: list[str] = []
    hash_set = hash_set_factory(
        Config(
            initial_capacity=4,
            hash_value=hash,
            compare_value=lambda a, b: 0 if a == b else 1,
            free_value=freed.append,
        ))

    assert hash_set.add("z") is True
    hash_set.clear()
    hash_set.clear()

    assert freed == ["z"]
