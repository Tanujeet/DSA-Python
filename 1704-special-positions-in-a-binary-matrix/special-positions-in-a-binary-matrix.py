class Solution:
    def numSpecial(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        row = [0]* m
        col = [0]* n


        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row[i]+=1
                    col[j]+=1
        


        return sum(
            grid[i][j] == 1 and row[i] ==1 and col[j] ==1
            for i in range(m)
            for j in range(n)
        )