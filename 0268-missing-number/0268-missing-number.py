class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        total = int(N*(N+ 1) / 2)
        for n in nums:
            total -= n
        return total
        