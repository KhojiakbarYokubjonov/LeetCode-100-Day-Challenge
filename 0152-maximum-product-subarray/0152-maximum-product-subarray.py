class Solution:
    """
    Idea: have 2 dp arrays: maxdp and mindp
    """
    def maxProduct(self, nums: List[int]) -> int:
        mindp = [0] * len(nums)
        maxdp = [0] * len(nums)
        mindp[0] = maxdp[0] = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] > 0:
                maxdp[i] = max(maxdp[i-1] * nums[i], nums[i])
                mindp[i] = min(mindp[i-1] * nums[i], nums[i])
            else:
                maxdp[i] = max(mindp[i-1] * nums[i], nums[i])
                mindp[i] = min(maxdp[i-1] * nums[i], nums[i])
        return max(maxdp)