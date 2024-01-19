class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        maxTime = 0
        adjList = collections.defaultdict(list)
        
        for u, v, time in times:
            adjList[u].append((v, time))
        
            
        heap = [(0, k)]
        visited = set()
        
        time = {}
        
        while heap:
            t, u = heapq.heappop(heap)
            if u in time:
                continue
            time[u] = t
            maxTime = max(t, maxTime)
            visited.add(u)
            
            for v, vt in adjList[u]:
                if v not in time:
                    heapq.heappush(heap, (t + vt, v))
   
        if len(visited) < n:
            return -1
        return maxTime
            
        
        