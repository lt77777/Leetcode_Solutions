# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        freq = dict()
        q = deque()
        if not root:
            return
        q.append(root)
        while len(q) > 0:
            curr = q.pop()
            if curr.val not in freq.keys():
                freq[curr.val] = 1
            else:
                freq[curr.val] += 1
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        rtn = []
        best = max(freq.values())
        for i in freq.keys():
            if freq[i] == best:
                rtn.append(i)
        return rtn
                
        
