class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        dp = [-1] * len(nums)
        def recursiveSol(i):
            if i >= len(nums):
                return 0
            if i == len(nums) - 1:
                return nums[i]
            if dp[i] != -1:
                return dp[i]
            
            dp[i] = max(nums[i] + recursiveSol(i+2), recursiveSol(i+1))
            return dp[i]
        res = recursiveSol(0)
        return res
        
            
                
        