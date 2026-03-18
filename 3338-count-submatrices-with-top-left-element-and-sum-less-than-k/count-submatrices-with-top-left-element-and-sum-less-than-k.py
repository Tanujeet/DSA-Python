class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[0]*n for _ in range(m)]
        cnt = 0

        for r in range(m):
            for c in range(n):
                dp[r][c] = grid[r][c]

                if r > 0:
                    dp[r][c] += dp[r-1][c]
                

                if c > 0:
                    dp[r][c] += dp[r][c-1]
                
                if r > 0 and c > 0:
                    dp[r][c] -= dp[r-1][c-1]
                
                if dp[r][c] <=k:
                    cnt +=1
        

        return cnt 