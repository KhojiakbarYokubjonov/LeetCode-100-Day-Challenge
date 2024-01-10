class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()
        found = set()
        if candidates == []:
            return []
        def DFS(start, nums, path, target,):
            
            if target < 0:
                return
            
            if target == 0:
                res.append(path)
                return
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                DFS(i+1, nums, path+[nums[i]], target - nums[i])
        DFS(0, candidates, [], target)
        
        return res
        