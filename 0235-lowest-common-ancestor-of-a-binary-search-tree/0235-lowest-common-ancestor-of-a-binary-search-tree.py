# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ancestor = None
        
        def helper(root, node):
            if not root:
                return root is node
            if root is node:
                return True
            return helper(root.left, node) or helper(root.right, node)
        
        def findBoth(root, p, q):
            nonlocal ancestor
            if not root:
                return False
            if ancestor:
                return True
            findBoth(root.left, p, q)
            findBoth(root.right, p, q)
            
            a = helper(root, p)
            b = helper(root, q)
            if a and b and ancestor == None:
                ancestor = root
            return a or b
           
        findBoth(root, p, q)
        return ancestor
        