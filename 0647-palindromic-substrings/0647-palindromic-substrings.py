class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        N = len(s)
        
        def pal(l, r):
            count = 0
            print(l,r, end=" ")
            while l>=0 and r < N:
                if s[l] != s[r]:
                    break
                count += 1
                l -= 1
                r += 1
            print(count)
            return count
            
        
        for i in range(N):
            res += pal(i,i)
            res += pal(i,i+1)
                
        return res
    
        
        