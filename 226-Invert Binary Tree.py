# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def invert(node):

            # If there is a node
            if node:

                # Invert the left subtree and the right subtree
                left, right = invert(node.left), invert(node.right)

                # Swap the head of the left subtree with the head of the right subtree
                node.left, node.right = right, left

            return node

        return invert(root)
