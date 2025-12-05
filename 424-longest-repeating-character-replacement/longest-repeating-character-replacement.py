from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        left = 0
        freq = Counter()
        maxFreq = 0

        for right in range(len(s)):
            freq[s[right]] += 1
            maxFreq = max(maxFreq, freq[s[right]])

            while (right - left + 1) - maxFreq > k:
                freq[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans
