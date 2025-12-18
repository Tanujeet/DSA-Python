class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)

        base = 0
        for i in range(n):
            base +=  strategy[i] * prices[i]


        prefOrig =[0] * (n+1)
        prefPrice =[0] *(n+1)

        for i in range(n):
            prefOrig[i + 1] = prefOrig[i] + strategy[i] * prices[i]
            prefPrice[i + 1] = prefPrice[i] + prices[i]

        half = k // 2
        maxGain = 0


        for i in range(n-k+1):
            origWindow = prefOrig[i + k] - prefOrig[i]

        
            newWindow = prefPrice[i + k] - prefPrice[i + half]

            gain = newWindow - origWindow

            maxGain = max(maxGain, gain)

        return base + maxGain   

