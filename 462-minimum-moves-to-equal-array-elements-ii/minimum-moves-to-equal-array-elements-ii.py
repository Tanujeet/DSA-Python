class Solution:
    def minMoves2(self, nums: List[int]) -> int:
       
        nums.sort()

        left, right, moves = 0, len(nums) - 1, 0

       
        while left < right:
            moves += nums[right] - nums[left]
            left += 1
            right -= 1

     
        return moves