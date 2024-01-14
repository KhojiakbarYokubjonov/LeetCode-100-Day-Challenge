class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rotten = []
        fresh = 0
        visited = set()
        
        M = len(grid)
        N = len(grid[0])
        
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                    
                elif grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        

        minutes = -1
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        print(rotten)
        while rotten != []:
            size = len(rotten)
            while size > 0:
                i, j = rotten.pop(0)
                grid[i][j] = 2
                if i-1 >= 0 and grid[i-1][j] == 1 and (i-1,j) not in visited:
                    rotten.append((i-1, j))
                    visited.add((i-1,j))
                if i+1 < M and grid[i+1][j] == 1 and (i+1,j) not in visited:
                    rotten.append((i+1, j))
                    visited.add((i+1, j))
                if j+1 < N and grid[i][j+1] == 1 and (i, j+1) not in visited:
                    rotten.append((i, j+1))
                    visited.add((i, j+1))
                if j-1 >= 0 and grid[i][j-1] == 1 and (i, j-1) not in visited:
                    rotten.append((i, j-1))
                    visited.add((i, j-1))
                size -= 1
            print(rotten)
            minutes += 1
            
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    return -1
        return minutes

        
"""
[[2,2],
[1,1],
[0,0],
[2,0]]
"""
            
        