# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def helper(root):
            if not root:
                return 'null'
            return ",".join([str(root.val), helper(root.left), helper(root.right)])
        output = helper(root)
        
        return helper(root)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")
        def helper():
            if data[0] == 'null':
                data.pop(0)
                return None
            
            root = TreeNode(int(data.pop(0)))
            root.left = helper()
            root.right = helper()
            return root
        root = helper()
        return root
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))