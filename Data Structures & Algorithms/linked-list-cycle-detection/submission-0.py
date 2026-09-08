# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        seen = set()
        curr_node = head

        while curr_node:
            if curr_node in seen:
                return True
            else:
                seen.add(curr_node)
                curr_node = curr_node.next
        
        return False
        