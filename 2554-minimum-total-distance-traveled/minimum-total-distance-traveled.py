class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort(key=lambda x: x[0])
        n = len(robot)

        factory_pos = []
        for f in factory:
            for _ in range(f[1]):
                factory_pos.append(f[0])

        fp = len(factory_pos)

        dp = [[float('inf')] * (fp + 1) for _ in range(n + 1)]


        for j in range(fp + 1):
            dp[n][j] = 0

      
        for i in range(n - 1, -1, -1):
            for j in range(fp - 1, -1, -1):
        
                assign = abs(robot[i] - factory_pos[j]) + dp[i + 1][j + 1]

           
                skip = dp[i][j + 1]

                dp[i][j] = min(assign, skip)

        return dp[0][0]