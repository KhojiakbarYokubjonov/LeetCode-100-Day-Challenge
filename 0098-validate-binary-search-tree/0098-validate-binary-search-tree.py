# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Idea: specify min and max boundaries for each node val
    """
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(root, minVal, maxVal):
            if not root:
                return True
            if root.val <= minVal or root.val >= maxVal:
                return False
            
            return helper(root.left, minVal, root.val) and helper(root.right, root.val, maxVal)
        
        return helper(root, float('-inf'), float('inf'))
            
        
        