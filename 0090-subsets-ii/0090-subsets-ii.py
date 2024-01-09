class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        def helper(start, subset, nums):
            res.append(subset.copy())
            
            for i in range(start, len(nums)):
                if not (i > start and nums[i] == nums[i-1]):
                    subset.append(nums[i])
                    helper(i+1, subset, nums)
                    subset.pop()
        helper(0, [], sorted(nums))
        return res
        