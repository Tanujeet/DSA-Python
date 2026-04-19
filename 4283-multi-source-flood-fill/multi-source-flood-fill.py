class Solution:
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:

        grid = [[0] * m for _ in range(n)]
        dist = [[float("inf")] * m for _ in range(n)]

        q = deque()

        for r,c, color in sources:
            grid[r][c] = color
            dist[r][c] = 0 
            q.append((r,c,color))
        

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:
            r,c,color = q.popleft()

            for dr , dc in directions:
                nr , nc = r + dr , c + dc


                if 0 <= nr < n and 0 <= nc < m:
                    if dist[nr][nc] > dist[r][c] + 1:
                        dist[nr][nc] = dist[r][c] + 1
                        grid[nr][nc] = color
                        q.append((nr,nc,color))
                    

                    elif dist[nr][nc] == dist[r][c] + 1:
                        if grid[nr][nc] < color:
                            grid[nr][nc] = color
                            q.append((nr,nc,color))
        

        return grid
