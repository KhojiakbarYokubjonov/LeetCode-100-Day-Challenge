class Solution:
    def simplifyPath(self, path: str) -> str:
        ignore = "."
        go_back = ".."
        if path == "" or len(path) == 1:
            return "/"
        i = 0
        stack = []
        if path[0] == "/":
            i += 1
        while i < len(path):
            current = ""
            while i < len(path) and path[i] != "/":
                current += path[i]
                i += 1
            if current  == "..":
                if stack: 
                    stack.pop()
                else: continue
            elif current == ".":
                continue
            elif current != "":
                stack.append(current)
            i += 1
        if not stack:
            return "/"
        res = ""
        for dir in stack:
            res += ("/" + dir)
        return res
            
        
        