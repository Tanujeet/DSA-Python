class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        adj = [[] for _ in range(n)]
        indegree = [0] * n
        ans = list(range(n))

        for rich in richer:
            adj[rich[0]].append(rich[1])
            indegree[rich[1]] +=1
        

        q = deque()

        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        


        while q:
            node =q.popleft()

            for nei in adj[node]:
                if quiet[ans[node]] < quiet[ans[nei]]:
                    ans[nei] = ans[node]

                
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)
        

        return ans 