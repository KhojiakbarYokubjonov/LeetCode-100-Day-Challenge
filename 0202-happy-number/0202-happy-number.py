class Solution:
    def isHappy(self, num: int) -> bool:
        seen = set()
        while num not in seen:
            seen.add(num)
            squares = [int(n)**2 for n in str(num)]
            num = sum(squares)
          
        return num == 1
        