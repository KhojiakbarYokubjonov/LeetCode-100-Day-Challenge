class Solution:

    def __init__(self, w: List[int]):
        self.weights = []
        self.total = 0
        for i in w:
            self.total += i
            self.weights.append(self.total)
        

    def pickIndex(self) -> int:
        # rand_val  = random.randint(1, self.total)
        # for i in range(len(self.weights)):
        #     if rand_val <= self.weights[i]:
        #         return i
        return self.binary_search()
    
    def binary_search(self):
        rand_val  = random.randint(1, self.total)
        low, high = 0, len(self.weights) - 1 
        
        while low <= high:
            middle = (low + high) // 2
            if rand_val > self.weights[middle]:
                low = middle + 1
            elif rand_val < self.weights[middle]:
                high = middle - 1
            else:
                return middle
        return low
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()