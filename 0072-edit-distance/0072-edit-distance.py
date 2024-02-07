class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # basecases
        if len(word1) == 0: return len(word2)
        if len(word2) == 0: return len(word1)
        
        dp = [[-math.inf] * (len(word2)+1) for i in range(len(word1)+1)]
        
        for i in range(len(word1)+1):
            dp[i][-1] = len(word1)-i
            
        for j in range(len(word2)+1):
            dp[-1][j] = len(word2)-j
    
    
        for i in range(len(word1)-1, -1, -1):
            for j in range(len(word2)-1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    insert  = 1 + dp[i][j+1]
                    delete  = 1 + dp[i+1][j]
                    repl    = 1 + dp[i+1][j+1]
                    
                    dp[i][j] = min(insert, delete, repl)
            
            
        return dp[0][0]
        
        
    def bruteforceSlow(word1, word2):
          
        def dfs(i, j):
            if i == len(word1) and j == len(word2):
                return 0
            if i == len(word1):
                return len(word2)-j
            if j == len(word2):
                return len(word1)-i
                
                
            if word1[i] == word2[j]:
                return dfs(i+1, j+1)
            else:
                insert =  1 + dfs(i, j+1 )
                delete = 1 + dfs(i+1, j)
                replace = 1 + dfs(i+1, j+1)
                ops = min(insert, delete, replace)
            
            return ops
        return dfs(0, 0)