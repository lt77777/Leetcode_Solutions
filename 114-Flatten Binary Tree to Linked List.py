class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:

        # check if root exists
        if root:
            
            temp = root.right # store the right part of root
            
            root.right = root.left  # move the left part to the right
            root.left = None        # clear left part
            
            curr = root
            while curr.right:       # use while loop to find the bottom right side
                curr = curr.right
            curr.right = temp       # attach temp back
            
            #recursion
            self.flatten(root.right)
