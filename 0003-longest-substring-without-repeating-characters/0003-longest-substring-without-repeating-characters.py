class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        overall = curr = 0
        start = end = 0
        pos = {}
        while end < len(s):
           
            if start != end and s[end] in s[start:end]:
                overall = max(overall, curr)
                start = pos[s[end]] + 1
                
                curr = end - start
                pos[s[end]] = end
            pos[s[end]] = end
            curr += 1
            end += 1
        return max(overall,curr)