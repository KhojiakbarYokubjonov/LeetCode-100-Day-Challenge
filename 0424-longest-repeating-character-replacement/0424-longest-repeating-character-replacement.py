class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        
        left = 0
        res = 0
        most_freq = 0
        
        for right in range(len(s)):
            ch = s[right]
            if ch not in count: count[ch] = 0
            count[ch] += 1
            most_freq = max(most_freq, count[ch])
            
            while (right - left + 1 - most_freq) > k:
                count[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
            
                
                
            
                
            
                
                
        