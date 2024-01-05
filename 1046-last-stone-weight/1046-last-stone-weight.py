class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        vals = []
        for v in stones:
            vals.append(-1 * v)
        heapq.heapify(vals)

        while len(vals) > 1:
            a, b = heappop(vals), heappop(vals)
            if a-b != 0:
                heappush(vals, a-b)
        return -1 * vals[0] if vals != [] else 0
        
            
        