class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mapping = {}
        roadmap = {}
        indegree = {}
        q = []
        if prerequisites == []:
            return True
        
        for course, prereq in prerequisites:
            if prereq not in mapping:
                mapping[prereq] = set()
            if course not in mapping:
                mapping[course] = set()

            mapping[course].add(prereq)
            indegree[course] = 1 + indegree.get(course, 0)
            if prereq not in indegree:
                indegree[prereq] = 0
        
        for course, prereq in prerequisites:
            if indegree[course] == 0 and course not in q:
                q.append(course)
            if indegree[prereq] == 0 and prereq not in q:
                q.append(prereq)
            if prereq not in roadmap:
                roadmap[prereq] = set()
            if course not in roadmap:
                roadmap[course] = set()
            roadmap[prereq].add(course)
            
        
        count = 0
        
        # print(mapping)
        # print(roadmap)
        # print(indegree)
        while q:
            course = q.pop()
            # print(course)
            if course in mapping:
                mapping.pop(course)

            for c in roadmap[course]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    q.append(c)
            count += 1
        
        return count == numCourses or len(mapping) == 0
            
        
"""

4
[[0,1],[0,2],[1,3],[3,0]]
"""       
        
        
        
        
        
        
        
        
        
        
        