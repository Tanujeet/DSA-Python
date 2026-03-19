class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        pref = [[0] * n for _ in range(m)]
        xpref = [[0] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                val = 0
                x  = 0

                if grid[r][c] == "X":
                    val = 1
                    x = 1

                elif grid[r][c] == "Y":
                    val = -1
                

                pref[r][c] = val
                xpref[r][c] = x

                if r > 0:
                    pref[r][c] += pref[r-1][c]
                    xpref[r][c] += xpref[r-1][c]
                
                if c > 0 :
                    pref[r][c] += pref[r][c-1]
                    xpref[r][c] += xpref[r][c-1]
                
                if r > 0 and c > 0:
                    pref[r][c] -= pref[r-1][c-1]
                    xpref[r][c] -= xpref[r-1][c-1]

        count = 0

        for r in range(m):
            for c in range(n):
                if pref[r][c] == 0 and xpref[r][c] > 0:
                    count +=1
        

        return count
                 



