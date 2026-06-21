from __future__ import annotations

from python.monotonicqueue import Config, WindowMonotonicQueue


def test_monotonic_queue_decreasing_for_sliding_window_max() -> None:
    queue = WindowMonotonicQueue(Config(decreasing=True))

    queue.push(1)
    queue.push(3)
    queue.push(2)

    assert queue.front() == (3, True)
    assert queue.pop(1) is False
    assert queue.pop(3) is True
    assert queue.front() == (2, True)


def test_monotonic_queue_increasing_for_sliding_window_min() -> None:
    queue = WindowMonotonicQueue(Config(decreasing=False))

    queue.push(3)
    queue.push(1)
    queue.push(2)

    assert queue.front() == (1, True)
    assert queue.pop(3) is False
    assert queue.pop(1) is True
    assert queue.front() == (2, True)
