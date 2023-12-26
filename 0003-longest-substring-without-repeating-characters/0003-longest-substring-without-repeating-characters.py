class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        chars = set()
        left = 0
        
        for right in range(len(s)):
            # deletes all the values added to the set up until [including] the first instance of current duplicate
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
            res = max(res, right - left + 1)
            chars.add(s[right])
        return res
            