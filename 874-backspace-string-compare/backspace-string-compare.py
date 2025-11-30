class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def checking(s):
            stack = []
            for ch in s:
                if ch == "#" and stack:
                    stack.pop()
                elif ch != "#":
                    stack.append(ch)    
            return stack


        return checking(s) == checking(t)            