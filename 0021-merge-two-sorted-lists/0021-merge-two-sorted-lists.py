# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val > list2.val:
            list1, list2 = list2, list1

        curr = list1
        
        while list2:
            if not curr.next:
                curr.next = list2
                break
            if curr.next.val > list2.val:
                temp = curr.next
                curr.next = list2
                temp2 = list2.next
                curr.next.next = temp
                list2 = temp2
            else:
                curr = curr.next
        return list1
        
        