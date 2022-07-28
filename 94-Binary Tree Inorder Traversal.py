# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        if not root.left and not root.right:
            return [root.val]
        
        left=self.inorderTraversal(root.left) if root.left else []
            
        right=self.inorderTraversal(root.right) if root.right else []
            
        return left + [root.val] + right
