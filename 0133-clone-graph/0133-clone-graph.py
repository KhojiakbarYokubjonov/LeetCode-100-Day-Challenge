"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        seen = {}
        def dfs(node):
            if node == None or node.val in seen:
                return
        
            seen[node.val] = []
            for n in node.neighbors:
                seen[node.val].append(n.val)
                dfs(n)
        dfs(node)
        if len(seen) == 0:
            return None
        root = None
        copy = {}
        for val in seen:
            copy[val] = Node(val)
            
        for k in seen:
            for n in seen[k]:
                copy[k].neighbors.append(copy[n])
        return copy[1]
        
        
            