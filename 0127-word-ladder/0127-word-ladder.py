class Solution:
    """
    asciiCode = ord('a')
    b = chr(asciiCode + 1)
    """
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        
        graph = collections.defaultdict(set)
        
        wordList = set(wordList + [beginWord])
        
        for w in wordList:
            for i in range(len(w)):
                w1, w2 = w[:i], w[i+1:]
                for ch in alphabet:
                    new = w1 + ch + w2
                    if new in wordList and new != w:
                        graph[w].add(new)
        q = [(beginWord, 0)]
        visited = set()
        
        while q:
            node, step = q.pop(0)
            if node == endWord:
                return step + 1
            visited.add(node)
            for v in graph[node]:
                if v not in visited:
                    q.append((v, step + 1))
        return 0
    
        