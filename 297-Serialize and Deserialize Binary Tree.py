# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        if not root: return 'N'
        
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        
        return ','.join([str(root.val), left, right])
        

    def deserialize(self, data):
        data = data.split(',')
        root = self.buildTree(data)
        return root
        
    def buildTree(self, data):
        val = data.pop(0)
        if val == 'N': return None
        node = TreeNode(val)
        node.left = self.buildTree(data)
        node.right = self.buildTree(data)
        return node

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
