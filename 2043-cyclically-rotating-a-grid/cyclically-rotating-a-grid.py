class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])


        def rotate(p,k):
            nums = []

            for j in range(p,n-p-1):
                nums.append(grid[p][j])
            

            for i in range(p,m-p-1):
                nums.append(grid[i][n-p-1])
            
            for j in range(n-p-1,p,-1):
                nums.append(grid[m-p-1][j])
            
            for i in range(m-p-1,p,-1):
                nums.append(grid[i][p])
            

            k %= len(nums)
            if k == 0:
                return
            
            nums = nums[k:] + nums[:k]

            idx = 0
            for j in range(p, n - p - 1):
                grid[p][j] = nums[idx]; idx += 1
            for i in range(p, m - p - 1):
                grid[i][n - p - 1] = nums[idx]; idx += 1
            for j in range(n - p - 1, p, -1):
                grid[m - p - 1][j] = nums[idx]; idx += 1
            for i in range(m - p - 1, p, -1):
                grid[i][p] = nums[idx]; idx += 1
        
        for p in range(min(m,n)//2):
            rotate(p,k)
        

        return grid