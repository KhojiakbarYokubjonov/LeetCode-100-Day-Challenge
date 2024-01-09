class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = [[]]
        for val in nums:
            result += [[val] + temp for temp in result]
            print(result)
        return result

        