# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p or not q:
            return False
        return self.bfs(p) == self.bfs(q)
    def bfs(self, a):
        rtn = [a.val]
        if a.left:
            rtn += self.bfs(a.left)
        else:
            rtn.append(None)
        if a.right:
            rtn += self.bfs(a.right)
        else:
            rtn.append(None)
        return rtn
        
