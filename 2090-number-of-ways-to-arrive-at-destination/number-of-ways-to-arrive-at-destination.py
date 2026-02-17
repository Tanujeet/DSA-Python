class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod = 10**9 + 7
        adj = [[] for _ in range(n)]
        for u, v, w in roads:
            adj[u].append((v, w))
            adj[v].append((u, w))


        dist = [float("inf")] * n 
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1
        q = [(0,0)]

        while q:
            d,u =  heapq.heappop(q)

            if d > dist[u]:
                continue 


            for v , w in adj[u]:
                if dist[v] > d + w:
                    dist[v] = d + w
                    ways[v] = ways[u]
                    heapq.heappush(q,(dist[v],v))

                elif dist[v] == d + w:
                    ways[v] = (ways[v] + ways[u]) % mod


        return ways[n-1]                       