class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [math.inf] * len(nums)
        dp[0] = 0
        
        for i in range(len(dp)):
            for j in range(1, nums[i]+1):
                if i+j < len(dp):
                    dp[i+j] = min(dp[i+j], 1+dp[i])
                if dp[-1] < math.inf:
                    return dp[-1]
        # print(dp)
        return dp[-1]
                
            
            
            
        
        