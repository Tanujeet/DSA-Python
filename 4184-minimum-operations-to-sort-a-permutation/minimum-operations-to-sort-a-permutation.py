class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        p = nums.index(0)
        INF = float('inf')
        ans = INF

   
        if all(nums[(p + i) % n] == i for i in range(n)):
            ans = min(ans, p, (n - p) % n + 2)

   
        if all(nums[(p - i) % n] == i for i in range(n)):
            ans = min(ans, 1 + (n - 1 - p), (p + 1) % n + 1)

        return -1 if ans == INF else ans