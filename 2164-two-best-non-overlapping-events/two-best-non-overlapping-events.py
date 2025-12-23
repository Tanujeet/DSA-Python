class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        minheap = []

        events.sort(key=lambda x: x[0])

        best = 0
        ans  = 0

        for s , e , v in events:
            while minheap and minheap[0][0] <s:
                _,val = heapq.heappop(minheap)
                best = max(best,val)


            ans = max(ans,best +  v)

            heapq.heappush(minheap,(e,v))    

        return ans