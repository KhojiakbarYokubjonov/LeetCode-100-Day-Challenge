class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = 1
        res = 0
        curr = 0
        
        for ch in s:
            if ch.isdigit():
                curr = curr * 10 + int(ch)
            
            elif ch in {"+", "-"}:
                
                res += sign * curr
                sign = 1 if ch == "+" else -1
                curr = 0
            
            elif ch == "(":
                stack.append(res)
                stack.append(sign)
                
                sign = 1                
                res = 0
            elif ch == ")":
                res += sign * curr
                last_op = stack.pop()
                last_res = stack.pop()
                res *= last_op
                res += last_res
                curr = 0
                
        return res + sign*curr
            
        