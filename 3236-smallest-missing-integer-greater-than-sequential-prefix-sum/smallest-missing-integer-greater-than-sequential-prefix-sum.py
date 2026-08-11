class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0 
        total = nums[0]


        while i + 1 < n and nums[i+1] == nums[i] + 1:
            i+=1 
            total += nums[i]
        


        s = set(nums)
        while total in s:
            total += 1
        


        return total