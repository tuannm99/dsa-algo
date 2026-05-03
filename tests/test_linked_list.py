from __future__ import annotations

from python.linkedlist.linkedlist import Config


def test_linked_list_push_peek_and_pop(linked_list_factory) -> None:
    linked_list = linked_list_factory()

    assert linked_list.is_empty() is True
    assert linked_list.front() == (None, False)
    assert linked_list.back() == (None, False)
    assert linked_list.get(0) == (None, False)
    assert linked_list.pop_back() == (None, False)
    assert linked_list.push_front(2) is True
    assert linked_list.push_back(3) is True
    assert linked_list.push_front(1) is True
    assert linked_list.size() == 3
    assert linked_list.front() == (1, True)
    assert linked_list.back() == (3, True)
    assert linked_list.get(1) == (2, True)
    assert linked_list.pop_front() == (1, True)
    assert linked_list.pop_back() == (3, True)
    assert linked_list.pop_front() == (2, True)
    assert linked_list.pop_front() == (None, False)
    assert linked_list.pop_back() == (None, False)


def test_linked_list_insert_remove_reverse_and_clear(
        linked_list_factory) -> None:
    freed: list[int] = []
    linked_list = linked_list_factory(Config(free_value=freed.append))

    for value in (1, 3, 4):
        assert linked_list.push_back(value) is True

    assert linked_list.insert(1, 2) is True
    assert linked_list.insert(4, 5) is True
    assert linked_list.insert(10, 99) is False
    assert linked_list.remove_at(2) == (3, True)
    assert linked_list.remove_at(9) == (None, False)
    assert linked_list.remove_value(4, lambda a, b: a - b) == (4, True)
    assert linked_list.remove_value(42, lambda a, b: a - b) == (None, False)

    seen: list[int] = []
    linked_list.reverse()
    linked_list.for_each(seen.append)
    assert seen == [5, 2, 1]

    linked_list.clear()
    assert freed == [1, 2, 5]
    assert linked_list.is_empty() is True


def test_linked_list_edge_indexes_and_empty_reverse(
        linked_list_factory) -> None:
    linked_list = linked_list_factory()

    linked_list.reverse()
    assert linked_list.insert(-1, 1) is False
    assert linked_list.insert(1, 1) is False
    assert linked_list.remove_at(-1) == (None, False)
    assert linked_list.remove_value(9, lambda a, b: a - b) == (None, False)
