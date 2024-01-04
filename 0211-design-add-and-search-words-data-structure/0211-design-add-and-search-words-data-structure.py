class WordDictionary:

    def __init__(self):
        self.table = {'in':False}

    def addWord(self, word: str) -> None:
        last = self.table
        
        for ch in word:
            if ch not in last:
                last[ch] = {'in':False}
            last = last[ch]
        last['in'] = True
        

    def search(self, word: str) -> bool:
        
        def helper(word, dic):
            if len(word) == 1 and word != '.':
                if word in dic: return dic[word]['in']
                return False
        
            last = dic
            for i in range(len(word)):
                if word[i] != '.':
                    if word[i] not in last:
                        return False
                    last = last[word[i]]
                        
                else:
                    # try replacing '.' with a char from dic and call search recursively
                    for ch in last:
                        if ch != 'in':
                            rest = "" if i+1 >= len(word) else word[i+1:]
                            new = ch + rest
                            if helper(new, last): return True
                    
                    # at this point none of the chars in dic match
                    return False
            
            # check if the word ends here
            return last['in']
        return helper(word, self.table)
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)