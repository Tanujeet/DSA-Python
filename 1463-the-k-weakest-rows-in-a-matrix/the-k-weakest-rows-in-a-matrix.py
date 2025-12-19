class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        maxheap = []

        for i , row in enumerate(mat):
            soldiers = sum(row)
            heapq.heappush(maxheap,(-soldiers,-i))

            if len(maxheap)>k:
                heapq.heappop(maxheap)

        result = []
        while maxheap:
            result.append(-heapq.heappop(maxheap)[1])

        return result[::-1]            

   