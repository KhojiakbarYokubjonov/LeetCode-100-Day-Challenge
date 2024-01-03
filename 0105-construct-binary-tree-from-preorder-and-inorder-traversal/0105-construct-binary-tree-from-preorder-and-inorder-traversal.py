# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
     def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        loc = {x : i for i, x in enumerate(inorder)}
        root = None
        stack = []
        for x in preorder: 
            if not root: root = node = TreeNode(x)
            elif loc[x] < loc[node.val]: 
                stack.append(node)
                node.left = node = TreeNode(x)
            else: 
                while stack and loc[stack[-1].val] < loc[x]:
                    node = stack.pop()
                node.right = node = TreeNode(x)

        return root
        