from __future__ import annotations

from python.heap.heap import Config


def test_heap_ordering_and_replace_top(heap_factory) -> None:
    heap = heap_factory(Config(initial_capacity=0, compare=lambda a, b: a - b))

    assert heap.peek() == (None, False)
    assert heap.pop() == (None, False)
    assert heap.replace_top(1) == (None, False)
    assert heap.push(3) is True
    assert heap.push(1) is True
    assert heap.push(2) is True
    assert heap.peek() == (1, True)
    assert heap.replace_top(4) == (1, True)
    assert heap.pop() == (2, True)
    assert heap.pop() == (3, True)
    assert heap.pop() == (4, True)
    assert heap.pop() == (None, False)


def test_heap_for_each_and_clear(heap_factory) -> None:
    freed: list[int] = []
    heap = heap_factory(
        Config(initial_capacity=0,
               compare=lambda a, b: a - b,
               free_value=freed.append))
    seen: list[int] = []

    for value in (5, 1, 4):
        assert heap.push(value) is True

    heap.for_each(seen.append)
    assert sorted(seen) == [1, 4, 5]

    heap.clear()
    assert sorted(freed) == [1, 4, 5]
    assert heap.is_empty() is True


def test_heap_clear_is_idempotent(heap_factory) -> None:
    freed: list[int] = []
    heap = heap_factory(
        Config(initial_capacity=0,
               compare=lambda a, b: a - b,
               free_value=freed.append))

    assert heap.push(2) is True
    heap.clear()
    heap.clear()

    assert freed == [2]
