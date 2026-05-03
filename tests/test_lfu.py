from __future__ import annotations

from python.lfu.lfu import Config


def test_lfu_put_get_touch_frequency_and_resize(lfu_factory) -> None:
    cache = lfu_factory(
        Config(
            capacity=2,
            hash_key=hash,
            compare_key=lambda a, b: 0 if a == b else 1,
        ))

    assert cache.put("a", 1) == (None, None, False, False)
    assert cache.put("b", 2) == (None, None, False, False)
    assert cache.get("a") == (1, True)
    assert cache.touch("a") is True
    assert cache.touch("missing") is False
    freq, ok = cache.frequency("a")
    assert ok is True
    assert freq >= 2
    assert cache.frequency("missing") == (0, False)

    evicted_key, evicted_value, replaced, evicted = cache.put("c", 3)
    assert evicted is True
    assert replaced is False
    assert (evicted_key, evicted_value) == ("b", 2)
    old_key, old_value, replaced, evicted = cache.put("a", 9)
    assert (old_key, old_value, replaced, evicted) == ("a", 1, True, False)
    assert cache.get("a") == (9, True)
    assert cache.peek("a") == (9, True)
    assert cache.remove("a") == ("a", 9, True)
    assert cache.remove("missing") == (None, None, False)

    evicted_items, resize_ok = cache.resize(1)
    assert resize_ok is True
    assert len(evicted_items) <= 1


def test_lfu_for_each_and_clear(lfu_factory) -> None:
    freed_keys: list[str] = []
    freed_values: list[int] = []
    cache = lfu_factory(
        Config(
            capacity=2,
            hash_key=hash,
            compare_key=lambda a, b: 0 if a == b else 1,
            free_key=freed_keys.append,
            free_value=freed_values.append,
        ))
    seen: dict[str, int] = {}

    assert cache.put("x", 10)[-1] is False
    assert cache.put("y", 20)[-1] is False
    cache.for_each(lambda key, value: seen.__setitem__(key, value))
    assert seen == {"x": 10, "y": 20}

    cache.clear()
    assert sorted(freed_keys) == ["x", "y"]
    assert sorted(freed_values) == [10, 20]
    assert cache.is_empty() is True


def test_lfu_clear_is_idempotent(lfu_factory) -> None:
    freed_keys: list[str] = []
    freed_values: list[int] = []
    cache = lfu_factory(
        Config(
            capacity=1,
            hash_key=hash,
            compare_key=lambda a, b: 0 if a == b else 1,
            free_key=freed_keys.append,
            free_value=freed_values.append,
        ))

    assert cache.put("k", 1)[-1] is False
    cache.clear()
    cache.clear()

    assert freed_keys == ["k"]
    assert freed_values == [1]
