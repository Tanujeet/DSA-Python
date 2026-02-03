class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        fresh = 0
        q = deque()


        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    fresh+=1


                elif grid[r][c] == 2:
                    q.append((r,c))    


        miniutes = 0  
        directions = [(1,0), (-1,0), (0,1), (0,-1)]  

        while q and fresh > 0:
            size = len(q)

            for _ in range(size):
                i,j = q.popleft()

                for dr,dc in directions:
                    nr ,nc =  i + dr , j + dc

                    if 0 <= nr < row and 0 <=nc < col and grid[nr][nc] ==1 :
                        grid[nr][nc] = 2
                        fresh -=1

                        q.append((nr,nc))

            miniutes +=1


        return -1 if fresh > 0 else miniutes                 
