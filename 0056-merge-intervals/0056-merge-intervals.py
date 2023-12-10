class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        if len(intervals) == 1:
            return intervals
        # sorts intervals by the first value
        intervals = sorted(intervals ,key=lambda l:l[0], reverse=False)
        res = [intervals[0]]
        for x, y in intervals[1:]:
            prev_y = res[-1][1]
            if x <= prev_y:
                res[-1][1] = max(res[-1][1], y)
            else:
                res.append([x,y])
        return res
            
            
        