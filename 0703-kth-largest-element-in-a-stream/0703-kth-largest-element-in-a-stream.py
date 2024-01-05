class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.vals = []
        self.k = k
        for val in nums:
            self.add(val)


    def add(self, val: int) -> int:
        if len(self.vals) < self.k:
            heappush(self.vals, val)
        else:
            heappush(self.vals, val)
            heappop(self.vals)
        return self.vals[0]
            

        
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)