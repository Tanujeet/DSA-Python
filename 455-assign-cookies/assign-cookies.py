class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        i = j = cnt = 0

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                cnt +=1
                i+=1
            j+=1
        

        return cnt 