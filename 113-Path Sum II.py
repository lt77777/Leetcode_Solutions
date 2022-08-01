# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        if not root:
            return []
		# Array to hold the final result to be returned
        final_result = []
		# Back Tracking Solution
        def backtrack(node, path, target_sum):
			# Base condition: If the node is leaf node and the value is exactly the value we need, add it to final result.
            if target_sum == node.val and node.left == None and node.right == None:
                path.append(node.val)
                final_result.append(path)
                return
            else:
				# Recursively traverse the left side of the current node with the new targetSum
                if node.left:
                    backtrack(node.left, path + [node.val], target_sum - node.val )
				# Recursively traverse the right side of the current node with the new targetSum
                if node.right:
                    backtrack(node.right, path + [node.val], target_sum - node.val)
                return
		# Call the backtrack function.
        backtrack(root, [], targetSum)
        return (final_result)
