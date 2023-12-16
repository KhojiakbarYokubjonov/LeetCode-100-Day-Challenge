class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def help(x,n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            
            result = help(x, n// 2)
            result *= result
            return result * x if n %2 == 1 else result
        
        res = help(x,abs(n))
        return res if n > 0 else 1 / res
        