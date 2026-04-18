class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        if k >= n//2:
            return sum(max(prices[i+1]- prices[i],0)for i in range(n-1))

        

        buy = [float('inf')] * k 
        sell = [0] * k

        for price in prices:
            for i in range(k):
                buy[i] = min(buy[i],price - (sell[i-1 ] if i > 0 else 0))
                sell[i] = max(sell[i],price - buy[i])
        
        return sell[-1]