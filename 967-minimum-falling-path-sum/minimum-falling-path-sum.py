class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [row[:] for row in grid]


        for i in range(1,n):
            for j in range(n):
                best = dp[i-1][j]

                if j > 0:
                    best = min(best,dp[i-1][j-1])
                
                if j < n-1:
                    best = min(best,dp[i-1][j+1])
                

                dp[i][j] = grid[i][j] + best
        
        return min(dp[n-1])