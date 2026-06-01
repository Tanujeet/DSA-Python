class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        total = 0

        n = len(cost)- 1

        while n >= 0:
            total+=cost[n]
            if n-1 >= 0:
                total +=cost[n-1]
            

            n-=3
        

        return total