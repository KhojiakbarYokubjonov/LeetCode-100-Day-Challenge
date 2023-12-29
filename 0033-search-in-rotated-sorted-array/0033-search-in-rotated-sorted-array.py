class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        N = len(nums)
        l, r = 0, N-1
        
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        pivot = l
        
        l, r = 0, N-1
        
        while l <= r:
            mid = (l + r) // 2
            actual_mid = (pivot + mid) % N
            if nums[actual_mid] > target:
                r = mid - 1
            elif nums[actual_mid] < target:
                l = mid + 1
            else:
                return actual_mid
            
        return -1
            
                
        