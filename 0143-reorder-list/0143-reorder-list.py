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
        if not head or not head.next:
            return head
        nodes = []
        
        curr = head
        
        while curr:
            nodes.append(curr)
            curr = curr.next
        
        l, r = 0, len(nodes)-1
        mid = len(nodes) // 2
        
        head = None
        
        while l < r:
            nodes[l].next, nodes[r].next = None, None
            if not head:
                curr = head = nodes[l]
                curr.next = nodes[r]
                curr = curr.next
            else:
                curr.next = nodes[l]
                curr.next.next = nodes[r]
                curr = curr.next.next
            l += 1
            r -= 1
        if len(nodes) % 2 == 1:
            nodes[l].next = None
            curr.next = nodes[l]

        return head
    
    
    
    
    
    
    
    
    
    
    
    
    
    
            