class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        if candidates == []:
            return []
        def DFS(nums, path, target):
            
            if target < 0:
                return
            
            if target == 0:
                res.append(path)
                return
            
            for i in range(len(nums)):
                DFS(nums[i:], path+[nums[i]], target - nums[i])
        DFS(candidates, [], target)
        
        return res
        