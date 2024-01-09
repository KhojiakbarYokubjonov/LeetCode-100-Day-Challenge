class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        def DFS(nums,perm):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for n in nums:
                if n not in perm:
                    perm.append(n)
                    DFS(nums, perm)
                    perm.pop()
        DFS(nums, [])
        return res
                
                
        