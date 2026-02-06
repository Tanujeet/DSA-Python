class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()
        visited = [[False]*n for _ in range(n)]

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    q.append((r,c))
                    visited[r][c] = True 

        if len(q) == 0 or len(q) == n*n:
            return -1 


        dirs = [(1,0), (-1,0), (0,1), (0,-1)] 
        level = -1

        while q:
            size = len(q)
            level +=1
            for _ in range(size):
                r,c = q.popleft()

                for dr,dc in  dirs:
                    nr,nc = r + dr , c + dc

                    if  0  <= nr <  n and 0<= nc < n:
                        if not visited[nr][nc] and grid[nr][nc] == 0:
                            visited[nr][nc] = True
                            q.append((nr,nc))

        return level                     
     
