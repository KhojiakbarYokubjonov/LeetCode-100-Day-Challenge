class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -num)
        heapq.heappush(self.minHeap, -1 * heapq.heappop(self.maxHeap))
        
        if len(self.minHeap) > len(self.maxHeap):
            heapq.heappush(self.maxHeap, -1 * heapq.heappop(self.minHeap))

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] - self.maxHeap[0]) / 2
        return -self.maxHeap[0]
                
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()