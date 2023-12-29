class Solution:
    """
    IDEA: first find the starting position of the sorted list; then just do the usual binary search
    """
    def search(self, nums: List[int], target: int) -> int:
        
        # find the 
        N = len(nums)
        l, r = 0, N-1
        
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        offset = l
        
        l, r = 0, N-1
        
        while l <= r:
            mid = (l + r) // 2
            actual_mid = (offset + mid) % N
            if nums[actual_mid] > target:
                r = mid - 1
            elif nums[actual_mid] < target:
                l = mid + 1
            else:
                return actual_mid
            
        return -1
            
                
        