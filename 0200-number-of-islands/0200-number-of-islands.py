class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        
        count = 0
        seen = set()
        def dfs(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]) or grid[row][col] == '0' or grid[row][col] == 'x':
                return 0
            grid[row][col] = 'x'
            return (1   + dfs(row, col-1)
                        + dfs(row, col+1)   
                        + dfs(row-1, col)
                        + dfs(row+1, col)
                        )
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1' and dfs(i,j) > 0:
                    count += 1
        return count
        
        
"""
[   ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]]
    

[   ['1', '1', '1', '1', '0'], 
    ['x', 'x', '0', '1', '0'], 
    ['x', 'x', '0', '0', '0'], 
    ['0', '0', '0', '0', '0']]

"""