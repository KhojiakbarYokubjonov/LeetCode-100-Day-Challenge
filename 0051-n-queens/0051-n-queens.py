class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set() # row + col
        negDiag  = set() # row - col
        
        board = []
        for i in range(n):
            temp = []
            for j in range(n):
                temp.append(".")
            board.append(temp)
        res = []
        
        def backtrack(row):
            if row == n:
                print(board)
                res.append(Solution.makeCopy(board))
                return
            
            for c in range(n):
                if c in col or (row + c) in posDiag or (row - c) in negDiag:
                    continue
                
                col.add(c)
                posDiag.add(row + c)
                negDiag.add(row - c)
                board[row][c] = 'Q'
                
                backtrack(row + 1)
                
                col.remove(c)
                posDiag.remove(row + c)
                negDiag.remove(row - c)
                
                board[row][c] = '.'
                
        backtrack(0)
        return res
    
    @staticmethod
    def makeCopy(board):
        new = []
        for row in board:
            new.append("".join(row))
        return new
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        