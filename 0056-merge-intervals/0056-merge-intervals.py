class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        stack = []  
        last = None
        
        for (x,y) in intervals:
            if not stack:
                stack.append([x,y])
                last = [x,y]
            else:
                if x <= last[1] and y <= last[1]:
                    continue
                elif x <= last[1]:
                    stack.pop()
                    stack.append([last[0], y])
                    last = [last[0], y]
                else:
                    stack.append([x,y])
                    last = [x,y]
        return stack
                    
        
        