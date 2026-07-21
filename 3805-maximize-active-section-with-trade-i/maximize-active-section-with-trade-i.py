class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)
        ans = i = 0
        pre, mx = float('-inf'), 0

        while i < n:
            j = i + 1
            while j < n and s[j] == s[i]:
                j += 1
            cur = j - i          # current run length

            if s[i] == '1':
                ans += cur        # 1's directly count, never "spent"
            else:
                mx = max(mx, pre + cur)   # best pair of adjacent 0-runs
                pre = cur

            i = j

        return ans + mx