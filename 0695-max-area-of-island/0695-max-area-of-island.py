class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        size = 0
        
        def dfs(r, c):
            nonlocal size
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[r]) or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            
            current = (1    + dfs(r-1,c)
                            + dfs(r+1,c)
                            + dfs(r,c-1)
                            + dfs(r,c+1)    )
            
            size = max(current, size)
            
            return current
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    dfs(i,j)
        return size
        
        