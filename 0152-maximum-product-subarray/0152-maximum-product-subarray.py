class Solution:
    """
    Idea: have 2 dp arrays: maxdp and mindp
    """
    def maxProduct(self, nums: List[int]) -> int:
  
        maxprod = mindp = maxdp = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] > 0:
                maxdp = max(maxdp * nums[i], nums[i])
                mindp = min(mindp * nums[i], nums[i])
            else:
                maxcopy = maxdp
                maxdp = max(mindp * nums[i], nums[i])
                mindp = min(maxcopy * nums[i], nums[i])
            maxprod = max(maxprod, maxdp)
        return maxprod