# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return sum(int(num) for num in self.binaryTreePaths(root))
        
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        # DFS solution
        output = []
        stack = [(root, '')]
        
        while stack:
            node, path = stack.pop()
            path += str(node.val)
            
            if not node.left and not node.right:
                output.append(path)
            if node.left:
                stack.append((node.left, path))
            if node.right:
                stack.append((node.right, path))
                
        return output
            
