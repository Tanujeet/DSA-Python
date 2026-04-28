class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m = len(grid)
        n = len(grid[0])
        flat = [grid[i][j] for i in range(m) for j in range(n)]
        
        rem = flat[0] % x
        for num in flat:
            if num % x != rem:
                return -1
        
        flat.sort()
        median = flat[len(flat) // 2]
        
        return sum(abs(num - median) // x for num in flat)