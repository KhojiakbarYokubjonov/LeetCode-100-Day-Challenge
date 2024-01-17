class Solution:
    """
    Idea: if the nodes a,b are already connected through the same parent, the a -> b edge is REDUNDANT
    """
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parent = [i for i in range(len(edges) + 1)]
        rank = [1 for i in range(len(edges) + 1)]
        
        
        def findRootParent(n):
            p = parent[n]
            
            while p != parent[p]:
                parent[p] = parent[parent[p]] # this line just speeds up the process
                p = parent[p]
            return p
        
        def connectNodes(a, b):
            """
            True: connected!
            False: already connected
            """
            rootA, rootB = findRootParent(a), findRootParent(b)
            
            if rootA == rootB:
                return False
            
            # decide the parent based on the ranks
            if rank[rootA] > rank[rootB]:
                parent[rootB] = rootA
                rank[rootA] += rank[rootB]
            else:
                parent[rootA] = rootB
                rank[rootB] += rank[rootA]
            return True
        
        
        for a, b in edges:
            # if we cannot connect them, they are already connected
            # so this edge is redundant
            if not connectNodes(a, b):
                return [a, b]
        
            