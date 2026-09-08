# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return

        # finds midpoint
        slow = head
        fast = head
        prev = None
        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # split list
        prev.next = None 

        # slow = head of second half
        prev_slow = None
        curr_node = slow

        while curr_node is not None:
            next_node = curr_node.next
            curr_node.next = prev_slow
            prev_slow = curr_node
            curr_node = next_node
        
        # now, second half reversed

        dummy = ListNode()
        tail = dummy

        l1 = head
        l2 = prev_slow

        while l1 and l2:
            tail.next = l1
            l1 = l1.next
            tail = tail.next
            tail.next = l2
            l2 = l2.next
            tail = tail.next
        
        tail.next = l1 if l1 else l2
            