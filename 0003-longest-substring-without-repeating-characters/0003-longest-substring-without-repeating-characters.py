class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        overall = curr = 0
        start = end = 0
        pos = {}
        while end < len(s):
           
            if start != end and s[end] in s[start:end]:
                overall = max(overall, curr)
                # updates the start position to the index right after the first instance of the duplicate value
                start = pos[s[end]] + 1
                # recalculates the current longest substring lenth
                curr = end - start + 1

            else:
                curr += 1
            pos[s[end]] = end
            end += 1
        return max(overall,curr)