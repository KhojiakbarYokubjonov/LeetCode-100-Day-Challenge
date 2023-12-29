class Solution:
    def findMin(self, nums: List[int]) -> int:
        return self.solutionTwo(nums)
        l, r = 0, len(nums) - 1
        
        res = nums[0]
        
        while l <= r:
            if nums[l] < nums[r]:
                return min(res, nums[l])
            
            mid = (l + r) // 2
            
            res = min(res, nums[mid])
            
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        
                
        return res
    
    def solutionTwo(self, nums):
        N = len(nums)
        l, r = 0, N-1
        
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]