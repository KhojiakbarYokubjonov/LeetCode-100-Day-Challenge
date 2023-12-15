class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = ""
        
        p = 0
        
        for c in s:
            val = (1 if c == "(" else -1 )
            if c not in "()":
                res += c
            elif p + val >= 0 and c in "()":
                res += c
                p += val
        p=0
        res2 = ""
        for i in range(len(res)-1,-1,-1):
            c = res[i]
            val = (1 if c == ")" else -1 )      
            if c not in "()":
                res2 += c
            elif p + val >= 0 and c in "()":
                res2 += c
                p += val
        return res2[::-1] if p==0 else ""
        