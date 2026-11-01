class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        second = head

        for _ in range(n):
            first = first.next

        if first is None:
            return head.next

        while first.next is not None:
            first = first.next
            second = second.next

        second.next = second.next.next

        return head