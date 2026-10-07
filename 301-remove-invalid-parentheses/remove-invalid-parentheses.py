from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # Step 1: kitne ( aur ) hatane hain
        rem_l = rem_r = 0
        for ch in s:
            if ch == '(':
                rem_l += 1
            elif ch == ')':
                if rem_l > 0:
                    rem_l -= 1
                else:
                    rem_r += 1

        n = len(s)
        res = set()
        path = []

        def dfs(i: int, left: int, right: int, rem_l: int, rem_r: int):
            if i == n:
                if rem_l == 0 and rem_r == 0:
                    res.add("".join(path))
                return

     
            if n - i < rem_l + rem_r:
                return

            ch = s[i]

            if ch == '(' and rem_l > 0:
                dfs(i + 1, left, right, rem_l - 1, rem_r)
            elif ch == ')' and rem_r > 0:
                dfs(i + 1, left, right, rem_l, rem_r - 1)

           
            path.append(ch)
            if ch == '(':
                dfs(i + 1, left + 1, right, rem_l, rem_r)
            elif ch == ')':
                if right < left:  
                    dfs(i + 1, left, right + 1, rem_l, rem_r)
            else:
                dfs(i + 1, left, right, rem_l, rem_r)
            path.pop()

        dfs(0, 0, 0, rem_l, rem_r)
        return list(res)