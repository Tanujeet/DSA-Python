class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        last_lower = {}
        first_upper = {}

        for i,c in enumerate(word):
            if c.islower():
                last_lower[c] = i

            else:
                if c not in first_upper:
                    first_upper[c] = i
        

        cnt = 0 

        for c in  last_lower:
            upper = c.upper()
            if upper in first_upper and last_lower[c] < first_upper[upper]:
                cnt +=1
        

        return cnt 