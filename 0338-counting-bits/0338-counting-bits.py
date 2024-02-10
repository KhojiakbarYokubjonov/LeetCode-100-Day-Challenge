class Solution:
    def countBits(self, n: int) -> List[int]:
        count = [0] * (n + 1)
        for i in range(n+1):
            count[i] = count[i >> 1] + i % 2
        return count
    
    
    
    
    
    def offsetSolution(n):
        countofones = [0] * (n+1)
        countofones[0] = 0
        
        offset = 1
        
        for i in range(1, n+1):
            if i == offset * 2:
                offset = i
            countofones[i] = 1 + countofones[i - offset]
        return countofones
   
                
             
        
        