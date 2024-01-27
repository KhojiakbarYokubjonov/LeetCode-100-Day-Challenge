class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subarray = [nums[0]]
        N = len(nums)
        
        for n in nums:
            index = bisect_left(subarray, n)
            if index == len(subarray):
                subarray.append(n)
            else:
                subarray[index] = n
        return len(subarray)
    
    
    def DPSolution(nums):
        dp = [1] * len(nums)
        
        maxlen = 1
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
            maxlen = max(maxlen, dp[i])
        return maxlen
                
            
        