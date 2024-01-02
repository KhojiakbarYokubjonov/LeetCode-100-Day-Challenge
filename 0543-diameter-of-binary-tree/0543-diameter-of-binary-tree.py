# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxD = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            
            # diameter may not always pass from the root
            # so we keep track of the max diam at each sub root
            self.maxD = max(self.maxD, left+right)
            return 1 + max(left, right)
        helper(root)
        return self.maxD
            
            
        