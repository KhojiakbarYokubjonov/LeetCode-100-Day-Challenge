class Solution:
    """
    Idea: calculate all the edge weights and find MST cost using Prim's or kruskal's algorithms
    """
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        def find(v):
            if v != parent[v]:
                parent[v] = find(parent[v])
            return parent[v]
        
        def union(v1, v2):
            rootv1, rootv2 = find(v1), find(v2)
            
            if rootv1 == rootv2:
                return False # already connected
            
            if rank[rootv1] > rank[rootv2]:
                parent[rootv2] = rootv1
                rank[rootv1] += rank[rootv2]
            else:
                parent[rootv1] = rootv2
                rank[rootv2] += rank[rootv1]
            return True
    
    
        n = len(points)
        heap = []
        parent = [i for i in range(len(points) + 1)]
        rank = [1 for _ in range(len(points) + 1)]
        
        for i in range(len(points)):
            x1, y1 = points[i][0], points[i][1]
            for j in range(i+1, len(points)):
                x2, y2 = points[j][0], points[j][1]
                
                distance = abs(x1 - x2) + abs(y1 - y2)
                heapq.heappush(heap, (distance, i, j))
        
        cost = 0
        while heap:
            dis, v1, v2 = heapq.heappop(heap)
            if union(v1, v2):
                cost += dis
        
        return cost
    
    
            
        
        
        
                    
        