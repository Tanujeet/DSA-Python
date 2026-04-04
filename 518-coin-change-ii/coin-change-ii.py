class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        n = len(coins)
        @lru_cache(maxsize=None)

        def solve(i, amount):
           
            if i == n:
                return 1 if amount == 0 else 0


            if amount == 0:
                return 1

            if amount < coins[i]:
                return solve(i + 1, amount)  
            take = solve(i, amount - coins[i])   
            skip = solve(i + 1, amount)           
            return take + skip

        return solve(0, amount)