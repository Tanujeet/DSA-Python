class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = 1
        curr = 0

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch in "+-":
                curr += sign * num 
                num = 0
                sign = 1 if ch == "+" else -1

            elif ch =="(":
                stack.append(curr)
                stack.append(sign)
                curr = 0
                sign =1

            elif ch == ")":
                curr+= sign * num 
                num = 0
                curr*= stack.pop()
                curr+= stack.pop()
                
        return curr + sign * num           
