class Solution:
    """
    Idea: have 2 dp arrays: maxdp and mindp
    """
    def maxProduct(self, nums: List[int]) -> int:
        """
        same solution without conditions
        """
        maxprod = mindp = maxdp = nums[0]
        
        for i in range(1, len(nums)):
            maxcopy = maxdp
            maxdp = max(maxdp * nums[i], mindp * nums[i], nums[i])
            mindp = min(mindp * nums[i], maxcopy * nums[i], nums[i])                
            maxprod = max(maxprod, maxdp)
        return maxprod
    
    
    def solution2(nums):
        """
        same as the below solution but without arrays
        """
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
    
    
    def solutionWithArrays(nums):
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