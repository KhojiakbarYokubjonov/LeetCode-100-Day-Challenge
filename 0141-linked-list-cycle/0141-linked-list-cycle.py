# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = {head}
        
        while head:
            if head.next in seen:
                return True
            seen.add(head.next)
            head = head.next
        return False
        
        