class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1]*n for i in range(m)]
        # print(dp)
        
        def dfs(x, y):
            if x < 0 or y < 0 or x >= m or y >= n:
                return 0
            if x == m-1 and y == n-1:
                dp[x][y] = 1
                return 1
            if dp[x][y] != -1:
                return dp[x][y]
            dp[x][y] = dfs(x+1,y) + dfs(x,y+1)
            
            return dp[x][y]
            
        
        dfs(0, 0)
        # print(dp)
        return dp[0][0]
        