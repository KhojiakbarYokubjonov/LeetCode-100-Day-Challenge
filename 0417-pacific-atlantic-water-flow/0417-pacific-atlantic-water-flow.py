class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        ROW = len(heights)
        COL = len(heights[0])
        
        def dfs(r, c, visited, prevH):
            if (r < 0 or c < 0 or r >= ROW or c >= COL
                or (r, c) in visited 
                or heights[r][c] < prevH):
                return
            visited.add((r,c))
            
            for i,j in directions:
                dfs(r+i, c+j, visited, heights[r][c])
            
        for col in range(COL):
            dfs(0, col, pac, heights[0][col])
            dfs(ROW-1, col, atl, heights[ROW-1][col])
            
        for row in range(ROW):
            dfs(row, 0, pac, heights[row][0])
            dfs(row, COL-1, atl, heights[row][col])
        
        res = []
        print(pac)
        print(atl)
        for i in range(ROW):
            for j in range(COL):
                if (i, j) in pac and (i, j) in atl:
                    res.append([i, j])
        return res
            
        