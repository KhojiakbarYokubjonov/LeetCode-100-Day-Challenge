class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adjList = collections.defaultdict(list)
        output = [math.inf for _ in range(n)]
        
        for fr, to, price in flights:
            adjList[fr].append((to, price))
            
        queue = deque()
        queue.append((src, -1, 0)) # startnode, k, cost
        
        
        while queue:
            node, stop, cost = queue.popleft()
            if stop >= k:
                continue
            
            for v, p in adjList[node]:
                if cost + p < output[v]:
                    output[v] = cost + p
                    queue.append((v, stop+1, cost+p))
        
        if output[dst] == math.inf:
            return -1
        return output[dst]
                
        
        