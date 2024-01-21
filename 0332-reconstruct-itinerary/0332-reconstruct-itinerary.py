class Solution:
    """
    Lexical order means the dictionary order:
    Word "LGA" comes before "LGB" in a dictionary
    """
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        trips = len(tickets)
        for a, b in tickets:
            # heapq.heappush(graph[a], b)
            graph[a].append(b)
            
            
        for node in graph:
            graph[node].sort()
            
        output = []
        
        def dfs(node):
            while graph[node]:
                # dfs(heapq.heappop(graph[node]))
                dfs(graph[node].pop(0))
            output.append(node)
        dfs("JFK")
        
        
        return reversed(output)
        