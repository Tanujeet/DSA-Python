class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        n = len(nums)
        limit = 100000000000000 

        suffix = [1] * n
        prod = 1

        for i in range(n-2,-1,-1):
            if prod > limit // nums[i+1]:
                prod = limit + 1
            
            else:
                prod *= nums[i+1]
            suffix[i] = prod
        

        totalSum = 0

        for i in range(n):
            if totalSum ==suffix[i]:
                return i
            
            totalSum += nums[i]
        

        return -1