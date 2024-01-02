# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        
        for head in lists:
            while head:
                nodes.append(head)
                head = head.next
        nodes.sort(key = lambda x:x.val)
        head = curr = None
        
        for n in nodes:
            n.next = None
            if not head:
                curr = head = n
            else:
                curr.next = n
                curr = curr.next
        return head
                
        
        
        
        
        