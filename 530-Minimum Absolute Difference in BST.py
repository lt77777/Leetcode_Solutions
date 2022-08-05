# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        quene = deque()
        quene.appendleft(root)
        nodes = []
        while len(quene) != 0:
            curr = quene.pop()
            nodes.append(curr.val)
            if curr.left:
                quene.appendleft(curr.left)
            if curr.right:
                quene.appendleft(curr.right)
        nodes.sort()
        rtn = 1000000
        for i in range(len(nodes)-1):
            curr = abs(nodes[i+1]-nodes[i])
            if curr < rtn:
                rtn = curr
        return rtn
 
