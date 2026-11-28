class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
     
        n = len(items)
        cnt = [0] * (n + 1)
        for f, _ in items:
            cnt[f] += 1

      
        mult = [0] * (n + 1)
        for f in range(1, n + 1):
            if cnt[f]:
                mult[f] = sum(cnt[k] for k in range(f, n + 1, f))

        m = min(p for _, p in items)

      
        deals = sorted((p, mult[f] - 1) for f, p in items if mult[f] > 1)

        
        total, rem = 0, budget
        for p, d in deals:
            if p > 2 * m or p > rem:
                break
            take = min(d, rem // p)
            total += 2 * take
            rem -= take * p

        total += rem // m
        return total