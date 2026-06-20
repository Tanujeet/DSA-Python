class Solution:
    def maxBuilding(self, n, r):
        r = [[1,0]] + sorted(r) + [[n,n-1]]

        for i in range(1, len(r)):
            r[i][1] = min(r[i][1], r[i-1][1] + r[i][0] - r[i-1][0])

        for i in range(len(r)-2, -1, -1):
            r[i][1] = min(r[i][1], r[i+1][1] + r[i+1][0] - r[i][0])

        ans = 0
        for i in range(len(r)-1):
            d = r[i+1][0] - r[i][0]
            ans = max(ans, (r[i][1] + r[i+1][1] + d) // 2)

        return ans