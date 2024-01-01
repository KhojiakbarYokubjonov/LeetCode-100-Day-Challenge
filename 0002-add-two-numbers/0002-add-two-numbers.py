# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        saved = 0
        result = ListNode(0)
        curr_result = result
        
        if not l1 and not l2:
            return ListNode(0)
        
        while l1 and l2:
            total = l1.val + l2.val + saved
            sec_digit = total % 10
            first_digit = (total - sec_digit) // 10
            
            curr_result.next = ListNode(total % 10)
            saved = first_digit
            
            curr_result = curr_result.next
            
            if not l1.next and not l2.next:
                break
            if not l1.next:
                l1.next = ListNode(0)
            if not l2.next:
                l2.next = ListNode(0)
            
            l1, l2 = l1.next, l2.next
        if saved:
            curr_result.next = ListNode(saved)
        return result.next
            
            
        