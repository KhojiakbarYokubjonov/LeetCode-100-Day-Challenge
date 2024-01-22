class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if len(nums) == 0:
            return 0
        if N < 3:
            return max(nums)
        dp = [0] * N
        
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, N):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        
        # print(dp)
        return dp[-1]
        
            
                
        