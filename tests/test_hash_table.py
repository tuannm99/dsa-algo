from __future__ import annotations

from python.hashtable.hashtable import Config


def test_hash_table_set_get_delete_and_resize(hash_table_factory) -> None:
    table = hash_table_factory(
        Config(
            initial_capacity=4,
            hash_key=hash,
            compare_key=lambda a, b: 0 if a == b else 1,
        ))

    assert table.is_empty() is True
    assert table.set("a", 1) is True
    assert table.set("b", 2) is True
    assert table.size() == 2
    assert table.contains("a") is True
    assert table.get("a") == (1, True)
    assert table.get("z") == (None, False)
    assert table.contains("z") is False
    assert table.set("a", 3) is True
    assert table.get("a") == (3, True)
    assert table.size() == 2
    assert table.resize(8) is True
    assert table.capacity() >= 8
    assert table.resize(1) is True
    assert table.delete("a") == ("a", 3, True)
    assert table.delete("a") == (None, None, False)
    assert table.delete("missing") == (None, None, False)


def test_hash_table_for_each_and_clear(hash_table_factory) -> None:
    freed_keys: list[str] = []
    freed_values: list[int] = []
    table = hash_table_factory(
        Config(
            initial_capacity=4,
            hash_key=hash,
            compare_key=lambda a, b: 0 if a == b else 1,
            free_key=freed_keys.append,
            free_value=freed_values.append,
        ))
    items: dict[str, int] = {}

    assert table.set("x", 10) is True
    assert table.set("y", 20) is True
    table.for_each(lambda key, value: items.__setitem__(key, value))
    assert items == {"x": 10, "y": 20}

    table.clear()
    assert sorted(freed_keys) == ["x", "y"]
    assert sorted(freed_values) == [10, 20]
    assert table.is_empty() is True


def test_hash_table_clear_is_idempotent(hash_table_factory) -> None:
    freed_keys: list[str] = []
    freed_values: list[int] = []
    table = hash_table_factory(
        Config(
            initial_capacity=4,
            hash_key=hash,
            compare_key=lambda a, b: 0 if a == b else 1,
            free_key=freed_keys.append,
            free_value=freed_values.append,
        ))

    assert table.set("only", 1) is True
    table.clear()
    table.clear()

    assert freed_keys == ["only"]
    assert freed_values == [1]
