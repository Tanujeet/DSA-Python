class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        q = [(grid[0][0],0,0)]
        dirs =[(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()


        while q:
            maxDist,r,c = heapq.heappop(q)

            if (r,c) in visited:
                continue 
            visited.add((r,c))

            if r == n - 1 and c == m - 1:
                return maxDist  


            for dr ,dc in dirs:
                nr , nc = r + dr , c + dc

                if 0 <= nr < n and 0 <= nc < m and (nr,nc) not in visited:
                    newDist = max(maxDist,grid[nr][nc])

                    heapq.heappush(q,(newDist,nr,nc))


        return -1                   