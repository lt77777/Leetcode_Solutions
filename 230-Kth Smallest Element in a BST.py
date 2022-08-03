# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = self.dfs(root)
        values.sort()
        return values[k-1]
    
    def dfs(self, root):
        if root is None:
            return []
        return self.dfs(root.left) + [root.val] + self.dfs(root.right)
