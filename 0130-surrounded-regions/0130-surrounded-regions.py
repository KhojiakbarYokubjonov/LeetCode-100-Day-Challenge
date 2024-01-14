class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        M = len(board)
        N = len(board[0])
        
        # top & bottom
        borderOs = set()
        for col in range(N):
            if board[0][col] == "O":
                borderOs.add((0,col))
            if board[M-1][col] == "O":
                borderOs.add((M-1,col))
        for row in range(M):
            if board[row][0] == "O":
                borderOs.add((row, 0))
            if board[row][N-1] == "O":
                borderOs.add((row, N-1))
                
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        
        def dfs(r, c):
            if (r < 0 or c < 0 or r == M or c == N 
                or board[r][c] == "T" or  board[r][c] == "X"):
                return
            board[r][c] = "T"
            
            for i,j in directions:
                dfs(r+i, c+j)
                
        for r, c in borderOs:
            dfs(r,c)
        
        for i in range(M):
            for j in range(N):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"
        
            
            
        