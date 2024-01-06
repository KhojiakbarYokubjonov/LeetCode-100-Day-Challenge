"""
Trie class implementation is a solution
for this LC question: https://leetcode.com/problems/implement-trie-prefix-tree/
"""
class Trie:

    def __init__(self):
        self.table = {'ref':0}
        
    def insert(self, word: str) -> None:
        lastTable = self.table
        lastTable['ref'] += 1
        i = 0
        while i < len(word):
            if word[i] not in lastTable:
                lastTable[word[i]] = {"in":False, 'ref':0}
            lastTable = lastTable[word[i]]
            lastTable['ref'] += 1
            i += 1
        lastTable['in'] = True
 
        

    def search(self, word: str) -> bool:
        lastTable = self.table
        for ch in word:
            if ch in lastTable:
                lastTable = lastTable[ch]
            else:
                return False
        return lastTable['in']

    def startsWith(self, prefix: str) -> bool:
        lastTable = self.table
        for ch in prefix:
            if ch in lastTable:
                lastTable = lastTable[ch]
            else:
                return False
        return True
    
    def remove(self, word):
        lastTable = self.table
        lastTable['ref'] -= 1
        for ch in word:
            if ch in lastTable:
                lastTable = lastTable[ch]
                lastTable['ref'] -= 1
        


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        t = Trie()
        for w in words:
            t.insert(w)
        result = set()
       
        def DFS(row, col, table, path):
            if (row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) 
                or board[row][col] not in table 
                or table[board[row][col]]['ref'] < 1
                or board[row][col] == 0):
                return
            
            string = path +board[row][col]
            if not t.startsWith(string):
                return
            elif t.search(string) and string not in result:
                result.add(string)
                t.remove(string)
            
            table = table[board[row][col]]
            ch = board[row][col]
            board[row][col] = 0
            # recursive search
            DFS(row-1,col, table, string)
            DFS(row+1,col, table, string)
            DFS(row,col-1, table, string)
            DFS(row,col+1, table, string)
            
            board[row][col] = ch
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                DFS(i,j, t.table, "")
        return list(result)
            
                
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
                
                
            