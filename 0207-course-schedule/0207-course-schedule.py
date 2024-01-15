class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = collections.defaultdict(list)
        
        for c, pre in prerequisites:
            adjList[pre].append(c)
            
        
        def cycle(current, tracker, visited):
            visited.add(current)
            tracker.add(current)
            for node in adjList[current]:
                if node in tracker: # means there is a cycle
                    return True
                # before calling cycle(), check if we havent already visited this node before
                elif node not in visited and cycle(node, tracker, visited):
                    return True
            tracker.remove(current)
            return False
        
        visited = set() # helps avoid visiting old nodes again
        for c in range(numCourses):
            tracker = set() # used to detect cycles
            if c not in visited and cycle(c, tracker, visited):
                return False
        return True
        
        
        
        
        
        
        
        
        
        
        