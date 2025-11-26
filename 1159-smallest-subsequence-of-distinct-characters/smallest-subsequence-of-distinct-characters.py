class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last={ch:i for i, ch in enumerate(s)}

        stack = []
        visited=set()

        for i , c in enumerate(s):
            if c in visited:
                continue
            while stack and stack[-1] > c and i < last[stack[-1]]:
                visited.remove(stack.pop())
            stack.append(c)        
            visited.add(c)


        return "".join(stack)    
        

