# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
       
        count = n
        def helper(head):
            nonlocal count
            if not head:
                return head
            head.next = helper(head.next)
            print(head)
            count -= 1
            if count == 0:
                return head.next
            
        
            
            return head
        return helper(head)