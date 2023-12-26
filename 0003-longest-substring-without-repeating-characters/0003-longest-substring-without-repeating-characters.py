class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        chars = set()
        left = 0
        
        for right in range(len(s)):
            
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
            res = max(res, right - left + 1)
            chars.add(s[right])
        return res
            