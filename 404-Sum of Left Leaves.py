# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        quene = deque()
        rtn = 0
        quene.append(root)
        while len(quene) != 0:
            curr = quene.pop()
            if curr.right:
                quene.appendleft(curr.right)
            if curr.left and not curr.left.left and not curr.left.right:
                rtn += curr.left.val
                continue
            if curr.left:
                quene.appendleft(curr.left)
        return rtn
