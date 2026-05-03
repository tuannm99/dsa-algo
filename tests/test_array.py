from __future__ import annotations

from typing import cast

from python.array import Array, Config


def test_array_implements_protocol(array_factory) -> None:
    arr: Array[int] = cast(Array[int], array_factory())
    assert arr.is_empty() is True
    assert arr.size() == 0
    assert arr.capacity() == 0
    assert arr.get(0) == (None, False)
    assert arr.remove(0) == (None, False)
    assert arr.pop() == (None, False)


def test_array_push_get_set_and_pop(array_factory) -> None:
    arr = array_factory()

    assert arr.push(10) is True
    assert arr.push(20) is True
    assert arr.size() == 2
    assert arr.get(0) == (10, True)
    assert arr.get(1) == (20, True)
    assert arr.get(2) == (None, False)

    assert arr.set(1, 25) is True
    assert arr.set(2, 30) is False
    assert arr.get(1) == (25, True)
    assert arr.pop() == (25, True)
    assert arr.pop() == (10, True)
    assert arr.pop() == (None, False)


def test_array_capacity_reserve_and_shrink_to_fit(array_factory) -> None:
    arr = array_factory(Config(initial_capacity=2))

    assert arr.capacity() == 2
    assert arr.push(1) is True
    assert arr.push(2) is True
    assert arr.capacity() == 2
    assert arr.push(3) is True
    assert arr.capacity() == 4

    assert arr.reserve(10) is True
    assert arr.capacity() == 10
    assert arr.reserve(2) is True
    assert arr.capacity() == 10
    assert arr.shrink_to_fit() is True
    assert arr.capacity() == 3


def test_array_handles_edge_indexes(array_factory) -> None:
    arr = array_factory()

    assert arr.insert(0, 1) is True
    assert arr.insert(-1, 2) is False
    assert arr.get(-1) == (None, False)
    assert arr.set(-1, 99) is False
    assert arr.remove(-1) == (None, False)
    assert arr.get(0) == (1, True)


def test_array_insert_remove_and_index_of(array_factory) -> None:
    arr = array_factory()
    arr.push(1)
    arr.push(3)

    assert arr.insert(1, 2) is True
    assert arr.get(0) == (1, True)
    assert arr.get(1) == (2, True)
    assert arr.get(2) == (3, True)
    assert arr.insert(4, 99) is False

    assert arr.index_of(2, lambda a, b: a - b) == 1
    assert arr.index_of(99, lambda a, b: a - b) == -1
    assert arr.remove(1) == (2, True)
    assert arr.remove(5) == (None, False)


def test_array_for_each_and_clear(array_factory) -> None:
    arr = array_factory()
    seen: list[int] = []

    for value in (4, 5, 6):
        arr.push(value)

    arr.for_each(seen.append)
    assert seen == [4, 5, 6]

    arr.clear()
    assert arr.is_empty() is True
    assert arr.size() == 0


def test_array_clear_calls_free_value(array_factory) -> None:
    freed: list[int] = []
    arr = array_factory(Config(free_value=freed.append))

    arr.push(7)
    arr.push(8)
    arr.clear()

    assert freed == [7, 8]
    assert arr.is_empty() is True


def test_array_clear_is_idempotent(array_factory) -> None:
    freed: list[int] = []
    arr = array_factory(Config(free_value=freed.append))

    arr.push(1)
    arr.clear()
    arr.clear()

    assert freed == [1]
    assert arr.size() == 0
