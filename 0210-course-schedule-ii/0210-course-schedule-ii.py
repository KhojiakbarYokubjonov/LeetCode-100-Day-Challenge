class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = collections.defaultdict(list)

        for c, pre in prerequisites:
            adjList[pre].append(c)
       
        # self.cyclic = False
        def dfs(current, tracker, visited, path):
            visited.add(current)
            tracker.add(current)
            for node in adjList[current]:
                if node in tracker: # means there is a cycle
                    return True
                if node not in visited and dfs(node, tracker, visited, path):
                    return True
            path.append(current)
            tracker.remove(current)
            return False

        path = []
        visited = set() # helps avoid visiting old nodes again
        
        for c in range(numCourses):
            tracker = set() # used to detect cycles
            if c not in visited and dfs(c, tracker, visited, path):
                return []
        path.reverse()
        return path
        