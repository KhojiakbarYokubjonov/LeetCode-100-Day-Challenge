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
        return self.solution2(root, subRoot)
        if not root:
            return root is subRoot
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) 
         
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p == q
    
    
    def solution2(self, root, subRoot):
        
        def preorderString(root):
            if not root:
                return "null"
            """
            $ sign is used to make the "subRootString in rootString" check more accurate
            """
            return "$" + str(root.val) + "$" + preorderString(root.left) + preorderString(root.right)
            
            
        rootString = preorderString(root)
        subRootString = preorderString(subRoot)
        
        return subRootString in rootString
        