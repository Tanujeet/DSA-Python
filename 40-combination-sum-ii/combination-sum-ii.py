class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(start, path, sum):
            if sum == target:
                res.append(path[:])
                return 


            if  sum > target:
                return

            for i in range(start,len(candidates)):
                if i > start and candidates[i]  == candidates[i-1]:
                    continue

                backtrack(i+1,path + [candidates[i]] , sum + candidates[i])

        backtrack(0,[], 0)

        return res               
