class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        
        def dfs(i, j, prev):
            if (i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j] <= prev):
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            
            
            top = bottom = left = right = 0
            if i+1 < len(matrix) and matrix[i][j] < matrix[i+1][j]:
                top = 1 + dfs(i+1, j, matrix[i][j])
            if i-1 >= 0 and matrix[i][j] < matrix[i-1][j]:
                bottom = 1 + dfs(i-1, j, matrix[i][j])
            if j+1 < len(matrix[0]) and matrix[i][j] < matrix[i][j+1]:
                right = 1 + dfs(i, j+1, matrix[i][j])
            if j-1 >= 0 and matrix[i][j] < matrix[i][j-1]:
                left = 1 + dfs(i, j-1, matrix[i][j])
            
            dp[(i, j)] = max(top, bottom, left, right)
            return dp[(i, j)]
        
        mxpath = -1
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                mxpath = max(dfs(i,j, -1), mxpath)
                
        return mxpath + 1 # add +1 to include the starting cell for the path
                
            
            
                
        