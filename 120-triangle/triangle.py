class Solution:
    def minimumTotal(self, nums: List[List[int]]) -> int:
        row = len(nums)
        dp = nums[row-1].copy()

        for r in range(row-2,-1,-1):
            for c in range(r+1):
                dp[c] = min(dp[c],dp[c+1]) + nums[r][c]
        

        return dp[0]