class Solution:
    def calculate(self, s: str) -> int:
        current = 0
        prev = 0
        cur_op = "+"
        total = 0
        
        i = 0
        while i < len(s):
            ch = s[i]
            
            if ch.isdigit():
                while i < len(s) and s[i].isdigit():
                    current = current*10 + int(s[i])
                    i += 1
                
                i -= 1
                if cur_op == "+":
                    total += current
                    prev = current
                if cur_op == "-":
                    total -= current
                    prev = -current
                if cur_op == "*":
                    total -= prev
                    total += prev * current
                    prev = prev * current
                if cur_op == "/":
                    total -= prev
                    total += int(prev / current)
                    prev = int(prev / current)
                
                current = 0
                    
            elif ch != " ":
                cur_op = ch
                
            i += 1
        return total
                
                
                
                
                

        
        
        
        
        