class Solution:
    def canFinish(self, numCourses: int, nums: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for a , b in nums:
            adj[b].append(a)


        state = [0]*numCourses


        def dfs(node):
            state[node] = 1

            for nei in adj[node]:
                if state[nei] == 0:
                    if not dfs(nei):
                        return False

                elif state[nei] == 1:
                    return False


            state[node] = 2
            return True



        for i in range(numCourses):
            if state[i] == 0:
                if not dfs(i):
                    return False

        return True                               

