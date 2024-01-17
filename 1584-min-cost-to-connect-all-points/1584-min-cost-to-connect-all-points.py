class Solution:
    """
    Idea: calculate all the edge weights and find MST cost using Prim's algorithm
    """
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        def find(v):
            if v != parent[v]:
                parent[v] = find(parent[v])
            return parent[v]
    
    
        n = len(points)
        heap = []
        parent = [i for i in range(len(points) + 1)]
        
        for i in range(len(points)):
            x1, y1 = points[i][0], points[i][1]
            for j in range(i+1, len(points)):
                x2, y2 = points[j][0], points[j][1]
                
                distance = abs(x1 - x2) + abs(y1 - y2)
                heapq.heappush(heap, (distance, i, j))
        
        cost = 0
        while heap:
            dis, v1, v2 = heapq.heappop(heap)
            rootv1, rootv2 = find(v1), find(v2)
            # if the two vertices are not connected, connect them
            if rootv1 != rootv2:
                parent[rootv1] = rootv2
                cost += dis
                
        
        
        return cost
    
    
            
        
        
        
                    
        