class Solution:

    def __init__(self, w: List[int]):
        self.weights = []
        self.total = 0
        for i in w:
            self.total += i
            self.weights.append(self.total)
        

    def pickIndex(self) -> int:
        rand_val  = random.randint(1, self.total)
        for i in range(len(self.weights)):
            if rand_val <= self.weights[i]:
                return i
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()