class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        dp = [0] * n
        longest = 0 


        for ch in text2:
            curr_len = 0

            for i , val in enumerate(dp):
                if curr_len < val:
                    curr_len = val
                
                elif ch == text1[i]:
                    dp[i] = curr_len + 1
                    longest = max(longest,curr_len + 1)
            

        return longest 