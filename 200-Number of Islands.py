class Solution(object):
    def numIslands(self, grid):
        island = 0
        
        def dfs(r, c):
            # base case
            if not(0 <= r < len(grid) and 0 <= c < len(grid[0])): return
            # not unvisited land
            if grid[r][c] != "1": return
            # mark current land as visited land
            grid[r][c] = "2"
            # traverse neighbors
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
            return
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1": 
                    dfs(r, c)
                    island += 1
        return island
    
