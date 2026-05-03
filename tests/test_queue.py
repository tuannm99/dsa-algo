from __future__ import annotations

from python.queue.queue import Config


def test_queue_fifo_behavior(queue_factory) -> None:
    queue = queue_factory(Config(initial_capacity=1))

    assert queue.is_empty() is True
    assert queue.peek() == (None, False)
    assert queue.dequeue() == (None, False)
    assert queue.enqueue(1) is True
    assert queue.enqueue(2) is True
    assert queue.peek() == (1, True)
    assert queue.dequeue() == (1, True)
    assert queue.dequeue() == (2, True)
    assert queue.dequeue() == (None, False)


def test_queue_for_each_and_clear(queue_factory) -> None:
    freed: list[int] = []
    queue = queue_factory(Config(free_value=freed.append))
    seen: list[int] = []

    for value in (4, 5, 6):
        assert queue.enqueue(value) is True

    queue.for_each(seen.append)
    assert seen == [4, 5, 6]

    queue.clear()
    assert sorted(freed) == [4, 5, 6]
    assert queue.is_empty() is True


def test_queue_clear_is_idempotent(queue_factory) -> None:
    freed: list[int] = []
    queue = queue_factory(Config(free_value=freed.append))

    assert queue.enqueue(1) is True
    queue.clear()
    queue.clear()

    assert freed == [1]
