class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        m = len(grid)
        n = len(grid[0])

        dp =[(0,0)] * n
        dp[0] = (grid[0][0],grid[0][0])

        for j in range(1,n):
            val = grid[0][j]
            prev_max,prev_min = dp[j-1]
            dp[j] = (prev_max * val,prev_min * val)
        

        for i in range(1,m):
            val = grid[i][0]
            prev_max,prev_min = dp[0]
            dp[0] = (prev_max * val , prev_min * val)



            for j in range(1,n):
                val = grid[i][j]

                top_max ,top_min = dp[j]
                left_max,left_min = dp[j-1]

                candidates = [
                    top_max * val,
                    top_min * val,
                    left_max * val,
                    left_min * val
                ]

                dp[j] = (max(candidates),min(candidates))
            

        res = dp[-1][0]

        return res % MOD if res>=0 else -1