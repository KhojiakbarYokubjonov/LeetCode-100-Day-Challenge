# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def helper(root, p,q):
            if root == None:
                return None
            if root.val in (p.val, q.val):
                return root
            
            nodel = helper(root.left,p,q)
            noder = helper(root.right,p,q)
            
            if nodel != None and noder != None:
                return root
            if nodel != None:
                return nodel
            if noder != None:
                return noder
        
        node = helper(root,p,q)
        return node
            
            
        