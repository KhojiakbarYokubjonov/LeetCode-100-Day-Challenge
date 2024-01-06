class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for t in tasks:
            count[t] = 1 + count.get(t, 0)
        
        maxHeap = []
        for c in count.values():
            maxHeap.append(-c)
            
        heapq.heapify(maxHeap)
        
        q = deque()
        time = 0
        
        while maxHeap or q:
            
            if len(maxHeap) > 0:
                task = heapq.heappop(maxHeap) + 1
                if task != 0:
                    q.append([task, time + n]) # stores task and wakeup time
            if q and q[0][1] == time:
                task = q.popleft()[0]
                heapq.heappush(maxHeap, task)
            time += 1
        return time
                
        
            