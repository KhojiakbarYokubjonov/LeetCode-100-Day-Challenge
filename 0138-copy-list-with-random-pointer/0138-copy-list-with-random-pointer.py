"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        curr = head
        
        new = Node(curr.val)
        newcopy = new
        mapping = {}
        mapping[curr] = new
        
        # creates a copy of the linked list and connects them via the next pointers
        while curr.next:
            new.next = Node(curr.next.val)
            
            # maps the old node to its new copy (used to connect the random pointers)
            mapping[curr.next] = new.next
            new = new.next
            curr = curr.next
        
        # finds the random points of the new linkedlist using the mapping
        for node in mapping:
            copy = mapping[node]
            old_random = node.random
            if old_random:
                copy.random = mapping[old_random]
                print(f"node[{copy.val}] rand [{copy.random.val}]")
            else:
                copy.random = None
        
        return newcopy
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        