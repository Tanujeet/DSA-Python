class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])

        q = deque()
        height = [[-1]*col for _ in range(row)]

        for r in range(row):
            for c in range(col):
                if mat[r][c] == 0:
                    height[r][c] = 0
                    q.append((r,c))


        dirs = [(1,0),(-1,0),(0,1),(0,-1)]


        while q:
            r,c = q.popleft()

            for dr ,dc in dirs:
                nr,nc = r + dr , c + dc

                if 0 <= nr < row and 0 <= nc < col and height[nr][nc] ==-1:
                    height[nr][nc] = height[r][c]+ 1

                    q.append((nr,nc))

        return height             
        