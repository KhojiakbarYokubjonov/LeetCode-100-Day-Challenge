class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        
        
        count = {}
        count2 = {}
        start, end = ord("a"), ord("z")
        for i in range(start, end + 1):
            count[i] = 0
            count2[i] = 0
        
        for ch in s1:
            num = ord(ch)
            count[num] += 1
            
        
        for i in range(len(s2)):
            num = ord(s2[i])
            count2[num] += 1
            if i - left + 1 == len(s1):
                # print(count2)
                if count == count2: return True
                else:
                    num = ord(s2[left])
                    count2[num] = max(0, count2[num] - 1)
                    left += 1
        print()    
        print(count2)
        return False
            
                