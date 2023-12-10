class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = None
        if len(intervals) == 0:
            return []
        if len(intervals) == 1:
            return intervals
        # sorts intervals by the first value
        intervals = sorted(intervals ,key=lambda l:l[0], reverse=False)
        res = []
        for i in range(1, len(intervals)):
            x,y = intervals[i]
            if merged == None:
                xp,yp = intervals[i-1]
                merged = [xp,yp]
            else:
                xp,yp = merged
            if x < xp and y >= xp:
                merged = [x, max(y, yp)]
            elif yp >= x and x >= xp:
                
                merged = [min(xp,x), max(y, yp)]
            else:
                res.append(merged)
                merged = [x,y]
                
        res.append(merged)
                
        return res
            
            
        