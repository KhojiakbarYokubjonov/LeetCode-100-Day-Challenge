class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        chars = list(s)
        stack = []
        
        for i in range(len(chars)):
            if chars[i] == "(":
                stack.append(i)
            elif chars[i] == ")":
                if stack != []:
                    stack.pop()
                else:
                    chars[i] = ""
        for ind in stack:
            chars[ind] = ""
        return "".join(chars)
            
        
        