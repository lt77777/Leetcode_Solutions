class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        for i in range(len(matrix)):                    # Same trick as problem 84.  
            matrix[i] += ["0"]
        
        m, n = len(matrix), len(matrix[0])
        h = [0 for _ in range(n)]
        res = 0
        
        for i in range(m):                              # Doing this problem row by row.
            stack = [-1]                                # Same trick as problem 84.  
            
            for j in range(n):
                if matrix[i][j] == "1":                 # Update h if current cell is not "0".
                    h[j] += 1           
                else:
                    h[j] = 0                            # Otherwise, there is no continuous "1" at current col, make h[j] 0 again.
                    
                while h[j] < h[stack[-1]]:              # Use increasing stack as problem 84. do.
                    height = h[stack.pop()]             # Since we have put 0 in the last col,
                    width = (j - stack[-1] - 1)         # It will always extract everything in stack.
                    res = max(res, width*height)
                
                stack.append(j)
                
        return res
        
