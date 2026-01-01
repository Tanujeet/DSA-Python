class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}

        def backtrack(index,CurrSum):

            #base Case
            if index == n:
                return 1 if CurrSum == target else 0

            if (index, CurrSum) in memo:
                return memo[(index, CurrSum)]

            #recurse
            ways = 0
            ways+=backtrack(index + 1, CurrSum + nums[index])
            ways+=backtrack(index + 1, CurrSum - nums[index])

            memo[(index, CurrSum)] = ways
            return ways



        #return 
        return backtrack(0,0)

    

