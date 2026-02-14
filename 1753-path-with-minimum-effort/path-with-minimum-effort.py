class Solution:
    def minimumEffortPath(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0 
         
        row = len(grid)
        col = len(grid[0])
        maxEffort = 0

        heap = [(0,0,0)]
        visited = set()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]


        while heap:
            effort,currRow,currCol = heapq.heappop(heap)


            maxEffort = max(maxEffort,effort)

            if (currRow, currCol) == (row - 1 , col -1):
                return maxEffort

            visited.add((currRow,currCol))    


            for dr, dc in dirs:
                nr , nc = currRow + dr , currCol + dc

                if 0 <= nr < row and 0 <= nc < col and (nr,nc) not in visited:
                    newEffort = abs(grid[nr][nc] - grid[currRow][currCol])
                    heapq.heappush(heap,(newEffort,nr,nc))


        return maxEffort             