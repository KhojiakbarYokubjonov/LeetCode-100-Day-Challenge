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
                return None,0
            if root.val in (p.val, q.val):
                return root, 1
            
            nodel,count = helper(root.left,p,q)
            if count == 2: 
                return nodel,count
            noder,count2 = helper(root.right,p,q)
            
            if nodel != None and noder != None:
                return root, 2
            if nodel != None:
                return nodel,1
            if noder != None:
                return noder,1
            return None,0
        
        node,_ = helper(root,p,q)
        return node
            
            
        