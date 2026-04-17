class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = float('inf')
        sell1 = 0
        buy2 = float('inf')
        sell2 = 0

        for price in prices:
            buy1  = min(buy1, price)              # 1st buy cost minimize karo
            sell1 = max(sell1, price - buy1)      # 1st sell profit maximize karo
            buy2  = min(buy2, price - sell1)      # 2nd buy: 1st profit se offset karo
            sell2 = max(sell2, price - buy2)      # 2nd sell profit maximize karo
            
        return sell2