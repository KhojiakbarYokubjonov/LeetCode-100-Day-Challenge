class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        maxelevation = grid[0][0]
        heap = [(0, 0, 0)] # elevation, row, col
        N = len(grid)
        currentEl = 0
        visited = set()
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        while heap:
            el, x, y = heapq.heappop(heap)
            visited.add((x, y))
            maxelevation = max(maxelevation, el)
            
            if (x,y) == (N-1, N-1):
                break
            for r, c in directions:
                if x+r in range(N) and  y+c in range(N) and (x+r, y+c) not in visited:
                    visited.add((x+r, y+c))
                    heapq.heappush(heap, (grid[x+r][y+c], x+r, y+c))
        
        return maxelevation
        
        
        
        