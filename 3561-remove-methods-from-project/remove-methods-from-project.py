class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for a , b in invocations:
            graph[a].append(b)

        

        suspicious = {k}

        queue = deque([k])

        while queue:
            node = queue.popleft()


            for next in graph[node]:
                if next not in suspicious:
                    suspicious.add(next)
                    queue.append(next)
        


        for a , b in invocations:
            if b in suspicious and a not in suspicious:
                return list(range(n))
        


        return [i for i in range(n) if i not in suspicious]
