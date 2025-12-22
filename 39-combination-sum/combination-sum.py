class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]

        def backtrack(index,target,path):

            if target == 0:
                res.append(path[:])
                return


            if target < 0 or index == len(candidates):
                return


            path.append(candidates[index])
            backtrack(index,target - candidates[index],path)
            path.pop()

            backtrack(index + 1 , target , path)

        backtrack(0,target,[])     
        return res       