from .linked_list import ListNode, reverse_list


def remove_nth_from_end(head: ListNode | None, n: int) -> ListNode | None:
    dummy = ListNode(0, head)
    slow = fast = dummy
    for _ in range(n):
        assert fast.next is not None
        fast = fast.next
    while fast.next is not None:
        slow = slow.next
        fast = fast.next
    assert slow.next is not None
    slow.next = slow.next.next
    return dummy.next


def reorder_list(head: ListNode | None) -> None:
    if head is None or head.next is None:
        return

    slow = fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

    second = reverse_list(slow.next)
    slow.next = None
    first = head

    while second is not None:
        next_first = first.next
        next_second = second.next
        first.next = second
        second.next = next_first
        first = next_first
        second = next_second
