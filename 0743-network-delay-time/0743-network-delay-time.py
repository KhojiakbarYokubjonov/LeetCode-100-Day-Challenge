class Solution:
    """
    Uses bellman ford algorithm
    """
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        cheapest = {i : math.inf for i in range(1, n+1)}
        cheapest[k] = 0
        adjlist = collections.defaultdict(list)
        
        for a, b, price in times:
            adjlist[a].append((b, price))
        

        for i in range(n):
            for u in range(1,n+1):
                for v, price in adjlist[u]:
                    cheapest[v] = min(cheapest[v], cheapest[u] + price)
        print(cheapest)
        mintime = max(cheapest.values())
        if mintime == math.inf:
            return -1
        return mintime
            
        
        