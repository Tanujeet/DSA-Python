class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maxSum = -10**4-1
        curr  = 0 

        left = 0 


        for right in range(n):
            curr+= nums[right]

            maxSum = max(maxSum,curr)


            while curr < 0 :
                curr -= nums[left]
                left += 1
        


        return maxSum