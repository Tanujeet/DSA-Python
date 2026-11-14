class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        min_sum = float('inf')


        for i in range(n):
            curr = 0 

            for j in range(i,n):

                curr += nums[j]

                lenght = j - i + 1


                if lenght > r:
                    break
            


                if lenght >= l and curr > 0:
                    min_sum = min(min_sum, curr)
        


        return -1 if min_sum == float('inf') else min_sum