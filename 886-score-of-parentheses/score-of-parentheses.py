class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for ch in s:
            if ch == "(":
                stack.append(0)
            else:  
                top = stack.pop()
                stack[-1] += max(1, top * 2)
        return stack[-1]
