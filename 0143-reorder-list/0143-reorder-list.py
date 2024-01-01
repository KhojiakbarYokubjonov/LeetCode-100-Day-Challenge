# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes = []
        
        curr = head
        
        while curr:
            nodes.append(curr)
            curr = curr.next
        
        l, r = 1, len(nodes)-1
        while l < len(nodes):
            last = nodes.pop()
            nodes.insert(l, last)
            l += 2
        head = nodes[0]
        curr = head
        
        for i in range(1, len(nodes)):
            nodes[i].next = None
            curr.next = nodes[i]
            curr = curr.next
        
        return head
            