class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0

        graph = defaultdict(list)
        for i , val in enumerate(arr):
            graph[val].append(i)
        

        q = deque([0])
        visited = {0}
        steps = 0 

        while q:
            size = len(q)
            for _ in range(size):
                curr = q.popleft()
                if curr == n-1:
                    return steps
                

                for nextIdx in (curr-1, curr + 1 ):
                    if 0 <= nextIdx < n and nextIdx not in visited:
                        visited.add(nextIdx)
                        q.append(nextIdx)
                    

                    if arr[curr] in graph:
                        for nextIdx in graph[arr[curr]]:
                            if nextIdx not in visited:
                                visited.add(nextIdx)
                                q.append(nextIdx)
                        

                        del graph[arr[curr]]
                
            steps += 1
        
        return -1
