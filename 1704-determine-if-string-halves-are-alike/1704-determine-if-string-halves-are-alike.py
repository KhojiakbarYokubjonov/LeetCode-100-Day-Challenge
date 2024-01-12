class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        
        def countVowels(string):
            count = 0
            for ch in string:
                if ch in {"a", "e", "o", "u", "i", "A", "O", "U", "I", "E"}:
                    count += 1
            print(string, count)
            return count
        
        halfInd = len(s) // 2
        return countVowels(s[:halfInd]) == countVowels(s[halfInd:])
