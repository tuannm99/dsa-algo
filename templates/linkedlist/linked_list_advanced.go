package linkedlist

func RemoveNthFromEnd(head *ListNode, n int) *ListNode {
	dummy := &ListNode{Next: head}
	slow, fast := dummy, dummy
	for i := 0; i < n; i++ {
		fast = fast.Next
	}
	for fast.Next != nil {
		slow = slow.Next
		fast = fast.Next
	}
	slow.Next = slow.Next.Next
	return dummy.Next
}

func ReorderList(head *ListNode) {
	if head == nil || head.Next == nil {
		return
	}

	slow, fast := head, head
	for fast.Next != nil && fast.Next.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}

	second := ReverseList(slow.Next)
	slow.Next = nil
	first := head

	for second != nil {
		nextFirst := first.Next
		nextSecond := second.Next
		first.Next = second
		second.Next = nextFirst
		first = nextFirst
		second = nextSecond
	}
}
