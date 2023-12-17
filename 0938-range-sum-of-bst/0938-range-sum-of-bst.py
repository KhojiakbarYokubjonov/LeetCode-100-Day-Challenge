# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return self.BFS(root,low, high)
        
    
    def solDFS(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        if low <= root.val <= high:
            return root.val + self.solDFS(root.left, low, high) + self.solDFS(root.right, low, high)
        return 0 + self.solDFS(root.left, low, high) + self.solDFS(root.right, low, high)

    def stackDFS(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        total = 0
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            if low <= node.val <= high:
                total += node.val
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return total
    
    def BFS(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        queue = []
        total = 0
        queue.append(root)
        
        while queue:
            node = queue.pop(0)
            if low <= node.val <= high:
                total += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return total
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        