class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        if N < 2:
            return False
        total = sum(nums)
        if total % 2 != 0: return False
        half = total // 2
        
        dp = {0} # 0 for when we dont include anything
        for i in range(N):
            nextDP = set()
            for val in dp:
                if val == half or val + nums[i] == half: return True
                nextDP.add(val)
                nextDP.add(val + nums[i])
            dp = nextDP
        return half in dp 
                
        