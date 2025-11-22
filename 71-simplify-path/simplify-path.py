class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        component = path.split('/')


        for ch in component:
            if ch =="" or ch == ".":
                continue

            elif ch =="..":
                if stack:
                    stack.pop()   
            else:
                stack.append(ch)
        return "/" + "/".join(stack)                 