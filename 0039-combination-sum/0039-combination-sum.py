class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        if candidates == []:
            return []
        def DFS(index):
            total = sum(path)
            if total == target:
                res.append(path.copy())
                return
            if total > target or index >= len(candidates):
                return
            
            path.append(candidates[index])
            
            DFS(index)
            path.pop()
            DFS(index + 1)
        DFS(0)
        
        return res
        