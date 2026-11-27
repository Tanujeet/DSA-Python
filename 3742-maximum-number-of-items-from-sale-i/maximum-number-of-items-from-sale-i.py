class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
       
        mn = min(price for _, price in items)

       
        cnts = []
        for factor_i, price_i in items:
            cnt = 0
            for factor_j, _ in items:
                if factor_j % factor_i == 0:
                    cnt += 1
            cnts.append((price_i, cnt))

      
        dp = [0] * (budget + 1)

      
        for price, cnt in cnts:
            for x in range(budget, price - 1, -1):
                dp[x] = max(dp[x], dp[x - price] + cnt)

       
        return max(dp[x] + (budget - x) // mn for x in range(budget + 1))