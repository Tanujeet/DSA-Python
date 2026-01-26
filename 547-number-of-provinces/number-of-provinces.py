class Solution:
    def findCircleNum(self, nums: List[List[int]]) -> int:
        n = len(nums)
        count = 0
        visited = set()
        
        def dfs(node):
            visited.add(node)
            for nei in range(n):
                if nums[node][nei] == 1 and nei not in visited:
                    dfs(nei)

        for i in range(n):
            if i not in visited:
                count +=1
                dfs(i)


        return count                 


