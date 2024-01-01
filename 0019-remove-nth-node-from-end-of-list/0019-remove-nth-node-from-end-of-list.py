# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
       
        def helper(head):
            nonlocal n
            if not head:
                return head
            head.next = helper(head.next)
            n -= 1
            if n == 0:
                return head.next
            
        
            
            return head
        return helper(head)