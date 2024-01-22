class Solution:
    """
    Idea: same approach as one used for House Robber I. if you count nums[0], you can go upto nums[-2]. If you begin with nums[2],          you can go till the end.
    """
    def rob(self, values: List[int]) -> int:
        N = len(values)
        if N == 1:
            return values[0]
        
        def helper(nums):
            if len(nums) == 0: 
                return 0
            if len(nums) < 3: 
                return max(nums)
            dp = [0] * len(nums)
            print(nums, dp)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                dp[i] = max(nums[i] + dp[i-2], dp[i-1])
            return dp[-1]
        
        return max(helper(values[:N-1]), helper(values[1:]))
        