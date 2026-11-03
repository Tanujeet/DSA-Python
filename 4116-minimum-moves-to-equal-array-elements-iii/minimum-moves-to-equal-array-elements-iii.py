class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxNum = max(nums)
        total = 0

        for num in nums:
            total += maxNum - num
        

        return total