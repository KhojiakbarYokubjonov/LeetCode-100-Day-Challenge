class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        
        for (x, y) in points:
            dis = (x)**2 + (y)**2
            distances.append([dis, x, y])
        distances.sort(key = lambda x:x[0])
        res = []
        i = 0
        while i < k:
            d, x, y = distances[i]
            res.append([x, y])
            i += 1
            
        return res

        
        