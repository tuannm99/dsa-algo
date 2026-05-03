from __future__ import annotations

from python.deque.deque import Config


def test_deque_double_ended_behavior(deque_factory) -> None:
    deque = deque_factory(Config(initial_capacity=1))

    assert deque.peek_front() == (None, False)
    assert deque.peek_back() == (None, False)
    assert deque.pop_back() == (None, False)
    assert deque.push_back(2) is True
    assert deque.push_front(1) is True
    assert deque.push_back(3) is True
    assert deque.peek_front() == (1, True)
    assert deque.peek_back() == (3, True)
    assert deque.pop_front() == (1, True)
    assert deque.pop_back() == (3, True)
    assert deque.pop_back() == (2, True)
    assert deque.pop_front() == (None, False)
    assert deque.pop_back() == (None, False)


def test_deque_for_each_and_clear(deque_factory) -> None:
    freed: list[int] = []
    deque = deque_factory(Config(free_value=freed.append))
    seen: list[int] = []

    for value in (7, 8, 9):
        assert deque.push_back(value) is True

    deque.for_each(seen.append)
    assert seen == [7, 8, 9]

    deque.clear()
    assert sorted(freed) == [7, 8, 9]
    assert deque.is_empty() is True


def test_deque_clear_is_idempotent(deque_factory) -> None:
    freed: list[int] = []
    deque = deque_factory(Config(free_value=freed.append))

    assert deque.push_front(1) is True
    deque.clear()
    deque.clear()

    assert freed == [1]
