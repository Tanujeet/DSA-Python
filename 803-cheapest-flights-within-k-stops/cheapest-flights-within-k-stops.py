class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adj = defaultdict(list)

        for u , v, w in flights:
            adj[u]. append((v,w))
        
        minCost = [float('inf')] * n

        minCost[src] = 0
        q = deque([(0,src,0)])


        while q:
            stops,u,cost = q.popleft()
            if stops > k:
                continue 



            for v,w in adj[u]:
                if cost + w < minCost[v]:
                    minCost[v] = cost + w
                    q.append((stops + 1 , v , minCost[v]))



        return minCost[dst] if minCost[dst] != float('inf') else -1   
