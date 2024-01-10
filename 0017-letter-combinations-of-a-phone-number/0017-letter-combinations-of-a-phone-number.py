class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {"1":"", 
                   "2":"abc", 
                   "3":"def", 
                   "4":"ghi", 
                   "5":"jkl",
                   "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = []
        
        def dfs(start, comb):
            if start >= len(digits) and len(comb) == len(digits) and digits != "":
                res.append(comb)
                return
            
            for i in range(start, len(digits)):
                if digits[i] in mapping:
                    for ch in mapping[digits[i]]:
                        dfs(i+1, comb+ch)
        dfs(0, "")
        
        return res
            
            
        
        