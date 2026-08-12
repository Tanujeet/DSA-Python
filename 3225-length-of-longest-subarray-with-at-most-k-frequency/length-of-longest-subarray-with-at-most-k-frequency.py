class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = {}
        left = 0 
        maxLen = 0 


        for right in range(n):
            freq[nums[right]] = freq.get(nums[right] , 0 ) + 1



            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                left += 1
            


            maxLen = max(maxLen, right - left + 1)
        


        return maxLen