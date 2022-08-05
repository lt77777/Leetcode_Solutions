class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rtn = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 0:
                    continue
                curr = 0
                if not x+1 == len(grid[0]):
                    if grid[y][x + 1] == 1:
                        curr += 1
                if not x-1 == -1:
                    if grid[y][x - 1] == 1:
                        curr += 1
                if not y+1 == len(grid):
                    if grid[y+1][x] == 1:
                        curr += 1
                if not y-1 == -1:
                    if grid[y-1][x] == 1:
                        curr += 1
                rtn += (4-curr)
        return rtn
                    
                    
                    
