class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = 0
        
        for n in nums:
            single = single ^ n
        return single
            
        