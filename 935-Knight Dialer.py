class Solution:
    def knightDialer(self, n: int) -> int:
        # TC: O(N)
        # SC: O(10)
        # start -> next
        #     0 -> 4, 6
        #     1 -> 6, 8
        #     2 -> 7, 9
        #     3 -> 4, 8
        #     4 -> 0, 3, 9
        #     5 -> 
        #     6 -> 0, 1, 7
        #     7 -> 2, 6
        #     8 -> 1, 3
        #     9 -> 2, 4
        # dp to store no. of possibilities starting at each digit from 0 to 9.
        # for n == 1, all are ones.
        dp = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

        for i in range(2, n + 1):
            dp = [
                dp[4] + dp[6],
                dp[6] + dp[8],
                dp[7] + dp[9],
                dp[4] + dp[8],
                dp[0] + dp[3] + dp[9],
                0,
                dp[0] + dp[1] + dp[7],
                dp[2] + dp[6],
                dp[1] + dp[3],
                dp[2] + dp[4]
            ]

        return sum(dp) % (10**9 + 7)
        
