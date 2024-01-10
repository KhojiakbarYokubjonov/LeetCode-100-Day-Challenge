class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(row, col, board, word):
            if len(word) == 0:
                # print("found")
                return True
            
            if ( row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) 
                or word[0] != board[row][col]):
                return False
            
            ch = board[row][col]
            board[row][col] = "x"
            res =   (dfs(row-1, col, board, word[1:]) or
                    dfs(row+1, col, board, word[1:]) or
                    dfs(row, col-1, board, word[1:]) or
                    dfs(row, col+1, board, word[1:]))
            board[row][col] = ch
            return  res
        
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == word[0] and dfs(row, col, board, word):
                    return True
        return False
                    
                
            
        