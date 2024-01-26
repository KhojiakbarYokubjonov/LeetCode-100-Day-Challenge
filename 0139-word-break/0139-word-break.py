class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        
        dp = [False] * (len(s) + 1) # +1 for an empty str
        dp[0] = True # empty str exists
        
        for start in range(len(s)):
            if dp[start] == False: continue
            for end in range(start+1, len(s)+1):
                if s[start:end] in words:
                    dp[end] = True
        return dp[-1]
        
        
    def inefficentDFSSolution(s, wordDict):
        """
        it works but not efficient
        """
        words = set(wordDict)
        
        
        def dfs(start, end):
            if start >= len(s):
                return True
            
            for i in range(start, end):
                # print(s[start:i+1])
                if s[start:i+1] in words:
                    if dfs(i+1, end):
                        return True
            return False
        return dfs(0, len(s))