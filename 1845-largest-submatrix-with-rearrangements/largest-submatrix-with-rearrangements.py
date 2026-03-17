class Solution:
    def largestSubmatrix(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0

        for i in range(1,m):
            for j in range(n):
                if grid[i][j] ==1:
                    grid[i][j] += grid[i-1][j]
        


        for i in range(m):
            grid[i].sort(reverse=True)

            for j in range(n):
                area = grid[i][j] *(j+1)
                res = max(res,area)
        

        return res 
        