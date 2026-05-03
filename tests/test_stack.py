from __future__ import annotations

from python.stack.stack import Config


def test_stack_lifo_behavior(stack_factory) -> None:
    stack = stack_factory(Config(initial_capacity=1))

    assert stack.is_empty() is True
    assert stack.peek() == (None, False)
    assert stack.pop() == (None, False)
    assert stack.push(1) is True
    assert stack.push(2) is True
    assert stack.size() == 2
    assert stack.peek() == (2, True)
    assert stack.pop() == (2, True)
    assert stack.pop() == (1, True)
    assert stack.pop() == (None, False)


def test_stack_for_each_and_clear(stack_factory) -> None:
    freed: list[int] = []
    stack = stack_factory(Config(free_value=freed.append))
    seen: list[int] = []

    for value in (1, 2, 3):
        assert stack.push(value) is True

    stack.for_each(seen.append)
    assert sorted(seen) == [1, 2, 3]

    stack.clear()
    assert sorted(freed) == [1, 2, 3]
    assert stack.is_empty() is True


def test_stack_clear_is_idempotent(stack_factory) -> None:
    freed: list[int] = []
    stack = stack_factory(Config(free_value=freed.append))

    assert stack.push(1) is True
    stack.clear()
    stack.clear()

    assert freed == [1]
