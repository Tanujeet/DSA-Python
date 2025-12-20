class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = []
        n = len(profits)

        for i in range(n):
            heapq.heappush(projects,(capital[i],profits[i]))

        maxheap = []

        for  _ in range(k):
            while projects and projects[0][0] <= w:
                cap,prof = heapq.heappop(projects)

                heapq.heappush(maxheap,-prof)   


            if not maxheap:
                break

            w += -heapq.heappop(maxheap)

        return w            