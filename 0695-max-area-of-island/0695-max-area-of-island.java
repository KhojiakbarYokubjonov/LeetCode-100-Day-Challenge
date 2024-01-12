class Solution {
    int maxSize = 0;
    public int maxAreaOfIsland(int[][] grid) {
        
        for(int i=0; i<grid.length; i++){
            for(int j=0; j<grid[i].length; j++) {
                if(grid[i][j] == 1) {
                    DFS(i, j, grid);
                }
            }
        }
        
        return maxSize;
        
    }
    
    private int DFS(int r, int c, int[][] grid) {
        if(r < 0 || r >= grid.length || c < 0 || c >= grid[r].length || grid[r][c] == 0) {
            return 0;
        }
        
        grid[r][c] = 0;
        
        int current = 1 + DFS(r-1,c, grid) 
                        + DFS(r+1,c, grid) 
                        + DFS(r,c-1, grid) 
                        + DFS(r,c+1, grid);
        maxSize = Math.max(maxSize, current);
        return current;
    }
}