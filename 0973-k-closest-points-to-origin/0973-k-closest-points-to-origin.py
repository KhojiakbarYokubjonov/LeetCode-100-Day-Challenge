class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        
        for (x, y) in points:
            dis = (x)**2 + (y)**2
            distances.append([dis, x, y])
        heapq.heapify(distances)
        res = []
        while k > 0:
            d, x, y = heapq.heappop(distances)
            res.append([x, y])
            k -= 1
            
        return res

        
        