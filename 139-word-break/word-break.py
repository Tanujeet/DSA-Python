class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [True] +[False] * n 

        for i in range(1,n+1):
            for ch in  wordDict:
                start = i - len(ch)

                if start >= 0 and dp[start] and s[start:i] == ch :
                    dp[i] = True
                    break
        

        return dp[-1]