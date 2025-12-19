class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap=[1]
        seen = {1}
        factors = [2, 3, 5]

        for _ in range(n):
            curr =  heapq.heappop(heap)

            for f in factors:
                nxt = curr*f
                if nxt not in seen:
                    seen.add(nxt)
                    heapq.heappush(heap,nxt)
        return curr            