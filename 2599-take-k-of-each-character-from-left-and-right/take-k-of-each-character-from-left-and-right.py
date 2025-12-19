class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        total = Counter(s)
        n = len(s)

        for ch in "abc":
            if total[ch] < k:
                return -1    
        

        limit = {'a':total['a'] - k,
        'b':total['b'] - k,
        'c':total['c'] - k}

        left = 0
        maxLen = 0
        window = Counter()


        for right in range(len(s)):
            window[s[right]]+=1

            while ( window['a'] > limit['a'] or window['b'] > limit['b'] or window['c'] > limit['c'] ):
                window[s[left]]-=1
                left +=1
            maxLen = max(maxLen,right-left+1)

        return n - maxLen        






    