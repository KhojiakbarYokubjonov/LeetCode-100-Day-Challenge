class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        if not s:
            return 0
        
        stack.append(s[0])
        i = 1
        while i < len(s):
            curr = s[i]
            if not stack:
                stack.append(curr)
            elif stack[-1] + curr == "()":
                stack.pop()
            else:
                stack.append(curr)
            i += 1
        return len(stack)
            
        