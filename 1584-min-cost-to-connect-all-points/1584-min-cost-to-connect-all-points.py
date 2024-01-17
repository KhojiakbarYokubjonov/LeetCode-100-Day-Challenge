class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjList = collections.defaultdict(list)
        n = len(points)
        
        for i in range(len(points)):
            x1, y1 = points[i][0], points[i][1]
            for j in range(i+1, len(points)):
                x2, y2 = points[j][0], points[j][1]
                
                distance = abs(x1 - x2) + abs(y1 - y2)
                adjList[i].append((distance, j))
                adjList[j].append((distance, i))
        
        cost = 0
        visited = set()
        heap = [(0, 0)] # dist, vertex
        
        while len(visited) < n:
            d, vertex = heapq.heappop(heap)
            if vertex in visited:
                continue
            visited.add(vertex)
            cost += d
            for node in adjList[vertex]:
                if node[1] not in visited:
                    heapq.heappush(heap, node)
        return cost
            
        
        
        
                    
        