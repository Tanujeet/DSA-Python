class Solution:
    def checkIfPrerequisite(self, numCourses: int, graph: List[List[int]], nums: List[List[int]]) -> List[bool]:
        adj = [ [] for _ in range(numCourses)]
        inDegree = [0] * numCourses

        for p in graph:
            adj[p[0]].append(p[1])
            inDegree[p[1]] += 1
        

        q = deque()

        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i)
        
        mp = defaultdict(set)

        while q:
            node = q.popleft()

            for nei in adj[node]:
                mp[nei].add(node)
                mp[nei].update(mp[node])
                inDegree[nei]-=1

                if inDegree[nei] == 0:
                    q.append(nei)
        

        return [q[0] in mp[q[1]] for q in nums ]