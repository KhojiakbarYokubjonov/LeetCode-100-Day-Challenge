# Definition for doubly-linked list.
class ListNode:
    def __init__(self, key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

        
    def __str__(self):
        return f"{self.key}={self.val}"
    
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.table = {} 
        self.left = ListNode(0,0)
        self.right = ListNode(0,0)
        
        self.left.next, self.right.prev = self.right, self.left
        
    
        
    def get(self, key: int) -> int:
        if key not in self.table:
            return -1
        self.remove(self.table[key])
        self.insert(self.table[key])
        return self.table[key].val
       

    def put(self, key: int, value: int) -> None:
        if key in self.table:
            self.remove(self.table[key])
        
        self.table[key] = ListNode(key, value)
        self.insert(self.table[key])
        
        
        if len(self.table) > self.capacity:
            temp = self.left.next
            self.remove(temp)
            print("deleting", self.left.next)
            self.table.pop(temp.key)
            
        
        
    
    
  # remove node from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert node at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
        
            
                    
                

















