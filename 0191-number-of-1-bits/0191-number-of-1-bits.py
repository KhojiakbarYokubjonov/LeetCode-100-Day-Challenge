class Solution:
    def hammingWeight(self, n: int) -> int:
        numberofbits = 32
        ones = 0
        
        for i in range(numberofbits):
            if n & 1 << i:
                ones += 1
        return ones
        