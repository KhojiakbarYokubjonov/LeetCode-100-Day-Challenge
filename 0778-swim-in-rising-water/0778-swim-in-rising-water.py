class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        maxelevation = grid[0][0]
        heap = [(0, 0, 0)] # elevation, row, col
        N = len(grid)
        currentEl = 0
        visited = set()
        while heap:
            el, x, y = heapq.heappop(heap)
            visited.add((x, y))
            maxelevation = max(maxelevation, el)
            
            if (x,y) == (N-1, N-1):
                break
            if x-1 >=0 and (x-1, y) not in visited:
                heapq.heappush(heap, (grid[x-1][y], x-1, y))
            if x+1 < N and (x+1, y) not in visited:
                heapq.heappush(heap, (grid[x+1][y], x+1, y))
            if y-1 >=0 and (x, y-1) not in visited:
                heapq.heappush(heap, (grid[x][y-1], x, y-1))
            if y+1 < N and (x, y+1) not in visited:
                heapq.heappush(heap, (grid[x][y+1], x, y+1))
        
        return maxelevation
        
        
        
        