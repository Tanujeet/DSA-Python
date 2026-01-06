class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        MaxSum = -10**4-1
        curr = 0

        left = 0

        for right in range(len(nums)):
            curr += nums[right]

            MaxSum = max(MaxSum,curr)

            while curr < 0:
                curr -= nums[left]
                left +=1

        return MaxSum        
