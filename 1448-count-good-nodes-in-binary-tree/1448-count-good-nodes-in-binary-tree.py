# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
     def goodNodes(self, root: TreeNode) -> int:
        # Our counter for the good nodes.
        count = 0
        
        def helper(root, mx):
            nonlocal count
            if not root:
                return
            if root.val >= mx:
                count += 1
                mx = root.val
            
            helper(root.left, mx)
            helper(root.right, mx)
            
        helper(root, root.val)
        
        return count
                
            
        
        