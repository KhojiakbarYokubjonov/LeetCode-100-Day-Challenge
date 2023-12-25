# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Idea: use the BFS approach and add the last node of each tree level to the output array
    """
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        nodes = []
        def DFS(current, level):
            if not current:
                return None
            if len(nodes)-1 < level:
                nodes.append(None)
            
            DFS(current.left, level+1)
            DFS(current.right, level+1)
            
            nodes[level] = current.val
        DFS(root, 0)
        return nodes
        