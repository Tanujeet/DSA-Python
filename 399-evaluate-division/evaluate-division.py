class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = self.build(equations,values)
        res = []

        for dividend , divisor in queries:
            if dividend not in graph or divisor not in graph:
                res.append(-1.0)
            else:
                Res = self.bfs(dividend,divisor,graph)
                res.append(Res)
        
        return res



    def build(self,equations,values):
        graph = defaultdict(dict)
        for (dividend,divisor),val in  zip(equations,values):
            graph[dividend][divisor] = val
            graph[divisor][dividend] = 1.0 / val
         
        return graph


    def bfs(self,start,end,graph):
        q = deque([(start,1.0)])
        visited =set()
        while q:
            node , val = q.popleft()

            if node == end:
                return val


            visited.add(node)

            for nei , wei in graph[node].items():
                if nei not in visited:
                    q.append((nei, val * wei))

        return -1.0                    