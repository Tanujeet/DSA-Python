class Solution:
    def calculate(self, s: str) -> int:
        stack =[] 
        last_op = "+"
        num = 0

        for ch in s + '+':
            if ch.isdigit():
                num = num*10 + int(ch)


            elif ch in '+-*/':
                if last_op =="+":
                    stack.append(num)
                elif last_op =="-":
                    stack.append(-num)
                elif last_op == "*":
                    stack.append(stack.pop()*num)
                else:
                    top = stack.pop()
                    stack.append(int(top/num))    
                last_op = ch
                num = 0 
        return sum(stack)                         


