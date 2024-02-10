class Solution:
    def countBits(self, n: int) -> List[int]:
        countofones = [0] * (n+1)
        countofones[0] = 0
        
        offset = 1
        
        for i in range(1, n+1):
            if i == offset * 2:
                offset = i
            countofones[i] = 1 + countofones[i - offset]
        return countofones
   
                
             
        
        