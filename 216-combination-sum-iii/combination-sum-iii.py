class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans  = []

        def backtrack(start,path,currSum):
            if len(path) == k:
                if currSum == n:
                    ans.append(path[:])
                return

            if currSum > n:
                return


            for num in range(start,10):
                path.append(num)
                backtrack(num + 1,path,currSum + num)
                path.pop()    

         


        backtrack(1,[],0)
        return ans    