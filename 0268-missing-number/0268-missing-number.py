class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missingnum = 0
        N = len(nums)
        for n in range(1, N+1):
            missingnum ^= n
            missingnum ^= nums[n-1]
        return missingnum
        
        
        
        
        
        
    def solutionOne(nums):
        N = len(nums)
        total = int(N*(N+ 1) / 2)
        for n in nums:
            total -= n
        return total
        