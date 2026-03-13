class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] ==1:
            return 0 
        

        rows = len(grid)
        cols = len(grid[0])

        dp = [0] * cols
        dp[0] = 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] ==1:
                    dp[c] = 0
                else:
                    if c > 0:
                        dp[c] += dp[c-1]
        


        return dp[cols-1]