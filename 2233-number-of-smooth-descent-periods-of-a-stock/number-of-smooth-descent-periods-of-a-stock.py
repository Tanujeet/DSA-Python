class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        chain = 1
        ans = 1

        for i in range(1,n):
            if prices[i] == prices[i-1] - 1:
                chain+=1
            else:
                chain = 1
            ans+=chain
        return ans           


    