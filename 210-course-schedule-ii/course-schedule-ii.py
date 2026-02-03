class Solution:
    def findOrder(self, numCourses: int, nums: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]

        for a,b in nums:
            adj[b].append(a)


        state = [0] * numCourses
        ans = []
        cycle = False


        def dfs(node):
            nonlocal cycle
            state[node] = 1 

            for nei in adj[node]:
                if state[nei] == 0:
                    dfs(nei)
                    if cycle:
                        return


                elif state[nei] == 1:
                    cycle = True
                    return


            state[node] = 2
            ans.append(node)     


        for i in range(numCourses):
            if state[i] == 0:
                dfs(i)
                if cycle:
                    return []    

        return ans[::-1]               

