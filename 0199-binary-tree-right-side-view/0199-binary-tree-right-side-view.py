# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Solution using the DFS
    """
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        nodes = []
        def DFS(current, level):
            if not current:
                return None
            # this is a placeholder for the current level, so that we can index into it later
            if len(nodes)-1 < level:
                nodes.append(None)
            
            DFS(current.left, level+1)
            DFS(current.right, level+1)
            
            nodes[level] = current.val
        DFS(root, 0)
        return nodes
        