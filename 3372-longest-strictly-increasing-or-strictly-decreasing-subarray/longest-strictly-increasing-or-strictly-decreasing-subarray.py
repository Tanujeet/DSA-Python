class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
       
        n = len(nums)
        ans = 1

        for i in range(n):

          
            length = 1
            for j in range(i + 1, n):
                if nums[j] > nums[j - 1]:
                    length += 1
                else:
                    break
            ans = max(ans, length)

            length = 1
            for j in range(i + 1, n):
                if nums[j] < nums[j - 1]:
                    length += 1
                else:
                    break
            ans = max(ans, length)

        return ans