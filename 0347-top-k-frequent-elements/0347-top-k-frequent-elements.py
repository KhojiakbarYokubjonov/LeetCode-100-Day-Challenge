class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        minn = maxx = None
        
        for val in nums:
            if val not in count:
                count[val] = 0
            count[val] += 1
            
        pairs = [(k,v) for k,v in count.items()]
        
        pairs.sort(key = lambda x:x[1], reverse=True)
        
        output = []
        for i in range(k):
            x,y = pairs[i]
            output.append(x)
        
        return output
            
        