class Solution:
    def isHappy(self, num: int) -> bool:
        seen = set()
        while num not in seen:
            seen.add(num)
            squares = []
            while num:
                squares.append((num % 10)**2)
                num //= 10
            num = sum(squares)
          
        return num == 1
        