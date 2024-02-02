class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[-1]*(m+1) for i in range(n+1)]
        
        def dfs(s1, s2,n, m):
            if n == 0 or m == 0:
                return 0
            if dp[n][m] != -1:
                return dp[n][m]
            
            if s1[n-1] == s2[m-1]:
                dp[n][m] = 1 + dfs(s1, s2, n-1, m-1)
                return dp[n][m]
                
            dp[n][m] = max(dfs(s1, s2, n-1, m), dfs(s1, s2, n, m-1))
            return dp[n][m]
        return dfs(text1, text2, n, m)
                
            
    
    
    
    
    
    
    def recursiveInefficient(self, text1, text2):
        def dfs(s1, s2, m, n):
            if m == 0 or n == 0:
                return 0
            if s1[m-1] == s2[n-1]:
                return 1 + dfs(s1, s2, m-1, n-1)
            return max(dfs(s1, s2, m-1, n), dfs(s1, s2, m, n-1))
        return dfs(text1, text2, len(text1), len(text2))       