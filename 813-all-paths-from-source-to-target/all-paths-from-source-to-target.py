class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        q = [(0,[0])]
        target = len(graph) - 1
        res = []

        while q:
            node,path = q.pop(0)

            if node == target:
                res.append(path)
                continue


            for nei in graph[node]:
                q.append((nei,path + [nei]))


        return res             
