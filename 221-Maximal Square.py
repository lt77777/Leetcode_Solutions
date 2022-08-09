class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        max_len_so_far = 0
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        # set the first row
        for i in range(n):
            dp[0][i] = 1 if matrix[0][i] == '1' else 0
            max_len_so_far = max(max_len_so_far, dp[0][i])
            
        # set the first column
        for i in range(m):
            dp[i][0] = 1 if matrix[i][0] == '1' else 0
            max_len_so_far = max(max_len_so_far, dp[i][0])
            
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                    
                else:
                    min_val = min(dp[i-1][j], dp[i][j-1])
                    if dp[i-min_val][j-min_val] > 0:
                        dp[i][j] = min_val + 1
                    else:
                        dp[i][j] = max(min_val, 1)
                max_len_so_far = max(max_len_so_far, dp[i][j])
        # print(dp) 
        return max_len_so_far * max_len_so_far
    
