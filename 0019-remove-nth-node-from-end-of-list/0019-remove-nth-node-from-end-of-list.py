# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
       
        def reverse(head):
            if not head or not head.next:
                return head
            
            new = reverse(head.next)
            head.next.next = head
            head.next = None
            
            return new
        reverseH = reverse(head)
        if reverseH and n == 1:
            return reverse(reverseH.next)
        curr = reverseH
        while curr and curr.next:
            if n-1 == 1:
                curr.next = curr.next.next
            else:
                curr = curr.next
            n -= 1
                
        # print(reverseH)
        
        return reverse(reverseH)