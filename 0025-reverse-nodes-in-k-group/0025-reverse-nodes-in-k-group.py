# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes = []

        while head:
            nodes.append(head)
            head = head.next
        def reverse(l, r):
            while l < r:
                nodes[l], nodes[r] = nodes[r], nodes[l]
                l += 1
                r -= 1
        for i in range(0, len(nodes), k):
            if i+k-1 < len(nodes):
                reverse(i, i+k-1)
        head = curr = None
        
        for n in nodes:
            n.next = None
            if not head:
                head = curr = n
            else:
                curr.next = n
                curr = curr.next
        return head
            
                
            