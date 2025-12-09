class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        cnt = 0
        left = 0
        char_count = {'a': 0, 'b': 0, 'c': 0}
        n = len(s)

        for right in range(n):
            char_count[s[right]]+=1

            while char_count['a'] > 0 and char_count['b'] > 0 and char_count['c'] > 0:
                cnt+= n-right
                char_count[s[left]]-=1
                left+=1


        return cnt        


