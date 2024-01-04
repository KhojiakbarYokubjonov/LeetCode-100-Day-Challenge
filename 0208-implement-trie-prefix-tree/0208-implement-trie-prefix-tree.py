class Node:
    def __init__(self, char):
        self.char = char
        self.present = False
class Trie:

    def __init__(self):
        self.table = {}
        # self.entrance = set()
        

    def insert(self, word: str) -> None:
        # self.entrance.add(word)
        lastTable = self.table
        i = 0
        while i < len(word):
            if word[i] not in lastTable:
                lastTable[word[i]] = {"in":False}
            lastTable = lastTable[word[i]]
            i += 1
        lastTable['in'] = True
        

    def search(self, word: str) -> bool:
        lastTable = self.table
        for ch in word:
            if ch in lastTable:
                lastTable = lastTable[ch]
            else:
                return False
        return lastTable['in']

    def startsWith(self, prefix: str) -> bool:
        lastTable = self.table
        for ch in prefix:
            if ch in lastTable:
                lastTable = lastTable[ch]
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)