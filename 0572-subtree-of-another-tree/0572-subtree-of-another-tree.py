# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.isEqual = False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return root is subRoot
        self.isEqual = self.isEqual or self.isSameTree(root, subRoot)
        l = self.isSubtree(root.left, subRoot)
        r = self.isSubtree(root.right, subRoot)
        
        return self.isEqual
        
        
        
            
        
        
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p == q
        