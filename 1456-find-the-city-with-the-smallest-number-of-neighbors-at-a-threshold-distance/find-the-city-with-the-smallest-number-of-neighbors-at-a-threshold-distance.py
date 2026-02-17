class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = [[] for _ in range(n)]

        for u , v ,w in edges:
            adj[u].append((v,w))
            adj[v].append((u,w))
        

        def fromSource(source: int) -> int:
            dist = [float("inf")] *n
            dist[source] = 0

            q = [(0,source)]

            while q:
                d , u = heapq.heappop(q)

                if d > dist[u]:
                    continue

                for v , w in adj[u]:
                    newDist = d + w
                    if newDist <= dist[v]:
                        dist[v] = newDist

                        heapq.heappush(q,(newDist,v))

            return dist
        

        ans = -1 
        minCount = float('inf')

        for src in range(n):
            dist = fromSource(src)

            count = 0 

            for i in range(n):
                if i != src and dist[i] <= distanceThreshold:
                    count +=1


            if count <= minCount:
                minCount = count
                ans = src


        return ans                 



        




