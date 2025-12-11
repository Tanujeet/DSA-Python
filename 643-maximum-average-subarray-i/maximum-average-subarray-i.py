class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        ans = 0
        n = len(nums)
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for right in range(k,n):
            window_sum += nums[right]
            window_sum-= nums[left]


            left+=1

            max_sum = max(max_sum,window_sum)

        return max_sum / k