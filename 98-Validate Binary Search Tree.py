# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def isValidNode(node, gt, lt):
    if not node:
        return True
    if node.val > gt and node.val < lt:
        valid_left = isValidNode(node.left, gt, node.val)
        valid_right = isValidNode(node.right, node.val, lt)
        return True if valid_left and valid_right else False
    else:
        return False
        

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return True if isValidNode(root, -2**31 - 1, 2**31 + 2) else False
