class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        for i in range(1, len(nums)):
            if sorted_nums[i] == sorted_nums[i-1]:
                return sorted_nums[i]
            
        