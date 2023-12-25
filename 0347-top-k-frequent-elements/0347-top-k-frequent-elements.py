class Solution:
    """
    Idea: uses the bucket sort algorithm
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        minn = maxx = None
        
        for val in nums:
            if val not in count:
                count[val] = 0
            count[val] += 1
            
        frequencies = [[] for i in range(len(nums)+1)]
        
        
        for key, v in count.items():
            frequencies[v].append(key)
        
        output = []
            
        for i in range(len(nums), 0, -1):
            for key in frequencies[i]:
                output.append(key)
                if len(output) == k:
                    return output