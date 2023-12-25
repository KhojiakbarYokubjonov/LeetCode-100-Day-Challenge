# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        nodes = []
        queue = [root]
        while queue:
            node = queue[-1]
            nodes.append(node.val)
            # remove all nodes in queue and add their children
            size = len(queue)
            while size > 0:
                curr = queue.pop(0)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                size -= 1
            
        return nodes
        