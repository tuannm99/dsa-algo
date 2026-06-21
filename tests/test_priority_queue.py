from __future__ import annotations

from python.priorityqueue import Config, HeapPriorityQueue


def test_priority_queue_min_first_and_stable_ties() -> None:
    queue = HeapPriorityQueue[str](Config(min_first=True))

    assert queue.peek() == (0, None, False)
    assert queue.push(2, "b") is True
    assert queue.push(1, "a") is True
    assert queue.push(1, "aa") is True
    assert queue.peek() == (1, "a", True)
    assert queue.pop() == (1, "a", True)
    assert queue.pop() == (1, "aa", True)
    assert queue.pop() == (2, "b", True)
    assert queue.pop() == (0, None, False)


def test_priority_queue_max_first_for_each_and_clear() -> None:
    freed: list[str] = []
    queue = HeapPriorityQueue[str](
        Config(min_first=False, free_value=freed.append))
    seen: list[str] = []

    assert queue.push(1, "low") is True
    assert queue.push(3, "high") is True
    assert queue.peek() == (3, "high", True)

    queue.for_each(seen.append)
    assert seen == ["high", "low"]

    queue.clear()
    assert sorted(freed) == ["high", "low"]
    assert queue.is_empty() is True
