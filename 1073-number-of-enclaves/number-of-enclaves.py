class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        visited = set()
        ans = 0

        def dfs(r,c):
            nonlocal island_size, touches_border

            if r < 0 or r>= row or c < 0 or c>= col:
                return  


            if grid[r][c] == 0 or (r,c) in visited:
                return


            visited.add((r,c))
            island_size +=1  


            if r == 0 or r == row - 1 or c == 0 or c == col -1:
                touches_border = True
            

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)


        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and (r,c) not in visited:
                    island_size = 0
                    touches_border = False
                    dfs(r,c)


                    if not touches_border:
                        ans += island_size

        return ans    


            



