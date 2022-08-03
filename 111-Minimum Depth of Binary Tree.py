# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)
    
    def dfs(self,root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if not root.left:
            return self.dfs(root.right) + 1
        if not root.right:
            return self.dfs(root.left) + 1
        return min(self.dfs(root.left) + 1, self.dfs(root.right) + 1)
        
