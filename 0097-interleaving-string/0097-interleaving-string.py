class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = {}
        
        def dfs(i, j, newstr, k):
            if k == len(s3):
                return 1
            if len(newstr) == len(s3) or i == len(s1) and j == len(s2):
                return 0
            
            if (i, j, newstr) in dp:
                return dp[(i, j, newstr)]
            res = 0
            dp[(i, j, newstr)] = 0
            if i < len(s1) and s1[i] == s3[k]:
                dp[(i, j, newstr)] += dfs(i+1,j, newstr + s1[i], k+1)
                if dp[(i, j, newstr)]: return 1
            if j < len(s2) and s2[j] == s3[k]:
                dp[(i, j, newstr)] += dfs(i, j+1, newstr + s2[j], k+1)
               
            return dp[(i, j, newstr)]
        # print(dp)
        return dfs(0, 0, "", 0)
        
        