class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans =  []

        def backtrack(path):
            if len(path) == len(nums):
                ans.append(path[:])
                return



            for x in nums:
                if x in path:
                    continue

                backtrack(path +[x])

        backtrack([])

        return ans                
