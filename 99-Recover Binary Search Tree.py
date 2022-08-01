# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        inorder = self.inOrder(root)
        print(inorder)
        for i in range(len(inorder)-1):
            if inorder[i].val > inorder[i+1].val:
                minNode = min(inorder[i+1:], key=lambda node: node.val)
                inorder[i].val, minNode.val = minNode.val, inorder[i].val
                break
    def inOrder(self, root):
        if not root:
            return []
        return self.inOrder(root.left) + [root] + self.inOrder(root.right)
    
